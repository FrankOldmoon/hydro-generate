# -*- coding: utf-8 -*-
"""P1030 求n个数的最大值"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [10, 20, 30, 40, 50]),
        (1, [100]),
        (4, [-1, 2, -3, 4]),
        (3, [5, 5, 5]),
        (2, [-10, -20]),
        (6, [1, 7, 3, 9, 2, 8]),
        (4, [32767, -32768, 0, 1]),
        (5, [100, 200, 150, 50, 250]),
        (1, [-5]),
    ]
    cases = [(f"{n}\n" + "".join(f"{x}\n" for x in arr), f"{max(arr)}\n")
             for n, arr in data]
    return make_problem(
        "P1030", "求n个数的最大值", ["入门", "循环结构", "for"],
        cases=cases,
        desc_en="Given an integer n followed by n integers (one per line), print "
                "the maximum among them.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line containing the maximum of the n integers.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），输出这 n 个整数中的最大值。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，输出这 n 个整数中的最大值。",
        py=("# P1030 求n个数的最大值（for 循环打擂台）\n"
            "n = int(input())            # 个数 n\n"
            "m = int(input())            # 先读第一个数作为当前最大值\n"
            "for i in range(1, n):       # for 循环：再读 n-1 个数\n"
            "    x = int(input())        # 每行一个整数\n"
            "    if x > m:               # 比当前最大值还大则更新\n"
            "        m = x\n"
            "print(m)                    # 输出最大值\n"),
        cpp=("// P1030 求n个数的最大值（for 循环）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入个数 n\n"
             "    int m;\n"
             "    cin >> m;                // 先读第一个数作为当前最大值\n"
             "    for (int i = 1; i < n; ++i) {  // for：再读 n-1 个数\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        if (x > m)          // 比当前最大值还大则更新\n"
             "            m = x;\n"
             "    }\n"
             "    cout << m << endl;       // 输出最大值\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1030 求n个数的最大值（for 循环）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 个数 n\n"
              "        int m = sc.nextInt();        // 先读第一个数作为当前最大值\n"
              "        for (int i = 1; i < n; ++i) {  // for：再读 n-1 个数\n"
              "            int x = sc.nextInt();\n"
              "            if (x > m)              // 比当前最大值还大则更新\n"
              "                m = x;\n"
              "        }\n"
              "        System.out.println(m);      // 输出最大值\n"
              "    }\n"
              "}\n"),
    )
