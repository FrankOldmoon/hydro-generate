# -*- coding: utf-8 -*-
"""P1031 最大公约数"""
import math
from generate import make_problem


def build():
    data = [
        (12, 8), (100, 75), (17, 5), (48, 36), (100, 10),
        (7, 7), (1000, 25), (13, 13), (60, 48), (1, 1),
    ]
    cases = [(f"{a}\n{b}\n", f"{math.gcd(a, b)}\n") for a, b in data]
    return make_problem(
        "P1031", "最大公约数", ["入门", "循环结构", "while"],
        cases=cases,
        desc_en="Given two positive integers a and b (one per line), print their "
                "greatest common divisor gcd(a, b).",
        input_en="Two lines: each line contains one positive integer. Denote them "
                 "a, b from top to bottom, satisfying $1\\leq a,b\\leq 32767$ .",
        output_en="One line containing gcd(a, b).",
        desc_zh="给定两个正整数 a 和 b（每行一个），输出它们的最大公约数 gcd(a, b)。",
        input_zh="两行：每行一个正整数，从上到下依次为 a、b，满足 $1\\leq a,b\\leq 32767$ 。",
        output_zh="一行，输出 gcd(a, b)。",
        py=("# P1031 最大公约数（while + 辗转相除法）\n"
            "a = int(input())            # 第一行：a\n"
            "b = int(input())            # 第二行：b\n"
            "while b != 0:               # while 循环：余数不为 0 就继续\n"
            "    a, b = b, a % b         # 辗转相除：a←b，b←a mod b\n"
            "print(a)                    # 循环结束时 a 即为 gcd\n"),
        cpp=("// P1031 最大公约数（while + 辗转相除法）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    cin >> a >> b;          // 依次读入 a、b（每行一个）\n"
             "    while (b != 0) {        // while：余数不为 0 就继续\n"
             "        int t = a % b;      // 辗转相除\n"
             "        a = b;\n"
             "        b = t;\n"
             "    }\n"
             "    cout << a << endl;      // 循环结束时 a 即为 gcd\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1031 最大公约数（while + 辗转相除法）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();   // 第一行：a\n"
              "        int b = sc.nextInt();   // 第二行：b\n"
              "        while (b != 0) {        // while：余数不为 0 就继续\n"
              "            int t = a % b;      // 辗转相除\n"
              "            a = b;\n"
              "            b = t;\n"
              "        }\n"
              "        System.out.println(a); // 循环结束时 a 即为 gcd\n"
              "    }\n"
              "}\n"),
    )
