# -*- coding: utf-8 -*-
"""P2087 背包最大价值（完全背包）"""
from generate import make_problem


def solve(n, V, items):
    # 完全背包参考解：每件物品可选无限次，正序更新
    f = [0] * (V + 1)
    for w, v in items:
        for j in range(w, V + 1):            # 正序：每件可选无限次
            if f[j - w] + v > f[j]:
                f[j] = f[j - w] + v
    return f[V]


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v in items:
        lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    items = []
    for i in range(n):
        w = (i * 5 + seed) % 18 + 1
        v = (i * 11 + seed * 3 + 1) % 70 + 1
        items.append((w, v))
    return items


def build():
    data = [
        (4, 10, [(1, 2), (2, 3), (3, 4), (4, 5)]),
        (3, 15, [(2, 5), (3, 7), (5, 12)]),
        (1, 18, [(4, 9)]),
        (1, 3, [(4, 9)]),
        (5, 30, [(3, 8), (5, 13), (7, 18), (2, 5), (4, 10)]),
        (6, 40, [(4, 7), (6, 11), (8, 15), (3, 5), (5, 9), (7, 13)]),
        (8, 25, [(2, 3), (3, 5), (4, 7), (5, 9), (6, 11), (7, 13), (1, 2), (8, 15)]),
        (20, 400, gen(20, 4)),
        (40, 700, gen(40, 12)),
        (60, 1000, gen(60, 27)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2087", "背包最大价值", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w and value v, and a knapsack of "
                "capacity V, each item may be chosen an unlimited number of times. "
                "Find the maximum total value that can be put into the knapsack.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain two integers w and v. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 个物品（每个物品有重量 w 和价值 v）和一个容量为 V 的背包，每件物品可选无限次，求能装入的最大总价值。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2087 背包最大价值（完全背包）\n"
            "# 每件物品可选无限次，一维 dp 正序更新\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0] * n; v = [0] * n\n"
            "for i in range(n):                        # 读入每个物品的重量与价值\n"
            "    w[i], v[i] = map(int, input().split())\n"
            "f = [0] * (V + 1)                         # f[j] 表示容量 j 的最大价值\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    for j in range(w[i], V + 1):          # 正序：每件可选无限次\n"
            "        if f[j - w[i]] + v[i] > f[j]:\n"
            "            f[j] = f[j - w[i]] + v[i]\n"
            "print(f[V])                               # 输出容量 V 的最大价值\n"),
        cpp=("// P2087 背包最大价值（完全背包）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];\n"
             "    int f[1005] = {0};                    // f[j] 表示容量 j 的最大价值\n"
             "    for (int i = 0; i < n; ++i)           // 枚举每件物品\n"
             "        for (int j = w[i]; j <= V; ++j)   // 正序：每件可选无限次\n"
             "            if (f[j - w[i]] + v[i] > f[j])\n"
             "                f[j] = f[j - w[i]] + v[i];\n"
             "    cout << f[V] << endl;                 // 输出容量 V 的最大价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2087 背包最大价值（完全背包）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); }\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示容量 j 的最大价值\n"
              "        for (int i = 0; i < n; ++i)               // 枚举每件物品\n"
              "            for (int j = w[i]; j <= V; ++j)       // 正序：每件可选无限次\n"
              "                if (f[j - w[i]] + v[i] > f[j])\n"
              "                    f[j] = f[j - w[i]] + v[i];\n"
              "        System.out.println(f[V]);                 // 输出容量 V 的最大价值\n"
              "    }\n"
              "}\n"),
    )
