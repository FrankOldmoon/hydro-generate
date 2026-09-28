# -*- coding: utf-8 -*-
"""P2011 字符三角形"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        lines = []
        for i in range(1, n + 1):
            lines.append(" " * (n - i) + "*" * (2 * i - 1))
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2011", "字符三角形", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, print an isosceles triangle of n lines made "
                "of '*', with the apex at the top. No trailing spaces on any line.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="n lines forming the isosceles triangle. Line i (1-based) has "
                  "(n-i) spaces followed by (2i-1) '*' characters.",
        desc_zh="给定整数 n，输出 n 行由 * 组成的等腰三角形（顶点在上），每行末尾无多余空格。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行，第 i 行（从 1 开始）先输出 n-i 个空格，再输出 2i-1 个 *。",
        py=("# P2011 字符三角形（嵌套循环：空格 + 星号）\n"
            "n = int(input())                  # 行数 n\n"
            "for i in range(1, n + 1):         # 第 i 行（从 1 开始）\n"
            "    print(' ' * (n - i) + '*' * (2 * i - 1))   # 空格 n-i 个，星号 2i-1 个\n"),
        cpp=("// P2011 字符三角形\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                       // 行数 n\n"
             "    for (int i = 1; i <= n; ++i) {  // 第 i 行\n"
             "        for (int j = 0; j < n - i; ++j) cout << ' ';     // 先输出 n-i 个空格\n"
             "        for (int j = 0; j < 2 * i - 1; ++j) cout << '*'; // 再输出 2i-1 个星号\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2011 字符三角形\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 行数 n\n"
              "        for (int i = 1; i <= n; ++i) { // 第 i 行\n"
              "            for (int j = 0; j < n - i; ++j) System.out.print(' ');     // n-i 个空格\n"
              "            for (int j = 0; j < 2 * i - 1; ++j) System.out.print('*'); // 2i-1 个星号\n"
              "            System.out.println();\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
