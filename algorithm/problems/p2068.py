# -*- coding: utf-8 -*-
"""P2068 二维差分"""
from generate import make_problem


def build():
    # (n, m, 操作列表[(x1,y1,x2,y2,c),...])，矩阵初始全 0，对子矩阵加 c
    data = [
        (2, 2, [(1, 1, 2, 2, 1), (1, 1, 1, 1, 3)]),
        (1, 1, [(1, 1, 1, 1, 5)]),
        (3, 3, [(1, 1, 3, 3, 1), (2, 2, 3, 3, 2), (1, 1, 2, 2, -1)]),
        (2, 3, [(1, 1, 2, 3, 2), (1, 1, 1, 2, 3)]),
        (4, 4, [(1, 1, 4, 4, 1), (2, 2, 3, 3, 5), (1, 1, 1, 1, -2)]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, m, q, seed):
        v = seed
        ops = []
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
            v = (v * 1103515245 + 12345) % (1 << 31)
            c = v % 201 - 100
            ops.append((x1, y1, x2, y2, c))
        return ops

    for n, m, q, seed in [(10, 10, 10, 3), (15, 12, 20, 11), (20, 20, 30, 23),
                          (30, 25, 40, 37), (50, 40, 50, 59)]:
        data.append((n, m, gen(n, m, q, seed)))

    cases = []
    for n, m, ops in data:
        # 暴力模拟作为期望输出
        a = [[0] * (m + 1) for _ in range(n + 1)]
        for x1, y1, x2, y2, c in ops:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    a[i][j] += c
        inp = f"{n} {m} {len(ops)}\n"
        for x1, y1, x2, y2, c in ops:
            inp += f"{x1} {y1} {x2} {y2} {c}\n"
        out_lines = []
        for i in range(1, n + 1):
            out_lines.append(" ".join(str(a[i][j]) for j in range(1, m + 1)))
        cases.append((inp, "\n".join(out_lines) + "\n"))

    return make_problem(
        "P2068", "二维差分", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="There is an n by m matrix initially all zero. Perform q "
                "operations: each adds c to every cell in the submatrix "
                "(x1,y1)-(x2,y2) (1-based). Output the final matrix using a 2D "
                "difference array.",
        input_en="The first line contains n, m and q. Then q lines, each with "
                 "five integers x1 y1 x2 y2 c.",
        output_en="n lines, each with m space-separated integers, the final "
                  "matrix.",
        desc_zh="给定 n×m 初始全 0 的矩阵，q 次操作给子矩阵 (x1,y1)-(x2,y2) 每个元素加 c，输出最终矩阵。",
        input_zh="第一行三个整数 n、m、q；接下来 q 行每行五个整数 x1 y1 x2 y2 c，表示给该子矩阵每个元素加 c。",
        output_zh="n 行，每行 m 个用空格分隔的整数，表示最终矩阵。",
        py=r"""# P2068 二维差分（二维差分数组 + 二维前缀和还原）
n, m, q = map(int, input().split())     # 行数 n、列数 m、操作数 q
d = [[0] * (m + 2) for _ in range(n + 2)]  # 二维差分数组，多一行一列便于边界
for _ in range(q):
    x1, y1, x2, y2, c = map(int, input().split())  # 子矩阵加 c
    d[x1][y1] += c                      # 差分四角更新
    d[x1][y2 + 1] -= c
    d[x2 + 1][y1] -= c
    d[x2 + 1][y2 + 1] += c
a = [[0] * (m + 1) for _ in range(n + 1)]
out_lines = []
for i in range(1, n + 1):
    row = []
    for j in range(1, m + 1):
        # 二维前缀和还原原矩阵
        a[i][j] = d[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        row.append(str(a[i][j]))
    out_lines.append(" ".join(row))
print("\n".join(out_lines))
""",
        cpp=r"""// P2068 二维差分（二维差分数组 + 二维前缀和还原）
#include <iostream>
using namespace std;
const int N = 105;
long long d[N][N], a[N][N];
int main() {
    int n, m, q;
    cin >> n >> m >> q;                 // 行数 n、列数 m、操作数 q
    while (q--) {
        int x1, y1, x2, y2;
        long long c;
        cin >> x1 >> y1 >> x2 >> y2 >> c;  // 子矩阵加 c
        d[x1][y1] += c;                 // 差分四角更新
        d[x1][y2 + 1] -= c;
        d[x2 + 1][y1] -= c;
        d[x2 + 1][y2 + 1] += c;
    }
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            a[i][j] = d[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1];  // 二维前缀和还原
            cout << a[i][j] << (j == m ? "\n" : " ");
        }
    return 0;
}
""",
        java=r"""// P2068 二维差分（二维差分数组 + 二维前缀和还原）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), q = sc.nextInt();  // 行 n、列 m、操作数 q
        long[][] d = new long[n + 2][m + 2];   // 二维差分数组
        while (q-- > 0) {
            int x1 = sc.nextInt(), y1 = sc.nextInt(), x2 = sc.nextInt(), y2 = sc.nextInt();
            long c = sc.nextLong();            // 子矩阵加 c
            d[x1][y1] += c;                    // 差分四角更新
            d[x1][y2 + 1] -= c;
            d[x2 + 1][y1] -= c;
            d[x2 + 1][y2 + 1] += c;
        }
        long[][] a = new long[n + 1][m + 1];
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                a[i][j] = d[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1];  // 二维前缀和还原
                if (j > 1) sb.append(" ");
                sb.append(a[i][j]);
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
""",
    )
