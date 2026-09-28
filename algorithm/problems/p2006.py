# -*- coding: utf-8 -*-
"""P2006 报七游戏"""
from generate import make_problem


def build():
    ns = [7, 17, 1, 10, 20, 30, 50, 70, 100, 200]

    def solve(n):
        # 1..n 中是 7 的倍数或含数字 7 的个数
        cnt = 0
        for i in range(1, n + 1):
            if i % 7 == 0 or '7' in str(i):
                cnt += 1
        return cnt

    cases = [(f"{n}\n", f"{solve(n)}\n") for n in ns]
    return make_problem(
        "P2006", "报七游戏", ["算法", "模拟"],
        cases=cases,
        desc_en="Count how many integers from 1 to n are either a multiple of 7 "
                "or contain the digit 7 (in decimal).",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 100000$ .",
        output_en="One line: the count of such integers between 1 and n.",
        desc_zh="统计 1 到 n 中是 7 的倍数或含有数字 7 的整数个数。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 100000$ 。",
        output_zh="一行，满足条件的整数个数。",
        py=("# P2006 报七游戏\n"
            "# 遍历 1..n，是 7 的倍数或含数字 7 则计数\n"
            "n = int(input())                  # 上界 n\n"
            "cnt = 0\n"
            "for i in range(1, n + 1):         # 遍历 1..n\n"
            "    if i % 7 == 0 or '7' in str(i):  # 7 的倍数或含 7\n"
            "        cnt += 1\n"
            "print(cnt)\n"),
        cpp=("// P2006 报七游戏\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "// 判断 x 的十进制表示中是否含数字 7\n"
             "bool has7(int x) {\n"
             "    while (x > 0) {\n"
             "        if (x % 10 == 7) return true;\n"
             "        x /= 10;\n"
             "    }\n"
             "    return false;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                     // 上界 n\n"
             "    int cnt = 0;\n"
             "    for (int i = 1; i <= n; ++i)  // 遍历 1..n\n"
             "        if (i % 7 == 0 || has7(i)) // 7 的倍数或含 7\n"
             "            ++cnt;\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2006 报七游戏\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    // 判断 x 的十进制表示中是否含数字 7\n"
              "    static boolean has7(int x) {\n"
              "        while (x > 0) {\n"
              "            if (x % 10 == 7) return true;\n"
              "            x /= 10;\n"
              "        }\n"
              "        return false;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 上界 n\n"
              "        int cnt = 0;\n"
              "        for (int i = 1; i <= n; ++i) // 遍历 1..n\n"
              "            if (i % 7 == 0 || has7(i)) // 7 的倍数或含 7\n"
              "                ++cnt;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
