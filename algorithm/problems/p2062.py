# -*- coding: utf-8 -*-
"""P2062 二维子矩阵和"""
from generate import make_problem


def build():
    # (n, m, 矩阵行列表, 查询[(x1,y1,x2,y2),...])，坐标 1-based 闭区间
    data = [
        (2, 2, [[1, 2], [3, 4]], [(1, 1, 2, 2), (1, 1, 1, 2)]),
        (1, 1, [[5]], [(1, 1, 1, 1)]),
        (3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [(1, 1, 3, 3), (2, 2, 3, 3), (1, 2, 2, 3)]),
        (2, 3, [[1, -1, 2], [3, 0, -2]], [(1, 1, 2, 3), (1, 2, 2, 2)]),
        (4, 4, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
         [(1, 1, 4, 4), (2, 2, 3, 3), (1, 1, 1, 1)]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, m, q, seed):
        v = seed
        mat = []
        for _ in range(n):
            row = []
            for _ in range(m):
                v = (v * 1103515245 + 12345) % (1 << 31)
                row.append(v % 201 - 100)     # -100..100
            mat.append(row)
        qs = []
        for _ in range(q):
            v = (v * 1103515245 + 12345) % (1 << 31)
            x1 = v % n + 1
            v = (v * 1103515245 + 12345) % (1 << 31)
            y1 = v % m + 1
            v = (v * 1103515245 + 12345) % (1 << 31)
            x2 = v % n + 1
            v = (v * 1103515245 + 12345) % (1 << 31)
            y2 = v % m + 1
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            qs.append((x1, y1, x2, y2))
        return mat, qs

    for n, m, q, seed in [(10, 10, 10, 3), (20, 15, 20, 11),
                          (30, 30, 30, 23), (50, 40, 50, 37),
                          (80, 60, 60, 59)]:
        mat, qs = gen(n, m, q, seed)
        data.append((n, m, mat, qs))

    cases = []
    for n, m, mat, qs in data:
        # 二维前缀和 s[i][j] = mat[i-1][j-1] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]
        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s[i][j] = (mat[i - 1][j - 1] + s[i - 1][j]
                           + s[i][j - 1] - s[i - 1][j - 1])
        inp = f"{n} {m}\n"
        for row in mat:
            inp += " ".join(map(str, row)) + "\n"
        inp += f"{len(qs)}\n"
        out = []
        for x1, y1, x2, y2 in qs:
            inp += f"{x1} {y1} {x2} {y2}\n"
            tot = (s[x2][y2] - s[x1 - 1][y2]
                   - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])
            out.append(str(tot))
        cases.append((inp, "\n".join(out) + "\n"))

    return make_problem(
        "P2062", "二维子矩阵和", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given an n by m matrix and q queries, each query asks for the "
                "sum of the submatrix from (x1,y1) to (x2,y2) (1-based, "
                "inclusive). Use a 2D prefix sum array.",
        input_en="The first line contains n and m. Then n lines, each with m "
                 "space-separated integers. Then a line with q. Then q lines, "
                 "each with four integers x1 y1 x2 y2.",
        output_en="q lines, each the sum of the queried submatrix.",
        desc_zh="给定 n×m 矩阵，q 次查询子矩阵 (x1,y1) 到 (x2,y2) 的和，每个查询输出一行结果。",
        input_zh="第一行两个整数 n 和 m；接下来 n 行每行 m 个用空格分隔的整数；再一行一个整数 q；接下来 q 行每行四个整数 x1 y1 x2 y2。",
        output_zh="共 q 行，每行一个整数，表示对应子矩阵的元素和。",
        py=r"""# P2062 二维子矩阵和（二维前缀和）
n, m = map(int, input().split())        # 矩阵行数 n、列数 m
s = [[0] * (m + 1) for _ in range(n + 1)]  # 二维前缀和，多一行一列便于边界
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        # 容斥原理构造前缀和
        s[i][j] = row[j - 1] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
q = int(input())                        # 查询数 q
out = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())  # 子矩阵两角 1-based
    # 容斥原理求子矩阵和
    tot = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
    out.append(str(tot))
print("\n".join(out))
""",
        cpp=r"""// P2062 二维子矩阵和（二维前缀和）
#include <iostream>
using namespace std;
const int N = 105;
long long s[N][N];
int main() {
    int n, m;
    cin >> n >> m;                      // 矩阵行数 n、列数 m
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            long long x;
            cin >> x;
            s[i][j] = x + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];  // 容斥构造
        }
    int q;
    cin >> q;                           // 查询数 q
    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;    // 子矩阵两角 1-based
        cout << s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1] << "\n";
    }
    return 0;
}
""",
        java=r"""// P2062 二维子矩阵和（二维前缀和）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();   // 矩阵行数 n、列数 m
        long[][] s = new long[n + 1][m + 1];      // 二维前缀和
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                s[i][j] = sc.nextLong() + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];  // 容斥构造
        int q = sc.nextInt();                     // 查询数 q
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int x1 = sc.nextInt(), y1 = sc.nextInt(), x2 = sc.nextInt(), y2 = sc.nextInt();
            sb.append(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]).append("\n");
        }
        System.out.print(sb);
    }
}
""",
    )
