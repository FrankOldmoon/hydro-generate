# -*- coding: utf-8 -*-
"""P1056 子串截取"""
from generate import make_problem


def build():
    data = [
        ("hello", 1, 3), ("world", 2, 4), ("abc", 1, 1), ("abcdef", 2, 5),
        ("python", 1, 4), ("test", 2, 3), ("abcdef", 3, 6), ("xy", 1, 2),
        ("Hello", 1, 5), ("abcde", 2, 4),
    ]
    cases = [(f"{s}\n{a}\n{b}\n", f"{s[a - 1:b]}\n") for s, a, b in data]
    return make_problem(
        "P1056", "子串截取", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and two positive integers a, b (one per line, "
                "with $1\\leq a\\leq b\\leq |s|$), print the substring of s from "
                "the a-th character to the b-th character (inclusive).",
        input_en="Three lines: the first line contains a string s (without spaces), "
                 "the second line contains a, the third line contains b, satisfying "
                 "$1\\leq |s|\\leq 100$ and $1\\leq a\\leq b\\leq |s|$ .",
        output_en="One line: the substring s[a..b] (1-based, inclusive).",
        desc_zh="给定一个字符串 s 和两个正整数 a、b，输出 s 从第 a 个字符到第 b 个字符"
                "（包含两端）的子串。",
        input_zh="三行：第一行一个字符串 s（不含空格），第二行一个正整数 a，第三行一个正整数 "
                 "b，满足 $1\\leq |s|\\leq 100$ 且 $1\\leq a\\leq b\\leq |s|$ 。",
        output_zh="一行，输出从第 a 个字符到第 b 个字符的子串。",
        py=("# P1056 子串截取（切片 [a-1:b]，1-based 转 0-based）\n"
            "s = input()               # 字符串 s\n"
            "a = int(input())          # 起始位置 a（从 1 开始）\n"
            "b = int(input())          # 结束位置 b（包含）\n"
            "print(s[a - 1:b])         # 切片截取\n"),
        cpp=("// P1056 子串截取\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    int a, b;\n"
             "    cin >> s >> a >> b;\n"
             "    cout << s.substr(a - 1, b - a + 1) << endl;  // 起始位置，长度\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1056 子串截取\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int a = sc.nextInt();\n"
              "        int b = sc.nextInt();\n"
              "        System.out.println(s.substring(a - 1, b));  // 起始(含)，结束(不含)\n"
              "    }\n"
              "}\n"),
    )
