# -*- coding: utf-8 -*-
"""P1098 汉诺塔最少步数"""
from generate import make_problem


def build():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 15]

    def hanoi(n):
        if n == 1:              # 一个盘子直接移，1 步，递归出口
            return 1
        return 2 * hanoi(n - 1) + 1   # 把上 n-1 个移走，移最大盘，再移回

    cases = [(f"{n}\n", f"{hanoi(n)}\n") for n in data]
    return make_problem(
        "P1098", "汉诺塔最少步数", ["入门", "递归"],
        cases=cases,
        desc_en="There are n disks of different sizes on a pillar. Move them to "
                "another pillar following the rules (one disk at a time, no "
                "larger disk on a smaller one). Print the minimum number of "
                "moves.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 20$ .",
        output_en="One line containing the minimum number of moves.",
        desc_zh="有 n 个大小不同的盘子叠在一根柱子上，按汉诺塔规则（每次移一个，大盘"
                "不能压小盘）移到另一根柱子。求最少移动步数并输出。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 20$ 。",
        output_zh="一行，输出最少移动步数。",
        py=("# P1098 汉诺塔最少步数（递归：hanoi(n)=2*hanoi(n-1)+1）\n"
            "def hanoi(n):               # 定义递归函数\n"
            "    if n == 1:             # 递归出口：1 个盘子 1 步\n"
            "        return 1\n"
            "    return 2 * hanoi(n - 1) + 1  # 移走上 n-1 个 + 移最大盘 + 移回\n"
            "\n"
            "n = int(input())           # 盘子数 n\n"
            "print(hanoi(n))\n"),
        cpp=("// P1098 汉诺塔最少步数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "long long hanoi(int n) {  // 递归求最少步数\n"
             "    if (n == 1) return 1; // 递归出口\n"
             "    return 2 * hanoi(n - 1) + 1;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    cout << hanoi(n) << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1098 汉诺塔最少步数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static long hanoi(int n) {  // 递归求最少步数\n"
              "        if (n == 1) return 1;   // 递归出口\n"
              "        return 2 * hanoi(n - 1) + 1;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        System.out.println(hanoi(n));\n"
              "    }\n"
              "}\n"),
    )
