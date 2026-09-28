# -*- coding: utf-8 -*-
"""
题目生成框架（通用、可复用）
========================
题目定义存放约定：
    按类别在根目录下建子目录（如 grammar、algorithm 等），每类下放
    problems/ 存放定义文件 pXXXX.py（如 grammar/problems/p1001.py），
    实现 build() 返回 make_problem(...)。

生成产物存放约定：
    每道题的数据输出到其定义文件所在子目录的 data/ 下，结构如下：
    <分类>/data/Pxxxx/
      ├── problem.yaml        # 题目名 / 标签 / 题号
      ├── problem_en.md       # 英文题面（无 --- 分隔，含至少 2 组示例）
      ├── problem_zh.md       # 中文题面（无 --- 分隔，含至少 2 组示例）
      ├── testdata/           # 1.in ~ N.in / 1.out ~ N.out
      └── additional_file/    # 1.py / 1.cpp / Main.java（带详细注释）

框架自动扫描根目录下所有含 problems/ 的一级子目录，无需指定分类名。
每个分类目录下会自动生成/更新 list.md（题目列表表格）：已有题目保留原
核心题意与考点，新增题目从定义推导。
约定：input 数据每行一个值；output 每行一个值。
重生成时会先清空对应题目目录、再重写全部产物；定义文件位于各分类的 problems/，不会被清除。

使用：
    python3 generate.py              # 重新生成所有题目
    python3 generate.py P1001 P1002  # 只生成指定题号

也可作为库导入：from generate import make_problem, gen_one, gen_list, fmt2, build_md
"""
import os
import sys
import re
import shutil
import decimal
import importlib.util
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))   # 框架根目录，其下各子目录为题目分类


# ----------------------------------------------------------------------------
# 基础工具
# ----------------------------------------------------------------------------
def w(path, content):
    """写文件，自动创建父目录。"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def fmt2(x):
    """浮点数保留两位小数（四舍五入，与 C printf %.2f 一致）。"""
    d = decimal.Decimal(str(x))
    return f"{d.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)}"


def build_md(desc, input_desc, output_desc, samples,
             limitation="1s, 1024KiB for each test case."):
    """拼装 problem_*.md。samples: [(in_text, out_text), ...] 至少 2 组。"""
    parts = [
        "# Description", desc, "",
        "# Format", "## Input", input_desc, "",
        "## Output", output_desc, "",
        "# Samples", "",
    ]
    for idx, (inp, out) in enumerate(samples, 1):
        parts += [
            f"```input{idx}", inp.rstrip("\n"), "```", "",
            f"```output{idx}", out.rstrip("\n"), "```", "",
        ]
    parts += ["# Limitation", limitation]
    return "\n".join(parts) + "\n"


def make_problem(pid, title, tags, *, cases,
                 desc_en, input_en, output_en,
                 desc_zh, input_zh, output_zh,
                 py, cpp, java, samples=None):
    """组装一道题的全部产物。cases: [(in_text, out_text), ...]。"""
    if samples is None:
        samples = cases[:2]  # 默认取前两组测试数据作为题面示例
    return {
        "pid": pid,
        "yaml": (f"title: {title}\ntag:\n"
                 + "".join(f"- {t}\n" for t in tags)
                 + f"pid: {pid}\n"),
        "en": build_md(desc_en, input_en, output_en, samples),
        "zh": build_md(desc_zh, input_zh, output_zh, samples),
        "cases": cases, "py": py, "cpp": cpp, "java": java,
        "title": title, "tags": tags, "desc_zh": desc_zh,
    }


def gen_one(prob):
    """把一道题写到磁盘（先清空旧目录再重写，幂等）。
    数据写到定义文件所在子目录的 data/ 下；定义文件不受影响。"""
    base = os.path.join(prob["data_dir"], prob["pid"])
    if os.path.exists(base):
        shutil.rmtree(base)
    w(os.path.join(base, "problem.yaml"), prob["yaml"])
    w(os.path.join(base, "problem_en.md"), prob["en"])
    w(os.path.join(base, "problem_zh.md"), prob["zh"])
    for i, (inp, out) in enumerate(prob["cases"], 1):
        w(os.path.join(base, "testdata", f"{i}.in"), inp)
        w(os.path.join(base, "testdata", f"{i}.out"), out)
    w(os.path.join(base, "additional_file", "1.py"), prob["py"])
    w(os.path.join(base, "additional_file", "1.cpp"), prob["cpp"])
    w(os.path.join(base, "additional_file", "Main.java"), prob["java"])


def derive_brief(prob):
    """从中文题面推导核心题意（取第一句）。"""
    desc = prob.get("desc_zh", "")
    for stop in ("。", "；", "\n"):
        idx = desc.find(stop)
        if idx > 0:
            return desc[:idx].strip()
    return desc.strip()


def derive_points(prob):
    """从标签推导考点（跳过通用标签如"入门"）。"""
    tags = prob.get("tags", [])
    pts = [t for t in tags if t != "入门"]
    return "、".join(pts) if pts else (tags[0] if tags else "")


def gen_list(category_dir, problems):
    """为一个分类生成/更新 list.md。
    已有题目保留原核心题意与考点（从现有 list.md 读取）；新题从定义推导。"""
    list_path = os.path.join(category_dir, "list.md")
    existing = {}
    if os.path.exists(list_path):
        with open(list_path, encoding="utf-8") as f:
            for line in f:
                m = re.match(
                    r"\|\s*(P\d+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\s*\|",
                    line)
                if m:
                    existing[m.group(1).strip()] = {
                        "brief": m.group(3).strip(),
                        "points": m.group(4).strip(),
                    }
    probs = sorted(problems, key=lambda x: x["pid"])
    lines = [
        "# 题目列表", "",
        f"共 {len(probs)} 道题，每题 10 组测试用例，均提供 Python / C++ / Java 三语言题解。",
        "",
        "| 题号 | 题目名 | 核心题意 | 考点 |",
        "|------|--------|----------|------|",
    ]
    for p in probs:
        if p["pid"] in existing:
            brief = existing[p["pid"]]["brief"]
            points = existing[p["pid"]]["points"]
        else:
            brief = derive_brief(p)
            points = derive_points(p)
        lines.append(f"| {p['pid']} | {p['title']} | {brief} | {points} |")
    w(list_path, "\n".join(lines) + "\n")


# ----------------------------------------------------------------------------
# 题目发现与入口
# ----------------------------------------------------------------------------
def discover():
    """扫描根目录下所有含 problems/ 的一级子目录，加载其中的 p*.py。
    每道题的 data_dir 指向其定义文件所在子目录的 data/。"""
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    problems = []
    for entry in sorted(os.listdir(ROOT)):
        defs_dir = os.path.join(ROOT, entry, "problems")
        if not os.path.isdir(defs_dir):
            continue
        data_dir = os.path.join(ROOT, entry, "data")
        for path in sorted(glob.glob(os.path.join(defs_dir, "p*.py"))):
            name = os.path.splitext(os.path.basename(path))[0]  # 如 p1001
            spec = importlib.util.spec_from_file_location(name, path)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            if hasattr(m, "build"):
                prob = m.build()
                prob["data_dir"] = data_dir
                problems.append(prob)
    return problems


def main():
    want = set(sys.argv[1:])
    all_problems = discover()
    todo = [p for p in all_problems if not want or p["pid"] in want]
    if not todo:
        print("没有匹配的题目。请在某子目录的 problems/ 下新建 pXXXX.py 并实现 build()。")
        return
    for p in todo:
        gen_one(p)
        print(f"generated {p['pid']}: {len(p['cases'])} cases")
    # 按分类生成/更新 list.md（基于该分类全部题目，保持表格完整）
    by_cat = {}
    for p in all_problems:
        cat_dir = os.path.dirname(p["data_dir"])
        by_cat.setdefault(cat_dir, []).append(p)
    for cat_dir, ps in by_cat.items():
        gen_list(cat_dir, ps)
        print(f"updated {os.path.join(cat_dir, 'list.md')}: {len(ps)} problems")


if __name__ == "__main__":
    main()
