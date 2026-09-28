# -*- coding: utf-8 -*-
"""P1015 梯形面积"""
from generate import make_problem, fmt2


def build():
    data = [
        (3, 5, 4), (1, 2, 3), (5, 5, 10), (10, 20, 5), (2, 4, 6),
        (7, 3, 8), (100, 50, 4), (1, 1, 1), (8, 12, 10), (6, 9, 7),
    ]
    cases = [(f"{a}\n{b}\n{h}\n", f"{fmt2((a + b) * h / 2)}\n") for a, b, h in data]
    return make_problem(
        "P1015", "梯形面积", ["入门", "数学", "几何"],
        cases=cases,
        desc_en="Given the upper base a, lower base b and height h of a trapezoid, "
                "print its area. The area is (a+b)*h/2, rounded to two decimal "
                "places.",
        input_en="Three lines: each line contains one positive integer. Denote them "
                 "a (upper base), b (lower base), h (height) from top to bottom, "
                 "satisfying $1\\leq a,b,h\\leq 32767$ .",
        output_en="One line: the area (a+b)*h/2 rounded to two decimal places.",
        desc_zh="给定梯形的上底 a、下底 b 和高 h，输出它的面积。面积为 (a+b)*h/2，"
                "保留两位小数。",
        input_zh="三行：每行一个正整数，从上到下依次为 a（上底）、b（下底）、h（高），"
                 "满足 $1\\leq a,b,h\\leq 32767$ 。",
        output_zh="一行，面积为 (a+b)*h/2，保留两位小数。",
        py=("# P1015 梯形面积\n"
            "# 每行一个正整数，依次读入上底 a、下底 b、高 h，输出面积（保留两位小数）\n"
            "a = int(input())                    # 第一行：上底 a\n"
            "b = int(input())                    # 第二行：下底 b\n"
            "h = int(input())                    # 第三行：高 h\n"
            "print('%.2f' % ((a + b) * h / 2))   # 面积 = (a+b)*h/2\n"),
        cpp=("// P1015 梯形面积\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b, h;\n"
             "    scanf(\"%d %d %d\", &a, &b, &h);          // 依次读入 a、b、h（每行一个）\n"
             "    printf(\"%.2f\\n\", (a + b) * h / 2.0);     // 面积，保留两位小数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1015 梯形面积\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();          // 第一行：上底 a\n"
              "        int b = sc.nextInt();          // 第二行：下底 b\n"
              "        int h = sc.nextInt();          // 第三行：高 h\n"
              "        System.out.printf(\"%.2f%n\", (a + b) * h / 2.0);  // 面积\n"
              "    }\n"
              "}\n"),
    )
