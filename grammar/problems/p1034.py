# -*- coding: utf-8 -*-
"""P1034 数字的位数"""
from generate import make_problem


def _digits(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


def build():
    data = [1, 9, 10, 99, 100, 999, 1000, 12345, 1000000000, 7]
    cases = [(f"{n}\n", f"{_digits(n)}\n") for n in data]
    return make_problem(
        "P1034", "数字的位数", ["入门", "循环结构", "while"],
        cases=cases,
        desc_en="Given a positive integer n, print the number of decimal digits "
                "it has.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000000000$ .",
        output_en="One line containing the number of digits of n.",
        desc_zh="给定一个正整数 n，输出它的十进制位数。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000000000$ 。",
        output_zh="一行，输出 n 的位数。",
        py=("# P1034 数字的位数（while：每次去掉一位并计数）\n"
            "n = int(input())            # 正整数 n\n"
            "c = 0                       # 位数计数\n"
            "while n > 0:                # while：n 还有未处理的位\n"
            "    c += 1                  # 位数加 1\n"
            "    n //= 10                # 去掉 n 的末位\n"
            "print(c)                    # 输出位数\n"),
        cpp=("// P1034 数字的位数（while）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入正整数 n\n"
             "    int c = 0;               // 位数计数\n"
             "    while (n > 0) {          // while：n 还有未处理的位\n"
             "        ++c;                 // 位数加 1\n"
             "        n /= 10;             // 去掉 n 的末位\n"
             "    }\n"
             "    cout << c << endl;       // 输出位数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1034 数字的位数（while）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 正整数 n\n"
              "        int c = 0;              // 位数计数\n"
              "        while (n > 0) {         // while：n 还有未处理的位\n"
              "            ++c;                // 位数加 1\n"
              "            n /= 10;            // 去掉 n 的末位\n"
              "        }\n"
              "        System.out.println(c); // 输出位数\n"
              "    }\n"
              "}\n"),
    )
