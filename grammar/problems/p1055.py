# -*- coding: utf-8 -*-
"""P1055 判断回文"""
from generate import make_problem


def build():
    data = ["aba", "abc", "a", "abba", "abab",
            "racecar", "hello", "madam", "level", "xyz"]
    cases = [(f"{s}\n", f"{'Yes' if s == s[::-1] else 'No'}\n") for s in data]
    return make_problem(
        "P1055", "判断回文", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, determine whether it is a palindrome (reads the "
                "same forwards and backwards). Print \"Yes\" if so, otherwise "
                "\"No\".",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: \"Yes\" if s is a palindrome, otherwise \"No\".",
        desc_zh="给定一个字符串 s，判断它是否为回文串（正读与反读相同）。是输出 \"Yes\"，"
                "否则输出 \"No\"。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，是回文输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1055 判断回文（与反转后比较）\n"
            "s = input()               # 字符串 s\n"
            "if s == s[::-1]:          # 与反转后相同则是回文\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1055 判断回文\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    string r = s;\n"
             "    reverse(r.begin(), r.end());\n"
             "    cout << (s == r ? \"Yes\" : \"No\") << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1055 判断回文\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        String r = new StringBuilder(s).reverse().toString();\n"
              "        System.out.println(s.equals(r) ? \"Yes\" : \"No\");\n"
              "    }\n"
              "}\n"),
    )
