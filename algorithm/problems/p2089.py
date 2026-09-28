# -*- coding: utf-8 -*-
"""P2089 背包记录方案"""
from generate import make_problem


def solve(n, V, items):
    # 0/1 背包：求最大价值并记录所选物品（字典序最小的方案）
    # dp[i][j] 表示用物品 i..n-1、容量为 j 时的最大价值
    dp = [[0] * (V + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        w, v = items[i]
        for j in range(V + 1):
            dp[i][j] = dp[i + 1][j]           # 不选物品 i
            if j >= w:                         # 选物品 i
                t = dp[i + 1][j - w] + v
                if t > dp[i][j]:
                    dp[i][j] = t
    best = dp[0][V]
    # 从前往后重构，遇到可选则选（保证字典序最小）
    chosen = []
    j = V
    for i in range(n):
        w, v = items[i]
        if j >= w and dp[i + 1][j - w] + v >= dp[i + 1][j]:
            chosen.append(i + 1)               # 1-based 编号
            j -= w
    return best, chosen


def make_input(n, V, items):
    lines = [f"{n} {V}"]
    for w, v in items:
        lines.append(f"{w} {v}")
    return "\n".join(lines) + "\n"


def gen(n, seed):
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
        (2, 5, [(3, 4), (2, 3)]),
        (5, 10, [(5, 10), (4, 40), (3, 50), (2, 30), (1, 20)]),
        (6, 20, [(10, 60), (5, 50), (5, 50), (3, 20), (2, 30), (4, 40)]),
        (8, 15, [(2, 3), (3, 4), (4, 5), (5, 8), (6, 10), (1, 2), (7, 14), (2, 5)]),
        (15, 200, gen(15, 11)),
        (30, 400, gen(30, 23)),
        (50, 600, gen(50, 37)),
    ]
    cases = []
    for n, V, items in data:
        best, chosen = solve(n, V, items)
        out = f"{best}\n" + " ".join(map(str, chosen)) + "\n"
        cases.append((make_input(n, V, items), out))
    return make_problem(
        "P2089", "背包记录方案", ["算法", "背包"],
        cases=cases,
        desc_en="Given n items, each with weight w and value v, and a knapsack of "
                "capacity V, each item may be chosen at most once. Find the maximum "
                "total value, and output the indices (1-based, ascending) of the chosen "
                "items. If multiple optimal solutions exist, output the one with the "
                "lexicographically smallest index set.",
        input_en="The first line contains two integers n and V. The following n lines "
                 "each contain two integers w and v. Constraints: $1\\leq n\\leq 100$, "
                 "$1\\leq V\\leq 1000$, $1\\leq w\\leq 1000$, $1\\leq v\\leq 1000$.",
        output_en="The first line is a single integer: the maximum total value. The "
                  "second line contains the indices (1-based, ascending) of the chosen "
                  "items, separated by spaces.",
        desc_zh="给定 n 个物品（每个物品有重量 w 和价值 v）和一个容量为 V 的背包，每件物品最多选一次，求能装入的最大总价值，并输出所选物品的编号（1 开始，升序）。若存在多个最优方案，输出编号字典序最小的一种。",
        input_zh="第一行两个整数 n 和 V。接下来 n 行每行两个整数 w 和 v。满足 $1\\leq n\\leq 100$，$1\\leq V\\leq 1000$，$1\\leq w\\leq 1000$，$1\\leq v\\leq 1000$。",
        output_zh="第一行一个整数，表示最大总价值。第二行若干个升序整数，表示所选物品的编号（1 开始），以空格分隔。",
        py=("# P2089 背包记录方案\n"
            "# 0/1 背包：dp[i][j] 用物品 i..n-1、容量 j 的最大价值，逆推后正向重构\n"
            "n, V = map(int, input().split())          # 读入物品数与容量\n"
            "w = [0] * n; v = [0] * n\n"
            "for i in range(n):                        # 读入每个物品\n"
            "    w[i], v[i] = map(int, input().split())\n"
            "dp = [[0] * (V + 1) for _ in range(n + 1)] # dp[i][j] 用物品 i..n-1 容量 j 的最大价值\n"
            "for i in range(n - 1, -1, -1):            # 逆序计算 dp\n"
            "    for j in range(V + 1):\n"
            "        dp[i][j] = dp[i + 1][j]           # 不选物品 i\n"
            "        if j >= w[i]:                     # 选物品 i\n"
            "            t = dp[i + 1][j - w[i]] + v[i]\n"
            "            if t > dp[i][j]:\n"
            "                dp[i][j] = t\n"
            "best = dp[0][V]\n"
            "chosen = []\n"
            "j = V\n"
            "for i in range(n):                        # 正向重构，优先选当前物品（字典序最小）\n"
            "    if j >= w[i] and dp[i + 1][j - w[i]] + v[i] >= dp[i + 1][j]:\n"
            "        chosen.append(i + 1)              # 1-based 编号\n"
            "        j -= w[i]\n"
            "print(best)                               # 输出最大价值\n"
            "print(' '.join(map(str, chosen)))         # 输出所选编号（升序）\n"),
        cpp=("// P2089 背包记录方案\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, V;\n"
             "    cin >> n >> V;                        // 读入物品数与容量\n"
             "    int w[105], v[105];\n"
             "    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];\n"
             "    static int dp[105][1005];             // dp[i][j] 用物品 i..n-1 容量 j 的最大价值\n"
             "    for (int i = n - 1; i >= 0; --i)      // 逆序计算 dp\n"
             "        for (int j = 0; j <= V; ++j) {\n"
             "            dp[i][j] = dp[i + 1][j];      // 不选物品 i\n"
             "            if (j >= w[i]) {              // 选物品 i\n"
             "                int t = dp[i + 1][j - w[i]] + v[i];\n"
             "                if (t > dp[i][j]) dp[i][j] = t;\n"
             "            }\n"
             "        }\n"
             "    cout << dp[0][V] << \"\\n\";           // 输出最大价值\n"
             "    vector<int> chosen;\n"
             "    int j = V;\n"
             "    for (int i = 0; i < n; ++i) {         // 正向重构，优先选当前物品（字典序最小）\n"
             "        if (j >= w[i] && dp[i + 1][j - w[i]] + v[i] >= dp[i + 1][j]) {\n"
             "            chosen.push_back(i + 1);      // 1-based 编号\n"
             "            j -= w[i];\n"
             "        }\n"
             "    }\n"
             "    for (size_t t = 0; t < chosen.size(); ++t) { // 输出所选编号（升序）\n"
             "        if (t) cout << \" \";\n"
             "        cout << chosen[t];\n"
             "    }\n"
             "    cout << \"\\n\";\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2089 背包记录方案\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt(), V = sc.nextInt();   // 读入物品数与容量\n"
              "        int[] w = new int[n], v = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { w[i] = sc.nextInt(); v[i] = sc.nextInt(); }\n"
              "        int[][] dp = new int[n + 1][V + 1];       // dp[i][j] 用物品 i..n-1 容量 j 的最大价值\n"
              "        for (int i = n - 1; i >= 0; --i) {        // 逆序计算 dp\n"
              "            for (int j = 0; j <= V; ++j) {\n"
              "                dp[i][j] = dp[i + 1][j];          // 不选物品 i\n"
              "                if (j >= w[i]) {                  // 选物品 i\n"
              "                    int t = dp[i + 1][j - w[i]] + v[i];\n"
              "                    if (t > dp[i][j]) dp[i][j] = t;\n"
              "                }\n"
              "            }\n"
              "        }\n"
              "        System.out.println(dp[0][V]);             // 输出最大价值\n"
              "        StringBuilder sb = new StringBuilder();\n"
              "        int j = V;\n"
              "        for (int i = 0; i < n; ++i) {             // 正向重构，优先选当前物品（字典序最小）\n"
              "            if (j >= w[i] && dp[i + 1][j - w[i]] + v[i] >= dp[i + 1][j]) {\n"
              "                if (sb.length() > 0) sb.append(' ');\n"
              "                sb.append(i + 1);                 // 1-based 编号\n"
              "                j -= w[i];\n"
              "            }\n"
              "        }\n"
              "        System.out.println(sb.toString());        // 输出所选编号（升序）\n"
              "    }\n"
              "}\n"),
    )
