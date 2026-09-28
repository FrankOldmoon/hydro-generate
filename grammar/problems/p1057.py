# -*- coding: utf-8 -*-
"""P1057 查找字符位置"""
from generate import make_problem


def build():
    data = [
        ("hello", 'l'), ("apple", 'p'), ("abc", 'z'), ("aaaa", 'a'),
        ("world", 'd'), ("banana", 'n'), ("test", 't'), ("xyz", 'y'),
        ("Hello", 'l'), ("abc123", '2'),
    ]
    cases = [(f"{s}\n{c}\n", f"{s.find(c) + 1}\n") for s, c in data]
    return make_problem(
        "P1057", "查找字符位置", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and a character c (one per line), print the "
                "1-based position of the first occurrence of c in s. If c does "
                "not appear in s, print 0.",
        input_en="Two lines: the first line contains a string s (without spaces), "
                 "the second line contains a single character c, satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the 1-based index of the first c, or 0 if not found.",
        desc_zh="给定一个字符串 s 和一个字符 c，输出 c 在 s 中第一次出现的位置（从 1 开始）。"
                "若 c 不在 s 中，输出 0。",
        input_zh="两行：第一行一个字符串 s（不含空格），第二行一个字符 c，满足 "
                 "$1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出 c 第一次出现的位置（从 1 开始），不存在则输出 0。",
        py=("# P1057 查找字符位置（find 方法，未找到返回 -1）\n"
            "s = input()               # 字符串 s\n"
            "c = input()               # 待查找的字符 c\n"
            "print(s.find(c) + 1)      # find 找首次位置，+1 转为从 1 开始；未找到 -1+1=0\n"),
        cpp=("// P1057 查找字符位置\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    char ch;\n"
             "    cin >> s >> ch;\n"
             "    size_t pos = s.find(ch);\n"
             "    if (pos == string::npos) cout << 0 << endl;     // 未找到\n"
             "    else cout << (int)pos + 1 << endl;              // +1 转为从 1 开始\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1057 查找字符位置\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        char ch = sc.next().charAt(0);\n"
              "        int pos = s.indexOf(ch);        // 未找到返回 -1\n"
              "        System.out.println(pos + 1);    // +1 转为从 1 开始；未找到 -1+1=0\n"
              "    }\n"
              "}\n"),
    )
