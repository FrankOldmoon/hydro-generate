# -*- coding: utf-8 -*-
"""P1007 长方形周长和面积"""
from generate import make_problem


def build():
    data = [
        (3, 4), (5, 5), (1, 1), (10, 20), (7, 3),
        (100, 50), (2, 8), (15, 15), (9, 6), (12, 5),
    ]
    cases = [(f"{a}\n{b}\n", f"{2 * (a + b)}\n{a * b}\n") for a, b in data]
    return make_problem(
        "P1007", "长方形周长和面积", ["入门", "数学", "几何"],
        cases=cases,
        desc_en="Given the length a and width b of a rectangle, print its "
                "perimeter and area. The first line of output is the perimeter "
                "2*(a+b), the second line is the area a*b.",
        input_en="Two lines: the first line contains positive integer a (length), "
                 "the second line contains positive integer b (width), satisfying "
                 "$1\\leq a,b\\leq 32767$ .",
        output_en="Two lines: the first line is the perimeter 2*(a+b), the second "
                  "line is the area a*b.",
        desc_zh="给定长方形的长 a 和宽 b，输出它的周长和面积。第一行输出周长 2*(a+b)，"
                "第二行输出面积 a*b。",
        input_zh="两行：第一行一个正整数 a（长），第二行一个正整数 b（宽），满足 "
                 "$1\\leq a,b\\leq 32767$ 。",
        output_zh="两行：第一行为周长 2*(a+b)，第二行为面积 a*b。",
        py=("# P1007 长方形周长和面积\n"
            "# 每行一个正整数，依次读入长 a 和宽 b，输出周长与面积\n"
            "a = int(input())      # 第一行：长 a\n"
            "b = int(input())      # 第二行：宽 b\n"
            "print(2 * (a + b))    # 第一行：周长\n"
            "print(a * b)          # 第二行：面积\n"),
        cpp=("// P1007 长方形周长和面积\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    cin >> a >> b;               // 依次读入长 a 和宽 b（每行一个）\n"
             "    cout << 2 * (a + b) << endl; // 第一行：周长\n"
             "    cout << a * b << endl;       // 第二行：面积\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1007 长方形周长和面积\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();          // 第一行：长 a\n"
              "        int b = sc.nextInt();          // 第二行：宽 b\n"
              "        System.out.println(2 * (a + b)); // 第一行：周长\n"
              "        System.out.println(a * b);       // 第二行：面积\n"
              "    }\n"
              "}\n"),
    )
