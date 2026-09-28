# -*- coding: utf-8 -*-
"""P1088 字符频次统计"""
from generate import make_problem


def build():
    data = [
        "hello", "aabbb", "abc", "aaaa", "zxy",
        "abab", "p", "mississippi", "aabbcc", "abcabc",
    ]

    cases = []
    for s in data:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        out = "".join(f"{ch} {d[ch]}\n" for ch in sorted(d.keys()))
        cases.append((f"{s}\n", out))
    return make_problem(
        "P1088", "字符频次统计", ["入门", "字典"],
        cases=cases,
        desc_en="Given a string, count the frequency of each character. Print "
                "each character and its count in ascending ASCII order.",
        input_en="One line containing a string s (without spaces), satisfying "
                 "$1\\leq |s|\\leq 1000$ .",
        output_en="Multiple lines: each line contains a character and its count, "
                  "separated by a space, in ascending ASCII order.",
        desc_zh="给定一个字符串，统计每个字符出现的次数，按字符 ASCII 升序输出。",
        input_zh="一行一个字符串 s（不含空格），满足 $1\\leq |s|\\leq 1000$ 。",
        output_zh="多行，每行一个字符和出现次数（空格分隔），按字符 ASCII 升序输出。",
        py=("# P1088 字符频次统计（dict 统计频次）\n"
            "s = input()                   # 字符串 s\n"
            "d = {}                        # 空字典\n"
            "for ch in s:\n"
            "    d[ch] = d.get(ch, 0) + 1  # 字符计数（get 取默认值 0）\n"
            "for ch in sorted(d.keys()):   # 按字符升序\n"
            "    print(ch, d[ch])\n"),
        cpp=("// P1088 字符频次统计\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <map>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    map<char, int> d;          // map 自动按 key 排序\n"
             "    for (char ch : s) d[ch]++;\n"
             "    for (auto &p : d)\n"
             "        cout << p.first << ' ' << p.second << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1088 字符频次统计\n"
              "import java.util.Scanner;\n"
              "import java.util.TreeMap;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        TreeMap<Character, Integer> d = new TreeMap<>();  // 自动排序\n"
              "        for (int i = 0; i < s.length(); ++i) {\n"
              "            char ch = s.charAt(i);\n"
              "            d.put(ch, d.getOrDefault(ch, 0) + 1);\n"
              "        }\n"
              "        for (char ch : d.keySet())\n"
              "            System.out.println(ch + \" \" + d.get(ch));\n"
              "    }\n"
              "}\n"),
    )
