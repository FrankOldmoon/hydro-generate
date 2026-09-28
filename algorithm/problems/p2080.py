# -*- coding: utf-8 -*-
"""P2080 传球游戏"""
from generate import make_problem


def pass_ball(n, m):
    # f[t][i] = 传 t 次后球在 i 号手中的方案数
    f = [[0] * (n + 1) for _ in range(m + 1)]
    f[0][1] = 1                       # 开始在 1 号
    for t in range(1, m + 1):
        for i in range(1, n + 1):
            left = i - 1 if i - 1 >= 1 else n   # 左邻（环形）
            right = i + 1 if i + 1 <= n else 1  # 右邻（环形）
            f[t][i] = f[t - 1][left] + f[t - 1][right]
    return f[m][1]


def build():
    data = [
        (3, 3), (3, 1), (4, 2), (5, 3), (6, 4),
        (3, 10), (4, 5), (5, 5), (10, 4), (4, 15),
    ]
    cases = []
    for n, m in data:
        cases.append((f"{n}\n{m}\n", f"{pass_ball(n, m)}\n"))
    return make_problem(
        "P2080", "传球游戏", ["算法", "线性DP"],
        cases=cases,
        desc_en="n people numbered 1..n sit in a circle. The ball starts at person 1. "
                "Each pass moves the ball to the left or right neighbor. After m "
                "passes, count the number of ways for the ball to return to person 1.",
        input_en="Two lines: the first line contains n (2 <= n <= 30), the second "
                 "line contains m (1 <= m <= 30).",
        output_en="The number of ways for the ball to return to person 1 after m passes.",
        desc_zh="n个人编号1到n围成一圈，球从1号开始，每次传给左邻或右邻，传m次后回到1号的方案数。",
        input_zh="两行，第一行一个整数n（2 <= n <= 30），第二行一个整数m（1 <= m <= 30）。",
        output_zh="传m次后回到1号的方案数。",
        py="""# P2080 传球游戏（动态规划，环形传递）
n = int(input())                      # 人数 n
m = int(input())                      # 传球次数 m
# f[t][i] 表示传 t 次后球在 i 号手中的方案数
f = [[0] * (n + 1) for _ in range(m + 1)]
f[0][1] = 1                           # 球初始在 1 号
for t in range(1, m + 1):
    for i in range(1, n + 1):
        left = i - 1 if i - 1 >= 1 else n   # 左邻（环形回绕）
        right = i + 1 if i + 1 <= n else 1  # 右邻（环形回绕）
        f[t][i] = f[t - 1][left] + f[t - 1][right]  # 从左/右邻传过来
print(f[m][1])                        # 输出回到 1 号的方案数
""",
        cpp="""// P2080 传球游戏（动态规划，环形传递）
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;                    // 人数 n，传球次数 m
    // f[t][i] 表示传 t 次后球在 i 号手中的方案数
    vector<vector<long long>> f(m + 1, vector<long long>(n + 1, 0));
    f[0][1] = 1;                      // 球初始在 1 号
    for (int t = 1; t <= m; t++)
        for (int i = 1; i <= n; i++) {
            int left = (i - 2 + n) % n + 1;   // 左邻（环形回绕）
            int right = i % n + 1;            // 右邻（环形回绕）
            f[t][i] = f[t - 1][left] + f[t - 1][right];  // 从左/右邻传过来
        }
    cout << f[m][1] << endl;          // 输出回到 1 号的方案数
    return 0;
}
""",
        java="""// P2080 传球游戏（动态规划，环形传递）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();         // 人数 n
        int m = sc.nextInt();         // 传球次数 m
        // f[t][i] 表示传 t 次后球在 i 号手中的方案数
        long[][] f = new long[m + 1][n + 1];
        f[0][1] = 1;                  // 球初始在 1 号
        for (int t = 1; t <= m; t++)
            for (int i = 1; i <= n; i++) {
                int left = (i - 2 + n) % n + 1;  // 左邻（环形回绕）
                int right = i % n + 1;           // 右邻（环形回绕）
                f[t][i] = f[t - 1][left] + f[t - 1][right];  // 从左/右邻传过来
            }
        System.out.println(f[m][1]);  // 输出回到 1 号的方案数
    }
}
""",
    )
