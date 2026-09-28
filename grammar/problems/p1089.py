# -*- coding: utf-8 -*-
"""P1089 出现次数最多的数"""
from generate import make_problem


def build():
    data = [
        (5, [1, 2, 2, 3, 3]),
        (5, [1, 1, 2, 2, 2]),
        (1, [5]),
        (3, [1, 1, 1]),
        (6, [3, 3, 2, 2, 1, 1]),
        (4, [1, 2, 3, 4]),
        (7, [5, 5, 5, 3, 3, 3, 1]),
        (2, [10, 20]),
        (8, [1, 2, 1, 2, 1, 2, 3, 3]),
        (6, [4, 4, 4, 4, 5, 5]),
    ]

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        best_x = None
        best_cnt = 0
        for x in sorted(d.keys()):
            if d[x] > best_cnt:
                best_cnt = d[x]
                best_x = x
        cases.append((inp, f"{best_x}\n"))
    return make_problem(
        "P1089", "出现次数最多的数", ["入门", "字典"],
        cases=cases,
        desc_en="Given n integers, find the one that appears most frequently. If "
                "there is a tie, choose the smallest value.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain an integer.",
        output_en="One line: the most frequent value (smallest if tied).",
        desc_zh="给定 n 个整数，输出出现次数最多的数。若有多个出现次数相同，取最小的。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个整数。",
        output_zh="一行，输出出现次数最多的数（次数相同取最小值）。",
        py=("# P1089 出现次数最多的数（dict 统计频次后找最大）\n"
            "n = int(input())              # 个数 n\n"
            "d = {}                        # 字典统计频次\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    d[x] = d.get(x, 0) + 1\n"
            "best_x = 0\n"
            "best_cnt = 0\n"
            "for x in sorted(d.keys()):   # 按 key 升序遍历\n"
            "    if d[x] > best_cnt:      # 严格大于才更新（相同保留较小的）\n"
            "        best_cnt = d[x]\n"
            "        best_x = x\n"
            "print(best_x)\n"),
        cpp=("// P1089 出现次数最多的数\n"
             "#include <iostream>\n"
             "#include <map>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    map<int, int> d;          // map 自动按 key 排序\n"
             "    for (int i = 0; i < n; ++i) { int x; cin >> x; d[x]++; }\n"
             "    int bestX = 0, bestCnt = 0;\n"
             "    for (auto &p : d)         // 升序遍历\n"
             "        if (p.second > bestCnt) { bestCnt = p.second; bestX = p.first; }\n"
             "    cout << bestX << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1089 出现次数最多的数\n"
              "import java.util.Scanner;\n"
              "import java.util.TreeMap;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        TreeMap<Integer, Integer> d = new TreeMap<>();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            d.put(x, d.getOrDefault(x, 0) + 1);\n"
              "        }\n"
              "        int bestX = 0, bestCnt = 0;\n"
              "        for (int x : d.keySet())       // 升序遍历\n"
              "            if (d.get(x) > bestCnt) { bestCnt = d.get(x); bestX = x; }\n"
              "        System.out.println(bestX);\n"
              "    }\n"
              "}\n"),
    )
