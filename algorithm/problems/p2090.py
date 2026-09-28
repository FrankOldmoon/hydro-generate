# -*- coding: utf-8 -*-
"""P2090 混合背包"""
from generate import make_problem


def solve(n, V, items):
    # 混合背包：t=0 为 0/1 背包（逆序），t=1 为完全背包（正序）
    f = [0] * (V + 1)
    for w, v, t in items:
        if t == 0:                            # 0/1：逆序更新
            for j in range(V, w - 1, -1):
                if f[j - w] + v > f[j]:
                    f[j] = f[j - w] + v
        else:                                 # 完全：正序更新
            for j in range(w, V + 1):
                if f[j - w] + v > f[j]:
                    f[j] = f[j - w] + v
    return f[V]


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v, t in items:
        lines.append(f"{w} {v} {t}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
    items = []
    for i in range(n):
        w = (i * 7 + seed) % 20 + 1
        v = (i * 13 + seed * 5 + 3) % 80 + 1
        t = (i + seed) % 2                    # 0 表示 0/1，1 表示完全
        items.append((w, v, t))
    return items


def build():
    data = [
        (3, 10, [(2, 3, 0), (3, 4, 1), (4, 5, 0)]),
        (2, 10, [(3, 5, 1), (7, 10, 0)]),
        (1, 20, [(3, 7, 1)]),
        (1, 2, [(3, 7, 1)]),
        (5, 20, [(2, 5, 0), (3, 7, 1), (5, 12, 0), (1, 2, 1), (4, 9, 0)]),
        (6, 25, [(3, 4, 1), (5, 8, 0), (7, 11, 1), (2, 3, 0), (4, 7, 1), (6, 10, 0)]),
        (8, 30, [(2, 3, 0), (3, 5, 1), (4, 7, 0), (5, 9, 1), (6, 11, 0), (7, 13, 1), (1, 2, 0), (8, 15, 1)]),
        (20, 400, gen(20, 4)),
        (40, 700, gen(40, 12)),
        (60, 1000, gen(60, 27)),
    ]
    cases = [(make_input(n, V, items), f"{solve(n, V, items)}\n")
             for n, V, items in data]
    return make_problem(
        "P2090", "混合背包", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items and a knapsack of capacity V. Each item has weight w, "
                "value v, and a type t: t=0 means it may be chosen at most once (0/1), "
                "t=1 means it may be chosen an unlimited number of times (complete). "
                "Find the maximum total value that can be put into the knapsack.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain three integers w, v and t. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$, $t\\in\\{0,1\\}$.",
        output_en="One line with a single integer: the maximum total value.",
        desc_zh="给定 n 个物品（每个物品有重量 w、价值 v 和类型 t）和一个容量为 V 的背包，t=0 表示该物品最多选一次（0/1 背包），t=1 表示可选无限次（完全背包），求能装入的最大总价值。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行三个整数 w、v、t。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$，$t\\in\\{0,1\\}$。",
        output_zh="一行一个整数，表示最大总价值。",
        py=("# P2090 混合背包\n"
            "# t=0 为 0/1 背包（逆序），t=1 为完全背包（正序）\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0]*n; v = [0]*n; t = [0]*n\n"
            "for i in range(n):                        # 读入每个物品\n"
            "    w[i], v[i], t[i] = map(int, input().split())\n"
            "f = [0] * (V + 1)                         # f[j] 表示容量 j 的最大价值\n"
            "for i in range(n):                        # 枚举每件物品\n"
            "    if t[i] == 0:                         # 0/1：逆序更新\n"
            "        for j in range(V, w[i] - 1, -1):\n"
            "            if f[j - w[i]] + v[i] > f[j]:\n"
            "                f[j] = f[j - w[i]] + v[i]\n"
            "    else:                                 # 完全：正序更新\n"
            "        for j in range(w[i], V + 1):\n"
            "            if f[j - w[i]] + v[i] > f[j]:\n"
            "                f[j] = f[j - w[i]] + v[i]\n"
            "print(f[V])                               # 输出容量 V 的最大价值\n"),
        cpp=("// P2090 混合背包\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105], t[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i] >> t[i];\n"
             "    int f[1005] = {0};                    // f[j] 表示容量 j 的最大价值\n"
             "    for (int i = 0; i < n; ++i) {         // 枚举每件物品\n"
             "        if (t[i] == 0) {                  // 0/1：逆序更新\n"
             "            for (int j = V; j >= w[i]; --j)\n"
             "                if (f[j - w[i]] + v[i] > f[j])\n"
             "                    f[j] = f[j - w[i]] + v[i];\n"
             "        } else {                          // 完全：正序更新\n"
             "            for (int j = w[i]; j <= V; ++j)\n"
             "                if (f[j - w[i]] + v[i] > f[j])\n"
             "                    f[j] = f[j - w[i]] + v[i];\n"
             "        }\n"
             "    }\n"
             "    cout << f[V] << endl;                 // 输出容量 V 的最大价值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2090 混合背包\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n], t = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); t[i] = sc.nextInt(); }\n"
              "        int[] f = new int[V + 1];                 // f[j] 表示容量 j 的最大价值\n"
              "        for (int i = 0; i < n; ++i) {             // 枚举每件物品\n"
              "            if (t[i] == 0) {                      // 0/1：逆序更新\n"
              "                for (int j = V; j >= w[i]; --j)\n"
              "                    if (f[j - w[i]] + v[i] > f[j])\n"
              "                        f[j] = f[j - w[i]] + v[i];\n"
              "            } else {                              // 完全：正序更新\n"
              "                for (int j = w[i]; j <= V; ++j)\n"
              "                    if (f[j - w[i]] + v[i] > f[j])\n"
              "                        f[j] = f[j - w[i]] + v[i];\n"
              "            }\n"
              "        }\n"
              "        System.out.println(f[V]);                 // 输出容量 V 的最大价值\n"
              "    }\n"
              "}\n"),
    )
