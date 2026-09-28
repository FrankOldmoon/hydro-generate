# -*- coding: utf-8 -*-
"""P1036 逆序输出"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3]),
        (5, [10, 20, 30, 40, 50]),
        (1, [7]),
        (4, [4, 8, 2, 6]),
        (2, [100, 200]),
        (6, [1, 1, 1, 2, 2, 2]),
        (3, [3, 2, 1]),
        (5, [5, 4, 3, 2, 1]),
        (4, [-1, 0, 1, 2]),
        (2, [9, 9]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in arr)
        out = "".join(f"{x}\n" for x in reversed(arr))
        cases.append((inp, out))
    return make_problem(
        "P1036", "逆序输出", ["入门", "列表", "一行一个"],
        cases=cases,
        desc_en="Given n followed by n integers (one per line), print them in "
                "reverse order (one per line).",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one integer, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="n lines: the n integers in reverse order, one per line.",
        desc_zh="给定一个正整数 n 和随后 n 个整数（每行一个），将它们按逆序输出（每行一个）。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数，满足 $1\\leq n\\leq 1000$ 且 "
                 "$-32768\\leq x_i\\leq 32767$ 。",
        output_zh="n 行，按逆序输出这 n 个整数，每行一个。",
        py=("# P1036 逆序输出（列表存储后逆序遍历）\n"
            "n = int(input())                       # 个数 n\n"
            "a = [int(input()) for _ in range(n)]   # 用列表存下所有数\n"
            "for x in reversed(a):                  # 逆序遍历列表\n"
            "    print(x)                           # 逐个输出\n"),
        cpp=("// P1036 逆序输出（vector 存储 + 逆序输出）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n);                 // 用 vector 存下所有数\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    for (int i = n - 1; i >= 0; --i)  // 逆序输出\n"
             "        cout << a[i] << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1036 逆序输出（数组存储 + 逆序输出）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];          // 用数组存下所有数\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        for (int i = n - 1; i >= 0; --i)  // 逆序输出\n"
              "            System.out.println(a[i]);\n"
              "    }\n"
              "}\n"),
    )
