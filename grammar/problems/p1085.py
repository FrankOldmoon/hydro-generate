# -*- coding: utf-8 -*-
"""P1085 判断水仙花数"""
from generate import make_problem


def build():
    data = [
        (1, [153]),
        (1, [370]),
        (4, [153, 370, 371, 407]),
        (1, [100]),
        (3, [100, 200, 300]),
        (2, [153, 154]),
        (1, [999]),
        (3, [111, 222, 333]),
        (2, [407, 408]),
        (1, [555]),
    ]

    def is_narcissistic(x):
        a = x // 100          # 百位
        b = x // 10 % 10      # 十位
        c = x % 10            # 个位
        return a * a * a + b * b * b + c * c * c == x

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{'Yes' if is_narcissistic(x) else 'No'}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1085", "判断水仙花数", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n three-digit positive integers, determine whether "
                "each is a narcissistic number (the sum of cubes of its digits "
                "equals itself). Print \"Yes\" or \"No\".",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a three-digit positive integer "
                 "($100\\leq x\\leq 999$).",
        output_en="n lines: \"Yes\" if narcissistic, otherwise \"No\".",
        desc_zh="给定 n 及 n 个三位正整数，判断每个数是否为水仙花数（各位数字的立方和"
                "等于自身）。是输出 \"Yes\"，否则输出 \"No\"。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个三位正整数（$100\\leq x\\leq 999$）。",
        output_zh="n 行，水仙花数输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1085 判断水仙花数（自定义函数判断水仙花数）\n"
            "def is_narcissistic(x):   # 定义判断水仙花数的函数\n"
            "    a = x // 100          # 百位\n"
            "    b = x // 10 % 10      # 十位\n"
            "    c = x % 10            # 个位\n"
            "    return a*a*a + b*b*b + c*c*c == x\n"
            "\n"
            "n = int(input())           # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if is_narcissistic(x):\n"
            "        print('Yes')\n"
            "    else:\n"
            "        print('No')\n"),
        cpp=("// P1085 判断水仙花数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_narcissistic(int x) {  // 判断水仙花数\n"
             "    int a = x / 100;\n"
             "    int b = x / 10 % 10;\n"
             "    int c = x % 10;\n"
             "    return a*a*a + b*b*b + c*c*c == x;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << (is_narcissistic(x) ? \"Yes\" : \"No\") << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1085 判断水仙花数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isNarcissistic(int x) {  // 判断水仙花数\n"
              "        int a = x / 100;\n"
              "        int b = x / 10 % 10;\n"
              "        int c = x % 10;\n"
              "        return a*a*a + b*b*b + c*c*c == x;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(isNarcissistic(x) ? \"Yes\" : \"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
