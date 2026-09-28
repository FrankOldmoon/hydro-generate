# -*- coding: utf-8 -*-
"""P1047 字符串拼接"""
from generate import make_problem


def build():
    data = [
        ("abc", "def"), ("Hello", "World"), ("a", "b"), ("12", "34"),
        ("x", "yz"), ("Good", "Job"), ("A", "B"), ("foo", "bar"),
        ("2024", "year"), ("left", "right"),
    ]
    cases = [(f"{a}\n{b}\n", f"{a + b}\n") for a, b in data]
    return make_problem(
        "P1047", "字符串拼接", ["入门", "字符串"],
        cases=cases,
        desc_en="Given two strings s1 and s2 (one per line), print their "
                "concatenation s1+s2.",
        input_en="Two lines: each line contains one string (without spaces), "
                 "denoted s1, s2, satisfying $1\\leq |s1|,|s2|\\leq 100$ .",
        output_en="One line: the concatenation s1+s2.",
        desc_zh="给定两个字符串 s1 和 s2（每行一个），输出将它们拼接后的结果 s1+s2。",
        input_zh="两行：每行一个字符串（不含空格），依次为 s1、s2，满足 "
                 "$1\\leq |s1|,|s2|\\leq 100$ 。",
        output_zh="一行，输出 s1+s2 的拼接结果。",
        py=("# P1047 字符串拼接（+ 连接两个字符串）\n"
            "s1 = input()              # 第一个字符串\n"
            "s2 = input()              # 第二个字符串\n"
            "print(s1 + s2)            # + 拼接\n"),
        cpp=("// P1047 字符串拼接\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s1, s2;\n"
             "    cin >> s1 >> s2;            // 依次读入两个字符串（每行一个）\n"
             "    cout << s1 + s2 << endl;    // + 拼接\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1047 字符串拼接\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s1 = sc.next();     // 第一个字符串\n"
              "        String s2 = sc.next();     // 第二个字符串\n"
              "        System.out.println(s1 + s2); // + 拼接\n"
              "    }\n"
              "}\n"),
    )
