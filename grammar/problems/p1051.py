# -*- coding: utf-8 -*-
"""P1051 统计元音字母"""
from generate import make_problem


def build():
    data = ["hello", "aeiou", "xyz", "apple", "banana",
            "queue", "sky", "beautiful", "aeon", "rhythm"]

    def cnt(s):
        return sum(1 for ch in s if ch in "aeiou")

    cases = [(f"{s}\n", f"{cnt(s)}\n") for s in data]
    return make_problem(
        "P1051", "统计元音字母", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s consisting of lowercase letters, print how many "
                "vowels (a, e, i, o, u) it contains.",
        input_en="One line containing a string s of lowercase letters, satisfying "
                 "$1\\leq |s|\\leq 100$ .",
        output_en="One line: the number of vowels in s.",
        desc_zh="给定一个由小写字母组成的字符串 s，输出其中元音字母（a、e、i、o、u）的个数。",
        input_zh="一行一个由小写字母组成的字符串 s，满足 $1\\leq |s|\\leq 100$ 。",
        output_zh="一行，输出元音字母的个数。",
        py=("# P1051 统计元音字母（遍历判断是否为 a/e/i/o/u）\n"
            "s = input()               # 字符串 s（小写字母）\n"
            "cnt = 0\n"
            "for ch in s:              # 遍历每个字符\n"
            "    if ch in 'aeiou':     # 是元音字母\n"
            "        cnt += 1\n"
            "print(cnt)\n"),
        cpp=("// P1051 统计元音字母\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    int cnt = 0;\n"
             "    for (char ch : s)               // 遍历每个字符\n"
             "        if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')\n"
             "            ++cnt;                  // 是元音字母\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1051 统计元音字母\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int cnt = 0;\n"
              "        for (int i = 0; i < s.length(); ++i) {\n"
              "            char ch = s.charAt(i);\n"
              "            if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')\n"
              "                ++cnt;\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
