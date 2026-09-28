# -*- coding: utf-8 -*-
"""P1017 两个数的较大值"""
from generate import make_problem


def build():
    data = [
        (3, 5), (5, 3), (7, 7), (-1, -2), (100, 50),
        (0, 1), (-10, 5), (32767, -32768), (42, 42), (-5, -3),
    ]
    cases = [(f"{a}\n{b}\n", f"{max(a, b)}\n") for a, b in data]
    return make_problem(
        "P1017", "两个数的较大值", ["入门", "分支结构", "单分支"],
        cases=cases,
        desc_en="Given two integers a and b (one per line), print the larger one.",
        input_en="Two lines: each line contains one integer. Denote them a, b "
                 "from top to bottom, satisfying $-32768\\leq a,b\\leq 32767$ .",
        output_en="One line containing the larger of a and b.",
        desc_zh="给定两个整数 a 和 b（每行一个），输出它们中的较大值。",
        input_zh="两行：每行一个整数，从上到下依次为 a、b，满足 $-32768\\leq a,b\\leq 32767$ 。",
        output_zh="一行，输出 a 和 b 中的较大值。",
        py=("# P1017 两个数的较大值（单分支：默认 a，仅当 b 更大时替换）\n"
            "a = int(input())   # 第一行：a\n"
            "b = int(input())   # 第二行：b\n"
            "m = a              # 默认较大者为 a\n"
            "if b > m:          # 单分支：b 更大则替换\n"
            "    m = b\n"
            "print(m)           # 输出较大值\n"),
        cpp=("// P1017 两个数的较大值（单分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    cin >> a >> b;     // 依次读入 a、b（每行一个）\n"
             "    int m = a;         // 默认较大者为 a\n"
             "    if (b > m)         // 单分支：b 更大则替换\n"
             "        m = b;\n"
             "    cout << m << endl; // 输出较大值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1017 两个数的较大值（单分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();   // 第一行：a\n"
              "        int b = sc.nextInt();   // 第二行：b\n"
              "        int m = a;              // 默认较大者为 a\n"
              "        if (b > m)              // 单分支：b 更大则替换\n"
              "            m = b;\n"
              "        System.out.println(m);  // 输出较大值\n"
              "    }\n"
              "}\n"),
    )
