# -*- coding: utf-8 -*-
"""P1059 判断是否全是数字"""
from generate import make_problem


def build():
    data = ["123", "12a3", "0", "abc", "007",
            "9999", "45x", "12345", "100", "42"]
    cases = [(f"{s}\n", f"{'Yes' if s.isdigit() else 'No'}\n") for s in data]
    return make_problem(
        "P1059", "判断是否全是数字", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, determine whether it consists entirely of digit "
                "characters. Print \"Yes\" if so, otherwise \"No\".",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: \"Yes\" if all characters are digits, otherwise \"No\".",
        desc_zh="给定一个字符串 s，判断它是否全部由数字字符组成。是输出 \"Yes\"，否则输出 "
                "\"No\"。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，全是数字输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1059 判断是否全是数字（isdigit 方法）\n"
            "s = input()               # 字符串 s\n"
            "if s.isdigit():           # 全是数字字符\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1059 判断是否全是数字\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <cctype>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    bool all = true;\n"
             "    for (char ch : s)\n"
             "        if (!isdigit(ch)) { all = false; break; }\n"
             "    cout << (all ? \"Yes\" : \"No\") << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1059 判断是否全是数字\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        boolean all = true;\n"
              "        for (int i = 0; i < s.length(); ++i)\n"
              "            if (!Character.isDigit(s.charAt(i))) { all = false; break; }\n"
              "        System.out.println(all ? \"Yes\" : \"No\");\n"
              "    }\n"
              "}\n"),
    )
