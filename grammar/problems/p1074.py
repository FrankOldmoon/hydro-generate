# -*- coding: utf-8 -*-
"""P1074 边缘元素之和"""
from generate import make_problem


def build():
    data = [
        (3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        (1, 1, [[7]]),
        (4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
        (3, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
        (1, 5, [[1, 2, 3, 4, 5]]),
        (5, 1, [[1], [2], [3], [4], [5]]),
        (3, 3, [[5, 5, 5], [5, 5, 5], [5, 5, 5]]),
        (4, 3, [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]),
        (3, 3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
        (2, 3, [[-1, 0, 1], [2, 3, 4]]),
    ]

    cases = []
    for n, m, mat in data:
        inp = f"{n}\n{m}\n" + "\n".join(" ".join(str(x) for x in row) for row in mat) + "\n"
        total = sum(sum(row) for row in mat)
        inner = 0
        for i in range(1, n - 1):          # 内部元素：非首末行且非首末列
            for j in range(1, m - 1):
                inner += mat[i][j]
        cases.append((inp, f"{total - inner}\n"))
    return make_problem(
        "P1074", "边缘元素之和", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given an n×m matrix, print the sum of its border elements (the "
                "first row, the last row, the first column, and the last column).",
        input_en="The first line contains a positive integer n, the second line contains a positive integer m. The "
                 "following n lines each contain m space-separated integers, "
                 "satisfying $1\\leq n,m\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="One line: the sum of border elements.",
        desc_zh="给定一个 n×m 的矩阵，输出最外圈（第一行、最后一行、第一列、最后一列）"
                "元素之和。",
        input_zh="第一行一个正整数 n，第二行一个正整数 m。接下来 n 行，每行 m 个用空格分隔的整数，"
                 "满足 $1\\leq n,m\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="一行，输出最外圈元素之和。",
        py=("# P1074 边缘元素之和（总和减去内部元素之和）\n"
            "n = int(input())                    # 行数 n\nm = int(input())                    # 列数 m\n"
            "a = []\n"
            "for i in range(n):\n"
            "    a.append(list(map(int, input().split())))\n"
            "total = 0\n"
            "inner = 0\n"
            "for i in range(n):\n"
            "    for j in range(m):\n"
            "        total += a[i][j]           # 所有元素之和\n"
            "        if 0 < i < n - 1 and 0 < j < m - 1:  # 内部元素\n"
            "            inner += a[i][j]\n"
            "print(total - inner)               # 边缘 = 总和 - 内部\n"),
        cpp=("// P1074 边缘元素之和\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    vector<vector<int>> a(n, vector<int>(m));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> a[i][j];\n"
             "    int total = 0, inner = 0;\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) {\n"
             "            total += a[i][j];\n"
             "            if (i > 0 && i < n - 1 && j > 0 && j < m - 1)\n"
             "                inner += a[i][j];       // 内部元素\n"
             "        }\n"
             "    cout << total - inner << endl;      // 边缘 = 总和 - 内部\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1074 边缘元素之和\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        int[][] a = new int[n][m];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) a[i][j] = sc.nextInt();\n"
              "        int total = 0, inner = 0;\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) {\n"
              "                total += a[i][j];\n"
              "                if (i > 0 && i < n - 1 && j > 0 && j < m - 1)\n"
              "                    inner += a[i][j];\n"
              "            }\n"
              "        System.out.println(total - inner);\n"
              "    }\n"
              "}\n"),
    )
