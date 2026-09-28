# -*- coding: utf-8 -*-
"""P1061 替换字符"""
from generate import make_problem


def build():
    data = [
        ("hello", 'l', 'L'), ("banana", 'a', 'A'), ("abc", 'x', 'y'),
        ("aaa", 'a', 'b'), ("Mississippi", 's', 'S'), ("world", 'o', '0'),
        ("test", 't', 'T'), ("Hello", 'l', 'L'), ("abc123", '1', 'X'),
        ("rrrr", 'r', 'R'),
    ]
    cases = [(f"{s}\n{a}\n{b}\n", f"{s.replace(a, b)}\n") for s, a, b in data]
    return make_problem(
        "P1061", "替换字符", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and two characters a, b (one per line), replace "
                "every occurrence of a in s with b and print the result.",
        input_en="Three lines: the first line contains a string s (without spaces), "
                 "the second line contains a single character a, the third line "
                 "contains a single character b, satisfying $1\\leq |s|\\leq 100$ .",
        output_en="One line: s with every a replaced by b.",
        desc_zh="给定一个字符串 s 和两个字符 a、b，将 s 中所有字符 a 替换为 b 后输出。",
        input_zh="三行：第一行一个字符串 s（不含空格），第二行一个字符 a，第三行一个字符 b，"
                 "满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出将所有 a 替换为 b 后的字符串。",
        py=("# P1061 替换字符（replace 方法）\n"
            "s = input()               # 字符串 s\n"
            "a = input()               # 被替换的字符 a\n"
            "b = input()               # 替换为的字符 b\n"
            "print(s.replace(a, b))    # 把所有 a 替换为 b\n"),
        cpp=("// P1061 替换字符\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    char a, b;\n"
             "    cin >> s >> a >> b;\n"
             "    for (char &ch : s)\n"
             "        if (ch == a) ch = b;        // 逐个替换\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1061 替换字符\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        char a = sc.next().charAt(0);\n"
              "        char b = sc.next().charAt(0);\n"
              "        System.out.println(s.replace(a, b));  // 把所有 a 替换为 b\n"
              "    }\n"
              "}\n"),
    )
