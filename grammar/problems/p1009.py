# -*- coding: utf-8 -*-
"""P1009 幂运算"""
from generate import make_problem


def build():
    data = [
        (2, 3), (2, 6), (3, 4), (5, 0), (10, 6),
        (7, 5), (100, 3), (1, 6), (4, 5), (12, 4),
    ]
    cases = [(f"{a}\n{b}\n", f"{a ** b}\n") for a, b in data]
    return make_problem(
        "P1009", "幂运算", ["入门", "数学"],
        cases=cases,
        desc_en="Given two integers a and b, print a raised to the power of b "
                "(i.e. a^b).",
        input_en="Two lines: the first line contains integer a (the base), the "
                 "second line contains integer b (the exponent), satisfying "
                 "$1\\leq a\\leq 100$ and $0\\leq b\\leq 6$ .",
        output_en="One line containing the value of a^b.",
        desc_zh="给定两个整数 a 和 b，输出 a 的 b 次幂（即 a^b）。",
        input_zh="两行：第一行一个整数 a（底数），第二行一个整数 b（指数），满足 $1\\leq a\\leq 100$ 且 $0\\leq b\\leq 6$ 。",
        output_zh="一行，输出 a^b 的值。",
        py=("# P1009 幂运算\n"
            "# 每行一个整数，依次读入底数 a 和指数 b，输出 a 的 b 次幂\n"
            "a = int(input())   # 底数 a\n"
            "b = int(input())   # 指数 b\n"
            "print(a ** b)      # a^b\n"),
        cpp=("// P1009 幂运算\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    long long a, b;\n"
             "    cin >> a >> b;        // 依次读入底数 a 和指数 b（每行一个）\n"
             "    long long r = 1;\n"
             "    for (int i = 0; i < b; i++) r *= a;  // 循环求 a^b\n"
             "    cout << r << endl;    // 输出 a^b\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1009 幂运算\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        long a = sc.nextLong();   // 底数 a\n"
              "        long b = sc.nextLong();   // 指数 b\n"
              "        long r = 1;\n"
              "        for (int i = 0; i < b; i++) r *= a;  // 循环求 a^b\n"
              "        System.out.println(r);  // 输出 a^b\n"
              "    }\n"
              "}\n"),
    )
