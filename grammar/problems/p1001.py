# -*- coding: utf-8 -*-
"""P1001 输出第二个数"""
from generate import make_problem


def build():
    data = [
        (1, 2, 3), (10, 20, 30), (5, 5, 5), (100, 200, 50), (0, 0, 0),
        (7, 8, 9), (-1, -2, -3), (32767, 0, -32768), (42, 99, 1), (11, 22, 33),
    ]
    cases = [(f"{a}\n{b}\n{c}\n", f"{b}\n") for a, b, c in data]
    return make_problem(
        "P1001", "输出第二个数", ["入门", "输入输出"],
        cases=cases,
        desc_en="Given three integers a, b and c (one per line), print only the "
                "second one, b.",
        input_en="Three lines: each line contains one integer. Denote them a, b, "
                 "c from top to bottom, satisfying $-32768\\leq a,b,c\\leq 32767$ .",
        output_en="One line containing only the second integer b.",
        desc_zh="给定三个整数 a、b、c（每行一个），只输出第二个数 b。",
        input_zh="三行：每行一个整数，从上到下依次为 a、b、c，满足 $-32768\\leq a,b,c\\leq 32767$ 。",
        output_zh="一行，只输出第二个整数 b。",
        py=("# P1001 输出第二个数\n"
            "# 每行一个整数，共三行，只输出第二个\n"
            "a = int(input())   # 第一行：a（不需要用到）\n"
            "b = int(input())   # 第二行：b\n"
            "c = int(input())   # 第三行：c（不需要用到）\n"
            "print(b)           # 只输出第二个\n"),
        cpp=("// P1001 输出第二个数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b, c;\n"
             "    cin >> a >> b >> c;   // 依次读入三个整数（每行一个）\n"
             "    cout << b << endl;    // 只输出第二个\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1001 输出第二个数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();   // 第一行：a\n"
              "        int b = sc.nextInt();   // 第二行：b\n"
              "        int c = sc.nextInt();   // 第三行：c\n"
              "        System.out.println(b); // 只输出第二个\n"
              "    }\n"
              "}\n"),
    )
