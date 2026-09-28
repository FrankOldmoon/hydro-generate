# -*- coding: utf-8 -*-
"""P1004 加减运算"""
from generate import make_problem


def build():
    data = [
        (10, 5), (5, 10), (100, 200), (0, 0), (32767, 0),
        (0, 32767), (12345, 6789), (999, 1), (500, 500), (32767, 32767),
    ]
    cases = [(f"{a}\n{b}\n", f"{a + b}\n{a - b}\n") for a, b in data]
    return make_problem(
        "P1004", "加减运算", ["入门", "数学", "四则运算"],
        cases=cases,
        desc_en="Given two integers a and b, print their sum and difference. "
                "The first line of output is a+b, the second line is a-b.",
        input_en="Two lines: the first line contains integer a, the second line "
                 "contains integer b, satisfying $0\\leq a,b\\leq 32767$ .",
        output_en="Two lines: the first line is the sum a+b, the second line is "
                  "the difference a-b.",
        desc_zh="给定两个整数 a 和 b，输出它们的和与差。第一行输出 a+b，第二行输出 a-b。",
        input_zh="两行：第一行一个整数 a，第二行一个整数 b，满足 $0\\leq a,b\\leq 32767$ 。",
        output_zh="两行：第一行为和 a+b，第二行为差 a-b。",
        py=("# P1004 加减运算\n"
            "# 每行一个整数，依次读入 a 和 b，输出它们的和与差\n"
            "a = int(input())   # 第一行：整数 a\n"
            "b = int(input())   # 第二行：整数 b\n"
            "print(a + b)       # 第一行：和\n"
            "print(a - b)       # 第二行：差\n"),
        cpp=("// P1004 加减运算\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    cin >> a >> b;         // 依次读入两个整数（每行一个）\n"
             "    cout << a + b << endl; // 第一行：和\n"
             "    cout << a - b << endl; // 第二行：差\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1004 加减运算\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();      // 第一行：整数 a\n"
              "        int b = sc.nextInt();      // 第二行：整数 b\n"
              "        System.out.println(a + b); // 第一行：和\n"
              "        System.out.println(a - b); // 第二行：差\n"
              "    }\n"
              "}\n"),
    )
