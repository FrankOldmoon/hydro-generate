# -*- coding: utf-8 -*-
"""P2039 删数字最大"""
from generate import make_problem


def build():
    # (数字字符串, 删除个数 k)
    data = [
        ("1432219", 3),
        ("12345", 2),
        ("54321", 2),
        ("10200", 1),
        ("987654321", 4),
        ("10", 1),
        ("43210", 2),
        ("100", 1),
        ("321", 1),
        ("11111", 2),
    ]
    cases = []
    for s, k in data:
        inp = f"{s}\n{k}\n"
        # 贪心：单调递减栈，能弹则弹；剩余 k 从末尾删
        stack = []
        rem = k
        for ch in s:
            while rem > 0 and stack and stack[-1] < ch:
                stack.pop()
                rem -= 1
            stack.append(ch)
        while rem > 0:          # 还没删够，从末尾删
            stack.pop()
            rem -= 1
        out = "".join(stack) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2039", "删数字最大", ["算法", "贪心"],
        cases=cases,
        desc_en="Given a non-negative integer represented as a digit string and an "
                "integer k, delete exactly k digits so that the remaining number is "
                "as large as possible. Output the remaining number (keeping the "
                "original digit order).",
        input_en="The first line contains a digit string s. The second line contains "
                 "an integer k.",
        output_en="One line containing the largest number after deleting exactly k "
                  "digits.",
        desc_zh="给定一个用数字字符串表示的非负整数和一个整数 k，删掉其中 k 个数字使剩余数字最大，输出剩余数字（保持原顺序）。",
        input_zh="第一行一个数字字符串 s。第二行一个整数 k。",
        output_zh="一行一个数字字符串，表示删除 k 个数字后能得到的最大数字。",
        py=("# P2039 删数字最大（贪心：单调递减栈，能弹则弹）\n"
            "s = input().strip()\n"
            "k = int(input())\n"
            "stack = []\n"
            "for ch in s:\n"
            "    while k > 0 and stack and stack[-1] < ch:  # 栈顶比当前小则弹出\n"
            "        stack.pop()\n"
            "        k -= 1\n"
            "    stack.append(ch)\n"
            "while k > 0:            # 还没删够，从末尾删\n"
            "    stack.pop()\n"
            "    k -= 1\n"
            "print(''.join(stack))\n"),
        cpp=("// P2039 删数字最大（贪心：单调递减栈）\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s; cin >> s;\n"
             "    int k; cin >> k;\n"
             "    string stack;\n"
             "    for (char ch : s) {\n"
             "        while (k > 0 && !stack.empty() && stack.back() < ch) {  // 栈顶小则弹\n"
             "            stack.pop_back();\n"
             "            --k;\n"
             "        }\n"
             "        stack.push_back(ch);\n"
             "    }\n"
             "    while (k > 0) {        // 还没删够，从末尾删\n"
             "        stack.pop_back();\n"
             "        --k;\n"
             "    }\n"
             "    cout << stack << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2039 删数字最大（贪心：单调递减栈）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        int k = sc.nextInt();\n"
              "        StringBuilder stack = new StringBuilder();\n"
              "        for (int i = 0; i < s.length(); ++i) {\n"
              "            char ch = s.charAt(i);\n"
              "            while (k > 0 && stack.length() > 0 && stack.charAt(stack.length()-1) < ch) {  // 栈顶小则弹\n"
              "                stack.deleteCharAt(stack.length()-1);\n"
              "                --k;\n"
              "            }\n"
              "            stack.append(ch);\n"
              "        }\n"
              "        while (k > 0) {        // 还没删够，从末尾删\n"
              "            stack.deleteCharAt(stack.length()-1);\n"
              "            --k;\n"
              "        }\n"
              "        System.out.println(stack.toString());\n"
              "    }\n"
              "}\n"),
    )
