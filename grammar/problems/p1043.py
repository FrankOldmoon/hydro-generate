# -*- coding: utf-8 -*-
"""P1043 某数出现次数"""
from generate import make_problem


def build():
    data = [
        (5, [1, 2, 3, 2, 2], 2),
        (3, [1, 2, 3], 4),
        (1, [5], 5),
        (4, [7, 7, 7, 7], 7),
        (6, [1, 2, 1, 2, 1, 2], 1),
        (3, [10, 20, 30], 20),
        (2, [0, 0], 0),
        (5, [-1, -2, -1, -3, -1], -1),
        (4, [5, 5, 5, 5], 3),
        (3, [100, 200, 100], 100),
    ]
    cases = []
    for n, arr, x in data:
        inp = f"{n}\n" + " ".join(str(v) for v in arr) + f"\n{x}\n"
        cases.append((inp, f"{arr.count(x)}\n"))
    return make_problem(
        "P1043", "某数出现次数", ["入门", "列表", "一行全部"],
        cases=cases,
        desc_en="Given n on the first line, n space-separated integers on the "
                "second line, and an integer x on the third line, print how many "
                "times x appears among the n integers.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers. The third line contains an "
                 "integer x, satisfying $1\\leq n\\leq 1000$ and "
                 "$-32768\\leq x_i, x\\leq 32767$ .",
        output_en="One line: the number of occurrences of x.",
        desc_zh="第一行为正整数 n，第二行为 n 个用空格分隔的整数，第三行为一个整数 x，输出 x "
                "在这 n 个数中出现的次数。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，第三行一个整数 x，满足 "
                 "$1\\leq n\\leq 1000$ 且 $-32768\\leq x_i, x\\leq 32767$ 。",
        output_zh="一行，输出 x 出现的次数。",
        py=("# P1043 某数出现次数（列表内置 count 方法）\n"
            "n = int(input())                              # 个数 n\n"
            "a = list(map(int, input().split()))           # 一行读入整个列表\n"
            "x = int(input())                              # 待查询的数 x\n"
            "print(a.count(x))                             # count 统计出现次数\n"),
        cpp=("// P1043 某数出现次数（count 算法）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    int x;\n"
             "    cin >> x;\n"
             "    cout << count(a.begin(), a.end(), x) << endl;  // 统计出现次数\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1043 某数出现次数（手动遍历计数）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        int x = sc.nextInt();\n"
              "        int cnt = 0;\n"
              "        for (int v : a)              // 遍历统计\n"
              "            if (v == x) ++cnt;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
