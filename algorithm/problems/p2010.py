# -*- coding: utf-8 -*-
"""P2010 简单表达式求值"""
from generate import make_problem, fmt2


def build():
    # (a, op, b)
    data = [
        (10, "+", 20), (50, "-", 18), (6, "*", 7), (10, "/", 4),
        (100, "+", 5), (7, "-", 10), (12, "*", 12), (22, "/", 7),
        (1, "/", 3), (8, "/", 5),
    ]

    def solve(a, op, b):
        if op == "+":
            return f"{a + b}"
        elif op == "-":
            return f"{a - b}"
        elif op == "*":
            return f"{a * b}"
        else:  # 除法保留两位小数
            return fmt2(a / b)

    cases = [(f"{a}\n{op}\n{b}\n", f"{solve(a, op, b)}\n") for a, op, b in data]
    return make_problem(
        "P2010", "简单表达式求值", ["算法", "模拟"],
        cases=cases,
        desc_en="Given two integers a, b and an operator op (one of +, -, *, /), "
                "output the value of a op b. For division, output the result "
                "rounded to two decimal places.",
        input_en="Three lines: the first line is integer a, the second line is "
                 "the operator op (+, -, *, /), the third line is integer b. "
                 "$-10000\\leq a,b\\leq 10000$ . For division, b is non-zero.",
        output_en="One line: the result. For +, -, * it is an integer; for / it "
                  "is rounded to two decimal places.",
        desc_zh="给定两个整数 a、b 和运算符 op（+、-、*、/ 之一），输出 a op b 的结果，"
                "其中除法结果保留两位小数。",
        input_zh="三行：第一行整数 a，第二行运算符 op（+、-、*、/ 之一），第三行整数 b。"
                 "$-10000\\leq a,b\\leq 10000$ ，除法时 b 非零。",
        output_zh="一行，运算结果（+、-、* 为整数，/ 保留两位小数）。",
        py=("# P2010 简单表达式求值\n"
            "# 读入 a、运算符 op、b，按 op 计算，除法保留两位小数\n"
            "a = int(input())                  # 整数 a\n"
            "op = input().strip()              # 运算符 op\n"
            "b = int(input())                  # 整数 b\n"
            "if op == '+':\n"
            "    print(a + b)\n"
            "elif op == '-':\n"
            "    print(a - b)\n"
            "elif op == '*':\n"
            "    print(a * b)\n"
            "else:                             # 除法保留两位小数\n"
            "    print('%.2f' % (a / b))\n"),
        cpp=("// P2010 简单表达式求值\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b;\n"
             "    string op;\n"
             "    cin >> a >> op >> b;          // 整数 a、运算符 op、整数 b\n"
             "    if (op == \"+\") cout << a + b << endl;\n"
             "    else if (op == \"-\") cout << a - b << endl;\n"
             "    else if (op == \"*\") cout << a * b << endl;\n"
             "    else printf(\"%.2f\\n\", 1.0 * a / b); // 除法保留两位小数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2010 简单表达式求值\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();       // 整数 a\n"
              "        String op = sc.next();      // 运算符 op\n"
              "        int b = sc.nextInt();       // 整数 b\n"
              "        switch (op) {\n"
              "            case \"+\": System.out.println(a + b); break;\n"
              "            case \"-\": System.out.println(a - b); break;\n"
              "            case \"*\": System.out.println(a * b); break;\n"
              "            default: System.out.printf(\"%.2f%n\", 1.0 * a / b); // 除法\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
