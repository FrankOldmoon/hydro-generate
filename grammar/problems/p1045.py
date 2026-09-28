# -*- coding: utf-8 -*-
"""P1045 求中位数"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [5, 4, 3, 2, 1]),
        (1, [7]),
        (3, [9, 1, 5]),
        (5, [10, 20, 30, 40, 50]),
        (3, [-1, -2, -3]),
        (5, [1, 1, 1, 1, 1]),
        (3, [100, 50, 75]),
        (5, [3, 1, 4, 1, 5]),
        (3, [0, -5, 5]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + " ".join(str(x) for x in arr) + "\n"
        med = sorted(arr)[len(arr) // 2]
        cases.append((inp, f"{med}\n"))
    return make_problem(
        "P1045", "求中位数", ["入门", "列表", "一行全部"],
        cases=cases,
        desc_en="Given an odd positive integer n on the first line and n integers "
                "on the second line (space-separated), print the median, i.e. the "
                "middle element after sorting in ascending order.",
        input_en="The first line contains a positive odd integer n. The second line "
                 "contains n space-separated integers, satisfying $1\\leq n\\leq 999$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line: the median (the middle element after sorting).",
        desc_zh="第一行为正奇数 n，第二行为 n 个用空格分隔的整数，输出这 n 个数的中位数"
                "（升序排序后位于正中间的那个数）。",
        input_zh="第一行一个正奇数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 999$ "
                 "且 $-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，输出中位数（升序排序后正中间的数）。",
        py=("# P1045 求中位数（排序后取正中间元素）\n"
            "n = int(input())                              # 个数 n（奇数）\n"
            "a = list(map(int, input().split()))           # 一行读入整个列表\n"
            "a.sort()                                      # 升序排序\n"
            "print(a[n // 2])                              # 正中间元素即中位数\n"),
        cpp=("// P1045 求中位数（排序后取正中间元素）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    sort(a.begin(), a.end());                // 升序排序\n"
             "    cout << a[n / 2] << endl;                // 正中间元素即中位数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1045 求中位数（排序后取正中间元素）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        Arrays.sort(a);                     // 升序排序\n"
              "        System.out.println(a[n / 2]);       // 正中间元素即中位数\n"
              "    }\n"
              "}\n"),
    )
