# 目录结构

题目「定义」与「生成产物」分离存放：

```
hydro_problems/
├── generate.py            # 通用生成框架（扫描 problems/p*.py，输出到 data/P*/）
├── index.md               # 本说明
├── problems/              # 题目定义（每题一个 pXXXX.py）
│   ├── p1001.py
│   ├── p1002.py
│   └── ...
└── data/                  # 生成的题目数据（每题一个目录）
    └── 题目编号(P+数字编号)/
        ├── problem.yaml
        ├── problem_en.md
        ├── problem_zh.md
        ├── testdata/
        │   ├── 1.in
        │   ├── 1.out
        │   ├── 2.in
        │   ├── 2.out
        │   ├── 3.in
        │   └── 3.out
        └── additional_file/
            ├── 1.py
            ├── 1.cpp
            └── 1.java
```

## problems/
problems/ 文件夹集中存储各题目的生成定义文件，每题一个，以题号小写命名（如 `p1001.py`）：
- `pXXXX.py`：该题目的生成定义文件，实现 `build()` 返回 `make_problem(...)`，供根目录 `generate.py` 框架扫描调用以重新生成本题。
  定义文件集中存放，重生成 `data/` 时不会被清除。

## data/
data/ 文件夹存储生成的题目数据，每题一个目录（`P+数字编号`）。重生成时会先清空对应题目目录再重写，幂等。

## additional_file
additional_file 文件夹里存储题目正确答案的代码文件，共 3 个文件：
- `1.py` / `1.cpp` / `1.java`：分别是 python、cpp、java 的正确答案代码，带详细注释

## problem.yaml
problem.yaml 文件里存储的是题目的一些基本信息，包括题目名、标签、题号等，内容如下：
```
title: 题目名
tag:
- 标签1
- 标签2
pid: 题号（P+数字）
```

## problem_en.md / problem_zh.md
problem_en.md（英文题目）和 problem_zh.md（中文题目）两个文件里的内容参考格式（生成时不要带 `---`），input 的数据每行一个值，题目中至少有两组 input 和 output 示例：

```
# Description
Given two integers x and y, print the sum.

# Format
## Input
Two integers x and y, satisfying $0\leq x,y\leq 32767$ .

## Output
One integer, the sum of x and y.

# Samples

```input1
123
500
```

```output1
623
```

# Limitation
1s, 1024KiB for each test case.
```

## 使用
```
python3 generate.py              # 重新生成所有题目
python3 generate.py P1001 P1002  # 只生成指定题号
```
