# -*- coding: utf-8 -*-
"""P2086 恰好装满最小价值"""
from generate import make_problem


def solve(n, V, items):
    # 0/1 背包求恰好装满容量 V 的最小价值，无法装满返回 -1
    INF = float('inf')
    f = [INF] * (V + 1)
    f[0] = 0                                # 容量 0 价值 0
    for w, v in items:
        for j in range(V, w - 1, -1):       # 0/1 逆序
            if f[j - w] + v < f[j]:
                f[j] = f[j - w] + v
    return f[V] if f[V] != INF else -1


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v in items:
        lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    items = []
    for i in range(n):
        w = (i * 7 + seed) % 25 + 1
        v = (i * 13 + seed * 5 + 3) % 90 + 1
        items.append((w, v))
    return items


def build():
    data = [
        (3, 5, [(2, 3), (3, 4), (5, 10)]),
        (3, 4, [(2, 3), (3, 4), (5, 10)]),
        (1, 5, [(5, 7)]),
        (1, 4, [(5, 7)]),
        (4, 10, [(2, 3), (3, 4), (5, 6), (4, 5)]),
        (5, 7, [(2, 3), (2, 5), (3, 4), (3, 6), (4, 7)]),
        (6, 12, [(5, 10), (5, 8), (2, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 23, [(5, 3), (10, 5), (15, 8), (20, 10)]),
        (20, 60, gen(20, 6)),
        (40, 120, gen(40, 15)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2086", "恰好装满最小价值", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w and value v, and a knapsack of "
                "capacity V, each item may be chosen at most once. Find the minimum "
                "total value such that the total weight is exactly V. If it is "
                "impossible to fill exactly V, output -1.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain two integers w and v. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="One line with a single integer: the minimum total value to exactly "
                  "fill V, or -1 if impossible.",
        desc_zh="给定 n 个物品（每个物品有重量 w 和价值 v）和一个容量为 V 的背包，每件物品最多选一次，求总重量恰好等于 V 时的最小总价值，无法恰好装满则输出 -1。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="一行一个整数，表示恰好装满 V 的最小总价值；若无法恰好装满输出 -1。",
        py=("# P2086 恰好装满最小价值\n"
            "# 0/1 背包求恰好装满的最小价值，INF 表示不可达\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0] * n; v = [0] * n\n"
            "for i in range(n):                        # 读入每个物品\n"
            "    w[i], v[i] = map(int, input().split())\n"
            "INF = 10 ** 9\n"
            "f = [INF] * (V + 1)                       # f[j] 表示恰好装满 j 的最小价值\n"
            "f[0] = 0                                  # 容量 0 价值 0\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    for j in range(V, w[i] - 1, -1):      # 0/1 逆序更新\n"
            "        if f[j - w[i]] + v[i] < f[j]:\n"
            "            f[j] = f[j - w[i]] + v[i]\n"
            "print(-1 if f[V] >= INF else f[V])        # 不可达输出 -1\n"),
        cpp=("// P2086 恰好装满最小价值\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];\n"
             "    const int INF = 1000000000;\n"
             "    int f[1005];                         // f[j] 表示恰好装满 j 的最小价值\n"
             "    for (int j = 0; j <= V; ++j) f[j] = INF;\n"
             "    f[0] = 0;                            // 容量 0 价值 0\n"
             "    for (int i = 0; i < n; ++i)          // 枚举每件物品\n"
             "        for (int j = V; j >= w[i]; --j)  // 0/1 逆序更新\n"
             "            if (f[j - w[i]] + v[i] < f[j])\n"
             "                f[j] = f[j - w[i]] + v[i];\n"
             "    cout << (f[V] >= INF ? -1 : f[V]) << endl;  // 不可达输出 -1\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2086 恰好装满最小价值\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); }\n"
              "        final int INF = 1000000000;\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示恰好装满 j 的最小价值\n"
              "        for (int j = 0; j <= V; ++j) f[j] = INF;\n"
              "        f[0] = 0;                                 // 容量 0 价值 0\n"
              "        for (int i = 0; i < n; ++i)               // 枚举每件物品\n"
              "            for (int j = V; j >= w[i]; --j)       // 0/1 逆序更新\n"
              "                if (f[j - w[i]] + v[i] < f[j])\n"
              "                    f[j] = f[j - w[i]] + v[i];\n"
              "        System.out.println(f[V] >= INF ? -1 : f[V]);  // 不可达输出 -1\n"
              "    }\n"
              "}\n"),
    )
