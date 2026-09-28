# -*- coding: utf-8 -*-
"""P2008 k进制转换"""
from generate import make_problem


def build():
    data = [
        (10, 2), (255, 16), (0, 2), (100, 8), (16, 16),
        (15, 16), (1000, 16), (255, 2), (255, 10), (7, 3),
    ]
    DIGITS = "0123456789ABCDEF"

    def solve(n, k):
        if n == 0:
            return "0"
        res = ""
        while n > 0:
            res = DIGITS[n % k] + res
            n //= k
        return res

    cases = [(f"{n}\n{k}\n", f"{solve(n, k)}\n") for n, k in data]
    return make_problem(
        "P2008", "k进制转换", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a non-negative decimal integer n and a base k (2 to 16), "
                "output the representation of n in base k. Digits 10 to 15 are "
                "represented by uppercase A to F.",
        input_en="Two lines: the first line is a non-negative integer n, the "
                 "second line is the base k, satisfying $0\\leq n\\leq 10^{18}$ and "
                 "$2\\leq k\\leq 16$ .",
        output_en="One line: the base-k representation of n (no leading zeros; 0 "
                  "is output as a single 0).",
        desc_zh="给定非负十进制整数 n 和进制 k（2 到 16），输出 n 的 k 进制表示，"
                "其中 10 到 15 用大写字母 A 到 F 表示。",
        input_zh="两行：第一行一个非负整数 n，第二行一个进制 k，满足 $0\\leq n\\leq 10^{18}$ "
                 "且 $2\\leq k\\leq 16$ 。",
        output_zh="一行，n 的 k 进制表示（无前导零，0 输出为 0）。",
        py=("# P2008 k进制转换\n"
            "# 除 k 取余，逆序拼接，10-15 用 A-F\n"
            "n = int(input())                  # 十进制非负整数 n\n"
            "k = int(input())                  # 目标进制 k\n"
            "d = '0123456789ABCDEF'\n"
            "if n == 0:\n"
            "    print(0)                      # 0 的任意进制都是 0\n"
            "else:\n"
            "    s = ''\n"
            "    while n > 0:                  # 除 k 取余\n"
            "        s = d[n % k] + s\n"
            "        n //= k\n"
            "    print(s)\n"),
        cpp=("// P2008 k进制转换\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    long long n;\n"
             "    int k;\n"
             "    cin >> n >> k;               // 十进制 n，目标进制 k\n"
             "    string d = \"0123456789ABCDEF\";\n"
             "    if (n == 0) { cout << 0 << endl; return 0; } // 0 特判\n"
             "    string s;\n"
             "    while (n > 0) {              // 除 k 取余，逆序拼接\n"
             "        s = d[n % k] + s;\n"
             "        n /= k;\n"
             "    }\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2008 k进制转换\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        long n = sc.nextLong();      // 十进制 n\n"
              "        int k = sc.nextInt();        // 目标进制 k\n"
              "        String d = \"0123456789ABCDEF\";\n"
              "        if (n == 0) { System.out.println(0); return; } // 0 特判\n"
              "        StringBuilder s = new StringBuilder();\n"
              "        while (n > 0) {              // 除 k 取余，逆序拼接\n"
              "            s.insert(0, d.charAt((int)(n % k)));\n"
              "            n /= k;\n"
              "        }\n"
              "        System.out.println(s);\n"
              "    }\n"
              "}\n"),
    )
