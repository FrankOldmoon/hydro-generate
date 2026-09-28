# -*- coding: utf-8 -*-
"""P1065 是否包含子串"""
from generate import make_problem


def build():
    data = [
        ("hello", "ell"), ("world", "abc"), ("abcabc", "cab"), ("a", "a"),
        ("python", "th"), ("Hello", "ell"), ("test", "es"), ("abc", "ab"),
        ("xyzxyz", "yzx"), ("programming", "gram"),
    ]
    cases = [(f"{s}\n{t}\n", f"{'Yes' if t in s else 'No'}\n") for s, t in data]
    return make_problem(
        "P1065", "是否包含子串", ["入门", "字符串"],
        cases=cases,
        desc_en="Given two strings s and t (one per line), determine whether t is "
                "a substring of s. Print \"Yes\" if so, otherwise \"No\".",
        input_en="Two lines: each line contains one string (without spaces), "
                 "denoted s, t, satisfying $1\\leq |s|,|t|\\leq 100$ and $|t|\\leq |s|$ .",
        output_en="One line: \"Yes\" if t is a substring of s, otherwise \"No\".",
        desc_zh="给定两个字符串 s 和 t，判断 t 是否是 s 的子串。是输出 \"Yes\"，否则输出 "
                "\"No\"。",
        input_zh="两行：每行一个字符串（不含空格），依次为 s、t，满足 $1\\leq |t|\\leq |s|\\leq 100$ 。",
        output_zh="一行，t 是 s 的子串输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1065 是否包含子串（in 运算符）\n"
            "s = input()               # 字符串 s\n"
            "t = input()               # 子串 t\n"
            "if t in s:                # 判断 t 是否为 s 的子串\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1065 是否包含子串\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s, t;\n"
             "    cin >> s >> t;\n"
             "    if (s.find(t) != string::npos) cout << \"Yes\" << endl;  // 找到\n"
             "    else cout << \"No\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1065 是否包含子串\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        String t = sc.next();\n"
              "        System.out.println(s.contains(t) ? \"Yes\" : \"No\");  // 判断是否包含\n"
              "    }\n"
              "}\n"),
    )
