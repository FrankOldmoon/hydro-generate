# -*- coding: utf-8 -*-
"""P1040 交换最大值与最小值后输出"""
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
        a = list(arr)
        i_max = a.index(max(a))
        i_min = a.index(min(a))
        a[i_max], a[i_min] = a[i_min], a[i_max]
        out = "".join(f"{x}\n" for x in a)
        cases.append((inp, out))
    return make_problem(
        "P1040", "交换最大值与最小值后输出", ["入门", "列表", "一行一个"],
        cases=cases,
        desc_en="Given n followed by n integers (one per line), swap the first "
                "occurrence of the maximum with the first occurrence of the "
                "minimum, then print the resulting list (one per line).",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="n lines: the list after swapping the first max and first min, "
                  "one per line.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），将第一个最大值与第一个最小值"
                "交换位置后，输出整个列表（每行一个）。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="n 行，交换第一个最大值与第一个最小值后，输出整个列表，每行一个。",
        py=("# P1040 交换最大值与最小值后输出（index 定位 + 交换）\n"
            "n = int(input())                       # 个数 n\n"
            "a = [int(input()) for _ in range(n)]   # 用列表存下所有数\n"
            "i = a.index(max(a))                    # 最大值第一次出现的下标\n"
            "j = a.index(min(a))                    # 最小值第一次出现的下标\n"
            "a[i], a[j] = a[j], a[i]                # 交换两位置\n"
            "for x in a:                            # 输出交换后的列表\n"
            "    print(x)\n"),
        cpp=("// P1040 交换最大值与最小值后输出\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    int i = 0, j = 0;\n"
             "    for (int k = 1; k < n; ++k) {     // 找第一个最大/最小值下标\n"
             "        if (a[k] > a[i]) i = k;\n"
             "        if (a[k] < a[j]) j = k;\n"
             "    }\n"
             "    swap(a[i], a[j]);                 // 交换两位置\n"
             "    for (int x : a) cout << x << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1040 交换最大值与最小值后输出\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        int i = 0, j = 0;\n"
              "        for (int k = 1; k < n; ++k) {  // 找第一个最大/最小值下标\n"
              "            if (a[k] > a[i]) i = k;\n"
              "            if (a[k] < a[j]) j = k;\n"
              "        }\n"
              "        int t = a[i]; a[i] = a[j]; a[j] = t;  // 交换\n"
              "        for (int x : a) System.out.println(x);\n"
              "    }\n"
              "}\n"),
    )
