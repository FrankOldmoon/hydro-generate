# -*- coding: utf-8 -*-
"""P1046 字符串长度"""
from generate import make_problem


def build():
    data = ["hello", "a", "abc123", "HelloWorld", "python",
            "x", "12345", "Test", "abc", "Programming"]
    cases = [(f"{s}\n", f"{len(s)}\n") for s in data]
    return make_problem(
        "P1046", "字符串长度", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, print its length (number of characters).",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line containing the length of s.",
        desc_zh="给定一个字符串 s，输出它的长度（字符个数）。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出字符串的长度。",
        py=("# P1046 字符串长度（len 求长度）\n"
            "s = input()                # 字符串 s\n"
            "print(len(s))              # len 求字符个数\n"),
        cpp=("// P1046 字符串长度\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;                  // 读入字符串 s\n"
             "    cout << s.length() << endl; // length 求长度\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1046 字符串长度\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();        // 读入字符串 s\n"
              "        System.out.println(s.length()); // length 求长度\n"
              "    }\n"
              "}\n"),
    )
