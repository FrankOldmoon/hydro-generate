# -*- coding: utf-8 -*-
"""P2074 数字三角形最大路径"""
from generate import make_problem


def tri(rows):
    n = len(rows)
    f = [row[:] for row in rows]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            f[i][j] += max(f[i + 1][j], f[i + 1][j + 1])
    return f[0][0]


def build():
    data = [
        [[7]],
        [[3], [1, 5]],
        [[1], [2, 3], [4, 5, 6]],
        [[9], [3, 8], [1, 2, 5]],
        [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]],
        [[3], [4, 1], [2, 8, 5], [1, 6, 9, 3]],
        [[2], [7, 4], [3, 8, 5], [9, 1, 6, 2], [4, 7, 2, 8, 3]],
        [[10], [20, 30]],
        [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]],
        [[-1], [-2, 3], [4, -5, 6], [-7, 8, -9, 10]],
    ]
    cases = []
    for rows in data:
        n = len(rows)
        inp = f"{n}\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)
        cases.append((inp, f"{tri(rows)}\n"))
    return make_problem(
        "P2074", "数字三角形最大路径", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given a number triangle of n rows, start from the top. Each step "
                "you may go down to the left or right below. Find the maximum sum "
                "from top to bottom.",
        input_en="The first line contains n (1 <= n <= 100). The following n lines "
                 "form the triangle: the i-th line contains i integers.",
        output_en="The maximum path sum from top to bottom.",
        desc_zh="给定一个n层数字三角形，从顶部出发，每步可以走到正下方或右下方，求从顶到底的最大路径和。",
        input_zh="第一行一个整数n（1 <= n <= 100），接下来n行构成三角形，第i行有i个整数。",
        output_zh="从顶到底的最大路径和。",
        py="""# P2074 数字三角形最大路径（线性DP：自底向上）
n = int(input())                      # 三角形层数 n
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))  # 逐行读取
f = [row[:] for row in a]             # 复制用于DP
for i in range(n - 2, -1, -1):        # 自底向上递推
    for j in range(i + 1):
        f[i][j] += max(f[i + 1][j], f[i + 1][j + 1])  # 取左下/右下较大者
print(f[0][0])                        # 顶部即为最大路径和
""",
        cpp="""// P2074 数字三角形最大路径（线性DP：自底向上）
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                         // 三角形层数 n
    vector<vector<int>> a(n);
    for (int i = 0; i < n; i++) {
        a[i].resize(i + 1);
        for (int j = 0; j <= i; j++) cin >> a[i][j];
    }
    vector<vector<int>> f = a;        // 复制用于DP
    for (int i = n - 2; i >= 0; i--)  // 自底向上递推
        for (int j = 0; j <= i; j++)
            f[i][j] += max(f[i + 1][j], f[i + 1][j + 1]);  // 取左下/右下较大者
    cout << f[0][0] << endl;          // 顶部即为最大路径和
    return 0;
}
""",
        java="""// P2074 数字三角形最大路径（线性DP：自底向上）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();         // 三角形层数 n
        int[][] a = new int[n][];
        for (int i = 0; i < n; i++) {
            a[i] = new int[i + 1];
            for (int j = 0; j <= i; j++) a[i][j] = sc.nextInt();
        }
        int[][] f = new int[n][];     // 复制用于DP
        for (int i = 0; i < n; i++) f[i] = a[i].clone();
        for (int i = n - 2; i >= 0; i--)  // 自底向上递推
            for (int j = 0; j <= i; j++)
                f[i][j] += Math.max(f[i + 1][j], f[i + 1][j + 1]);  // 取左下/右下较大者
        System.out.println(f[0][0]);  // 顶部即为最大路径和
    }
}
""",
    )
