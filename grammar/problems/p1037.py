# -*- coding: utf-8 -*-
"""P1037 升序输出"""
from generate import make_problem


def build():
    data = [
        (3, [3, 1, 2]),
        (5, [5, 4, 3, 2, 1]),
        (1, [7]),
        (4, [10, -5, 0, 3]),
        (6, [2, 2, 1, 1, 3, 3]),
        (2, [200, 100]),
        (3, [1, 1, 1]),
        (5, [9, 3, 7, 1, 5]),
        (4, [0, -1, -2, -3]),
        (2, [5, 5]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in arr)
        out = "".join(f"{x}\n" for x in sorted(arr))
        cases.append((inp, out))
    return make_problem(
        "P1037", "升序输出", ["入门", "列表", "一行一个"],
        cases=cases,
        desc_en="Given n followed by n integers (one per line), print them sorted "
                "in ascending order (one per line).",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="n lines: the n integers sorted in ascending order, one per line.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），将它们升序排序后输出（每行一个）。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="n 行，升序排序后输出，每行一个。",
        py=("# P1037 升序输出（列表内置 sort 排序）\n"
            "n = int(input())                       # 个数 n\n"
            "a = [int(input()) for _ in range(n)]   # 用列表存下所有数\n"
            "a.sort()                               # 列表内置方法：升序排序\n"
            "for x in a:                            # 顺序输出\n"
            "    print(x)\n"),
        cpp=("// P1037 升序输出（vector + sort）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    sort(a.begin(), a.end());          // 升序排序\n"
             "    for (int x : a) cout << x << endl; // 顺序输出\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1037 升序输出（数组 + Arrays.sort）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        Arrays.sort(a);                // 升序排序\n"
              "        for (int x : a) System.out.println(x);\n"
              "    }\n"
              "}\n"),
    )
