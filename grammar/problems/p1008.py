# -*- coding: utf-8 -*-
"""P1008 圆的周长和面积"""
from generate import make_problem, fmt2

PI = "3.14"  # 题面中 π 取 3.14


def build():
    data = [1, 2, 3, 5, 7, 10, 4, 6, 8, 9]
    pi = 3.14
    cases = [(f"{r}\n", f"{fmt2(2 * pi * r)}\n{fmt2(pi * r * r)}\n") for r in data]
    return make_problem(
        "P1008", "圆的周长和面积", ["入门", "数学", "几何"],
        cases=cases,
        desc_en="Given the radius r of a circle, print its circumference and area "
                "(take $\\pi=3.14$, round the results to two decimal places). The "
                "first line of output is the circumference $2\\pi r$, the second "
                "line is the area $\\pi r^2$.",
        input_en="One line containing a positive integer r (radius), satisfying "
                 "$1\\leq r\\leq 32767$ .",
        output_en="Two lines: the first line is the circumference $2\\pi r$, the "
                  "second line is the area $\\pi r^2$, both rounded to two decimal "
                  "places (with $\\pi=3.14$).",
        desc_zh="给定圆的半径 r，输出它的周长和面积（π 取 3.14，结果保留两位小数）。第一行"
                "输出周长 $2\\pi r$，第二行输出面积 $\\pi r^2$。",
        input_zh="一行一个正整数 r（半径），满足 $1\\leq r\\leq 32767$ 。",
        output_zh="两行：第一行为周长 $2\\pi r$，第二行为面积 $\\pi r^2$，均保留两位小数"
                  "（π 取 3.14）。",
        py=("# P1008 圆的周长和面积\n"
            "# 读入半径 r，输出周长与面积（π 取 3.14，保留两位小数）\n"
            "r = int(input())              # 半径 r\n"
            "pi = 3.14\n"
            "print('%.2f' % (2 * pi * r))  # 第一行：周长\n"
            "print('%.2f' % (pi * r * r))  # 第二行：面积\n"),
        cpp=("// P1008 圆的周长和面积\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int r;\n"
             "    scanf(\"%d\", &r);              // 读入半径 r\n"
             "    const double pi = 3.14;\n"
             "    printf(\"%.2f\\n\", 2 * pi * r); // 第一行：周长\n"
             "    printf(\"%.2f\\n\", pi * r * r); // 第二行：面积\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1008 圆的周长和面积\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int r = sc.nextInt();              // 半径 r\n"
              "        final double pi = 3.14;\n"
              "        System.out.printf(\"%.2f%n\", 2 * pi * r); // 第一行：周长\n"
              "        System.out.printf(\"%.2f%n\", pi * r * r); // 第二行：面积\n"
              "    }\n"
              "}\n"),
    )
