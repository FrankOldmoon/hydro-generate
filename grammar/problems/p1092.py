# -*- coding: utf-8 -*-
"""P1092 括号匹配"""
from generate import make_problem


def build():
    data = ["()", "(())", "(()", ")(", "((()))", "()()", "(()())",
            "((()", ")", "((())"]

    def check(s):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    cases = [(f"{s}\n", f"{'Yes' if check(s) else 'No'}\n") for s in data]
    return make_problem(
        "P1092", "括号匹配", ["入门", "栈"],
        cases=cases,
        desc_en="Given a string consisting only of '(' and ')', determine whether "
                "the brackets are matched. Print \"Yes\" or \"No\".",
        input_en="One line containing a string of '(' and ')', satisfying "
                 "$1\\leq |s|\\leq 1000$ .",
        output_en="One line: \"Yes\" if matched, otherwise \"No\".",
        desc_zh="给定一个只由 '(' 和 ')' 组成的字符串，判断括号是否匹配。是输出 \"Yes\"，"
                "否则输出 \"No\"。",
        input_zh="一行一个由 '(' 和 ')' 组成的字符串，满足 $1\\leq |s|\\leq 1000$ 。",
        output_zh="一行，匹配输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1092 括号匹配（栈模拟）\n"
            "s = input()                   # 括号字符串\n"
            "stack = []                    # 用列表模拟栈\n"
            "ok = True\n"
            "for ch in s:\n"
            "    if ch == '(':\n"
            "        stack.append(ch)      # 左括号入栈\n"
            "    else:                     # 右括号\n"
            "        if not stack:         # 栈空则不匹配\n"
            "            ok = False\n"
            "            break\n"
            "        stack.pop()           # 匹配左括号出栈\n"
            "if ok and not stack:          # 全部匹配且栈空\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1092 括号匹配\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string s;\n"
             "    cin >> s;\n"
             "    vector<char> st;          // 用 vector 模拟栈\n"
             "    bool ok = true;\n"
             "    for (char ch : s) {\n"
             "        if (ch == '(') st.push_back(ch);\n"
             "        else {\n"
             "            if (st.empty()) { ok = false; break; }\n"
             "            st.pop_back();\n"
             "        }\n"
             "    }\n"
             "    cout << (ok && st.empty() ? \"Yes\" : \"No\") << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1092 括号匹配\n"
              "import java.util.Scanner;\n"
              "import java.util.ArrayDeque;\n"
              "import java.util.Deque;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String s = sc.next();\n"
              "        Deque<Character> st = new ArrayDeque<>();  // 栈\n"
              "        boolean ok = true;\n"
              "        for (int i = 0; i < s.length(); ++i) {\n"
              "            char ch = s.charAt(i);\n"
              "            if (ch == '(') st.push(ch);\n"
              "            else {\n"
              "                if (st.isEmpty()) { ok = false; break; }\n"
              "                st.pop();\n"
              "            }\n"
              "        }\n"
              "        System.out.println(ok && st.isEmpty() ? \"Yes\" : \"No\");\n"
              "    }\n"
              "}\n"),
    )
