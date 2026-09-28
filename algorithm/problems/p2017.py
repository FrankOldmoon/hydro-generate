# -*- coding: utf-8 -*-
"""P2017 沙漏图形"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        lines = []
        for i in range(n):                  # 上半部分（含最窄中间行）
            stars = 2 * (n - i) - 1
            lines.append(" " * i + "*" * stars)
        for i in range(1, n):              # 下半部分（镜像，不含中间行）
            stars = 2 * i + 1
            lines.append(" " * (n - 1 - i) + "*" * stars)
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2017", "沙漏图形", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, print an hourglass of (2n-1) lines made of "
                "'*'. The widest line (top and bottom) has (2n-1) '*' characters; "
                "the narrowest middle line has one '*'. No trailing spaces.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="(2n-1) lines forming the hourglass. The top n lines shrink from "
                  "(2n-1) down to 1 '*' (one fewer '*' pair and one more leading "
                  "space per line); the bottom (n-1) lines mirror back to (2n-1).",
        desc_zh="给定整数 n，输出 2n-1 行由 * 组成的沙漏形，最上最下两行各有 2n-1 个 *，中间最窄一行有 1 个 *，每行末尾无多余空格。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="2n-1 行沙漏，上半 n 行从 2n-1 个 * 逐行少 2 个、前导空格多 1 个，直到中间 1 个 *；下半 n-1 行镜像还原到 2n-1 个 *。",
        py=("# P2017 沙漏图形（上半递减，下半镜像递增）\n"
            "n = int(input())                  # 参数 n\n"
            "for i in range(n):               # 上半部分（含中间最窄行）\n"
            "    stars = 2 * (n - i) - 1      # 本行星号数\n"
            "    print(' ' * i + '*' * stars)\n"
            "for i in range(1, n):            # 下半部分（镜像，不含中间行）\n"
            "    stars = 2 * i + 1\n"
            "    print(' ' * (n - 1 - i) + '*' * stars)\n"),
        cpp=("// P2017 沙漏图形\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                       // 参数 n\n"
             "    for (int i = 0; i < n; ++i) {   // 上半部分（含中间行）\n"
             "        int stars = 2 * (n - i) - 1;\n"
             "        for (int j = 0; j < i; ++j) cout << ' ';        // 前导空格\n"
             "        for (int j = 0; j < stars; ++j) cout << '*';    // 星号\n"
             "        cout << endl;\n"
             "    }\n"
             "    for (int i = 1; i < n; ++i) {   // 下半部分（镜像）\n"
             "        int stars = 2 * i + 1;\n"
             "        for (int j = 0; j < n - 1 - i; ++j) cout << ' ';\n"
             "        for (int j = 0; j < stars; ++j) cout << '*';\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2017 沙漏图形\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 参数 n\n"
              "        for (int i = 0; i < n; ++i) {  // 上半部分（含中间行）\n"
              "            int stars = 2 * (n - i) - 1;\n"
              "            for (int j = 0; j < i; ++j) System.out.print(' ');\n"
              "            for (int j = 0; j < stars; ++j) System.out.print('*');\n"
              "            System.out.println();\n"
              "        }\n"
              "        for (int i = 1; i < n; ++i) {  // 下半部分（镜像）\n"
              "            int stars = 2 * i + 1;\n"
              "            for (int j = 0; j < n - 1 - i; ++j) System.out.print(' ');\n"
              "            for (int j = 0; j < stars; ++j) System.out.print('*');\n"
              "            System.out.println();\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
