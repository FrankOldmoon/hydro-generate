# -*- coding: utf-8 -*-
"""P1013 三数求和与平均值"""
from generate import make_problem, fmt2


def build():
    data = [
        (1, 2, 3), (10, 20, 30), (1, 1, 1), (5, 5, 8), (7, 8, 9),
        (1, 2, 4), (10, 10, 11), (3, 3, 5), (100, 200, 300), (0, 0, 1),
    ]
    cases = [(f"{a}\n{b}\n{c}\n",
              f"{a + b + c}\n{fmt2((a + b + c) / 3)}\n") for a, b, c in data]
    return make_problem(
        "P1013", "三数求和与平均值", ["入门", "数学"],
        cases=cases,
        desc_en="Given three integers a, b and c (one per line), print their sum "
                "and average. The first line of output is the sum a+b+c, the "
                "second line is the average (a+b+c)/3 rounded to two decimal "
                "places.",
        input_en="Three lines: each line contains one integer. Denote them a, b, "
                 "c from top to bottom, satisfying $-1000\\leq a,b,c\\leq 1000$ .",
        output_en="Two lines: the first line is the sum a+b+c, the second line is "
                  "the average (a+b+c)/3 rounded to two decimal places.",
        desc_zh="给定三个整数 a、b、c（每行一个），输出它们的和与平均值。第一行输出和 a+b+c，第二行输出平均值 (a+b+c)/3（保留两位小数）。",
        input_zh="三行：每行一个整数，从上到下依次为 a、b、c，满足 $-1000\\leq a,b,c\\leq 1000$ 。",
        output_zh="两行：第一行为和 a+b+c，第二行为平均值 (a+b+c)/3（保留两位小数）。",
        py=("# P1013 三数求和与平均值\n"
            "# 每行一个整数，共三行，输出和与平均值（平均值保留两位小数）\n"
            "a = int(input())   # 第一行：a\n"
            "b = int(input())   # 第二行：b\n"
            "c = int(input())   # 第三行：c\n"
            "s = a + b + c               # 和\n"
            "print(s)                    # 第一行：和\n"
            "print('%.2f' % (s / 3))     # 第二行：平均值，保留两位小数\n"),
        cpp=("// P1013 三数求和与平均值\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b, c;\n"
             "    scanf(\"%d %d %d\", &a, &b, &c);   // 依次读入三个整数（每行一个）\n"
             "    int s = a + b + c;                 // 和\n"
             "    printf(\"%d\\n\", s);               // 第一行：和\n"
             "    printf(\"%.2f\\n\", s / 3.0);       // 第二行：平均值，保留两位小数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1013 三数求和与平均值\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();   // 第一行：a\n"
              "        int b = sc.nextInt();   // 第二行：b\n"
              "        int c = sc.nextInt();   // 第三行：c\n"
              "        int s = a + b + c;      // 和\n"
              "        System.out.println(s);  // 第一行：和\n"
              "        System.out.printf(\"%.2f%n\", s / 3.0); // 第二行：平均值，保留两位小数\n"
              "    }\n"
              "}\n"),
    )
