# -*- coding: utf-8 -*-
"""P2002 约瑟夫问题"""
from generate import make_problem


def build():
    data = [
        (5, 2), (7, 3), (5, 3), (6, 5), (1, 1),
        (2, 1), (4, 2), (8, 4), (10, 2), (12, 3),
    ]

    def solve(n, m):
        # 约瑟夫递推：f(1)=0(0-based)，f(i)=(f(i-1)+m)%i，答案 f(n)+1
        f = 0
        for i in range(2, n + 1):
            f = (f + m) % i
        return f + 1

    cases = [(f"{n}\n{m}\n", f"{solve(n, m)}\n") for n, m in data]
    return make_problem(
        "P2002", "约瑟夫问题", ["算法", "模拟"],
        cases=cases,
        desc_en="n people numbered 1..n sit in a circle. Starting from person 1, "
                "count off 1,2,...,m repeatedly; the person who says m leaves the "
                "circle. Find the number of the last remaining person (1-based).",
        input_en="Two lines: the first line is a positive integer n, the second "
                 "line is a positive integer m, satisfying $1\\leq n\\leq 1000$ and "
                 "$1\\leq m\\leq 1000$ .",
        output_en="One line: the number of the last remaining person (1-based).",
        desc_zh="n 个人编号 1..n 围成一圈，从 1 号开始依次报数 1,2,…,m，报到 m 的人出列，"
                "求最后剩下的人的编号（1-based）。",
        input_zh="两行：第一行一个正整数 n，第二行一个正整数 m，满足 $1\\leq n\\leq 1000$ 且 "
                 "$1\\leq m\\leq 1000$ 。",
        output_zh="一行，最后剩下的人的编号（1-based）。",
        py=("# P2002 约瑟夫问题（递推法）\n"
            "# f(1)=0（0-based），f(i)=(f(i-1)+m)%i，最终答案为 f(n)+1\n"
            "n = int(input())                 # 人数 n\n"
            "m = int(input())                 # 报数到 m 出列\n"
            "f = 0                            # 1 人时的幸存者下标\n"
            "for i in range(2, n + 1):        # 递推到 n 人\n"
            "    f = (f + m) % i\n"
            "print(f + 1)                     # 转 1-based 输出\n"),
        cpp=("// P2002 约瑟夫问题（递推法）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;               // 人数 n，报数 m\n"
             "    int f = 0;                   // 1 人时的幸存者下标（0-based）\n"
             "    for (int i = 2; i <= n; ++i) // 递推到 n 人\n"
             "        f = (f + m) % i;\n"
             "    cout << f + 1 << endl;       // 转 1-based 输出\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2002 约瑟夫问题（递推法）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();         // 人数 n\n"
              "        int m = sc.nextInt();         // 报数 m\n"
              "        int f = 0;                    // 1 人时的幸存者下标（0-based）\n"
              "        for (int i = 2; i <= n; ++i)  // 递推到 n 人\n"
              "            f = (f + m) % i;\n"
              "        System.out.println(f + 1);   // 转 1-based 输出\n"
              "    }\n"
              "}\n"),
    )
