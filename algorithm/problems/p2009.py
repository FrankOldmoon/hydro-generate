# -*- coding: utf-8 -*-
"""P2009 数字根"""
from generate import make_problem


def build():
    ns = [38, 99, 1, 9, 10, 100, 7, 12345, 999999, 123456789]

    def solve(n):
        # 反复求各位数字之和，直到 < 10
        while n >= 10:
            n = sum(int(c) for c in str(n))
        return n

    cases = [(f"{n}\n", f"{solve(n)}\n") for n in ns]
    return make_problem(
        "P2009", "数字根", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a positive integer n, repeatedly replace it by the sum of "
                "its decimal digits until the result is a single digit. Output "
                "this final digit (the digital root).",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10^{9}$ .",
        output_en="One line: the digital root of n (a single digit).",
        desc_zh="给定正整数 n，反复求各位数字之和，直到结果小于 10，输出这个数字根。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10^{9}$ 。",
        output_zh="一行，n 的数字根（一个个位数）。",
        py=("# P2009 数字根\n"
            "# 反复求各位数字之和，直到结果 < 10\n"
            "n = int(input())                  # 正整数 n\n"
            "while n >= 10:                    # 多位数继续求和\n"
            "    n = sum(int(c) for c in str(n))  # 各位数字之和\n"
            "print(n)\n"),
        cpp=("// P2009 数字根\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    long long n;\n"
             "    cin >> n;                     // 正整数 n\n"
             "    while (n >= 10) {             // 多位数继续求和\n"
             "        long long s = 0;\n"
             "        while (n > 0) {           // 求各位数字之和\n"
             "            s += n % 10;\n"
             "            n /= 10;\n"
             "        }\n"
             "        n = s;\n"
             "    }\n"
             "    cout << n << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2009 数字根\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        long n = sc.nextLong();    // 正整数 n\n"
              "        while (n >= 10) {          // 多位数继续求和\n"
              "            long s = 0;\n"
              "            while (n > 0) {        // 求各位数字之和\n"
              "                s += n % 10;\n"
              "                n /= 10;\n"
              "            }\n"
              "            n = s;\n"
              "        }\n"
              "        System.out.println(n);\n"
              "    }\n"
              "}\n"),
    )
