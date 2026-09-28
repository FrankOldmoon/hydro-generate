# -*- coding: utf-8 -*-
"""P1097 斐波那契数列第n项"""
from generate import make_problem


def build():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 15]

    def fib(n):
        if n <= 2:          # 前两项都是 1，递归出口
            return 1
        return fib(n - 1) + fib(n - 2)

    cases = [(f"{n}\n", f"{fib(n)}\n") for n in data]
    return make_problem(
        "P1097", "斐波那契数列第n项", ["入门", "递归"],
        cases=cases,
        desc_en="The Fibonacci sequence is defined as: F(1)=1, F(2)=1, and "
                "F(n)=F(n-1)+F(n-2) for n>2. Given n, print F(n).",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 30$ .",
        output_en="One line containing F(n).",
        desc_zh="斐波那契数列定义：F(1)=1，F(2)=1，n>2 时 F(n)=F(n-1)+F(n-2)。给定 "
                "n，求 F(n) 并输出。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 30$ 。",
        output_zh="一行，输出 F(n)。",
        py=("# P1097 斐波那契数列第n项（递归：fib(n)=fib(n-1)+fib(n-2)）\n"
            "def fib(n):                # 定义递归函数\n"
            "    if n <= 2:            # 递归出口：前两项为 1\n"
            "        return 1\n"
            "    return fib(n - 1) + fib(n - 2)\n"
            "\n"
            "n = int(input())           # 正整数 n\n"
            "print(fib(n))\n"),
        cpp=("// P1097 斐波那契数列第n项\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "long long fib(int n) {    // 递归求斐波那契\n"
             "    if (n <= 2) return 1; // 递归出口\n"
             "    return fib(n - 1) + fib(n - 2);\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    cout << fib(n) << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1097 斐波那契数列第n项\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static long fib(int n) {  // 递归求斐波那契\n"
              "        if (n <= 2) return 1; // 递归出口\n"
              "        return fib(n - 1) + fib(n - 2);\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        System.out.println(fib(n));\n"
              "    }\n"
              "}\n"),
    )
