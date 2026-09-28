# -*- coding: utf-8 -*-
"""P2015 蛇形矩阵"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        a = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i % 2 == 0:
                    a[i][j] = i * n + j + 1      # 偶数行从左到右
                else:
                    a[i][j] = i * n + (n - 1 - j) + 1  # 奇数行从右到左
        lines = [" ".join(str(a[i][j]) for j in range(n)) for i in range(n)]
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2015", "蛇形矩阵", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, fill an n*n matrix with 1..n*n in serpentine "
                "(snake) order: start at the top-left going right; at the boundary "
                "move down to the next row and reverse direction, alternating each "
                "row. Print the matrix.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="n lines, each containing n space-separated integers: the "
                  "serpentine-filled matrix.",
        desc_zh="给定整数 n，将 1 到 n² 蛇形填入 n×n 矩阵：从左上角向右开始，到边界后下移一行并反向，每行方向交替，最后输出该矩阵。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行，每行 n 个用空格分隔的整数，表示蛇形填数后的矩阵。",
        py=("# P2015 蛇形矩阵（行方向交替：偶数行左→右，奇数行右→左）\n"
            "n = int(input())                      # 矩阵阶数 n\n"
            "a = [[0] * n for _ in range(n)]       # n×n 矩阵\n"
            "for i in range(n):\n"
            "    for j in range(n):\n"
            "        if i % 2 == 0:                # 偶数行：从左到右\n"
            "            a[i][j] = i * n + j + 1\n"
            "        else:                         # 奇数行：从右到左\n"
            "            a[i][j] = i * n + (n - 1 - j) + 1\n"
            "for i in range(n):                    # 输出矩阵\n"
            "    print(' '.join(map(str, a[i])))\n"),
        cpp=("// P2015 蛇形矩阵\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                          // 矩阵阶数 n\n"
             "    vector<vector<int>> a(n, vector<int>(n));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < n; ++j) {\n"
             "            if (i % 2 == 0) a[i][j] = i * n + j + 1;            // 偶数行左→右\n"
             "            else a[i][j] = i * n + (n - 1 - j) + 1;            // 奇数行右→左\n"
             "        }\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        for (int j = 0; j < n; ++j) {\n"
             "            if (j) cout << ' ';\n"
             "            cout << a[i][j];\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2015 蛇形矩阵\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();             // 矩阵阶数 n\n"
              "        int[][] a = new int[n][n];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < n; ++j) {\n"
              "                if (i % 2 == 0) a[i][j] = i * n + j + 1;       // 偶数行左→右\n"
              "                else a[i][j] = i * n + (n - 1 - j) + 1;       // 奇数行右→左\n"
              "            }\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            StringBuilder sb = new StringBuilder();\n"
              "            for (int j = 0; j < n; ++j) {\n"
              "                if (j > 0) sb.append(' ');\n"
              "                sb.append(a[i][j]);\n"
              "            }\n"
              "            System.out.println(sb);\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
