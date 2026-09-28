# -*- coding: utf-8 -*-
"""P1039 最大值的下标"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [5, 4, 3, 2, 1]),
        (1, [7]),
        (4, [3, 9, 2, 9]),
        (2, [100, 200]),
        (3, [1, 1, 1]),
        (5, [2, 8, 8, 3, 8]),
        (4, [-5, -3, -7, -1]),
        (2, [9, 9]),
        (6, [10, 20, 30, 40, 50, 60]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in arr)
        idx = arr.index(max(arr))
        cases.append((inp, f"{idx}\n"))
    return make_problem(
        "P1039", "最大值的下标", ["入门", "列表", "一行一个"],
        cases=cases,
        desc_en="Given n followed by n integers (one per line), print the index "
                "(0-based) of the first occurrence of the maximum value.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line containing the 0-based index of the first maximum.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），输出最大值第一次出现的下标"
                "（下标从 0 开始）。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，输出最大值第一次出现的下标（从 0 开始）。",
        py=("# P1039 最大值的下标（列表内置 max + index）\n"
            "n = int(input())                       # 个数 n\n"
            "a = [int(input()) for _ in range(n)]   # 用列表存下所有数\n"
            "print(a.index(max(a)))                 # max 求最大值，index 求其下标\n"),
        cpp=("// P1039 最大值的下标（vector + 手动查找）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    int idx = 0;\n"
             "    for (int i = 1; i < n; ++i)       // 查找第一个最大值的下标\n"
             "        if (a[i] > a[idx]) idx = i;   // 严格大于，保证取第一次出现\n"
             "    cout << idx << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1039 最大值的下标（数组 + 手动查找）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        int idx = 0;\n"
              "        for (int i = 1; i < n; ++i)    // 查找第一个最大值的下标\n"
              "            if (a[i] > a[idx]) idx = i; // 严格大于，保证取第一次出现\n"
              "        System.out.println(idx);\n"
              "    }\n"
              "}\n"),
    )
