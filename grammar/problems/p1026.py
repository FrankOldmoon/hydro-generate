# -*- coding: utf-8 -*-
"""P1026 求1到n的和"""
from generate import make_problem


def build():
    data = [1, 10, 100, 5, 50, 1000, 7, 32767, 2, 999]
    cases = [(f"{n}\n", f"{sum(range(1, n + 1))}\n") for n in data]
    return make_problem(
        "P1026", "求1到n的和", ["入门", "循环结构", "for"],
        cases=cases,
        desc_en="Given a positive integer n, print the sum 1+2+...+n.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 32767$ .",
        output_en="One line containing the sum $\\sum_{i=1}^{n} i$.",
        desc_zh="给定一个正整数 n，输出 1+2+...+n 的和。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 32767$ 。",
        output_zh="一行，输出 $\\sum_{i=1}^{n} i$ 的和。",
        py=("# P1026 求1到n的和（for 循环累加）\n"
            "n = int(input())            # 正整数 n\n"
            "s = 0                       # 累加和初始化为 0\n"
            "for i in range(1, n + 1):   # for 循环：i 从 1 到 n\n"
            "    s += i                  # 逐项累加\n"
            "print(s)                    # 输出和\n"),
        cpp=("// P1026 求1到n的和（for 循环）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入正整数 n\n"
             "    int s = 0;               // 累加和\n"
             "    for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
             "        s += i;\n"
             "    cout << s << endl;       // 输出和\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1026 求1到n的和（for 循环）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 正整数 n\n"
              "        int s = 0;                   // 累加和\n"
              "        for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
              "            s += i;\n"
              "        System.out.println(s);      // 输出和\n"
              "    }\n"
              "}\n"),
    )
