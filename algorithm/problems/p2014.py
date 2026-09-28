# -*- coding: utf-8 -*-
"""P2014 字符金字塔"""
from generate import make_problem


def build():
    data = [(1, '*'), (2, '#'), (3, '$'), (4, '@'), (5, '+'),
            (6, '.'), (7, 'o'), (8, 'x'), (9, 'A'), (10, '=')]

    def make(n, c):
        lines = []
        for i in range(1, n + 1):
            lines.append(" " * (n - i) + c * (2 * i - 1))
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n{c}\n", make(n, c)) for n, c in data]
    return make_problem(
        "P2014", "字符金字塔", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n and a character c, print an n-level pyramid "
                "made of c. Level i (1-based) has (2i-1) characters centered with "
                "leading spaces. No trailing spaces on any line.",
        input_en="Two lines: the first line contains a positive integer n, the "
                 "second line contains a single character c (not a space), "
                 "satisfying $1\\leq n\\leq 10$ .",
        output_en="n lines forming the pyramid. Level i has (n-i) leading spaces "
                  "followed by (2i-1) copies of c.",
        desc_zh="给定整数 n 和字符 c，输出 n 层由 c 组成的字符金字塔，第 i 层有 2i-1 个字符，居中排列，每行末尾无多余空格。",
        input_zh="两行：第一行一个正整数 n，第二行一个字符 c（不为空格），满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行金字塔，第 i 行先输出 n-i 个空格，再输出 2i-1 个字符 c。",
        py=("# P2014 字符金字塔（用指定字符 c 替代星号）\n"
            "n = int(input())                  # 层数 n\n"
            "c = input().strip()               # 组成字符 c\n"
            "for i in range(1, n + 1):         # 第 i 层\n"
            "    print(' ' * (n - i) + c * (2 * i - 1))   # 空格 n-i 个，字符 2i-1 个\n"),
        cpp=("// P2014 字符金字塔\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    char c;\n"
             "    cin >> n >> c;                   // 层数 n 与字符 c\n"
             "    for (int i = 1; i <= n; ++i) {   // 第 i 层\n"
             "        for (int j = 0; j < n - i; ++j) cout << ' ';   // 前导空格\n"
             "        for (int j = 0; j < 2 * i - 1; ++j) cout << c; // 输出字符 c\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2014 字符金字塔\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 层数 n\n"
              "        char c = sc.next().charAt(0); // 组成字符 c\n"
              "        for (int i = 1; i <= n; ++i) { // 第 i 层\n"
              "            for (int j = 0; j < n - i; ++j) System.out.print(' ');\n"
              "            for (int j = 0; j < 2 * i - 1; ++j) System.out.print(c);\n"
              "            System.out.println();\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
