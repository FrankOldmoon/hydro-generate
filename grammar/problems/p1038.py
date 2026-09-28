# -*- coding: utf-8 -*-
"""P1038 大于平均值的个数"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (4, [1, 2, 3, 4]),
        (5, [10, 10, 10, 10, 10]),
        (1, [5]),
        (4, [1, 1, 1, 9]),
        (2, [0, 10]),
        (3, [1, 2, 6]),
        (6, [1, 2, 3, 4, 5, 6]),
        (5, [-2, -1, 0, 1, 2]),
        (3, [100, 200, 300]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in arr)
        avg = sum(arr) / len(arr)
        cnt = sum(1 for x in arr if x > avg)
        cases.append((inp, f"{cnt}\n"))
    return make_problem(
        "P1038", "大于平均值的个数", ["入门", "列表", "一行一个"],
        cases=cases,
        desc_en="Given n followed by n integers (one per line), print how many of "
                "them are strictly greater than the average.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line containing the count of elements strictly greater than "
                  "the average.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），输出其中严格大于平均值的个数。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，输出严格大于平均值的元素个数。",
        py=("# P1038 大于平均值的个数（先存列表，再算均值，再统计）\n"
            "n = int(input())                       # 个数 n\n"
            "a = [int(input()) for _ in range(n)]   # 用列表存下所有数\n"
            "avg = sum(a) / len(a)                  # 平均值（用浮点避免整除）\n"
            "cnt = 0\n"
            "for x in a:                            # 再次遍历列表\n"
            "    if x > avg:                        # 大于平均值则计数\n"
            "        cnt += 1\n"
            "print(cnt)\n"),
        cpp=("// P1038 大于平均值的个数（vector 两遍遍历）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);\n"
             "    int s = 0;\n"
             "    for (int i = 0; i < n; ++i) { cin >> a[i]; s += a[i]; }\n"
             "    double avg = (double)s / n;       // 平均值\n"
             "    int cnt = 0;\n"
             "    for (int x : a)                   // 再次遍历列表\n"
             "        if (x > avg) ++cnt;\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1038 大于平均值的个数（数组两遍遍历）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        int s = 0;\n"
              "        for (int i = 0; i < n; ++i) { a[i] = sc.nextInt(); s += a[i]; }\n"
              "        double avg = (double) s / n;  // 平均值\n"
              "        int cnt = 0;\n"
              "        for (int x : a)               // 再次遍历列表\n"
              "            if (x > avg) ++cnt;\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
