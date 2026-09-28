# -*- coding: utf-8 -*-
"""P1053 大写转小写"""
from generate import make_problem


def build():
    data = ["Hello", "ABC", "WorLD", "aBc", "PYTHON",
            "Test", "ABCDEF", "xYz", "Good", "HELLO"]
    cases = [(f"{s}\n", f"{s.lower()}\n") for s in data]
    return make_problem(
        "P1053", "大写转小写", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s consisting of letters, convert all uppercase "
                "letters in it to lowercase and print the result.",
        input_en="One line containing a string s of letters, satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: s with all letters converted to lowercase.",
        desc_zh="给定一个由字母组成的字符串 s，将其中的大写字母全部转为小写后输出。",
        input_zh="一行一个由字母组成的字符串 s，满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出全部转为小写后的字符串。",
        py=("# P1053 大写转小写（lower 方法）\n"
            "s = input()               # 字符串 s\n"
            "print(s.lower())          # 全部转为小写\n"),
        cpp=("// P1053 大写转小写\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <cctype>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    for (char &ch : s) ch = tolower(ch);  // 逐个转小写\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1053 大写转小写\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        System.out.println(s.toLowerCase());  // 全部转为小写\n"
              "    }\n"
              "}\n"),
    )
