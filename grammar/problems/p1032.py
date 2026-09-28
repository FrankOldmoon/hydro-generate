# -*- coding: utf-8 -*-
"""P1032 Collatz步数"""


def _steps(n):
    s = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        s += 1
    return s


from generate import make_problem


def build():
    data = [1, 2, 3, 6, 7, 27, 16, 5, 10, 100]
    cases = [(f"{n}\n", f"{_steps(n)}\n") for n in data]
    return make_problem(
        "P1032", "Collatz步数", ["入门", "循环结构", "while"],
        cases=cases,
        desc_en="Given a positive integer n, repeatedly apply the rule: if n is "
                "even, set n = n/2; otherwise set n = 3*n+1. Print how many steps "
                "are needed to reach 1 (n=1 needs 0 steps).",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000$ .",
        output_en="One line containing the number of steps to reach 1.",
        desc_zh="给定一个正整数 n，反复执行规则：n 为偶数则 n=n/2，n 为奇数则 n=3*n+1。"
                "输出到达 1 所需的步数（n=1 时为 0 步）。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000$ 。",
        output_zh="一行，输出到达 1 所需的步数。",
        py=("# P1032 Collatz步数（while：直到 n 变为 1）\n"
            "n = int(input())            # 正整数 n\n"
            "s = 0                       # 步数计数\n"
            "while n != 1:               # while：n 不为 1 就继续\n"
            "    if n % 2 == 0:          # 偶数\n"
            "        n = n // 2\n"
            "    else:                   # 奇数\n"
            "        n = 3 * n + 1\n"
            "    s += 1                  # 步数加 1\n"
            "print(s)                    # 输出步数\n"),
        cpp=("// P1032 Collatz步数（while）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入正整数 n\n"
             "    int s = 0;               // 步数计数\n"
             "    while (n != 1) {         // while：n 不为 1 就继续\n"
             "        if (n % 2 == 0)      // 偶数\n"
             "            n /= 2;\n"
             "        else                // 奇数\n"
             "            n = 3 * n + 1;\n"
             "        ++s;                 // 步数加 1\n"
             "    }\n"
             "    cout << s << endl;       // 输出步数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1032 Collatz步数（while）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 正整数 n\n"
              "        int s = 0;              // 步数计数\n"
              "        while (n != 1) {        // while：n 不为 1 就继续\n"
              "            if (n % 2 == 0)     // 偶数\n"
              "                n /= 2;\n"
              "            else               // 奇数\n"
              "                n = 3 * n + 1;\n"
              "            ++s;                // 步数加 1\n"
              "        }\n"
              "        System.out.println(s); // 输出步数\n"
              "    }\n"
              "}\n"),
    )
