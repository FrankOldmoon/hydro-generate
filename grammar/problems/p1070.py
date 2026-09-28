# -*- coding: utf-8 -*-
"""P1070 主对角线之和"""
from generate import make_problem


def build():
    data = [
        (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        (1, [[7]]),
        (2, [[10, 20], [30, 40]]),
        (4, [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]),
        (3, [[5, 5, 5], [5, 5, 5], [5, 5, 5]]),
        (2, [[1, 2], [3, 4]]),
        (5, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]),
        (3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
        (2, [[-1, 0], [2, 3]]),
        (4, [[2, 4, 6, 8], [1, 3, 5, 7], [9, 7, 5, 3], [8, 6, 4, 2]]),
    ]

    cases = []
    for n, mat in data:
        inp = f"{n}\n" + "\n".join(" ".join(str(x) for x in row) for row in mat) + "\n"
        diag = sum(mat[i][i] for i in range(n))
        cases.append((inp, f"{diag}\n"))
    return make_problem(
        "P1070", "主对角线之和", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given an n×n square matrix, print the sum of its main diagonal "
                "(from top-left to bottom-right).",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain n space-separated integers, satisfying "
                 "$1\\leq n\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="One line: the sum of the main diagonal.",
        desc_zh="给定一个 n×n 的方阵，输出主对角线（左上到右下）元素之和。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行 n 个用空格分隔的整数，"
                 "满足 $1\\leq n\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="一行，输出主对角线元素之和。",
        py=("# P1070 主对角线之和（a[i][i] 即主对角线）\n"
            "n = int(input())                    # 方阵阶数 n\n"
            "a = []\n"
            "for i in range(n):\n"
            "    a.append(list(map(int, input().split())))\n"
            "s = 0\n"
            "for i in range(n):                  # 主对角线下标 i==j\n"
            "    s += a[i][i]\n"
            "print(s)\n"),
        cpp=("// P1070 主对角线之和\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<vector<int>> a(n, vector<int>(n));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < n; ++j) cin >> a[i][j];\n"
             "    int s = 0;\n"
             "    for (int i = 0; i < n; ++i) s += a[i][i];  // 主对角线 i==j\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1070 主对角线之和\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[][] a = new int[n][n];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < n; ++j) a[i][j] = sc.nextInt();\n"
              "        int s = 0;\n"
              "        for (int i = 0; i < n; ++i) s += a[i][i];  // 主对角线 i==j\n"
              "        System.out.println(s);\n"
              "    }\n"
              "}\n"),
    )
