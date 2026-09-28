# -*- coding: utf-8 -*-
"""P2020 螺旋输出"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def matrix(n):
        # 用与位置相关的取值，便于核对螺旋顺序（不等于遍历序本身）
        return [[(i + 1) * 10 + (j + 1) for j in range(n)] for i in range(n)]

    def make(n, mat):
        res = []
        top, bottom, left, right = 0, n - 1, 0, n - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):      # 上边：左→右
                res.append(mat[top][j])
            top += 1
            for i in range(top, bottom + 1):      # 右边：上→下
                res.append(mat[i][right])
            right -= 1
            if top <= bottom:                     # 下边：右→左
                for j in range(right, left - 1, -1):
                    res.append(mat[bottom][j])
                bottom -= 1
            if left <= right:                     # 左边：下→上
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
        return "".join("{0}\n".format(x) for x in res)

    cases = []
    for n in ns:
        mat = matrix(n)
        inp = f"{n}\n" + "\n".join(" ".join(str(x) for x in row) for row in mat) + "\n"
        cases.append((inp, make(n, mat)))
    return make_problem(
        "P2020", "螺旋输出", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n and an n*n matrix, traverse all elements in "
                "clockwise spiral order starting from the top-left corner (go right "
                "along the top, then down the right, then left along the bottom, "
                "then up the left, and spiral inward), printing each element on "
                "its own line.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain n space-separated integers, satisfying "
                 "$1\\leq n\\leq 10$ and $1\\leq a_{ij}\\leq 999$ .",
        output_en="(n*n) lines: all matrix elements in clockwise spiral order, one "
                  "per line.",
        desc_zh="给定整数 n 和一个 n×n 矩阵，从左上角开始顺时针螺旋遍历所有元素（上边向右、右边向下、下边向左、左边向上，逐层向内），每个元素单独一行输出。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 10$ 且 $1\\leq a_{ij}\\leq 999$ 。",
        output_zh="共 n×n 行，按顺时针螺旋顺序输出矩阵的所有元素，每行一个。",
        py=("# P2020 螺旋输出（顺时针螺旋：上→右→下→左，逐层向内）\n"
            "n = int(input())                                      # 矩阵阶数 n\n"
            "a = [list(map(int, input().split())) for _ in range(n)]  # 读入 n×n 矩阵\n"
            "res = []\n"
            "top, bottom, left, right = 0, n - 1, 0, n - 1   # 当前层的四个边界\n"
            "while top <= bottom and left <= right:\n"
            "    for j in range(left, right + 1):       # 上边：左→右\n"
            "        res.append(a[top][j])\n"
            "    top += 1\n"
            "    for i in range(top, bottom + 1):       # 右边：上→下\n"
            "        res.append(a[i][right])\n"
            "    right -= 1\n"
            "    if top <= bottom:                      # 下边：右→左\n"
            "        for j in range(right, left - 1, -1):\n"
            "            res.append(a[bottom][j])\n"
            "        bottom -= 1\n"
            "    if left <= right:                      # 左边：下→上\n"
            "        for i in range(bottom, top - 1, -1):\n"
            "            res.append(a[i][left])\n"
            "        left += 1\n"
            "for x in res:                              # 每个元素单独一行\n"
            "    print(x)\n"),
        cpp=("// P2020 螺旋输出\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                                  // 矩阵阶数 n\n"
             "    vector<vector<int>> a(n, vector<int>(n));\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        for (int j = 0; j < n; ++j) cin >> a[i][j];\n"
             "    vector<int> res;\n"
             "    int top = 0, bottom = n - 1, left = 0, right = n - 1; // 当前层边界\n"
             "    while (top <= bottom && left <= right) {\n"
             "        for (int j = left; j <= right; ++j) res.push_back(a[top][j]);  // 上边左→右\n"
             "        top++;\n"
             "        for (int i = top; i <= bottom; ++i) res.push_back(a[i][right]); // 右边上→下\n"
             "        right--;\n"
             "        if (top <= bottom) {                                            // 下边右→左\n"
             "            for (int j = right; j >= left; --j) res.push_back(a[bottom][j]);\n"
             "            bottom--;\n"
             "        }\n"
             "        if (left <= right) {                                            // 左边下→上\n"
             "            for (int i = bottom; i >= top; --i) res.push_back(a[i][left]);\n"
             "            left++;\n"
             "        }\n"
             "    }\n"
             "    for (int x : res) cout << x << endl;            // 每个元素单独一行\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2020 螺旋输出\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();                   // 矩阵阶数 n\n"
              "        int[][] a = new int[n][n];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < n; ++j) a[i][j] = sc.nextInt();\n"
              "        StringBuilder sb = new StringBuilder();\n"
              "        int top = 0, bottom = n - 1, left = 0, right = n - 1; // 当前层边界\n"
              "        while (top <= bottom && left <= right) {\n"
              "            for (int j = left; j <= right; ++j) sb.append(a[top][j]).append('\\n');   // 上边左→右\n"
              "            top++;\n"
              "            for (int i = top; i <= bottom; ++i) sb.append(a[i][right]).append('\\n'); // 右边上→下\n"
              "            right--;\n"
              "            if (top <= bottom) {                                              // 下边右→左\n"
              "                for (int j = right; j >= left; --j) sb.append(a[bottom][j]).append('\\n');\n"
              "                bottom--;\n"
              "            }\n"
              "            if (left <= right) {                                              // 左边下→上\n"
              "                for (int i = bottom; i >= top; --i) sb.append(a[i][left]).append('\\n');\n"
              "                left++;\n"
              "            }\n"
              "        }\n"
              "        System.out.print(sb);                // 每个元素单独一行\n"
              "    }\n"
              "}\n"),
    )
