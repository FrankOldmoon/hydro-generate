# -*- coding: utf-8 -*-
"""P1078 组合数计算"""
from generate import make_problem


def build():
    data = [
        (5, 2), (1, 0), (1, 1), (10, 3), (6, 3),
        (7, 7), (8, 0), (5, 3), (12, 5), (10, 5),
    ]

    def fact(k):
        r = 1
        for i in range(1, k + 1):
            r *= i
        return r

    cases = []
    for n, m in data:
        inp = f"{n}\n{m}\n"
        c = fact(n) // (fact(m) * fact(n - m))
        cases.append((inp, f"{c}\n"))
    return make_problem(
        "P1078", "组合数计算", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and m, compute the combination number C(n,m) = "
                "n! / (m! * (n-m)!).",
        input_en="Two lines: the first line contains n, the second line contains "
                 "m, satisfying $0\\leq m\\leq n\\leq 12$ .",
        output_en="One line: the value of C(n,m).",
        desc_zh="给定 n 和 m，计算组合数 C(n,m) = n! / (m! * (n-m)!)。",
        input_zh="两行：第一行一个非负整数 n，第二行一个非负整数 m，满足 $0\\leq m\\leq n\\leq 12$ 。",
        output_zh="一行，输出 C(n,m) 的值。",
        py=("# P1078 组合数计算（自定义阶乘函数）\n"
            "def fact(k):                  # 定义阶乘函数\n"
            "    r = 1\n"
            "    for i in range(1, k + 1):\n"
            "        r *= i\n"
            "    return r\n"
            "\n"
            "n = int(input())              # n\n"
            "m = int(input())              # m\n"
            "c = fact(n) // (fact(m) * fact(n - m))  # 组合数公式\n"
            "print(c)\n"),
        cpp=("// P1078 组合数计算\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int fact(int k) {             // 阶乘函数\n"
             "    int r = 1;\n"
             "    for (int i = 1; i <= k; ++i) r *= i;\n"
             "    return r;\n"
             "}\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    cout << fact(n) / (fact(m) * fact(n - m)) << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1078 组合数计算\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static int fact(int k) {  // 阶乘函数\n"
              "        int r = 1;\n"
              "        for (int i = 1; i <= k; ++i) r *= i;\n"
              "        return r;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        System.out.println(fact(n) / (fact(m) * fact(n - m)));\n"
              "    }\n"
              "}\n"),
    )
