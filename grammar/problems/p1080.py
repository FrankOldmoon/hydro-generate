# -*- coding: utf-8 -*-
"""P1080 因子个数统计"""
from generate import make_problem


def build():
    data = [
        (5, [6, 12, 1, 7, 28]),
        (1, [1]),
        (3, [2, 3, 4]),
        (1, [100]),
        (4, [10, 16, 25, 36]),
        (2, [13, 17]),
        (1, [60]),
        (3, [8, 9, 10]),
        (2, [1000, 999]),
        (1, [48]),
    ]

    def count_factors(x):
        cnt = 0
        i = 1
        while i <= x:
            if x % i == 0:
                cnt += 1
            i += 1
        return cnt

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{count_factors(x)}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1080", "因子个数统计", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n positive integers, print the number of positive "
                "divisors of each (including 1 and itself).",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a positive integer, satisfying "
                 "$1\\leq x\\leq 10000$ .",
        output_en="n lines: the divisor count of each number.",
        desc_zh="给定 n 及 n 个正整数，输出每个数的因子个数（含 1 和自身）。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个正整数，满足 "
                 "$1\\leq x\\leq 10000$ 。",
        output_zh="n 行，每行输出对应数的因子个数。",
        py=("# P1080 因子个数统计（自定义函数统计因子）\n"
            "def count_factors(x):     # 定义统计因子个数的函数\n"
            "    cnt = 0\n"
            "    i = 1\n"
            "    while i <= x:         # 遍历 1 到 x\n"
            "        if x % i == 0:    # 能整除则是因子\n"
            "            cnt += 1\n"
            "        i += 1\n"
            "    return cnt\n"
            "\n"
            "n = int(input())           # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    print(count_factors(x))\n"),
        cpp=("// P1080 因子个数统计\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int count_factors(int x) {  // 统计因子个数\n"
             "    int cnt = 0;\n"
             "    for (int i = 1; i <= x; ++i)\n"
             "        if (x % i == 0) ++cnt;\n"
             "    return cnt;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << count_factors(x) << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1080 因子个数统计\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static int countFactors(int x) {  // 统计因子个数\n"
              "        int cnt = 0;\n"
              "        for (int i = 1; i <= x; ++i)\n"
              "            if (x % i == 0) ++cnt;\n"
              "        return cnt;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(countFactors(x));\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
