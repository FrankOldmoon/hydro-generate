# -*- coding: utf-8 -*-
"""P2085 背包方案数"""
from generate import make_problem


def solve(n, V, items):
    # 0/1 背包方案数：求总重量恰好等于 V 的不同选取方案数
    f = [0] * (V + 1)
    f[0] = 1                               # 容量 0 有 1 种方案（什么都不选）
    for w, v in items:
        for j in range(V, w - 1, -1):      # 0/1 逆序
            f[j] += f[j - w]
    return f[V]


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v in items:
        lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    # 权重较小，保证方案数非平凡且在 long 范围内
    items = []
    for i in range(n):
        w = (i * 3 + seed) % 10 + 1        # 1..10
        v = (i * 7 + seed * 2) % 50 + 1
        items.append((w, v))
    return items


def build():
    data = [
        (4, 5, [(1, 1), (2, 1), (3, 1), (4, 1)]),
        (3, 4, [(1, 1), (2, 1), (3, 1)]),
        (5, 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
        (3, 2, [(5, 1), (6, 1), (7, 1)]),
        (6, 8, [(2, 5), (3, 7), (5, 12), (1, 2), (4, 9), (6, 11)]),
        (8, 10, [(1, 3), (2, 5), (3, 7), (4, 9), (5, 2), (2, 4), (1, 6), (3, 8)]),
        (10, 15, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        (15, 30, gen(15, 3)),
        (20, 40, gen(20, 8)),
        (25, 50, gen(25, 14)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2085", "背包方案数", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w and value v, and a knapsack of "
                "capacity V, each item may be chosen at most once. Count the number of "
                "different subsets whose total weight is exactly V.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain two integers w and v. Constraints: $1\\leq n\\leq 30$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="One line with a single integer: the number of subsets with total "
                  "weight exactly V.",
        desc_zh="给定 n 个物品（每个物品有重量 w 和价值 v）和一个容量为 V 的背包，每件物品最多选一次，求总重量恰好等于 V 的不同选取方案数。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 30$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="一行一个整数，表示总重量恰好等于 V 的方案数。",
        py=("# P2085 背包方案数\n"
            "# 0/1 背包：f[j] 表示总重量恰为 j 的方案数\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0] * n; v = [0] * n\n"
            "for i in range(n):                        # 读入每个物品\n"
            "    w[i], v[i] = map(int, input().split())\n"
            "f = [0] * (V + 1)                         # f[j] 表示重量恰为 j 的方案数\n"
            "f[0] = 1                                  # 重量 0 有 1 种方案\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    for j in range(V, w[i] - 1, -1):      # 0/1 逆序更新\n"
            "        f[j] += f[j - w[i]]\n"
            "print(f[V])                               # 输出重量恰为 V 的方案数\n"),
        cpp=("// P2085 背包方案数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[35], v[35];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];\n"
             "    long long f[1005] = {0};              // f[j] 表示重量恰为 j 的方案数\n"
             "    f[0] = 1;                             // 重量 0 有 1 种方案\n"
             "    for (int i = 0; i < n; ++i)           // 枚举每件物品\n"
             "        for (int j = V; j >= w[i]; --j)   // 0/1 逆序更新\n"
             "            f[j] += f[j - w[i]];\n"
             "    cout << f[V] << endl;                 // 输出重量恰为 V 的方案数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2085 背包方案数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); }\n"
              "        long[] f = new long[V + 1];               // f[j] 表示重量恰为 j 的方案数\n"
              "        f[0] = 1;                                 // 重量 0 有 1 种方案\n"
              "        for (int i = 0; i < n; ++i)               // 枚举每件物品\n"
              "            for (int j = V; j >= w[i]; --j)       // 0/1 逆序更新\n"
              "                f[j] += f[j - w[i]];\n"
              "        System.out.println(f[V]);                 // 输出重量恰为 V 的方案数\n"
              "    }\n"
              "}\n"),
    )
