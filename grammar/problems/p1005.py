# -*- coding: utf-8 -*-
"""P1005 乘除运算"""
from generate import make_problem, fmt2


def build():
    data = [
        (10, 5), (7, 2), (100, 3), (1, 3), (9, 3),
        (100, 7), (22, 7), (1, 1), (255, 10), (1000, 8),
    ]
    cases = [(f"{a}\n{b}\n", f"{a * b}\n{fmt2(a / b)}\n") for a, b in data]
    return make_problem(
        "P1005", "乘除运算", ["入门", "数学", "四则运算"],
        cases=cases,
        desc_en="Given two positive integers a and b, print their product and "
                "quotient. The first line of output is a*b, the second line is "
                "a/b rounded to two decimal places.",
        input_en="Two lines: the first line contains positive integer a, the "
                 "second line contains positive integer b, satisfying "
                 "$1\\leq a,b\\leq 32767$ .",
        output_en="Two lines: the first line is the product a*b, the second line "
                  "is the quotient a/b rounded to two decimal places.",
        desc_zh="给定两个正整数 a 和 b，输出它们的积与商。第一行输出 a*b，第二行输出 a/b "
                "的结果（保留两位小数）。",
        input_zh="两行：第一行一个正整数 a，第二行一个正整数 b，满足 $1\\leq a,b\\leq 32767$ 。",
        output_zh="两行：第一行为积 a*b，第二行为商 a/b（保留两位小数）。",
        py=("# P1005 乘除运算\n"
            "# 每行一个正整数，依次读入 a 和 b，输出积与商（商保留两位小数）\n"
            "a = int(input())            # 第一行：正整数 a\n"
            "b = int(input())            # 第二行：正整数 b\n"
            "print(a * b)                # 第一行：积\n"
            "print('%.2f' % (a / b))     # 第二行：商，保留两位小数\n"),
        cpp=("// P1005 乘除运算\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    scanf(\"%d %d\", &a, &b);          // 依次读入两个正整数（每行一个）\n"
             "    printf(\"%d\\n\", a * b);            // 第一行：积\n"
             "    printf(\"%.2f\\n\", 1.0 * a / b);    // 第二行：商，保留两位小数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1005 乘除运算\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();          // 第一行：正整数 a\n"
              "        int b = sc.nextInt();          // 第二行：正整数 b\n"
              "        System.out.println(a * b);     // 第一行：积\n"
              "        System.out.printf(\"%.2f%n\", 1.0 * a / b); // 第二行：商，保留两位小数\n"
              "    }\n"
              "}\n"),
    )
