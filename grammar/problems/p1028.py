# -*- coding: utf-8 -*-
"""P1028 求1到n的平方和"""
from generate import make_problem


def build():
    data = [1, 3, 5, 10, 2, 7, 100, 4, 6, 50]
    cases = [(f"{n}\n", f"{sum(i * i for i in range(1, n + 1))}\n") for n in data]
    return make_problem(
        "P1028", "求1到n的平方和", ["入门", "循环结构", "for"],
        cases=cases,
        desc_en="Given a positive integer n, print the sum of squares "
                "1*1 + 2*2 + ... + n*n.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000$ .",
        output_en="One line containing $\\sum_{i=1}^{n} i^2$.",
        desc_zh="给定一个正整数 n，输出 1²+2²+…+n² 的平方和。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000$ 。",
        output_zh="一行，输出 $\\sum_{i=1}^{n} i^2$ 的平方和。",
        py=("# P1028 求1到n的平方和（for 循环累加 i*i）\n"
            "n = int(input())            # 正整数 n\n"
            "s = 0                       # 累加和初始化为 0\n"
            "for i in range(1, n + 1):   # for 循环：i 从 1 到 n\n"
            "    s += i * i              # 累加 i 的平方\n"
            "print(s)                    # 输出平方和\n"),
        cpp=("// P1028 求1到n的平方和（for 循环）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入正整数 n\n"
             "    int s = 0;               // 累加和\n"
             "    for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
             "        s += i * i;          // 累加 i 的平方\n"
             "    cout << s << endl;       // 输出平方和\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1028 求1到n的平方和（for 循环）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 正整数 n\n"
              "        int s = 0;                   // 累加和\n"
              "        for (int i = 1; i <= n; ++i)  // for：i 从 1 到 n\n"
              "            s += i * i;              // 累加 i 的平方\n"
              "        System.out.println(s);      // 输出平方和\n"
              "    }\n"
              "}\n"),
    )
