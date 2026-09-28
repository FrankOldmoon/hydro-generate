# -*- coding: utf-8 -*-
"""P1048 首尾字符"""
from generate import make_problem


def build():
    data = ["hello", "abc", "a", "xyz", "ab",
            "Programming", "test", "12345", "Hi", "Z"]
    cases = [(f"{s}\n", f"{s[0]} {s[-1]}\n") for s in data]
    return make_problem(
        "P1048", "首尾字符", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, print its first character and its last "
                "character, separated by a space.",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the first character and the last character of s, "
                  "separated by a space.",
        desc_zh="给定一个字符串 s，输出它的第一个字符和最后一个字符（以空格分隔）。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出第一个字符和最后一个字符，以空格分隔。",
        py=("# P1048 首尾字符（下标访问首末字符）\n"
            "s = input()               # 字符串 s\n"
            "print(s[0], s[-1])        # 第一个和最后一个字符，空格分隔\n"),
        cpp=("// P1048 首尾字符\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    cout << s[0] << ' ' << s[s.length() - 1] << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1048 首尾字符\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        System.out.println(s.charAt(0) + \" \" + s.charAt(s.length() - 1));\n"
              "    }\n"
              "}\n"),
    )
