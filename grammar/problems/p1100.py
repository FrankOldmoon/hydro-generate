# -*- coding: utf-8 -*-
"""P1100 递归倒序输出整数各位"""
from generate import make_problem


def build():
    data = [123, 1, 12, 100, 9876, 5, 10, 1000, 54321, 9]

    def print_reverse(n):
        # 先输出末位，再递归处理剩余，实现倒序
        print(n % 10)          # 输出末位
        if n >= 10:            # 还有高位则继续递归
            print_reverse(n // 10)

    cases = []
    for n in data:
        out = ""
        x = n
        while True:
            out += f"{x % 10}\n"
            if x < 10:
                break
            x //= 10
        cases.append((f"{n}\n", out))
    return make_problem(
        "P1100", "倒序输出整数各位", ["入门", "递归"],
        cases=cases,
        desc_en="Given a positive integer n, print its decimal digits in reverse "
                "order, one digit per line.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000000000$ .",
        output_en="Several lines: the digits of n from last to first, one per "
                  "line.",
        desc_zh="给定一个正整数 n，将它的各位数字按倒序输出，每位一行。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000000000$ 。",
        output_zh="若干行，按从低位到高位的顺序输出 n 的各位数字，每位一行。",
        py=("# P1100 递归倒序输出整数各位（先输出末位再递归）\n"
            "def print_reverse(n):     # 定义递归函数\n"
            "    print(n % 10)        # 先输出末位（个位）\n"
            "    if n >= 10:          # 还有高位则继续递归\n"
            "        print_reverse(n // 10)\n"
            "\n"
            "n = int(input())          # 正整数 n\n"
            "print_reverse(n)\n"),
        cpp=("// P1100 递归倒序输出整数各位\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "void print_reverse(int n) {  // 递归倒序输出\n"
             "    cout << n % 10 << endl;  // 输出末位\n"
             "    if (n >= 10) print_reverse(n / 10);  // 还有高位则递归\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    print_reverse(n);\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1100 递归倒序输出整数各位\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static void printReverse(int n) {  // 递归倒序输出\n"
              "        System.out.println(n % 10);   // 输出末位\n"
              "        if (n >= 10) printReverse(n / 10);  // 还有高位则递归\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        printReverse(n);\n"
              "    }\n"
              "}\n"),
    )
