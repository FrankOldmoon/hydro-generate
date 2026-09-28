# -*- coding: utf-8 -*-
"""P1063 字符串比较"""
from generate import make_problem


def build():
    data = [
        ("abc", "abd"), ("z", "a"), ("abc", "abc"), ("ab", "abc"),
        ("hello", "world"), ("Python", "python"), ("abc", "abb"),
        ("test", "test"), ("123", "124"), ("apple", "apply"),
    ]

    def cmp(s1, s2):
        if s1 < s2:
            return s1
        if s1 > s2:
            return s2
        return "Equal"

    cases = [(f"{a}\n{b}\n", f"{cmp(a, b)}\n") for a, b in data]
    return make_problem(
        "P1063", "字符串比较", ["入门", "字符串"],
        cases=cases,
        desc_en="Given two strings s1 and s2 (one per line), print the "
                "lexicographically smaller one. If they are equal, print \"Equal\".",
        input_en="Two lines: each line contains one string (without spaces), "
                 "denoted s1, s2, satisfying $1\\leq |s1|,|s2|\\leq 100$ .",
        output_en="One line: the lexicographically smaller string, or \"Equal\".",
        desc_zh="给定两个字符串 s1 和 s2，按字典序输出较小的那个。若两者相等，输出 "
                "\"Equal\"。",
        input_zh="两行：每行一个字符串（不含空格），依次为 s1、s2，满足 "
                 "$1\\leq |s1|,|s2|\\leq 100$ 。",
        output_zh="一行，输出字典序较小的字符串，相等则输出 \"Equal\"。",
        py=("# P1063 字符串比较（字典序比较）\n"
            "s1 = input()              # 第一个字符串\n"
            "s2 = input()              # 第二个字符串\n"
            "if s1 < s2:               # s1 字典序在前\n"
            "    print(s1)\n"
            "elif s1 > s2:             # s2 字典序在前\n"
            "    print(s2)\n"
            "else:                     # 相等\n"
            "    print('Equal')\n"),
        cpp=("// P1063 字符串比较\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s1, s2;\n"
             "    cin >> s1 >> s2;\n"
             "    if (s1 < s2) cout << s1 << endl;\n"
             "    else if (s1 > s2) cout << s2 << endl;\n"
             "    else cout << \"Equal\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1063 字符串比较\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s1 = sc.next();\n"
              "        String s2 = sc.next();\n"
              "        int c = s1.compareTo(s2);   // 字典序比较\n"
              "        if (c < 0) System.out.println(s1);\n"
              "        else if (c > 0) System.out.println(s2);\n"
              "        else System.out.println(\"Equal\");\n"
              "    }\n"
              "}\n"),
    )
