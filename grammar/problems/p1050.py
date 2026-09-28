# -*- coding: utf-8 -*-
"""P1050 第k个字符"""
from generate import make_problem


def build():
    data = [
        ("hello", 1), ("hello", 3), ("abc", 2), ("xyz", 3), ("world", 5),
        ("abc", 1), ("test", 4), ("python", 2), ("Hello", 1), ("a", 1),
    ]
    cases = [(f"{s}\n{k}\n", f"{s[k - 1]}\n") for s, k in data]
    return make_problem(
        "P1050", "第k个字符", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a string s and a positive integer k (one per line), print "
                "the k-th character of s (1-based).",
        input_en="Two lines: the first line contains a string s (without spaces), "
                 "the second line contains a positive integer k, satisfying "
                 "$1\\leq |s|\\leq 100$ and $1\\leq k\\leq |s|$ .",
        output_en="One line: the k-th character of s.",
        desc_zh="给定一个字符串 s 和一个正整数 k，输出 s 的第 k 个字符（k 从 1 开始）。",
        input_zh="两行：第一行一个字符串 s（不含空格），第二行一个正整数 k，满足 "
                 "$1\\leq |s|\\leq 100$ 且 $1\\leq k\\leq |s|$ 。",
        output_zh="一行，输出 s 的第 k 个字符。",
        py=("# P1050 第k个字符（下标访问）\n"
            "s = input()               # 字符串 s\n"
            "k = int(input())          # 位置 k（从 1 开始）\n"
            "print(s[k - 1])           # 转为 0 开始下标\n"),
        cpp=("// P1050 第k个字符\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    int k;\n"
             "    cin >> s >> k;\n"
             "    cout << s[k - 1] << endl;   // 转为 0 开始下标\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1050 第k个字符\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int k = sc.nextInt();\n"
              "        System.out.println(s.charAt(k - 1));  // 转为 0 开始下标\n"
              "    }\n"
              "}\n"),
    )
