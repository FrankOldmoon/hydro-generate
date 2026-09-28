# -*- coding: utf-8 -*-
"""P1052 统计指定字符"""
from generate import make_problem


def build():
    data = [
        ("hello", 'l'), ("apple", 'p'), ("abc", 'z'), ("aaaa", 'a'),
        ("Mississippi", 's'), ("world", 'o'), ("banana", 'n'),
        ("test", 't'), ("abc123", '1'), ("Hello", 'H'),
    ]
    cases = [(f"{s}\n{c}\n", f"{s.count(c)}\n") for s, c in data]
    return make_problem(
        "P1052", "统计指定字符", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and a character c (one per line), print how many "
                "times c appears in s.",
        input_en="Two lines: the first line contains a string s (without spaces), "
                 "the second line contains a single character c, satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the number of occurrences of c in s.",
        desc_zh="给定一个字符串 s 和一个字符 c，输出 c 在 s 中出现的次数。",
        input_zh="两行：第一行一个字符串 s（不含空格），第二行一个字符 c，满足 "
                 "$1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出 c 出现的次数。",
        py=("# P1052 统计指定字符（count 方法）\n"
            "s = input()               # 字符串 s\n"
            "c = input()               # 待统计的字符 c\n"
            "print(s.count(c))         # count 统计出现次数\n"),
        cpp=("// P1052 统计指定字符\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    char ch;\n"
             "    cin >> s >> ch;\n"
             "    int cnt = 0;\n"
             "    for (char x : s) if (x == ch) ++cnt;\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1052 统计指定字符\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        char ch = sc.next().charAt(0);\n"
              "        int cnt = 0;\n"
              "        for (int i = 0; i < s.length(); ++i)\n"
              "            if (s.charAt(i) == ch) ++cnt;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
