# -*- coding: utf-8 -*-
"""P1076 三数最大值"""
from generate import make_problem


def build():
    data = [
        (3, [(1, 2, 3), (10, 5, 8), (-1, 0, 1)]),
        (1, [(7, 3, 5)]),
        (2, [(5, 5, 5), (1, 1, 1)]),
        (4, [(3, 7, 5), (2, 8, 4), (9, 1, 6), (0, 0, 0)]),
        (1, [(100, 200, 50)]),
        (3, [(-5, -3, -1), (0, 0, 1), (1, 2, 3)]),
        (2, [(42, 17, 88), (9, 9, 8)]),
        (1, [(0, -1, -2)]),
        (5, [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]),
        (2, [(3, 1, 2), (6, 4, 5)]),
    ]

    cases = []
    for n, groups in data:
        inp = f"{n}\n"
        for a, b, c in groups:
            inp += f"{a}\n{b}\n{c}\n"
        out = "".join(f"{max(a, b, c)}\n" for a, b, c in groups)
        cases.append((inp, out))
    return make_problem(
        "P1076", "三数最大值", ["入门", "函数"],
        cases=cases,
        desc_en="Given n groups of three integers, print the maximum of each group.",
        input_en="The first line contains a positive integer n. The following 3n "
                 "lines each contain one integer, grouped in sets of three.",
        output_en="n lines: the maximum of each group.",
        desc_zh="给定 n 组数据，每组三个整数，输出每组的最大值。",
        input_zh="第一行一个正整数 n。接下来 3n 行，每行一个整数，每 3 个为一组。",
        output_zh="n 行，每行输出对应组的最大值。",
        py=("# P1076 三数最大值（自定义函数求三数最大值）\n"
            "def max3(a, b, c):             # 定义求三数最大值的函数\n"
            "    m = a\n"
            "    if b > m:\n"
            "        m = b\n"
            "    if c > m:\n"
            "        m = c\n"
            "    return m\n"
            "\n"
            "n = int(input())               # 组数 n\n"
            "for i in range(n):\n"
            "    a = int(input())           # 读入三个数\n"
            "    b = int(input())\n"
            "    c = int(input())\n"
            "    print(max3(a, b, c))       # 调用函数\n"),
        cpp=("// P1076 三数最大值\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int max3(int a, int b, int c) {  // 求三数最大值\n"
             "    int m = a;\n"
             "    if (b > m) m = b;\n"
             "    if (c > m) m = c;\n"
             "    return m;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int a, b, c;\n"
             "        cin >> a >> b >> c;\n"
             "        cout << max3(a, b, c) << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1076 三数最大值\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static int max3(int a, int b, int c) {  // 求三数最大值\n"
              "        int m = a;\n"
              "        if (b > m) m = b;\n"
              "        if (c > m) m = c;\n"
              "        return m;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int a = sc.nextInt();\n"
              "            int b = sc.nextInt();\n"
              "            int c = sc.nextInt();\n"
              "            System.out.println(max3(a, b, c));\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
