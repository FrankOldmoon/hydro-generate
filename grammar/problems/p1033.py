# -*- coding: utf-8 -*-
"""P1033 反转数字"""
from generate import make_problem


def _rev(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r


def build():
    data = [123, 100, 0, 5, 1200, 12345, 1000, 9, 10, 9876]
    cases = [(f"{n}\n", f"{_rev(n)}\n") for n in data]
    return make_problem(
        "P1033", "反转数字", ["入门", "循环结构", "while"],
        cases=cases,
        desc_en="Given a non-negative integer n, print the number formed by "
                "reversing its decimal digits (leading zeros of the reversed "
                "number are dropped). For example, 1200 becomes 21.",
        input_en="One line containing a non-negative integer n, satisfying "
                 "$0\\leq n\\leq 1000000000$ .",
        output_en="One line containing the reversed number.",
        desc_zh="给定一个非负整数 n，输出将其十进制各位反转后得到的数（反转后前导 0 舍去）。"
                "例如 1200 反转后为 21。",
        input_zh="一行一个非负整数 n，满足 $0\\leq n\\leq 1000000000$ 。",
        output_zh="一行，输出反转后的数。",
        py=("# P1033 反转数字（while：逐位取余拼接到新数）\n"
            "n = int(input())            # 非负整数 n\n"
            "r = 0                       # 反转后的数\n"
            "while n > 0:                # while：n 还有未处理的位\n"
            "    r = r * 10 + n % 10     # 取出末位拼到 r 的末尾\n"
            "    n //= 10                # 去掉 n 的末位\n"
            "print(r)                    # 输出反转后的数（n=0 时 r=0）\n"),
        cpp=("// P1033 反转数字（while）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入非负整数 n\n"
             "    int r = 0;               // 反转后的数\n"
             "    while (n > 0) {          // while：n 还有未处理的位\n"
             "        r = r * 10 + n % 10; // 取出末位拼到 r 的末尾\n"
             "        n /= 10;             // 去掉 n 的末位\n"
             "    }\n"
             "    cout << r << endl;       // 输出反转后的数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1033 反转数字（while）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 非负整数 n\n"
              "        int r = 0;              // 反转后的数\n"
              "        while (n > 0) {         // while：n 还有未处理的位\n"
              "            r = r * 10 + n % 10; // 取出末位拼到 r 的末尾\n"
              "            n /= 10;            // 去掉 n 的末位\n"
              "        }\n"
              "        System.out.println(r); // 输出反转后的数\n"
              "    }\n"
              "}\n"),
    )
