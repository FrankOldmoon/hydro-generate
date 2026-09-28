# -*- coding: utf-8 -*-
"""P1029 求n个数的和"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [10, 20, 30, 40, 50]),
        (1, [100]),
        (4, [-1, 2, -3, 4]),
        (2, [0, 0]),
        (6, [1, 1, 1, 1, 1, 1]),
        (3, [100, 200, 300]),
        (1, [-50]),
        (5, [5, 5, 5, 5, 5]),
        (2, [32767, -32767]),
    ]
    cases = [(f"{n}\n" + "".join(f"{x}\n" for x in arr), f"{sum(arr)}\n")
             for n, arr in data]
    return make_problem(
        "P1029", "求n个数的和", ["入门", "循环结构", "for"],
        cases=cases,
        desc_en="Given an integer n followed by n integers (one per line), print "
                "their sum.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line containing the sum of the n integers.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），输出这 n 个整数的和。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，输出这 n 个整数的和。",
        py=("# P1029 求n个数的和（for 循环读入并累加）\n"
            "n = int(input())            # 个数 n\n"
            "s = 0                       # 累加和\n"
            "for i in range(n):          # for 循环：读 n 个数\n"
            "    x = int(input())        # 每行一个整数\n"
            "    s += x                  # 累加\n"
            "print(s)                    # 输出和\n"),
        cpp=("// P1029 求n个数的和（for 循环）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入个数 n\n"
             "    int s = 0;               // 累加和\n"
             "    for (int i = 0; i < n; ++i) {  // for：读 n 个数\n"
             "        int x;\n"
             "        cin >> x;            // 每行一个整数\n"
             "        s += x;              // 累加\n"
             "    }\n"
             "    cout << s << endl;       // 输出和\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1029 求n个数的和（for 循环）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();        // 个数 n\n"
              "        int s = 0;                   // 累加和\n"
              "        for (int i = 0; i < n; ++i) {  // for：读 n 个数\n"
              "            int x = sc.nextInt();    // 每行一个整数\n"
              "            s += x;                  // 累加\n"
              "        }\n"
              "        System.out.println(s);      // 输出和\n"
              "    }\n"
              "}\n"),
    )
