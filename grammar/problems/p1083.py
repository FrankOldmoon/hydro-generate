# -*- coding: utf-8 -*-
"""P1083 判断完全平方数"""
from generate import make_problem


def build():
    data = [
        (5, [1, 2, 4, 9, 10]),
        (1, [1]),
        (3, [3, 4, 5]),
        (1, [16]),
        (4, [36, 37, 49, 50]),
        (2, [81, 82]),
        (1, [144]),
        (3, [2, 3, 5]),
        (2, [64, 65]),
        (1, [10000]),
    ]

    def is_square(x):
        i = 1
        while i * i <= x:
            if i * i == x:
                return True
            i += 1
        return False

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{'Yes' if is_square(x) else 'No'}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1083", "判断完全平方数", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n positive integers, determine whether each is a "
                "perfect square (i.e., there exists an integer k such that "
                "k*k equals the number). Print \"Yes\" or \"No\".",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a positive integer.",
        output_en="n lines: \"Yes\" if perfect square, otherwise \"No\".",
        desc_zh="给定 n 及 n 个正整数，判断每个数是否为完全平方数（存在整数 k 使 "
                "k×k 等于该数）。是输出 \"Yes\"，否则输出 \"No\"。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个正整数。",
        output_zh="n 行，完全平方数输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1083 判断完全平方数（自定义函数判断）\n"
            "def is_square(x):          # 定义判断完全平方数的函数\n"
            "    i = 1\n"
            "    while i * i <= x:      # 从 1 开始试\n"
            "        if i * i == x:\n"
            "            return True\n"
            "        i += 1\n"
            "    return False\n"
            "\n"
            "n = int(input())            # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if is_square(x):\n"
            "        print('Yes')\n"
            "    else:\n"
            "        print('No')\n"),
        cpp=("// P1083 判断完全平方数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_square(int x) {    // 判断完全平方数\n"
             "    for (int i = 1; i * i <= x; ++i)\n"
             "        if (i * i == x) return true;\n"
             "    return false;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << (is_square(x) ? \"Yes\" : \"No\") << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1083 判断完全平方数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isSquare(int x) {  // 判断完全平方数\n"
              "        for (int i = 1; i * i <= x; ++i)\n"
              "            if (i * i == x) return true;\n"
              "        return false;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(isSquare(x) ? \"Yes\" : \"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
