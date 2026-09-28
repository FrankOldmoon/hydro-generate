# -*- coding: utf-8 -*-
"""P1006 商和余数"""
from generate import make_problem


def build():
    data = [
        (10, 3), (7, 2), (100, 10), (0, 5), (5, 7),
        (17, 5), (100, 7), (256, 16), (999, 1), (32767, 100),
    ]
    cases = [(f"{a}\n{b}\n", f"{a // b}\n{a % b}\n") for a, b in data]
    return make_problem(
        "P1006", "商和余数", ["入门", "数学", "四则运算"],
        cases=cases,
        desc_en="Given two integers a and b (b is positive), print the integer "
                "quotient and the remainder of a divided by b. The first line "
                "of output is the integer quotient a/b, the second line is the "
                "remainder a%b.",
        input_en="Two lines: the first line contains integer a, the second line "
                 "contains integer b (b is positive), satisfying "
                 "$0\\leq a\\leq 32767$ and $1\\leq b\\leq 32767$ .",
        output_en="Two lines: the first line is the integer quotient a/b, the "
                  "second line is the remainder a%b.",
        desc_zh="给定两个整数 a 和 b（b 为正整数），输出 a 除以 b 的整商和余数。第一行输出"
                "整商 a/b，第二行输出余数 a%b。",
        input_zh="两行：第一行一个整数 a，第二行一个正整数 b，满足 $0\\leq a\\leq 32767$ 且 "
                 "$1\\leq b\\leq 32767$ 。",
        output_zh="两行：第一行为整商 a/b，第二行为余数 a%b。",
        py=("# P1006 商和余数\n"
            "# 每行一个整数，依次读入 a 和 b(b>0)，输出整商与余数\n"
            "a = int(input())   # 第一行：整数 a\n"
            "b = int(input())   # 第二行：正整数 b\n"
            "print(a // b)      # 第一行：整商\n"
            "print(a % b)       # 第二行：余数\n"),
        cpp=("// P1006 商和余数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    cin >> a >> b;         // 依次读入两个整数（每行一个）\n"
             "    cout << a / b << endl; // 第一行：整商\n"
             "    cout << a % b << endl; // 第二行：余数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1006 商和余数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();      // 第一行：整数 a\n"
              "        int b = sc.nextInt();      // 第二行：正整数 b\n"
              "        System.out.println(a / b); // 第一行：整商\n"
              "        System.out.println(a % b); // 第二行：余数\n"
              "    }\n"
              "}\n"),
    )
