# -*- coding: utf-8 -*-
"""P1081 数字各位之和"""
from generate import make_problem


def build():
    data = [
        (5, [123, 0, 999, 100, 5]),
        (1, [0]),
        (3, [1, 12, 123]),
        (1, [9999]),
        (4, [10, 20, 30, 40]),
        (2, [111, 222]),
        (1, [1000000]),
        (3, [7, 77, 777]),
        (2, [99, 999]),
        (1, [5]),
    ]

    def digit_sum(x):
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{digit_sum(x)}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1081", "数字各位之和", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n non-negative integers, print the sum of digits of "
                "each number.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a non-negative integer.",
        output_en="n lines: the digit sum of each number.",
        desc_zh="给定 n 及 n 个非负整数，输出每个数的各位数字之和。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个非负整数。",
        output_zh="n 行，每行输出对应数的各位数字之和。",
        py=("# P1081 数字各位之和（自定义函数求各位之和）\n"
            "def digit_sum(x):           # 定义求各位数字之和的函数\n"
            "    s = 0\n"
            "    while x > 0:\n"
            "        s += x % 10         # 取个位累加\n"
            "        x //= 10            # 去掉个位\n"
            "    return s\n"
            "\n"
            "n = int(input())            # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    print(digit_sum(x))     # 调用函数\n"),
        cpp=("// P1081 数字各位之和\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int digit_sum(int x) {      // 求各位数字之和\n"
             "    int s = 0;\n"
             "    while (x > 0) {\n"
             "        s += x % 10;\n"
             "        x /= 10;\n"
             "    }\n"
             "    return s;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << digit_sum(x) << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1081 数字各位之和\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static int digitSum(int x) {  // 求各位数字之和\n"
              "        int s = 0;\n"
              "        while (x > 0) {\n"
              "            s += x % 10;\n"
              "            x /= 10;\n"
              "        }\n"
              "        return s;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(digitSum(x));\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
