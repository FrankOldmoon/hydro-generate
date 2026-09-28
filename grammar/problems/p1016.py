# -*- coding: utf-8 -*-
"""P1016 求绝对值"""
from generate import make_problem


def build():
    data = [5, -5, 0, -100, 32767, -32768, 1, -1, 42, -42]
    cases = [(f"{n}\n", f"{abs(n)}\n") for n in data]
    return make_problem(
        "P1016", "求绝对值", ["入门", "分支结构", "单分支"],
        cases=cases,
        desc_en="Given an integer n, print its absolute value |n|.",
        input_en="One line containing an integer n, satisfying "
                 "$-32768\\leq n\\leq 32767$ .",
        output_en="One line containing the absolute value of n.",
        desc_zh="给定一个整数 n，输出它的绝对值 |n|。",
        input_zh="一行一个整数 n，满足 $-32768\\leq n\\leq 32767$ 。",
        output_zh="一行，输出 n 的绝对值。",
        py=("# P1016 求绝对值（单分支：仅当 n<0 时取反）\n"
            "n = int(input())   # 整数 n\n"
            "if n < 0:          # 单分支：负数才需要取反\n"
            "    n = -n         # 取相反数变为正数\n"
            "print(n)           # 输出绝对值\n"),
        cpp=("// P1016 求绝对值（单分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;        // 读入整数 n\n"
             "    if (n < 0)       // 单分支：负数才取反\n"
             "        n = -n;\n"
             "    cout << n << endl;  // 输出绝对值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1016 求绝对值（单分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 整数 n\n"
              "        if (n < 0)              // 单分支：负数才取反\n"
              "            n = -n;\n"
              "        System.out.println(n);  // 输出绝对值\n"
              "    }\n"
              "}\n"),
    )
