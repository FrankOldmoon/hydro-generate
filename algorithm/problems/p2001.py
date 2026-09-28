# -*- coding: utf-8 -*-
"""P2001 逢三跳过"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 5, 6, 10, 15, 20, 30, 100]

    def solve(n):
        # 从 1 数到 n，跳过 3 的倍数，其余每行一个输出
        return "".join(f"{i}\n" for i in range(1, n + 1) if i % 3 != 0)

    cases = [(f"{n}\n", solve(n)) for n in ns]
    return make_problem(
        "P2001", "逢三跳过", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, list the numbers from 1 to n in ascending "
                "order, skipping multiples of 3. Print one number per line.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000$ .",
        output_en="Several lines: the numbers from 1 to n that are not multiples "
                  "of 3, one per line in ascending order.",
        desc_zh="给定正整数 n，从 1 数到 n，跳过 3 的倍数，其余数按升序每行一个输出。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000$ 。",
        output_zh="若干行，按升序每行输出一个不是 3 的倍数的数。",
        py=("# P2001 逢三跳过\n"
            "# 读入 n，从 1 到 n，跳过 3 的倍数，其余每行输出\n"
            "n = int(input())                 # 读入上界 n\n"
            "for i in range(1, n + 1):        # 遍历 1..n\n"
            "    if i % 3 != 0:               # 不是 3 的倍数才输出\n"
            "        print(i)                 # 每行一个\n"),
        cpp=("// P2001 逢三跳过\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                    // 读入上界 n\n"
             "    for (int i = 1; i <= n; ++i) // 遍历 1..n\n"
             "        if (i % 3 != 0)          // 不是 3 的倍数才输出\n"
             "            cout << i << endl;   // 每行一个\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2001 逢三跳过\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 读入上界 n\n"
              "        for (int i = 1; i <= n; ++i) {  // 遍历 1..n\n"
              "            if (i % 3 != 0)             // 不是 3 的倍数才输出\n"
              "                System.out.println(i); // 每行一个\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
