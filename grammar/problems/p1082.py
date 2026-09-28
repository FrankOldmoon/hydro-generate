# -*- coding: utf-8 -*-
"""P1082 判断完全数"""
from generate import make_problem


def build():
    data = [
        (5, [6, 12, 28, 7, 1]),
        (1, [6]),
        (3, [28, 496, 8128]),
        (1, [10]),
        (4, [6, 28, 496, 8128]),
        (2, [12, 18]),
        (1, [496]),
        (3, [1, 2, 3]),
        (2, [8128, 100]),
        (1, [30]),
    ]

    def is_perfect(x):
        if x < 2:
            return False
        s = 0
        i = 1
        while i < x:
            if x % i == 0:
                s += i
            i += 1
        return s == x

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{'Yes' if is_perfect(x) else 'No'}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1082", "判断完全数", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n positive integers, determine whether each is a "
                "perfect number. A perfect number equals the sum of its proper "
                "divisors (excluding itself). For example, 6 = 1 + 2 + 3.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a positive integer, satisfying "
                 "$1\\leq x\\leq 10000$ .",
        output_en="n lines: \"Yes\" if perfect, otherwise \"No\".",
        desc_zh="给定 n 及 n 个正整数，判断每个数是否为完全数。完全数等于除自身外所有"
                "真因子之和，例如 6 = 1 + 2 + 3。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个正整数，满足 "
                 "$1\\leq x\\leq 10000$ 。",
        output_zh="n 行，是完全数输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1082 判断完全数（自定义函数求真因子之和）\n"
            "def is_perfect(x):       # 定义判断完全数的函数\n"
            "    if x < 2:            # 1 及以下不可能是完全数\n"
            "        return False\n"
            "    s = 0\n"
            "    i = 1\n"
            "    while i < x:         # 遍历 1 到 x-1（真因子不含自身）\n"
            "        if x % i == 0:   # 能整除则是真因子\n"
            "            s += i\n"
            "        i += 1\n"
            "    return s == x        # 真因子之和等于自身则是完全数\n"
            "\n"
            "n = int(input())          # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if is_perfect(x):\n"
            "        print('Yes')\n"
            "    else:\n"
            "        print('No')\n"),
        cpp=("// P1082 判断完全数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_perfect(int x) {  // 判断完全数\n"
             "    if (x < 2) return false;\n"
             "    int s = 0;\n"
             "    for (int i = 1; i < x; ++i)\n"
             "        if (x % i == 0) s += i;  // 累加真因子\n"
             "    return s == x;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << (is_perfect(x) ? \"Yes\" : \"No\") << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1082 判断完全数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isPerfect(int x) {  // 判断完全数\n"
              "        if (x < 2) return false;\n"
              "        int s = 0;\n"
              "        for (int i = 1; i < x; ++i)\n"
              "            if (x % i == 0) s += i;  // 累加真因子\n"
              "        return s == x;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(isPerfect(x) ? \"Yes\" : \"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
