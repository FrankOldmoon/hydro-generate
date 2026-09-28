# -*- coding: utf-8 -*-
"""P1035 n能被k整除几次"""


def _count(n, k):
    c = 0
    while n % k == 0:
        c += 1
        n //= k
    return c


from generate import make_problem


def build():
    data = [
        (24, 2), (12, 2), (100, 2), (100, 5), (7, 2),
        (81, 3), (1, 2), (32, 2), (1000, 10), (18, 3),
    ]
    cases = [(f"{n}\n{k}\n", f"{_count(n, k)}\n") for n, k in data]
    return make_problem(
        "P1035", "n能被k整除几次", ["入门", "循环结构", "while"],
        cases=cases,
        desc_en="Given two positive integers n and k (k >= 2, one per line), print "
                "the largest exponent e such that k^e divides n (i.e. how many "
                "times n can be divided by k with no remainder).",
        input_en="Two lines: each line contains one positive integer. Denote them "
                 "n, k from top to bottom, satisfying $1\\leq n\\leq 1000000000$ "
                 "and $2\\leq k\\leq 1000$ .",
        output_en="One line containing the largest e with $k^e \\mid n$.",
        desc_zh="给定两个正整数 n 和 k（k≥2，每行一个），输出能整除 n 的 k 的最高幂次，"
                "即 n 最多能被 k 整除多少次。",
        input_zh="两行：每行一个正整数，从上到下依次为 n、k，满足 $1\\leq n\\leq 1000000000$ "
                 "且 $2\\leq k\\leq 1000$ 。",
        output_zh="一行，输出最大的 e 使得 $k^e\\mid n$。",
        py=("# P1035 n能被k整除几次（while：能整除就除一次并计数）\n"
            "n = int(input())            # 第一行：n\n"
            "k = int(input())            # 第二行：k\n"
            "c = 0                       # 整除次数\n"
            "while n % k == 0:           # while：n 仍能被 k 整除\n"
            "    c += 1                  # 次数加 1\n"
            "    n //= k                 # n 除以 k\n"
            "print(c)                    # 输出次数\n"),
        cpp=("// P1035 n能被k整除几次（while）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, k;\n"
             "    cin >> n >> k;          // 依次读入 n、k（每行一个）\n"
             "    int c = 0;              // 整除次数\n"
             "    while (n % k == 0) {    // while：n 仍能被 k 整除\n"
             "        ++c;                // 次数加 1\n"
             "        n /= k;             // n 除以 k\n"
             "    }\n"
             "    cout << c << endl;      // 输出次数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1035 n能被k整除几次（while）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 第一行：n\n"
              "        int k = sc.nextInt();   // 第二行：k\n"
              "        int c = 0;              // 整除次数\n"
              "        while (n % k == 0) {    // while：n 仍能被 k 整除\n"
              "            ++c;                // 次数加 1\n"
              "            n /= k;             // n 除以 k\n"
              "        }\n"
              "        System.out.println(c); // 输出次数\n"
              "    }\n"
              "}\n"),
    )
