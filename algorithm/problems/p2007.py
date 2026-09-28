# -*- coding: utf-8 -*-
"""P2007 阶乘末尾零"""
from generate import make_problem


def build():
    ns = [5, 10, 0, 1, 7, 20, 25, 50, 100, 1000]

    def solve(n):
        # n! 末尾 0 的个数 = floor(n/5)+floor(n/25)+...
        cnt = 0
        p = 5
        while p <= n:
            cnt += n // p
            p *= 5
        return cnt

    cases = [(f"{n}\n", f"{solve(n)}\n") for n in ns]
    return make_problem(
        "P2007", "阶乘末尾零", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a non-negative integer n, compute the number of trailing "
                "zeros in n! (n factorial).",
        input_en="One line containing a non-negative integer n, satisfying "
                 "$0\\leq n\\leq 100000$ .",
        output_en="One line: the number of trailing zeros in n!.",
        desc_zh="给定非负整数 n，求 n! 末尾有多少个 0。",
        input_zh="一行一个非负整数 n，满足 $0\\leq n\\leq 100000$ 。",
        output_zh="一行，n! 末尾 0 的个数。",
        py=("# P2007 阶乘末尾零\n"
            "# 末尾 0 的个数 = sum(floor(n/5^k))，统计 5 的因子个数\n"
            "n = int(input())                  # 非负整数 n\n"
            "cnt = 0\n"
            "p = 5\n"
            "while p <= n:                     # 累加 n//5, n//25, ...\n"
            "    cnt += n // p\n"
            "    p *= 5\n"
            "print(cnt)\n"),
        cpp=("// P2007 阶乘末尾零\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                     // 非负整数 n\n"
             "    int cnt = 0;\n"
             "    for (long long p = 5; p <= n; p *= 5) // 累加 n/5, n/25, ...\n"
             "        cnt += n / p;\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2007 阶乘末尾零\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 非负整数 n\n"
              "        int cnt = 0;\n"
              "        for (long p = 5; p <= n; p *= 5) // 累加 n/5, n/25, ...\n"
              "            cnt += n / p;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
