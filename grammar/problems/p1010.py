# -*- coding: utf-8 -*-
"""P1010 华氏度摄氏度转换"""
from generate import make_problem, fmt2


def build():
    data = [0, 10, 15, 25, 30, 35, 37, 100, 23, 40]
    cases = [(f"{c}\n", f"{fmt2(c * 9 / 5 + 32)}\n") for c in data]
    return make_problem(
        "P1010", "华氏度摄氏度转换", ["入门", "数学"],
        cases=cases,
        desc_en="Given a temperature in degrees Celsius, convert it to degrees "
                "Fahrenheit using the formula $F = C \\times 9 / 5 + 32$, rounded "
                "to two decimal places.",
        input_en="One line containing an integer C (temperature in degrees "
                 "Celsius), satisfying $-100\\leq C\\leq 200$ .",
        output_en="One line containing the temperature in degrees Fahrenheit, "
                  "rounded to two decimal places.",
        desc_zh="给定一个摄氏度温度 C，将其转换为华氏度温度 F，公式为 $F = C \\times 9 / 5 + 32$，结果保留两位小数。",
        input_zh="一行一个整数 C（摄氏度温度），满足 $-100\\leq C\\leq 200$ 。",
        output_zh="一行，输出华氏度温度，保留两位小数。",
        py=("# P1010 华氏度摄氏度转换\n"
            "# 读入摄氏度 C，输出华氏度 F = C*9/5+32（保留两位小数）\n"
            "c = int(input())                 # 摄氏度 C\n"
            "f = c * 9 / 5 + 32               # 华氏度 F\n"
            "print('%.2f' % f)                # 保留两位小数\n"),
        cpp=("// P1010 华氏度摄氏度转换\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int c;\n"
             "    scanf(\"%d\", &c);                  // 读入摄氏度 C\n"
             "    printf(\"%.2f\\n\", c * 9.0 / 5 + 32); // 华氏度 F，保留两位小数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1010 华氏度摄氏度转换\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int c = sc.nextInt();          // 摄氏度 C\n"
              "        System.out.printf(\"%.2f%n\", c * 9.0 / 5 + 32); // 华氏度 F，保留两位小数\n"
              "    }\n"
              "}\n"),
    )
