# -*- coding: utf-8 -*-
"""P2018 杨辉三角"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        lines = []
        tri = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):          # 中间元素 = 上一行相邻两元素之和
                row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
            tri.append(row)
            lines.append(" ".join(map(str, row)))
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2018", "杨辉三角", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, print the first n rows of Pascal's triangle. "
                "Each row is printed on one line with its elements separated by "
                "single spaces.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="n lines: row i (1-based) contains i space-separated integers, "
                  "the i-th row of Pascal's triangle (each inner element equals "
                  "the sum of the two elements above it).",
        desc_zh="给定整数 n，输出杨辉三角的前 n 行，每行元素之间用空格分隔。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行，第 i 行输出 i 个用空格分隔的整数，即杨辉三角第 i 行（每个内部元素等于其上方相邻两元素之和）。",
        py=("# P2018 杨辉三角（每个内部元素 = 上一行相邻两元素之和）\n"
            "n = int(input())                  # 行数 n\n"
            "tri = []\n"
            "for i in range(n):                # 第 i 行（从 0 开始）\n"
            "    row = [1] * (i + 1)           # 首尾元素均为 1\n"
            "    for j in range(1, i):         # 计算中间元素\n"
            "        row[j] = tri[i - 1][j - 1] + tri[i - 1][j]\n"
            "    tri.append(row)\n"
            "    print(' '.join(map(str, row)))\n"),
        cpp=("// P2018 杨辉三角\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                       // 行数 n\n"
             "    int tri[15][15];\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        tri[i][0] = tri[i][i] = 1;            // 首尾元素为 1\n"
             "        for (int j = 1; j < i; ++j)           // 计算中间元素\n"
             "            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j];\n"
             "        for (int j = 0; j <= i; ++j) {        // 输出第 i 行\n"
             "            if (j) cout << ' ';\n"
             "            cout << tri[i][j];\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2018 杨辉三角\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 行数 n\n"
              "        int[][] tri = new int[n][n];\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            tri[i][0] = 1; tri[i][i] = 1;          // 首尾元素为 1\n"
              "            for (int j = 1; j < i; ++j)            // 计算中间元素\n"
              "                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j];\n"
              "            StringBuilder sb = new StringBuilder();\n"
              "            for (int j = 0; j <= i; ++j) {         // 输出第 i 行\n"
              "                if (j > 0) sb.append(' ');\n"
              "                sb.append(tri[i][j]);\n"
              "            }\n"
              "            System.out.println(sb);\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
