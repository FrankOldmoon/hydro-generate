# -*- coding: utf-8 -*-
"""P2013 九九乘法表"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        lines = []
        for i in range(1, n + 1):
            parts = ["{0}*{1}={2}".format(j, i, j * i) for j in range(1, i + 1)]
            lines.append(" ".join(parts))
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2013", "九九乘法表", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, print an n*n multiplication table. Line i "
                "(1-based) contains i formulas separated by a single space, each "
                "of the form j*i=result for j=1..i.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="n lines: line i contains i formulas 'j*i=result' (j from 1 to i) "
                  "separated by single spaces.",
        desc_zh="给定整数 n，输出 n×n 乘法表，第 i 行有 i 个式子，格式为 j*i=result（j 从 1 到 i），式子间用空格分隔。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行，第 i 行输出 i 个式子 j*i=result（j 从 1 到 i），式子之间用一个空格分隔。",
        py=("# P2013 九九乘法表（嵌套循环：行 i 有 i 个式子）\n"
            "n = int(input())                  # 行数 n\n"
            "for i in range(1, n + 1):         # 第 i 行\n"
            "    row = []\n"
            "    for j in range(1, i + 1):     # j 从 1 到 i\n"
            "        row.append(f'{j}*{i}={j*i}')\n"
            "    print(' '.join(row))          # 式子之间用空格分隔\n"),
        cpp=("// P2013 九九乘法表\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                       // 行数 n\n"
             "    for (int i = 1; i <= n; ++i) {  // 第 i 行\n"
             "        for (int j = 1; j <= i; ++j) {  // j 从 1 到 i\n"
             "            if (j > 1) cout << ' ';     // 式子之间输出一个空格\n"
             "            cout << j << '*' << i << '=' << j * i;\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2013 九九乘法表\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 行数 n\n"
              "        for (int i = 1; i <= n; ++i) { // 第 i 行\n"
              "            StringBuilder sb = new StringBuilder();\n"
              "            for (int j = 1; j <= i; ++j) {  // j 从 1 到 i\n"
              "                if (j > 1) sb.append(' ');  // 式子之间输出一个空格\n"
              "                sb.append(j).append('*').append(i).append('=').append(j * i);\n"
              "            }\n"
              "            System.out.println(sb);\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
