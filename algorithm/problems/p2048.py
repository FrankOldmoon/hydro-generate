# -*- coding: utf-8 -*-
"""P2048 数塔最大路径"""
from generate import make_problem

def tower_max(tri):
    n = len(tri)
    dp = tri[-1][:]                       # 最后一行作为初始 dp
    for i in range(n - 2, -1, -1):        # 自底向上递推
        for j in range(i + 1):
            dp[j] = tri[i][j] + max(dp[j], dp[j + 1])
    return dp[0]

def make_tri(n, seed):
    tri = []
    v = seed
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            v = (v * 7 + 3) % 99 + 1      # 1~99 的伪随机数
            row.append(v)
        tri.append(row)
    return tri

def build():
    tris = [[[5]], [[1], [2, 3]]]         # 前 2 组：小而清晰
    for n in range(3, 11):                # 第 3~10 组：3 到 10 层
        tris.append(make_tri(n, n * 13 + 1))
    cases = []
    for tri in tris:
        n = len(tri)
        inp = f"{n}\n" + "\n".join(" ".join(map(str, row)) for row in tri) + "\n"
        cases.append((inp, f"{tower_max(tri)}\n"))
    return make_problem(
        "P2048","数塔最大路径",["算法","递推递归"],
        cases=cases,
        desc_en="Given a number triangle of n levels, start from the top and move to the lower-left or lower-right neighbor each step. Find the maximum path sum to the bottom.",
        input_en="First line: n. Then n lines, the i-th line contains i integers.",
        output_en="The maximum path sum.",
        desc_zh="给定n层数字三角形，从顶部出发每步走向左下或右下相邻数字，求到底部的路径最大数字和。",
        input_zh="第一行一个整数n；接下来n行，第i行有i个整数。",
        output_zh="路径最大和。",
        py="""# P2048 数塔最大路径
n = int(input())                        # 读取层数 n
a = []                                  # 存储数字三角形
for i in range(n):
    a.append(list(map(int, input().split())))  # 读取第 i 行
dp = a[n - 1][:]                        # 自底向上，从最后一行开始
for i in range(n - 2, -1, -1):          # 从倒数第二行向上递推
    for j in range(i + 1):
        dp[j] = a[i][j] + max(dp[j], dp[j + 1])  # 取左下、右下较大者
print(dp[0])                            # 输出最大路径和
""",
        cpp="""// P2048 数塔最大路径
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;                                    // 读取层数 n
    vector<vector<int>> a(n);                    // 存储数字三角形
    for (int i = 0; i < n; i++) {
        a[i].resize(i + 1);
        for (int j = 0; j <= i; j++)             // 读取第 i 行
            cin >> a[i][j];
    }
    vector<int> dp(a[n - 1]);                    // 自底向上，从最后一行开始
    for (int i = n - 2; i >= 0; i--)             // 从倒数第二行向上递推
        for (int j = 0; j <= i; j++)
            dp[j] = a[i][j] + max(dp[j], dp[j + 1]);  // 取左下、右下较大者
    cout << dp[0] << endl;                       // 输出最大路径和
    return 0;
}
""",
        java="""// P2048 数塔最大路径
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();                    // 读取层数 n
        int[][] a = new int[n][];                // 存储数字三角形
        for (int i = 0; i < n; i++) {
            a[i] = new int[i + 1];
            for (int j = 0; j <= i; j++)         // 读取第 i 行
                a[i][j] = sc.nextInt();
        }
        int[] dp = a[n - 1].clone();             // 自底向上，从最后一行开始
        for (int i = n - 2; i >= 0; i--)         // 从倒数第二行向上递推
            for (int j = 0; j <= i; j++)
                dp[j] = a[i][j] + Math.max(dp[j], dp[j + 1]);  // 取左下、右下较大者
        System.out.println(dp[0]);               // 输出最大路径和
    }
}
""",
    )
