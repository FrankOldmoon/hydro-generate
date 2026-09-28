# -*- coding: utf-8 -*-
"""P2005 连续数求和"""
from generate import make_problem


def build():
    ns = [3, 15, 1, 2, 5, 6, 9, 10, 16, 100]

    def solve(n):
        # 枚举起始数 start，累加连续正整数直到和 >= n，等于 n 则计数（至少两项）
        cnt = 0
        for start in range(1, n):
            s = 0
            x = start
            while s < n:
                s += x
                x += 1
            if s == n:
                cnt += 1
        return cnt

    cases = [(f"{n}\n", f"{solve(n)}\n") for n in ns]
    return make_problem(
        "P2005", "连续数求和", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a positive integer n, count the number of ways to write n "
                "as a sum of at least two consecutive positive integers.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10000$ .",
        output_en="One line: the number of such representations.",
        desc_zh="给定正整数 n，求 n 能表示成多少种至少两个连续正整数之和的方案数。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10000$ 。",
        output_zh="一行，方案数。",
        py=("# P2005 连续数求和\n"
            "# 枚举起始数 start，逐个累加连续正整数，和等于 n 则计数（至少两项）\n"
            "n = int(input())                  # 正整数 n\n"
            "cnt = 0\n"
            "for start in range(1, n):         # 起始数从 1 到 n-1\n"
            "    s = 0\n"
            "    x = start\n"
            "    while s < n:                  # 累加连续正整数\n"
            "        s += x\n"
            "        x += 1\n"
            "    if s == n:                    # 恰好等于 n\n"
            "        cnt += 1\n"
            "print(cnt)\n"),
        cpp=("// P2005 连续数求和\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                     // 正整数 n\n"
             "    int cnt = 0;\n"
             "    for (int start = 1; start < n; ++start) { // 起始数\n"
             "        long long s = 0;\n"
             "        for (int x = start; s < n; ++x) s += x; // 累加连续正整数\n"
             "        if (s == n) ++cnt;        // 恰好等于 n\n"
             "    }\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2005 连续数求和\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 正整数 n\n"
              "        int cnt = 0;\n"
              "        for (int start = 1; start < n; ++start) { // 起始数\n"
              "            long s = 0;\n"
              "            for (int x = start; s < n; ++x) s += x; // 累加连续正整数\n"
              "            if (s == n) ++cnt;      // 恰好等于 n\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
