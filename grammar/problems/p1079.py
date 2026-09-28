# -*- coding: utf-8 -*-
"""P1079 判断闰年"""
from generate import make_problem


def build():
    data = [
        (5, [2000, 1900, 2020, 2021, 2024]),
        (1, [2000]),
        (1, [1900]),
        (1, [2400]),
        (1, [2100]),
        (3, [1996, 1997, 1998]),
        (2, [2023, 2024]),
        (1, [1800]),
        (4, [2000, 2001, 2002, 2003]),
        (2, [1600, 1700]),
    ]

    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    cases = []
    for n, years in data:
        inp = f"{n}\n" + "".join(f"{y}\n" for y in years)
        out = "".join(f"{'Yes' if is_leap(y) else 'No'}\n" for y in years)
        cases.append((inp, out))
    return make_problem(
        "P1079", "判断闰年", ["入门", "函数"],
        cases=cases,
        desc_en="Given n years, determine whether each is a leap year. A leap year "
                "is divisible by 400, or divisible by 4 but not by 100.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a year (a positive integer).",
        output_en="n lines: \"Yes\" if leap year, otherwise \"No\".",
        desc_zh="给定 n 个年份，判断每个是否为闰年。闰年规则：能被 400 整除，或能被 4 "
                "整除但不能被 100 整除。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个年份（正整数）。",
        output_zh="n 行，闰年输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1079 判断闰年（自定义函数判断闰年）\n"
            "def is_leap(year):           # 定义判断闰年的函数\n"
            "    if year % 400 == 0:\n"
            "        return True\n"
            "    if year % 100 == 0:\n"
            "        return False\n"
            "    if year % 4 == 0:\n"
            "        return True\n"
            "    return False\n"
            "\n"
            "n = int(input())             # 年份个数 n\n"
            "for i in range(n):\n"
            "    year = int(input())\n"
            "    if is_leap(year):\n"
            "        print('Yes')\n"
            "    else:\n"
            "        print('No')\n"),
        cpp=("// P1079 判断闰年\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_leap(int year) {      // 判断闰年\n"
             "    if (year % 400 == 0) return true;\n"
             "    if (year % 100 == 0) return false;\n"
             "    if (year % 4 == 0) return true;\n"
             "    return false;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int year;\n"
             "        cin >> year;\n"
             "        cout << (is_leap(year) ? \"Yes\" : \"No\") << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1079 判断闰年\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isLeap(int year) {  // 判断闰年\n"
              "        if (year % 400 == 0) return true;\n"
              "        if (year % 100 == 0) return false;\n"
              "        if (year % 4 == 0) return true;\n"
              "        return false;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int year = sc.nextInt();\n"
              "            System.out.println(isLeap(year) ? \"Yes\" : \"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
