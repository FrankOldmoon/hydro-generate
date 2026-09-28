# -*- coding: utf-8 -*-
"""P2088 二维费用背包"""
from generate import make_problem


def solve(n, V, W, items):
    # 二维费用 0/1 背包：体积不超过 V、重量不超过 W，每件最多选一次
    f = [[0] * (W + 1) for _ in range(V + 1)]
    for v, w, val in items:                 # v=体积, w=重量, val=价值
        for j in range(V, v - 1, -1):       # 体积逆序
            for k in range(W, w - 1, -1):   # 重量逆序
                if f[j - v][k - w] + val > f[j][k]:
                    f[j][k] = f[j - v][k - w] + val
    return f[V][W]


def make_input(n, V, W, items):
    lines = [f"{n} {V} {W}"]
    for v, w, val in items:
        lines.append(f"{v} {w} {val}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    items = []
    for i in range(n):
        v = (i * 7 + seed) % 20 + 1         # 体积 1..20
        w = (i * 11 + seed * 3) % 20 + 1     # 重量 1..20
        val = (i * 13 + seed * 5 + 3) % 90 + 1
        items.append((v, w, val))
    return items


def build():
    data = [
        (3, 10, 10, [(2, 3, 4), (3, 4, 5), (4, 5, 6)]),
        (2, 5, 5, [(2, 3, 10), (3, 2, 12)]),
        (1, 10, 10, [(5, 5, 7)]),
        (1, 4, 4, [(5, 5, 7)]),
        (5, 15, 15, [(2, 3, 8), (3, 4, 10), (5, 6, 15), (4, 2, 9), (1, 5, 6)]),
        (6, 20, 20, [(3, 4, 11), (5, 6, 18), (4, 3, 12), (6, 5, 20), (2, 2, 7), (7, 8, 25)]),
        (8, 25, 25, [(2, 3, 6), (3, 5, 9), (4, 7, 12), (5, 2, 10), (6, 4, 14), (7, 6, 16), (1, 1, 3), (8, 9, 20)]),
        (20, 80, 80, gen(20, 4)),
        (35, 100, 100, gen(35, 11)),
        (50, 100, 100, gen(50, 19)),
    ]
    cases = [(make_input(n, V, W, items), f"{solve(n, V, W, items)}\n")
             for n, V, W, items in data]
    return make_problem(
        "P2088", "二维费用背包", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with volume v, weight w, and value val, and a "
                "knapsack with volume capacity V and weight capacity W, each item may "
                "be chosen at most once. Find the maximum total value such that the "
                "total volume does not exceed V and the total weight does not exceed W.",
        input_en="The first line contains three integers n, V and W. The following n "
                 "lines each contain three integers v, w and val. Constraints: "
                 "$1\\leq n\\leq 100$, $1\\leq V\\leq 1000$, $1\\leq W\\leq 1000$, "
                 "$1\\leq v\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq val\\leq 1000$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 个物品（每个物品有体积 v、重量 w 和价值 val）和一个背包，背包体积上限为 V、重量上限为 W，每件物品最多选一次，求总体积不超过 V 且总重量不超过 W 时的最大总价值。",
        input_zh="第一行三个整数 n、V、W。接下来 n 行每行三个整数 v、w、val。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq W\\leq 1000$，$1\\leq v\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq val\\leq 1000$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2088 二维费用背包\n"
            "# 0/1 背包加一维费用：f[j][k] 体积 j、重量 k 的最大价值\n"
            "n, V, W = map(int, input().split())       # 读入物品数、体积上限、重量上限\n"
            "v = [0]*n; w = [0]*n; val = [0]*n\n"
            "for i in range(n):                        # 读入每个物品\n"
            "    v[i], w[i], val[i] = map(int, input().split())\n"
            "f = [[0] * (W + 1) for _ in range(V + 1)] # f[j][k] 体积 j、重量 k 的最大价值\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    for j in range(V, v[i] - 1, -1):      # 体积逆序（0/1）\n"
            "        for k in range(W, w[i] - 1, -1):  # 重量逆序（0/1）\n"
            "            if f[j - v[i]][k - w[i]] + val[i] > f[j][k]:\n"
            "                f[j][k] = f[j - v[i]][k - w[i]] + val[i]\n"
            "print(f[V][W])                             # 输出最大总价值\n"),
        cpp=("// P2088 二维费用背包\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V, W;\n"
             "    cin >> n >> V >> W;                   // 读入物品数、体积上限、重量上限\n"
             "    int v[105], w[105], val[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> v[i] >> w[i] >> val[i];\n"
             "    int f[1005][1005];                    // f[j][k] 体积 j、重量 k 的最大价值\n"
             "    for (int j = 0; j <= V; ++j)\n"
             "        for (int k = 0; k <= W; ++k) f[j][k] = 0;\n"
             "    for (int i = 0; i < n; ++i)           // 枚举每件物品\n"
             "        for (int j = V; j >= v[i]; --j)   // 体积逆序（0/1）\n"
             "            for (int k = W; k >= w[i]; --k) // 重量逆序（0/1）\n"
             "                if (f[j - v[i]][k - w[i]] + val[i] > f[j][k])\n"
             "                    f[j][k] = f[j - v[i]][k - w[i]] + val[i];\n"
             "    cout << f[V][W] << endl;              // 输出最大总价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2088 二维费用背包\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt(), W = sc.nextInt();\n"
              "        int[] v = new int[n], w = new int[n], val = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { v[i] = sc.nextInt(); w[i] = sc.nextInt(); val[i] = sc.nextInt(); }\n"
              "        int[][] f = new int[V + 1][W + 1];            // f[j][k] 体积 j、重量 k 的最大价值\n"
              "        for (int i = 0; i < n; ++i)                   // 枚举每件物品\n"
              "            for (int j = V; j >= v[i]; --j)           // 体积逆序（0/1）\n"
              "                for (int k = W; k >= w[i]; --k)       // 重量逆序（0/1）\n"
              "                    if (f[j - v[i]][k - w[i]] + val[i] > f[j][k])\n"
              "                        f[j][k] = f[j - v[i]][k - w[i]] + val[i];\n"
              "        System.out.println(f[V][W]);                  // 输出最大总价值\n"
              "    }\n"
              "}\n"),
    )
