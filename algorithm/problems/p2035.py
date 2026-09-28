# -*- coding: utf-8 -*-
"""P2035 部分背包"""
from generate import make_problem, fmt2


def build():
    # (容量 W, 物品列表[(重量, 价值)])
    data = [
        (50, [(10, 60), (20, 100), (30, 120)]),
        (10, [(5, 10)]),
        (100, [(10, 20), (20, 30), (30, 50)]),
        (50, [(10, 20), (20, 40), (30, 90)]),
        (5, [(10, 100)]),
        (20, [(5, 50), (5, 50), (5, 50), (5, 50)]),
        (15, [(10, 60), (5, 20), (5, 10)]),
        (3, [(4, 10), (2, 3)]),
        (25, [(10, 30), (15, 60), (5, 10)]),
        (40, [(10, 50), (20, 80), (10, 20)]),
    ]
    cases = []
    for W, items in data:
        inp = f"{W}\n{len(items)}\n" + "".join(f"{w} {v}\n" for w, v in items)
        # 贪心：按单位价值降序，尽量多取
        order = sorted(items, key=lambda it: -(it[1] / it[0]))
        total = 0.0
        rem = W
        for w, v in order:
            if rem <= 0:
                break
            take = min(rem, w)
            total += v * take / w
            rem -= take
        out = fmt2(total) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2035", "部分背包", ["算法", "贪心"],
        cases=cases,
        desc_en="Given a knapsack of capacity W and n items, each with a weight and a "
                "value, items can be divided. Find the maximum total value that can "
                "be carried. Output the value rounded to two decimal places.",
        input_en="The first line contains an integer W, the knapsack capacity. The "
                 "second line contains an integer n. The following n lines each "
                 "contain two integers weight and value.",
        output_en="One line containing the maximum total value, rounded to two "
                  "decimal places.",
        desc_zh="给定背包容量 W 和 n 个物品（每个物品有重量和价值，物品可分割），求能装入的最大总价值，保留两位小数。",
        input_zh="第一行一个整数 W 表示背包容量。第二行一个整数 n。接下来 n 行，每行两个整数 weight 和 value。",
        output_zh="一行一个实数，表示最大总价值，保留两位小数。",
        py=("# P2035 部分背包（贪心：按单位价值降序尽量多取）\n"
            "W = int(input())               # 背包容量\n"
            "n = int(input())               # 物品数\n"
            "items = []\n"
            "for _ in range(n):\n"
            "    w, v = map(int, input().split())\n"
            "    items.append((w, v))\n"
            "items.sort(key=lambda x: -(x[1] / x[0]))  # 按单位价值降序\n"
            "total = 0.0\n"
            "rem = W\n"
            "for w, v in items:\n"
            "    if rem <= 0:\n"
            "        break\n"
            "    take = min(rem, w)        # 当前物品能取的量\n"
            "    total += v * take / w     # 对应价值\n"
            "    rem -= take\n"
            "print('%.2f' % total)\n"),
        cpp=("// P2035 部分背包（贪心：按单位价值降序尽量多取）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int W, n;\n"
             "    cin >> W >> n;\n"
             "    vector<pair<int,int>> items;  // (重量, 价值)\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int w, v; cin >> w >> v;\n"
             "        items.push_back({w, v});\n"
             "    }\n"
             "    sort(items.begin(), items.end(), [](auto a, auto b){\n"
             "        return (double)a.second / a.first > (double)b.second / b.first;  // 单位价值降序\n"
             "    });\n"
             "    double total = 0.0;\n"
             "    int rem = W;\n"
             "    for (auto &it : items) {\n"
             "        if (rem <= 0) break;\n"
             "        int take = min(rem, it.first);   // 能取的量\n"
             "        total += (double)it.second * take / it.first;  // 对应价值\n"
             "        rem -= take;\n"
             "    }\n"
             "    printf(\"%.2f\\n\", total);\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2035 部分背包（贪心：按单位价值降序尽量多取）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int W = sc.nextInt();\n"
              "        int n = sc.nextInt();\n"
              "        int[][] items = new int[n][2];\n"
              "        for (int i = 0; i < n; ++i) { items[i][0] = sc.nextInt(); items[i][1] = sc.nextInt(); }\n"
              "        Arrays.sort(items, (a, b) -> Double.compare((double)b[1]/b[0], (double)a[1]/a[0]));  // 单位价值降序\n"
              "        double total = 0.0;\n"
              "        int rem = W;\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            if (rem <= 0) break;\n"
              "            int take = Math.min(rem, items[i][0]);   // 能取的量\n"
              "            total += (double) items[i][1] * take / items[i][0];  // 对应价值\n"
              "            rem -= take;\n"
              "        }\n"
              "        System.out.printf(\"%.2f%n\", total);\n"
              "    }\n"
              "}\n"),
    )
