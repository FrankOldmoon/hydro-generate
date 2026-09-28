# -*- coding: utf-8 -*-
"""P1027 求n的阶乘"""
import math
from generate import make_problem


def build():
    data = [0, 1, 5, 10, 3, 7, 12, 4, 6, 8]
    cases = [(f"{n}\n", f"{math.factorial(n)}\n") for n in data]
    return make_problem(
        "P1027", "求n的阶乘", ["入门", "循环结构", "for"],
        cases=cases,
        desc_en="Given a non-negative integer n, print n factorial (n! = "
                "1*2*...*n, and 0! = 1).",
        input_en="One line containing a non-negative integer n, satisfying "
                 "$0\\leq n\\leq 12$ .",
        output_en="One line containing n! .",
        desc_zh="给定一个非负整数 n，输出 n 的阶乘 n!（n! = 1×2×…×n，规定 0! = 1）。",
        input_zh="一行一个非负整数 n，满足 $0\\leq n\\leq 12$ 。",
        output_zh="一行，输出 n! 。",
        py=("# P1027 求n的阶乘（for 循环累乘）\n"
            "n = int(input())            # 非负整数 n\n"
            "p = 1                       # 累乘积初始化为 1\n"
            "for i in range(1, n + 1):   # for 循环：i 从 1 到 n\n"
            "    p *= i                  # 逐项累乘\n"
            "print(p)                    # 输出 n!\n"),
        cpp=("// P1027 求n的阶乘（for 循环）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入非负整数 n\n"
             "    long long p = 1;         // 累乘积（用 long long 防溢出）\n"
             "    for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
             "        p *= i;\n"
             "    cout << p << endl;       // 输出 n!\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1027 求n的阶乘（for 循环）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 非负整数 n\n"
              "        long p = 1;                  // 累乘积\n"
              "        for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
              "            p *= i;\n"
              "        System.out.println(p);      // 输出 n!\n"
              "    }\n"
              "}\n"),
    )
