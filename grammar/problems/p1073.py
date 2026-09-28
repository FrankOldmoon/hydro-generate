# -*- coding: utf-8 -*-
"""P1073 矩阵转置"""
from generate import make_problem


def build():
    data = [
        (2, 3, [[1, 2, 3], [4, 5, 6]]),
        (1, 1, [[7]]),
        (3, 3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]]),
        (2, 2, [[10, 20], [30, 40]]),
        (1, 4, [[1, 2, 3, 4]]),
        (4, 1, [[1], [2], [3], [4]]),
        (3, 2, [[5, 5], [5, 5], [5, 5]]),
        (2, 4, [[0, 0, 0, 0], [1, 1, 1, 1]]),
        (3, 3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
        (2, 3, [[-1, 0, 1], [2, 3, 4]]),
    ]

    cases = []
    for n, m, mat in data:
        inp = f"{n}\n{m}\n" + "\n".join(" ".join(str(x) for x in row) for row in mat) + "\n"
        trans = [[mat[i][j] for i in range(n)] for j in range(m)]
        out = "\n".join(" ".join(str(x) for x in row) for row in trans) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P1073", "矩阵转置", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given an n×m matrix, print its transpose (an m×n matrix where "
                "the element at (j, i) is the original element at (i, j)).",
        input_en="The first line contains a positive integer n, the second line contains a positive integer m. The "
                 "following n lines each contain m space-separated integers, "
                 "satisfying $1\\leq n,m\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="m lines: the transposed matrix, each line containing n "
                  "space-separated integers.",
        desc_zh="给定一个 n×m 的矩阵，输出它的转置矩阵（m×n，即行列互换）。",
        input_zh="第一行一个正整数 n，第二行一个正整数 m。接下来 n 行，每行 m 个用空格分隔的整数，"
                 "满足 $1\\leq n,m\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="m 行，每行 n 个用空格分隔的整数，表示转置后的矩阵。",
        py=("# P1073 矩阵转置（行列互换：b[j][i] = a[i][j]）\n"
            "n = int(input())                    # 行数 n\nm = int(input())                    # 列数 m\n"
            "a = []\n"
            "for i in range(n):\n"
            "    a.append(list(map(int, input().split())))\n"
            "b = [[0] * n for _ in range(m)]    # 转置矩阵 m×n\n"
            "for i in range(n):\n"
            "    for j in range(m):\n"
            "        b[j][i] = a[i][j]          # 行列互换\n"
            "for j in range(m):                 # 输出转置矩阵\n"
            "    print(' '.join(map(str, b[j])))\n"),
        cpp=("// P1073 矩阵转置\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    vector<vector<int>> a(n, vector<int>(m));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> a[i][j];\n"
             "    vector<vector<int>> b(m, vector<int>(n));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j)\n"
             "            b[j][i] = a[i][j];               // 行列互换\n"
             "    for (int i = 0; i < m; ++i) {\n"
             "        for (int j = 0; j < n; ++j) {\n"
             "            if (j) cout << ' ';\n"
             "            cout << b[i][j];\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1073 矩阵转置\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        int[][] a = new int[n][m];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) a[i][j] = sc.nextInt();\n"
              "        int[][] b = new int[m][n];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j)\n"
              "                b[j][i] = a[i][j];           // 行列互换\n"
              "        for (int i = 0; i < m; ++i) {\n"
              "            StringBuilder sb = new StringBuilder();\n"
              "            for (int j = 0; j < n; ++j) {\n"
              "                if (j > 0) sb.append(' ');\n"
              "                sb.append(b[i][j]);\n"
              "            }\n"
              "            System.out.println(sb.toString());\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
