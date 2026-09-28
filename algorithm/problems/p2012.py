# -*- coding: utf-8 -*-
"""P2012 字符菱形"""
from generate import make_problem


def build():
    ns = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    def make(n):
        lines = []
        m = n // 2
        for i in range(n):
            if i <= m:
                stars = 2 * i + 1
            else:
                stars = 2 * (n - 1 - i) + 1
            lines.append(" " * ((n - stars) // 2) + "*" * stars)
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2012", "字符菱形", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an odd integer n, print a diamond of n lines made of '*', "
                "with the widest line in the middle. No trailing spaces on any line.",
        input_en="One line containing an odd positive integer n, satisfying "
                 "$1\\leq n\\leq 19$ .",
        output_en="n lines forming the diamond. The middle line (line (n+1)/2) has "
                  "n '*' characters; lines above/below it shrink by two '*' and "
                  "gain one leading space per step.",
        desc_zh="给定一个奇数 n，输出 n 行由 * 组成的菱形（中间一行最长），每行末尾无多余空格。",
        input_zh="一行一个奇数正整数 n，满足 $1\\leq n\\leq 19$ 。",
        output_zh="n 行菱形，中间第 (n+1)/2 行有 n 个 *，向上向下每行少 2 个 * 并增加 1 个前导空格。",
        py=("# P2012 字符菱形（上半增、下半减）\n"
            "n = int(input())                  # 行数 n（奇数）\n"
            "m = n // 2                        # 中间行下标\n"
            "for i in range(n):\n"
            "    if i <= m:                    # 上半部分（含中间行）\n"
            "        stars = 2 * i + 1\n"
            "    else:                         # 下半部分\n"
            "        stars = 2 * (n - 1 - i) + 1\n"
            "    print(' ' * ((n - stars) // 2) + '*' * stars)\n"),
        cpp=("// P2012 字符菱形\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                    // 行数 n（奇数）\n"
             "    int m = n / 2;               // 中间行下标\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int stars = (i <= m) ? 2 * i + 1 : 2 * (n - 1 - i) + 1;\n"
             "        for (int j = 0; j < (n - stars) / 2; ++j) cout << ' '; // 前导空格\n"
             "        for (int j = 0; j < stars; ++j) cout << '*';           // 星号\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2012 字符菱形\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();       // 行数 n（奇数）\n"
              "        int m = n / 2;              // 中间行下标\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int stars = (i <= m) ? 2 * i + 1 : 2 * (n - 1 - i) + 1;\n"
              "            for (int j = 0; j < (n - stars) / 2; ++j) System.out.print(' ');\n"
              "            for (int j = 0; j < stars; ++j) System.out.print('*');\n"
              "            System.out.println();\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
