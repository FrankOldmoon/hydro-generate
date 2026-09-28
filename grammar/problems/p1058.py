# -*- coding: utf-8 -*-
"""P1058 统计大写字母"""
from generate import make_problem


def build():
    data = ["Hello", "ABC", "aBcD", "abc", "HelloWorld",
            "PYTHON", "Test", "aB", "ABCDEF", "xYz"]
    cases = [(f"{s}\n", f"{sum(1 for ch in s if ch.isupper())}\n") for s in data]
    return make_problem(
        "P1058", "统计大写字母", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s, print how many uppercase letters it contains.",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the number of uppercase letters in s.",
        desc_zh="给定一个字符串 s，输出其中大写字母的个数。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出大写字母的个数。",
        py=("# P1058 统计大写字母（isupper 判断）\n"
            "s = input()               # 字符串 s\n"
            "cnt = 0\n"
            "for ch in s:\n"
            "    if ch.isupper():      # 是大写字母\n"
            "        cnt += 1\n"
            "print(cnt)\n"),
        cpp=("// P1058 统计大写字母\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <cctype>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    int cnt = 0;\n"
             "    for (char ch : s)\n"
             "        if (isupper(ch)) ++cnt;   // 是大写字母\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1058 统计大写字母\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int cnt = 0;\n"
              "        for (int i = 0; i < s.length(); ++i)\n"
              "            if (Character.isUpperCase(s.charAt(i))) ++cnt;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
