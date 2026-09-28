# -*- coding: utf-8 -*-
"""P1002 三数同行输出"""
from generate import make_problem


def build():
    data = [
        (1, 2, 3), (10, 20, 30), (5, 5, 5), (100, 200, 50), (0, 0, 0),
        (7, 8, 9), (-1, -2, -3), (32767, 0, -32768), (42, 99, 1), (11, 22, 33),
    ]
    cases = [(f"{a}\n{b}\n{c}\n", f"{a} {b} {c}\n") for a, b, c in data]
    return make_problem(
        "P1002", "三数同行输出", ["入门", "输入输出"],
        cases=cases,
        desc_en="Given three integers a, b and c (one per line), print them on a "
                "single line separated by single spaces, in the order a b c.",
        input_en="Three lines: each line contains one integer. Denote them a, b, "
                 "c from top to bottom, satisfying $-32768\\leq a,b,c\\leq 32767$ .",
        output_en="One line containing the three integers separated by single "
                  "spaces, in the order a b c.",
        desc_zh="给定三个整数 a、b、c（每行一个），将它们以空格为间隔输出在同一行，顺序为 a b c。",
        input_zh="三行：每行一个整数，从上到下依次为 a、b、c，满足 $-32768\\leq a,b,c\\leq 32767$ 。",
        output_zh="一行，三个整数以空格为间隔，顺序为 a b c。",
        py=("# P1002 三数同行输出\n"
            "# 每行一个整数，共三行，以空格间隔输出在同一行\n"
            "a = int(input())   # 第一行：a\n"
            "b = int(input())   # 第二行：b\n"
            "c = int(input())   # 第三行：c\n"
            "print(a, b, c)     # 以空格间隔输出在同一行\n"),
        cpp=("// P1002 三数同行输出\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b, c;\n"
             "    cin >> a >> b >> c;          // 依次读入三个整数（每行一个）\n"
             "    cout << a << \" \" << b << \" \" << c << endl; // 以空格间隔输出在同一行\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1002 三数同行输出\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();   // 第一行：a\n"
              "        int b = sc.nextInt();   // 第二行：b\n"
              "        int c = sc.nextInt();   // 第三行：c\n"
              "        System.out.println(a + \" \" + b + \" \" + c); // 以空格间隔输出在同一行\n"
              "    }\n"
              "}\n"),
    )
