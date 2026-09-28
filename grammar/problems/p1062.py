# -*- coding: utf-8 -*-
"""P1062 删除指定字符"""
from generate import make_problem


def build():
    data = [
        ("hello", 'l'), ("banana", 'a'), ("abc", 'x'), ("aaaa", 'a'),
        ("Mississippi", 's'), ("world", 'o'), ("test", 't'),
        ("Hello", 'l'), ("abc123", '1'), ("rrrr", 'r'),
    ]
    cases = [(f"{s}\n{c}\n", f"{s.replace(c, '')}\n") for s, c in data]
    return make_problem(
        "P1062", "删除指定字符", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and a character c (one per line), remove every "
                "occurrence of c from s and print the result.",
        input_en="Two lines: the first line contains a string s (without spaces), "
                 "the second line contains a single character c, satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: s with every c removed.",
        desc_zh="给定一个字符串 s 和一个字符 c，将 s 中所有字符 c 删除后输出。",
        input_zh="两行：第一行一个字符串 s（不含空格），第二行一个字符 c，满足 "
                 "$1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出删除所有 c 后的字符串。",
        py=("# P1062 删除指定字符（replace 替换为空串）\n"
            "s = input()               # 字符串 s\n"
            "c = input()               # 待删除的字符 c\n"
            "print(s.replace(c, ''))   # 替换为空串即删除\n"),
        cpp=("// P1062 删除指定字符\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    char c;\n"
             "    cin >> s >> c;\n"
             "    string r;\n"
             "    for (char ch : s)\n"
             "        if (ch != c) r += ch;       // 不等于 c 的保留\n"
             "    cout << r << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1062 删除指定字符\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        char c = sc.next().charAt(0);\n"
              "        StringBuilder sb = new StringBuilder();\n"
              "        for (int i = 0; i < s.length(); ++i)\n"
              "            if (s.charAt(i) != c) sb.append(s.charAt(i));  // 不等于 c 的保留\n"
              "        System.out.println(sb.toString());\n"
              "    }\n"
              "}\n"),
    )
