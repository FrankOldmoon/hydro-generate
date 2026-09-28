# -*- coding: utf-8 -*-
"""P1041 降序输出"""
from generate import make_problem


def build():
    data = [
        (3, [3, 1, 2]),
        (5, [1, 2, 3, 4, 5]),
        (1, [7]),
        (4, [10, -5, 0, 3]),
        (6, [2, 2, 1, 1, 3, 3]),
        (2, [100, 200]),
        (3, [1, 1, 1]),
        (5, [9, 3, 7, 1, 5]),
        (4, [0, -1, -2, -3]),
        (2, [5, 5]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + " ".join(str(x) for x in arr) + "\n"
        out = " ".join(str(x) for x in sorted(arr, reverse=True)) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P1041", "降序输出", ["入门", "列表", "一行全部"],
        cases=cases,
        desc_en="Given n on the first line and n integers on the second line "
                "(space-separated), print them sorted in descending order on one "
                "line (space-separated).",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line: the n integers sorted in descending order, "
                  "space-separated.",
        desc_zh="第一行为正整数 n，第二行为 n 个用空格分隔的整数，将它们降序排序后在一行内"
                "输出（以空格分隔）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，降序排序后以空格分隔输出。",
        py=("# P1041 降序输出（一行读入 + sort 降序）\n"
            "n = int(input())                              # 个数 n\n"
            "a = list(map(int, input().split()))           # 一行读入整个列表\n"
            "a.sort(reverse=True)                          # 列表内置方法：降序排序\n"
            "print(' '.join(map(str, a)))                  # 空格分隔输出\n"),
        cpp=("// P1041 降序输出（vector + sort 降序）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    sort(a.begin(), a.end(), greater<int>()); // 降序排序\n"
             "    for (int i = 0; i < n; ++i) {             // 空格分隔输出\n"
             "        if (i) cout << ' ';\n"
             "        cout << a[i];\n"
             "    }\n"
             "    cout << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1041 降序输出（数组 + 升序排序后倒序输出）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        Arrays.sort(a);                     // 升序排序\n"
              "        for (int i = n - 1; i >= 0; --i) {   // 倒序输出即降序\n"
              "            if (i < n - 1) System.out.print(' ');\n"
              "            System.out.print(a[i]);\n"
              "        }\n"
              "        System.out.println();\n"
              "    }\n"
              "}\n"),
    )
