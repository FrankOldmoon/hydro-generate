# -*- coding: utf-8 -*-
"""P1071 矩阵最大值"""
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
        mx = max(max(row) for row in mat)
        cases.append((inp, f"{mx}\n"))
    return make_problem(
        "P1071", "矩阵最大值", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given an n×m matrix, print the maximum element.",
        input_en="The first line contains a positive integer n, the second line contains a positive integer m. The "
                 "following n lines each contain m space-separated integers, "
                 "satisfying $1\\leq n,m\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="One line: the maximum element.",
        desc_zh="给定一个 n×m 的矩阵，输出其中最大的元素。",
        input_zh="第一行一个正整数 n，第二行一个正整数 m。接下来 n 行，每行 m 个用空格分隔的整数，"
                 "满足 $1\\leq n,m\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="一行，输出矩阵中的最大元素。",
        py=("# P1071 矩阵最大值（逐行取 max 再取总 max）\n"
            "n = int(input())                    # 行数 n\nm = int(input())                    # 列数 m\n"
            "a = []\n"
            "for i in range(n):\n"
            "    a.append(list(map(int, input().split())))\n"
            "mx = a[0][0]\n"
            "for i in range(n):                 # 遍历所有元素\n"
            "    for j in range(m):\n"
            "        if a[i][j] > mx:\n"
            "            mx = a[i][j]\n"
            "print(mx)\n"),
        cpp=("// P1071 矩阵最大值\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    vector<vector<int>> a(n, vector<int>(m));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> a[i][j];\n"
             "    int mx = a[0][0];\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j)\n"
             "            if (a[i][j] > mx) mx = a[i][j];\n"
             "    cout << mx << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1071 矩阵最大值\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        int[][] a = new int[n][m];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) a[i][j] = sc.nextInt();\n"
              "        int mx = a[0][0];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j)\n"
              "                if (a[i][j] > mx) mx = a[i][j];\n"
              "        System.out.println(mx);\n"
              "    }\n"
              "}\n"),
    )
