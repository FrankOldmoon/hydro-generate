# -*- coding: utf-8 -*-
"""P1054 字符串反转"""
from generate import make_problem


def build():
    data = ["hello", "abc", "a", "12345", "world",
            "abcd", "xy", "racecar", "Test", "Python"]
    cases = [(f"{s}\n", f"{s[::-1]}\n") for s in data]
    return make_problem(
        "P1054", "字符串反转", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, print the string obtained by reversing s.",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the reversed string.",
        desc_zh="给定一个字符串 s，输出将其反转后的字符串。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出反转后的字符串。",
        py=("# P1054 字符串反转（切片 [::-1]）\n"
            "s = input()               # 字符串 s\n"
            "print(s[::-1])            # 切片反转\n"),
        cpp=("// P1054 字符串反转\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    reverse(s.begin(), s.end());  // 反转\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1054 字符串反转\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        System.out.println(new StringBuilder(s).reverse().toString());\n"
              "    }\n"
              "}\n"),
    )
