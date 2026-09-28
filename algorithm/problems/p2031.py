# -*- coding: utf-8 -*-
"""P2031 最少硬币"""
from generate import make_problem


def build():
    # (金额, 面值列表，已降序且贪心可得最优)
    data = [
        (100, [25, 10, 5, 1]),
        (63, [25, 10, 5, 1]),
        (99, [50, 20, 10, 5, 1]),
        (1, [25, 10, 5, 1]),
        (30, [25, 10, 5, 1]),
        (40, [25, 10, 5, 1]),
        (17, [10, 5, 1]),
        (1000, [500, 100, 50, 10, 5, 1]),
        (6, [10, 5, 1]),
        (80, [50, 20, 10, 5, 1]),
    ]
    cases = []
    for amount, coins in data:
        inp = f"{amount}\n{len(coins)}\n{' '.join(map(str, coins))}\n"
        # 贪心：面值已降序，每次尽量多取大面值
        a = amount
        ans = 0
        for c in coins:
            ans += a // c
            a %= c
        out = f"{ans}\n"
        cases.append((inp, out))
    return make_problem(
        "P2031", "最少硬币", ["算法", "贪心"],
        cases=cases,
        desc_en="Given an amount and several coin denominations (already sorted in "
                "descending order, and the greedy strategy yields the optimal "
                "solution), find the minimum number of coins needed to make up "
                "exactly that amount.",
        input_en="The first line contains an integer amount. The second line contains "
                 "an integer m, the number of coin denominations. The third line "
                 "contains m space-separated integers, the coin denominations in "
                 "descending order.",
        output_en="One line containing the minimum number of coins.",
        desc_zh="给定一个金额和若干种硬币面值（面值已降序且贪心可得最优解），求凑成该金额所需的最少硬币数。",
        input_zh="第一行一个整数表示金额。第二行一个整数 m 表示面值种数。第三行 m 个降序排列的整数表示各面值。",
        output_zh="一行一个整数，表示最少硬币数。",
        py=("# P2031 最少硬币（贪心：面值降序，每次尽量多取大面值）\n"
            "amount = int(input())          # 金额\n"
            "m = int(input())               # 面值种数\n"
            "coins = list(map(int, input().split()))  # 降序面值\n"
            "ans = 0\n"
            "for c in coins:                # 从大面值到小面值\n"
            "    ans += amount // c         # 尽量多取该面值\n"
            "    amount %= c                # 剩余金额\n"
            "print(ans)\n"),
        cpp=("// P2031 最少硬币（贪心：面值降序取尽可能多的大面值）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int amount, m;\n"
             "    cin >> amount >> m;\n"
             "    long long ans = 0;\n"
             "    for (int i = 0; i < m; ++i) {\n"
             "        int c; cin >> c;          // 当前面值（降序给出）\n"
             "        ans += amount / c;        // 尽量多取\n"
             "        amount %= c;              // 剩余金额\n"
             "    }\n"
             "    cout << ans << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2031 最少硬币（贪心：面值降序取尽可能多的大面值）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int amount = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        long ans = 0;\n"
              "        for (int i = 0; i < m; ++i) {\n"
              "            int c = sc.nextInt();  // 当前面值（降序）\n"
              "            ans += amount / c;     // 尽量多取\n"
              "            amount %= c;            // 剩余金额\n"
              "        }\n"
              "        System.out.println(ans);\n"
              "    }\n"
              "}\n"),
    )
