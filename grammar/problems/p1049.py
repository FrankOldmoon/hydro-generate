# -*- coding: utf-8 -*-
"""P1049 字符串重复"""
from generate import make_problem


def build():
    data = [
        ("ab", 3), ("a", 5), ("hi", 2), ("x", 1), ("ok", 0),
        ("Ha", 4), ("z", 3), ("Go", 2), ("xy", 4), ("m", 6),
    ]
    cases = [(f"{s}\n{n}\n", f"{s * n}\n") for s, n in data]
    return make_problem(
        "P1049", "字符串重复", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and a non-negative integer n (one per line), "
                "print the string formed by repeating s n times.",
        input_en="Two lines: the first line contains a string s (without spaces), "
                 "the second line contains a non-negative integer n, satisfying "
                 "$1\\leq |s|\\leq 100$ and $0\\leq n\\leq 100$ .",
        output_en="One line: s repeated n times.",
        desc_zh="给定一个字符串 s 和一个非负整数 n，输出将 s 重复 n 次的结果。",
        input_zh="两行：第一行一个字符串 s（不含空格），第二行一个非负整数 n，满足 "
                 "$1\\leq |s|\\leq 100$ 且 $0\\leq n\\leq 100$ 。",
        output_zh="一行，输出 s 重复 n 次的结果。",
        py=("# P1049 字符串重复（* 重复字符串）\n"
            "s = input()               # 字符串 s\n"
            "n = int(input())          # 重复次数 n\n"
            "print(s * n)              # * 重复 n 次\n"),
        cpp=("// P1049 字符串重复\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    int n;\n"
             "    cin >> s >> n;\n"
             "    for (int i = 0; i < n; ++i) cout << s;  // 循环输出 n 次\n"
             "    cout << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1049 字符串重复\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) System.out.print(s);\n"
              "        System.out.println();\n"
              "    }\n"
              "}\n"),
    )
