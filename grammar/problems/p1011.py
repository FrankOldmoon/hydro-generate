# -*- coding: utf-8 -*-
"""P1011 等差数列计算"""
from generate import make_problem


def build():
    data = [
        (1, 1, 10), (2, 3, 5), (5, 0, 7), (1, 2, 100), (10, 5, 3),
        (0, 1, 5), (100, -1, 50), (3, 3, 3), (7, 4, 6), (1, 1, 1),
    ]
    cases = []
    for a1, d, n in data:
        an = a1 + (n - 1) * d
        sn = n * (a1 + an) // 2
        cases.append((f"{a1}\n{d}\n{n}\n", f"{an}\n{sn}\n"))
    return make_problem(
        "P1011", "等差数列计算", ["入门", "数学", "数列"],
        cases=cases,
        desc_en="Given the first term a1, the common difference d and the number "
                "of terms n of an arithmetic sequence, print the n-th term an and "
                "the sum of the first n terms Sn. The first line of output is "
                "an = a1 + (n-1)*d, the second line is Sn = n*(a1+an)/2.",
        input_en="Three lines: the first line contains integer a1 (first term), "
                 "the second line contains integer d (common difference), the "
                 "third line contains integer n (number of terms), satisfying "
                 "$-1000\\leq a1,d\\leq 1000$ and $1\\leq n\\leq 1000$ .",
        output_en="Two lines: the first line is the n-th term an, the second line "
                  "is the sum of the first n terms Sn.",
        desc_zh="给定等差数列的首项 a1、公差 d 和项数 n，输出第 n 项 an 和前 n 项之和 Sn。第一行输出 an = a1 + (n-1)*d，第二行输出 Sn = n*(a1+an)/2。",
        input_zh="三行：第一行一个整数 a1（首项），第二行一个整数 d（公差），第三行一个整数 n（项数），满足 $-1000\\leq a1,d\\leq 1000$ 且 $1\\leq n\\leq 1000$ 。",
        output_zh="两行：第一行为第 n 项 an，第二行为前 n 项之和 Sn。",
        py=("# P1011 等差数列计算\n"
            "# 每行一个整数，依次读入首项 a1、公差 d、项数 n，输出第 n 项与前 n 项和\n"
            "a1 = int(input())   # 首项 a1\n"
            "d = int(input())    # 公差 d\n"
            "n = int(input())    # 项数 n\n"
            "an = a1 + (n - 1) * d          # 第 n 项\n"
            "sn = n * (a1 + an) // 2        # 前 n 项和（整除保证整数）\n"
            "print(an)                      # 第一行：第 n 项\n"
            "print(sn)                      # 第二行：前 n 项和\n"),
        cpp=("// P1011 等差数列计算\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    long long a1, d, n;\n"
             "    cin >> a1 >> d >> n;          // 依次读入 a1、d、n（每行一个）\n"
             "    long long an = a1 + (n - 1) * d;   // 第 n 项\n"
             "    long long sn = n * (a1 + an) / 2;  // 前 n 项和\n"
             "    cout << an << endl;          // 第一行：第 n 项\n"
             "    cout << sn << endl;          // 第二行：前 n 项和\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1011 等差数列计算\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        long a1 = sc.nextLong();   // 首项 a1\n"
              "        long d = sc.nextLong();    // 公差 d\n"
              "        long n = sc.nextLong();    // 项数 n\n"
              "        long an = a1 + (n - 1) * d;     // 第 n 项\n"
              "        long sn = n * (a1 + an) / 2;    // 前 n 项和\n"
              "        System.out.println(an);   // 第一行：第 n 项\n"
              "        System.out.println(sn);   // 第二行：前 n 项和\n"
              "    }\n"
              "}\n"),
    )
