# -*- coding: utf-8 -*-
"""P2084 分组背包"""
from generate import make_problem


def solve(n, V, groups):
    # 分组背包参考解：每组最多选一件，组内枚举物品、容量逆序
    f = [0] * (V + 1)
    for g in groups:
        for j in range(V, -1, -1):          # 容量逆序（保证每组只更新一次）
            for w, v in g:
                if j >= w and f[j - w] + v > f[j]:
                    f[j] = f[j - w] + v
    return f[V]


def make_input(n, V, groups):
    lines = [f"{n} {V}"]
    for g in groups:
        lines.append(str(len(g)))
        for w, v in g:
            lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen_groups(n, seed):
    groups = []
    for i in range(n):
        k = (i + seed) % 4 + 1              # 每组 1..4 件
        g = []
        for t in range(k):
            w = (i * 7 + t * 3 + seed) % 25 + 1
            v = (i * 13 + t * 5 + seed * 2) % 90 + 1
            g.append((w, v))
        groups.append(g)
    return groups


def build():
    data = [
        (2, 10, [[(2, 3), (3, 5)], [(4, 6), (5, 8)]]),
        (3, 8, [[(1, 2)], [(2, 3), (3, 4)], [(4, 7)]]),
        (1, 10, [[(5, 7), (3, 4)]]),
        (1, 2, [[(5, 7)]]),
        (4, 15, [[(2, 5), (3, 6)], [(4, 9)], [(1, 2), (5, 11)], [(3, 7), (6, 13)]]),
        (5, 20, [[(3, 8), (5, 10)], [(2, 4), (4, 7)], [(6, 13)], [(1, 3), (7, 15)], [(4, 9), (8, 17)]]),
        (6, 25, [[(2, 5)], [(3, 7), (6, 12)], [(4, 8)], [(5, 10), (1, 2)], [(7, 14)], [(3, 6), (8, 16)]]),
        (15, 200, gen_groups(15, 5)),
        (30, 500, gen_groups(30, 13)),
        (50, 800, gen_groups(50, 21)),
    ]
    cases = [(make_input(n, V, groups), f"{solve(n, V, groups)}\n")
             for n, V, groups in data]
    return make_problem(
        "P2084", "分组背包", ["算法", "背包"],
        cases=cases,
        desc_en="Given n groups of items and a knapsack of capacity V, each group "
                "contains several items (each with weight w and value v). At most one "
                "item may be chosen from each group. Find the maximum total value.",
        input_en="The first line contains two integers n and V. For each group: a line "
                 "with an integer k (number of items in the group), followed by k lines "
                 "each containing two integers w and v. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq k\\leq 10$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 组物品和一个容量为 V 的背包，每组有若干物品（每个物品有重量 w 和价值 v），每组最多选一件，求能装入的最大总价值。",
        input_zh="第一行两个整数 n 和 V。接下来依次描述 n 组：每组第一行一个整数 k 表示该组物品数，随后 k 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq k\\leq 10$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2084 分组背包\n"
            "# 每组最多选一件：容量逆序、组内枚举物品\n"
            "n, V = map(int, input().split())          # 读入组数与容量\n"
            "groups = []\n"
            "for _ in range(n):                        # 读入每组物品\n"
            "    k = int(input())\n"
            "    g = []\n"
            "    for _ in range(k):\n"
            "        w, v = map(int, input().split())\n"
            "        g.append((w, v))\n"
            "    groups.append(g)\n"
            "f = [0] * (V + 1)                         # f[j] 表示容量 j 的最大价值\n"
            "for g in groups:                          # 枚举每组\n"
            "    for j in range(V, -1, -1):            # 容量逆序保证每组只选一件\n"
            "        for w, v in g:                    # 组内枚举每件物品\n"
            "            if j >= w and f[j - w] + v > f[j]:\n"
            "                f[j] = f[j - w] + v\n"
            "print(f[V])                               # 输出容量 V 的最大价值\n"),
        cpp=("// P2084 分组背包\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入组数与容量\n"
             "    int f[1005] = {0};                    // f[j] 表示容量 j 的最大价值\n"
             "    for (int gi = 0; gi < n; ++gi) {      // 枚举每组\n"
             "        int k; cin >> k;\n"
             "        vector<int> w(k), v(k);\n"
             "        for (int t = 0; t < k; ++t) cin >> w[t] >> v[t];\n"
             "        for (int j = V; j >= 0; --j)      // 容量逆序保证每组只选一件\n"
             "            for (int t = 0; t < k; ++t)   // 组内枚举每件物品\n"
             "                if (j >= w[t] && f[j - w[t]] + v[t] > f[j])\n"
             "                    f[j] = f[j - w[t]] + v[t];\n"
             "    }\n"
             "    cout << f[V] << endl;                 // 输出容量 V 的最大价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2084 分组背包\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入组数与容量\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示容量 j 的最大价值\n"
              "        for (int gi = 0; gi < n; ++gi) {          // 枚举每组\n"
              "            int k = sc.nextInt();\n"
              "            int[] w = new int[k], v = new int[k];\n"
              "            for (int t = 0; t < k; ++t) { w[t] = sc.nextInt(); v[t] = sc.nextInt(); }\n"
              "            for (int j = V; j >= 0; --j)          // 容量逆序保证每组只选一件\n"
              "                for (int t = 0; t < k; ++t)       // 组内枚举每件物品\n"
              "                    if (j >= w[t] && f[j - w[t]] + v[t] > f[j])\n"
              "                        f[j] = f[j - w[t]] + v[t];\n"
              "        }\n"
              "        System.out.println(f[V]);                 // 输出容量 V 的最大价值\n"
              "    }\n"
              "}\n"),
    )
