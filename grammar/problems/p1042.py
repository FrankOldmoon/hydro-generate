# -*- coding: utf-8 -*-
"""P1042 第二大的数"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [5, 5, 4, 4, 3]),
        (2, [1, 2]),
        (4, [10, 20, 30, 40]),
        (3, [100, 100, 50]),
        (5, [7, 7, 7, 8, 8]),
        (4, [1, 1, 1, 2]),
        (3, [9, 5, 9]),
        (2, [3, 7]),
        (6, [1, 2, 3, 4, 5, 6]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + " ".join(str(x) for x in arr) + "\n"
        s = sorted(arr)
        mx = s[-1]
        second = mx
        for v in reversed(s):          # 从大到小找第一个严格小于最大值的数
            if v < mx:
                second = v
                break
        cases.append((inp, f"{second}\n"))
    return make_problem(
        "P1042", "第二大的数", ["入门", "列表", "一行全部"],
        cases=cases,
        desc_en="Given n on the first line and n integers on the second line "
                "(space-separated), print the second largest distinct value. It is "
                "guaranteed that there are at least two distinct values.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ , and at least two distinct "
                 "values exist.",
        output_en="One line: the second largest distinct value.",
        desc_zh="第一行为正整数 n，第二行为 n 个用空格分隔的整数，输出其中第二大的数"
                "（去重后的第二大）。保证至少有两个不同的数。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 1000$ "
                 "且 $-32768\\leq x_i\\leq 32767$ ，且至少有两个不同的数。",
        output_zh="一行，输出第二大的数（去重后）。",
        py=("# P1042 第二大的数（sort 排序后找严格小于最大值的数）\n"
            "n = int(input())                              # 个数 n\n"
            "a = list(map(int, input().split()))           # 一行读入整个列表\n"
            "a.sort()                                      # 列表内置方法：升序排序\n"
            "mx = a[-1]                                    # 末尾即最大值\n"
            "second = mx\n"
            "for i in range(len(a) - 2, -1, -1):           # 从后往前找严格小于最大值的\n"
            "    if a[i] < mx:\n"
            "        second = a[i]\n"
            "        break\n"
            "print(second)\n"),
        cpp=("// P1042 第二大的数（排序后找严格小于最大值的数）\n"
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
             "    int mx = a[n - 1];                       // 最大值\n"
             "    int second = mx;\n"
             "    for (int i = n - 2; i >= 0; --i)         // 从后往前找严格小于最大值的\n"
             "        if (a[i] < mx) { second = a[i]; break; }\n"
             "    cout << second << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1042 第二大的数（排序后找严格小于最大值的数）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        Arrays.sort(a);                     // 升序排序\n"
              "        int mx = a[n - 1];                  // 最大值\n"
              "        int second = mx;\n"
              "        for (int i = n - 2; i >= 0; --i) {  // 从后往前找严格小于最大值的\n"
              "            if (a[i] < mx) { second = a[i]; break; }\n"
              "        }\n"
              "        System.out.println(second);\n"
              "    }\n"
              "}\n"),
    )
