# -*- coding: utf-8 -*-
"""P2083 多重背包"""
from generate import make_problem


def solve(n, V, items):
    # 多重背包参考解：每件最多选 c 次，二进制拆分转 0/1 背包
    f = [0] * (V + 1)
    for w, v, c in items:
        rem = c
        k = 1
        while rem > 0:
            take = min(k, rem)              # 取 take 件作为一组
            ww, vv = w * take, v * take
            for j in range(V, ww - 1, -1):  # 0/1 逆序
                if f[j - ww] + vv > f[j]:
                    f[j] = f[j - ww] + vv
            rem -= take
            k <<= 1
    return f[V]


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v, c in items:
        lines.append(f"{w} {v} {c}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    items = []
    for i in range(n):
        w = (i * 7 + seed) % 25 + 1
        v = (i * 13 + seed * 5 + 3) % 90 + 1
        c = (i * 3 + seed) % 6 + 1          # 数量 1..6
        items.append((w, v, c))
    return items


def build():
    data = [
        (3, 10, [(2, 3, 2), (3, 4, 1), (4, 5, 3)]),
        (2, 10, [(3, 5, 4), (7, 10, 1)]),
        (1, 20, [(3, 7, 5)]),
        (1, 5, [(3, 7, 5)]),
        (4, 15, [(2, 5, 3), (3, 7, 2), (5, 12, 1), (1, 2, 10)]),
        (5, 25, [(4, 9, 3), (5, 10, 2), (6, 13, 4), (3, 6, 5), (2, 4, 6)]),
        (6, 30, [(3, 4, 4), (5, 8, 3), (7, 11, 2), (2, 3, 6), (4, 7, 3), (6, 10, 2)]),
        (15, 300, gen(15, 9)),
        (30, 600, gen(30, 17)),
        (50, 1000, gen(50, 29)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2083", "多重背包", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w, value v, and available count c, "
                "and a knapsack of capacity V, each item may be chosen at most c times. "
                "Find the maximum total value that can be put into the knapsack.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain three integers w, v and c. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$, $1\\leq c\\leq 100$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 个物品（每个物品有重量 w、价值 v 和数量 c）和一个容量为 V 的背包，每件物品最多选 c 次，求能装入的最大总价值。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行三个整数 w、v、c。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$，$1\\leq c\\leq 100$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2083 多重背包\n"
            "# 每件最多选 c 次，二进制拆分转 0/1 背包\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0]*n; v = [0]*n; c = [0]*n\n"
            "for i in range(n):                        # 读入每个物品的重量、价值、数量\n"
            "    w[i], v[i], c[i] = map(int, input().split())\n"
            "f = [0] * (V + 1)                         # f[j] 表示容量 j 的最大价值\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    rem = c[i]; k = 1\n"
            "    while rem > 0:                        # 二进制拆分\n"
            "        take = min(k, rem)                # 取 take 件为一组\n"
            "        ww, vv = w[i]*take, v[i]*take\n"
            "        for j in range(V, ww - 1, -1):    # 0/1 逆序更新\n"
            "            if f[j - ww] + vv > f[j]:\n"
            "                f[j] = f[j - ww] + vv\n"
            "        rem -= take; k <<= 1\n"
            "print(f[V])                               # 输出容量 V 的最大价值\n"),
        cpp=("// P2083 多重背包\n"
             "#include <iostream>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105], c[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i] >> c[i];\n"
             "    int f[1005] = {0};                    // f[j] 表示容量 j 的最大价值\n"
             "    for (int i = 0; i < n; ++i) {         // 枚举每件物品\n"
             "        int rem = c[i], k = 1;\n"
             "        while (rem > 0) {                 // 二进制拆分\n"
             "            int take = min(k, rem);       // 取 take 件为一组\n"
             "            int ww = w[i]*take, vv = v[i]*take;\n"
             "            for (int j = V; j >= ww; --j) // 0/1 逆序更新\n"
             "                if (f[j - ww] + vv > f[j])\n"
             "                    f[j] = f[j - ww] + vv;\n"
             "            rem -= take; k <<= 1;\n"
             "        }\n"
             "    }\n"
             "    cout << f[V] << endl;                 // 输出容量 V 的最大价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2083 多重背包\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n], c = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); c[i] = sc.nextInt(); }\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示容量 j 的最大价值\n"
              "        for (int i = 0; i < n; ++i) {             // 枚举每件物品\n"
              "            int rem = c[i], k = 1;\n"
              "            while (rem > 0) {                     // 二进制拆分\n"
              "                int take = Math.min(k, rem);      // 取 take 件为一组\n"
              "                int ww = w[i]*take, vv = v[i]*take;\n"
              "                for (int j = V; j >= ww; --j)     // 0/1 逆序更新\n"
              "                    if (f[j - ww] + vv > f[j])\n"
              "                        f[j] = f[j - ww] + vv;\n"
              "                rem -= take; k <<= 1;\n"
              "            }\n"
              "        }\n"
              "        System.out.println(f[V]);                 // 输出容量 V 的最大价值\n"
              "    }\n"
              "}\n"),
    )
