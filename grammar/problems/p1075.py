# -*- coding: utf-8 -*-
"""P1075 矩阵加法"""
from generate import make_problem


def build():
    data = [
        (2, 3, [[1, 2, 3], [4, 5, 6]], [[6, 5, 4], [3, 2, 1]]),
        (1, 1, [[7]], [[3]]),
        (3, 3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[3, 3, 3], [2, 2, 2], [1, 1, 1]]),
        (2, 2, [[10, 20], [30, 40]], [[1, 2], [3, 4]]),
        (1, 4, [[1, 2, 3, 4]], [[4, 3, 2, 1]]),
        (4, 1, [[1], [2], [3], [4]], [[4], [3], [2], [1]]),
        (3, 2, [[5, 5], [5, 5], [5, 5]], [[1, 2], [3, 4], [5, 6]]),
        (2, 4, [[0, 0, 0, 0], [1, 1, 1, 1]], [[1, 1, 1, 1], [0, 0, 0, 0]]),
        (3, 3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        (2, 3, [[-1, 0, 1], [2, 3, 4]], [[1, 0, -1], [-2, -3, -4]]),
    ]

    cases = []
    for n, m, ma, mb in data:
        inp = f"{n}\n{m}\n"
        inp += "\n".join(" ".join(str(x) for x in row) for row in ma) + "\n"
        inp += "\n".join(" ".join(str(x) for x in row) for row in mb) + "\n"
        mc = [[ma[i][j] + mb[i][j] for j in range(m)] for i in range(n)]
        out = "\n".join(" ".join(str(x) for x in row) for row in mc) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P1075", "矩阵加法", ["入门", "二维列表"],
        cases=cases,
        desc_en="Given two n×m matrices A and B, print their sum A+B (element-wise "
                "addition).",
        input_en="The first line contains a positive integer n, the second line contains a positive integer m. The next "
                 "n lines are matrix A, followed by n lines for matrix B, each "
                 "line containing m space-separated integers, satisfying "
                 "$1\\leq n,m\\leq 100$ and $-1000\\leq a_{ij}\\leq 1000$ .",
        output_en="n lines: the sum matrix A+B, each line containing m "
                  "space-separated integers.",
        desc_zh="给定两个 n×m 的矩阵 A 和 B，输出它们的和 A+B（对应位置相加）。",
        input_zh="第一行一个正整数 n，第二行一个正整数 m。接下来 n 行为矩阵 A，再接下来 n 行为矩阵 B，"
                 "每行 m 个用空格分隔的整数，满足 $1\\leq n,m\\leq 100$ 且 $-1000\\leq a_{ij}\\leq 1000$ 。",
        output_zh="n 行，每行 m 个用空格分隔的整数，表示 A+B 的结果。",
        py=("# P1075 矩阵加法（对应位置相加）\n"
            "n = int(input())                    # 行数 n\nm = int(input())                    # 列数 m\n"
            "a = []\n"
            "for i in range(n):                 # 读入矩阵 A\n"
            "    a.append(list(map(int, input().split())))\n"
            "b = []\n"
            "for i in range(n):                 # 读入矩阵 B\n"
            "    b.append(list(map(int, input().split())))\n"
            "for i in range(n):                 # 对应位置相加并输出\n"
            "    row = [a[i][j] + b[i][j] for j in range(m)]\n"
            "    print(' '.join(map(str, row)))\n"),
        cpp=("// P1075 矩阵加法\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    vector<vector<int>> a(n, vector<int>(m)), b(n, vector<int>(m));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> a[i][j];\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < m; ++j) cin >> b[i][j];\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        for (int j = 0; j < m; ++j) {\n"
             "            if (j) cout << ' ';\n"
             "            cout << a[i][j] + b[i][j];   // 对应相加\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1075 矩阵加法\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        int[][] a = new int[n][m], b = new int[n][m];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) a[i][j] = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < m; ++j) b[i][j] = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            StringBuilder sb = new StringBuilder();\n"
              "            for (int j = 0; j < m; ++j) {\n"
              "                if (j > 0) sb.append(' ');\n"
              "                sb.append(a[i][j] + b[i][j]);\n"
              "            }\n"
              "            System.out.println(sb.toString());\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
