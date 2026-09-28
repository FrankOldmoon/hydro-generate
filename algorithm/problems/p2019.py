# -*- coding: utf-8 -*-
"""P2019 Z字形遍历"""
from generate import make_problem


def build():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def matrix(n):
        # 用与位置相关的取值，便于核对遍历顺序（不等于遍历序本身）
        return [[(i + 1) * 10 + (j + 1) for j in range(n)] for i in range(n)]

    def make(n, mat):
        res = []
        for s in range(2 * n - 1):          # 第 s+1 条对角线
            if s % 2 == 0:                   # 偶数对角线：向右上（行减列增）
                r = min(s, n - 1)
                while r >= 0 and s - r < n:
                    res.append(mat[r][s - r])
                    r -= 1
            else:                            # 奇数对角线：向左下（行增列减）
                r = max(0, s - (n - 1))
                while r < n and s - r >= 0:
                    res.append(mat[r][s - r])
                    r += 1
        return "".join("{0}\n".format(x) for x in res)

    cases = []
    for n in ns:
        mat = matrix(n)
        inp = f"{n}\n" + "\n".join(" ".join(str(x) for x in row) for row in mat) + "\n"
        cases.append((inp, make(n, mat)))
    return make_problem(
        "P2019", "Z字形遍历", ["算法", "模拟"],
        cases=cases,
        desc_en="Given an integer n and an n*n matrix, traverse all elements in "
                "zigzag (Z-shape) order along anti-diagonals and print each element "
                "on its own line. Start at the top-left corner: the 1st diagonal "
                "goes up-right, the 2nd goes down-left, the 3rd up-right, and so "
                "on, alternating until all elements are visited.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain n space-separated integers, satisfying "
                 "$1\\leq n\\leq 10$ and $1\\leq a_{ij}\\leq 999$ .",
        output_en="(n*n) lines: all matrix elements in zigzag diagonal order, one "
                  "per line.",
        desc_zh="给定整数 n 和一个 n×n 矩阵，按对角线之字形（Z 字形）遍历所有元素，每个元素单独一行输出。从左上角出发，第 1 条对角线向右上，第 2 条向左下，第 3 条向右上，依次交替，直到遍历完所有元素。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 10$ 且 $1\\leq a_{ij}\\leq 999$ 。",
        output_zh="共 n×n 行，按对角线之字形遍历顺序输出矩阵的所有元素，每行一个。",
        py=("# P2019 Z字形遍历（按反对角线之字形：偶数对角线右上，奇数对角线左下）\n"
            "n = int(input())                                      # 矩阵阶数 n\n"
            "a = [list(map(int, input().split())) for _ in range(n)]  # 读入 n×n 矩阵\n"
            "res = []\n"
            "for s in range(2 * n - 1):           # 第 s+1 条反对角线（s = i + j）\n"
            "    if s % 2 == 0:                    # 偶数对角线：向右上\n"
            "        r = min(s, n - 1)\n"
            "        while r >= 0 and s - r < n:\n"
            "            res.append(a[r][s - r]); r -= 1\n"
            "    else:                             # 奇数对角线：向左下\n"
            "        r = max(0, s - (n - 1))\n"
            "        while r < n and s - r >= 0:\n"
            "            res.append(a[r][s - r]); r += 1\n"
            "for x in res:                        # 每个元素单独一行\n"
            "    print(x)\n"),
        cpp=("// P2019 Z字形遍历\n"
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
             "    for (int s = 0; s <= 2 * n - 2; ++s) {     // 第 s+1 条反对角线\n"
             "        if (s % 2 == 0) {                       // 偶数对角线：向右上\n"
             "            for (int r = (s < n - 1 ? s : n - 1); r >= 0 && s - r < n; --r)\n"
             "                res.push_back(a[r][s - r]);\n"
             "        } else {                                // 奇数对角线：向左下\n"
             "            for (int r = (s - (n - 1) > 0 ? s - (n - 1) : 0); r < n && s - r >= 0; ++r)\n"
             "                res.push_back(a[r][s - r]);\n"
             "        }\n"
             "    }\n"
             "    for (int x : res) cout << x << endl;        // 每个元素单独一行\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2019 Z字形遍历\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();                   // 矩阵阶数 n\n"
              "        int[][] a = new int[n][n];\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            for (int j = 0; j < n; ++j) a[i][j] = sc.nextInt();\n"
              "        StringBuilder sb = new StringBuilder();\n"
              "        for (int s = 0; s <= 2 * n - 2; ++s) {  // 第 s+1 条反对角线\n"
              "            if (s % 2 == 0) {                    // 偶数对角线：向右上\n"
              "                for (int r = (s < n - 1 ? s : n - 1); r >= 0 && s - r < n; --r)\n"
              "                    sb.append(a[r][s - r]).append('\\n');\n"
              "            } else {                             // 奇数对角线：向左下\n"
              "                for (int r = (s - (n - 1) > 0 ? s - (n - 1) : 0); r < n && s - r >= 0; ++r)\n"
              "                    sb.append(a[r][s - r]).append('\\n');\n"
              "            }\n"
              "        }\n"
              "        System.out.print(sb);                   // 每个元素单独一行\n"
              "    }\n"
              "}\n"),
    )
