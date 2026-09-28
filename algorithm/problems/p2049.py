# -*- coding: utf-8 -*-
"""P2049 组合数"""
from generate import make_problem

def comb(n, m):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][m]

def build():
    data=[(5,2),(10,3),(1,0),(1,1),(10,5),
          (20,10),(30,15),(30,0),(15,7),(25,12)]
    cases=[]
    for n,m in data:
        cases.append((f"{n}\n{m}\n", f"{comb(n,m)}\n"))
    return make_problem(
        "P2049","组合数",["算法","递推递归"],
        cases=cases,
        desc_en="Given n and m, compute the binomial coefficient C(n, m) using Pascal's triangle.",
        input_en="Two integers n and m, one per line.",
        output_en="C(n, m).",
        desc_zh="给定n、m，求组合数C(n,m)的值。",
        input_zh="两行，每行一个整数，依次为n、m。",
        output_zh="C(n,m) 的值。",
        py="""# P2049 组合数
n = int(input())                         # 读取 n
m = int(input())                         # 读取 m
C = [[0] * (n + 1) for _ in range(n + 1)]  # 杨辉三角
for i in range(n + 1):                   # 递推构建杨辉三角
    C[i][0] = 1                          # C(i,0)=1
    for j in range(1, i + 1):
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]  # 递推公式
print(C[n][m])                           # 输出 C(n, m)
""",
        cpp="""// P2049 组合数
#include <iostream>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;                              // 读取 n, m
    long long C[35][35] = {0};                  // 杨辉三角
    for (int i = 0; i <= n; i++) {              // 递推构建杨辉三角
        C[i][0] = 1;                            // C(i,0)=1
        for (int j = 1; j <= i; j++)
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];  // 递推公式
    }
    cout << C[n][m] << endl;                    // 输出 C(n, m)
    return 0;
}
""",
        java="""// P2049 组合数
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();                   // 读取 n
        int m = sc.nextInt();                   // 读取 m
        long[][] C = new long[35][35];          // 杨辉三角
        for (int i = 0; i <= n; i++) {          // 递推构建杨辉三角
            C[i][0] = 1;                        // C(i,0)=1
            for (int j = 1; j <= i; j++)
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];  // 递推公式
        }
        System.out.println(C[n][m]);            // 输出 C(n, m)
    }
}
""",
    )
