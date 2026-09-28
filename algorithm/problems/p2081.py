# -*- coding: utf-8 -*-
"""P2081 0/1背包"""
from generate import make_problem


def solve(n, V, items):
    # 0/1 背包参考解：每件物品最多选一次，求容量 V 内的最大价值
    f = [0] * (V + 1)
    for w, v in items:
        for j in range(V, w - 1, -1):          # 逆序更新保证每件只选一次
            if f[j - w] + v > f[j]:
                f[j] = f[j - w] + v
    return f[V]


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v in items:
        lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    # 确定性生成 n 个物品，保证可复现
    items = []
    for i in range(n):
        w = (i * 7 + seed) % 30 + 1
        v = (i * 13 + seed * 5 + 3) % 100 + 1
        items.append((w, v))
    return items


def build():
    data = [
        (3, 10, [(2, 3), (3, 4), (4, 5)]),
        (4, 5, [(1, 2), (2, 3), (3, 4), (4, 5)]),
        (1, 10, [(5, 7)]),
        (1, 3, [(5, 7)]),
        (5, 10, [(5, 10), (4, 40), (3, 50), (2, 30), (1, 20)]),
        (6, 20, [(10, 60), (5, 50), (5, 50), (3, 20), (2, 30), (4, 40)]),
        (8, 15, [(2, 3), (3, 4), (4, 5), (5, 8), (6, 10), (1, 2), (7, 14), (2, 5)]),
        (15, 80, gen(15, 11)),
        (30, 300, gen(30, 23)),
        (50, 500, gen(50, 37)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2081", "0/1背包", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w and value v, and a knapsack of "
                "capacity V, each item may be chosen at most once. Find the maximum "
                "total value that can be put into the knapsack.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain two integers w and v. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 个物品（每个物品有重量 w 和价值 v）和一个容量为 V 的背包，每件物品最多选一次，求能装入的最大总价值。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2081 0/1背包\n"
            "# 每件物品最多选一次，一维 dp 逆序更新\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0] * n; v = [0] * n\n"
            "for i in range(n):                        # 读入每个物品的重量与价值\n"
            "    w[i], v[i] = map(int, input().split())\n"
            "f = [0] * (V + 1)                         # f[j] 表示容量 j 的最大价值\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    for j in range(V, w[i] - 1, -1):      # 逆序保证每件只选一次\n"
            "        if f[j - w[i]] + v[i] > f[j]:\n"
            "            f[j] = f[j - w[i]] + v[i]\n"
            "print(f[V])                               # 输出容量 V 的最大价值\n"),
        cpp=("// P2081 0/1背包\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];\n"
             "    int f[1005] = {0};                    // f[j] 表示容量 j 的最大价值\n"
             "    for (int i = 0; i < n; ++i)           // 枚举每件物品\n"
             "        for (int j = V; j >= w[i]; --j)   // 逆序保证每件只选一次\n"
             "            if (f[j - w[i]] + v[i] > f[j])\n"
             "                f[j] = f[j - w[i]] + v[i];\n"
             "    cout << f[V] << endl;                 // 输出容量 V 的最大价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2081 0/1背包\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); }\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示容量 j 的最大价值\n"
              "        for (int i = 0; i < n; ++i)               // 枚举每件物品\n"
              "            for (int j = V; j >= w[i]; --j)       // 逆序保证每件只选一次\n"
              "                if (f[j - w[i]] + v[i] > f[j])\n"
              "                    f[j] = f[j - w[i]] + v[i];\n"
              "        System.out.println(f[V]);                 // 输出容量 V 的最大价值\n"
              "    }\n"
              "}\n"),
    )
