# -*- coding: utf-8 -*-
"""P2016 回形矩阵"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def make(n):
        a = [[0] * n for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1
        while num <= n * n:
            for j in range(left, right + 1):      # 上边：左→右
                a[top][j] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):      # 右边：上→下
                a[i][right] = num
                num += 1
            right -= 1
            for j in range(right, left - 1, -1):  # 下边：右→左
                a[bottom][j] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):  # 左边：下→上
                a[i][left] = num
                num += 1
            left += 1
        lines = [" ".join(str(a[i][j]) for j in range(n)) for i in range(n)]
        return "\n".join(lines) + "\n"

    cases = [(f"{n}\n", make(n)) for n in ns]
    return make_problem(
        "P2016", "回形矩阵", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n, fill an n*n matrix with 1..n*n in spiral "
                "(clockwise, outside-in) order starting from the top-left corner, "
                "then print the matrix.",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 10$ .",
        output_en="n lines, each containing n space-separated integers: the "
                  "spiral-filled matrix.",
        desc_zh="给定整数 n，将 1 到 n² 从外向内顺时针螺旋填入 n×n 矩阵（从左上角开始），最后输出该矩阵。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 10$ 。",
        output_zh="n 行，每行 n 个用空格分隔的整数，表示回形（螺旋）填数后的矩阵。",
        py=("# P2016 回形矩阵（顺时针螺旋填数：上→右→下→左，逐层向内）\n"
            "n = int(input())                      # 矩阵阶数 n\n"
            "a = [[0] * n for _ in range(n)]       # n×n 矩阵\n"
            "num = 1\n"
            "top, bottom, left, right = 0, n - 1, 0, n - 1   # 当前层的四个边界\n"
            "while num <= n * n:\n"
            "    for j in range(left, right + 1):       # 上边：左→右\n"
            "        a[top][j] = num; num += 1\n"
            "    top += 1\n"
            "    for i in range(top, bottom + 1):       # 右边：上→下\n"
            "        a[i][right] = num; num += 1\n"
            "    right -= 1\n"
            "    for j in range(right, left - 1, -1):   # 下边：右→左\n"
            "        a[bottom][j] = num; num += 1\n"
            "    bottom -= 1\n"
            "    for i in range(bottom, top - 1, -1):   # 左边：下→上\n"
            "        a[i][left] = num; num += 1\n"
            "    left += 1\n"
            "for i in range(n):                    # 输出矩阵\n"
            "    print(' '.join(map(str, a[i])))\n"),
        cpp=("// P2016 回形矩阵\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                          // 矩阵阶数 n\n"
             "    vector<vector<int>> a(n, vector<int>(n, 0));\n"
             "    int num = 1;\n"
             "    int top = 0, bottom = n - 1, left = 0, right = n - 1; // 当前层边界\n"
             "    while (num <= n * n) {\n"
             "        for (int j = left; j <= right; ++j) a[top][j] = num++;    // 上边左→右\n"
             "        top++;\n"
             "        for (int i = top; i <= bottom; ++i) a[i][right] = num++;  // 右边上→下\n"
             "        right--;\n"
             "        for (int j = right; j >= left; --j) a[bottom][j] = num++; // 下边右→左\n"
             "        bottom--;\n"
             "        for (int i = bottom; i >= top; --i) a[i][left] = num++;   // 左边下→上\n"
             "        left++;\n"
             "    }\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        for (int j = 0; j < n; ++j) {\n"
             "            if (j) cout << ' ';\n"
             "            cout << a[i][j];\n"
             "        }\n"
             "        cout << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2016 回形矩阵\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();             // 矩阵阶数 n\n"
              "        int[][] a = new int[n][n];\n"
              "        int num = 1;\n"
              "        int top = 0, bottom = n - 1, left = 0, right = n - 1; // 当前层边界\n"
              "        while (num <= n * n) {\n"
              "            for (int j = left; j <= right; ++j) a[top][j] = num++;    // 上边左→右\n"
              "            top++;\n"
              "            for (int i = top; i <= bottom; ++i) a[i][right] = num++;  // 右边上→下\n"
              "            right--;\n"
              "            for (int j = right; j >= left; --j) a[bottom][j] = num++; // 下边右→左\n"
              "            bottom--;\n"
              "            for (int i = bottom; i >= top; --i) a[i][left] = num++;   // 左边下→上\n"
              "            left++;\n"
              "        }\n"
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
