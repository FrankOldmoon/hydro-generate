# -*- coding: utf-8 -*-
"""P1060 判断是否全是字母"""
from generate import make_problem


def build():
    data = ["abc", "ab1", "Hello", "PYTHON", "abc123",
            "123", "Test", "xyz", "aB3", "world"]
    cases = [(f"{s}\n", f"{'Yes' if s.isalpha() else 'No'}\n") for s in data]
    return make_problem(
        "P1060", "判断是否全是字母", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, determine whether it consists entirely of "
                "letters. Print \"Yes\" if so, otherwise \"No\".",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: \"Yes\" if all characters are letters, otherwise "
                  "\"No\".",
        desc_zh="给定一个字符串 s，判断它是否全部由字母组成。是输出 \"Yes\"，否则输出 "
                "\"No\"。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，全是字母输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1060 判断是否全是字母（isalpha 方法）\n"
            "s = input()               # 字符串 s\n"
            "if s.isalpha():           # 全是字母\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1060 判断是否全是字母\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <cctype>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    bool all = true;\n"
             "    for (char ch : s)\n"
             "        if (!isalpha(ch)) { all = false; break; }\n"
             "    cout << (all ? \"Yes\" : \"No\") << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1060 判断是否全是字母\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        boolean all = true;\n"
              "        for (int i = 0; i < s.length(); ++i)\n"
              "            if (!Character.isLetter(s.charAt(i))) { all = false; break; }\n"
              "        System.out.println(all ? \"Yes\" : \"No\");\n"
              "    }\n"
              "}\n"),
    )
