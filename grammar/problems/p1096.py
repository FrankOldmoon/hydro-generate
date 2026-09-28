# -*- coding: utf-8 -*-
"""P1096 递归十进制转二进制"""
from generate import make_problem


def build():
    data = [0, 1, 2, 3, 5, 8, 10, 16, 100, 255]

    def dec2bin(n):
        if n <= 1:                  # 递归出口：0 或 1 直接返回对应字符
            return str(n)
        return dec2bin(n // 2) + str(n % 2)   # 高位在前，末位在后

    cases = [(f"{n}\n", f"{dec2bin(n)}\n") for n in data]
    return make_problem(
        "P1096", "十进制转二进制", ["入门", "递归"],
        cases=cases,
        desc_en="Given a non-negative integer n, print its binary representation "
                "(without leading zeros; n=0 prints \"0\").",
        input_en="One line containing a non-negative integer n, satisfying "
                 "$0\\leq n\\leq 1000000000$ .",
        output_en="One line containing the binary representation of n.",
        desc_zh="给定一个非负整数 n，求它的二进制表示（不含前导 0，n=0 输出 "
                "\"0\"）并输出。",
        input_zh="一行一个非负整数 n，满足 $0\\leq n\\leq 1000000000$ 。",
        output_zh="一行，输出 n 的二进制表示。",
        py=("# P1096 递归十进制转二进制（递归：高位 + 末位）\n"
            "def dec2bin(n):             # 定义递归函数\n"
            "    if n <= 1:            # 递归出口：0 或 1\n"
            "        return str(n)\n"
            "    return dec2bin(n // 2) + str(n % 2)  # 高位在前，末位在后\n"
            "\n"
            "n = int(input())           # 非负整数 n\n"
            "print(dec2bin(n))\n"),
        cpp=("// P1096 递归十进制转二进制\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "string dec2bin(int n) {   // 递归转二进制\n"
             "    if (n <= 1) return to_string(n);  // 递归出口\n"
             "    return dec2bin(n / 2) + to_string(n % 2);\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    cout << dec2bin(n) << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1096 递归十进制转二进制\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static String dec2bin(int n) {  // 递归转二进制\n"
              "        if (n <= 1) return Integer.toString(n);  // 递归出口\n"
              "        return dec2bin(n / 2) + (n % 2);\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        System.out.println(dec2bin(n));\n"
              "    }\n"
              "}\n"),
    )
