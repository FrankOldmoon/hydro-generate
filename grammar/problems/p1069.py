# -*- coding: utf-8 -*-
"""P1069 每列求和"""
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
        out = "".join(f"{sum(mat[i][j] for i in range(n))}\n" for j in range(m))
        cases.append((inp, out))
    return make_problem(
        "P1069", "每列求和", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given an n×m matrix, print the sum of each column (one sum per "
                "line).",
        input_en="The first line contains a positive integer n, the second line contains a positive integer m. The "
                 "following n lines each contain m space-separated integers, "
                 "satisfying $1\\leq n,m\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="m lines: the sum of each column.",
        desc_zh="给定一个 n×m 的矩阵，输出每一列的元素之和（每行一个）。",
        input_zh="第一行一个正整数 n，第二行一个正整数 m。接下来 n 行，每行 m 个用空格分隔的整数，"
                 "满足 $1\\leq n,m\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="m 行，每行输出对应列的元素之和。",
        py=("# P1069 每列求和（固定列、遍历行求和）\n"
            "n = int(input())                    # 行数 n\nm = int(input())                    # 列数 m\n"
            "a = []\n"
            "for i in range(n):\n"
            "    a.append(list(map(int, input().split())))\n"
            "for j in range(m):                 # 逐列求和\n"
            "    s = 0\n"
            "    for i in range(n):             # 遍历该列所有行\n"
            "        s += a[i][j]\n"
            "    print(s)\n"),
        cpp=("// P1069 每列求和\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    vector<vector<int>> a(n, vector<int>(m));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> a[i][j];\n"
             "    for (int j = 0; j < m; ++j) {\n"
             "        int s = 0;\n"
             "        for (int i = 0; i < n; ++i) s += a[i][j];\n"
             "        cout << s << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1069 每列求和\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        int[][] a = new int[n][m];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) a[i][j] = sc.nextInt();\n"
              "        for (int j = 0; j < m; ++j) {\n"
              "            int s = 0;\n"
              "            for (int i = 0; i < n; ++i) s += a[i][j];\n"
              "            System.out.println(s);\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
