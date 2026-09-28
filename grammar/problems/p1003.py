# -*- coding: utf-8 -*-
"""P1003 Hi 字符串"""
from generate import make_problem


def build():
    data = ["Tom", "Alice", "World", "Python", "Java",
            "Cpp", "Hydro", "123", "a", "Hello"]
    cases = [(f"{s}\n", f"Hi {s}\n") for s in data]
    return make_problem(
        "P1003", "Hi 字符串", ["入门", "输入输出", "字符串"],
        cases=cases,
        desc_en="Given a string s (a single word without spaces), print \"Hi \" "
                "followed by s.",
        input_en="One line containing a string s (a single word without spaces), "
                 "with length $1\\leq |s|\\leq 100$ .",
        output_en="One line containing \"Hi \" followed by s (i.e. Hi s).",
        desc_zh="给定一个字符串 s（不含空格的单个单词），输出 \"Hi \" 加上 s。",
        input_zh="一行一个字符串 s（不含空格的单个单词），长度满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出 \"Hi \" 加上 s（即 Hi s）。",
        py=("# P1003 Hi 字符串\n"
            "# 读入一个字符串，输出 Hi 加上该字符串\n"
            "s = input()        # 读入字符串 s\n"
            "print('Hi', s)     # 输出 Hi s（print 自动加空格）\n"),
        cpp=("// P1003 Hi 字符串\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;             // 读入字符串 s（不含空格）\n"
             "    cout << \"Hi \" << s << endl; // 输出 Hi s\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1003 Hi 字符串\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();      // 读入字符串 s（不含空格）\n"
              "        System.out.println(\"Hi \" + s); // 输出 Hi s\n"
              "    }\n"
              "}\n"),
    )
