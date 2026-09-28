# -*- coding: utf-8 -*-
"""P2071 爬楼梯"""
from generate import make_problem

MOD = 10**9 + 7


def ways(n):
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b % MOD


def build():
    data = [1, 2, 3, 4, 5, 10, 20, 50, 100, 1000]
    cases = []
    for n in data:
        cases.append((f"{n}\n", f"{ways(n)}\n"))
    return make_problem(
        "P2071", "爬楼梯", ["算法", "线性DP"],
        cases=cases,
        desc_en="There are n steps. Each time you can climb 1 or 2 steps. Count the number of ways to reach the top, modulo 10^9+7.",
        input_en="One integer n (1 <= n <= 1000).",
        output_en="The number of ways modulo 10^9+7.",
        desc_zh="有n级台阶，每次可以走1级或2级，求走到顶部的方案数，结果对10^9+7取模。",
        input_zh="一个整数n（1 <= n <= 1000）。",
        output_zh="方案数对10^9+7取模的值。",
        py="""# P2071 爬楼梯（线性DP：每次1或2步，方案数对1e9+7取模）
MOD = 10**9 + 7
n = int(input())                # 台阶数 n
a, b = 1, 1                     # f[0]=1, f[1]=1
for i in range(2, n + 1):       # 递推 f[i]=f[i-1]+f[i-2]
    a, b = b, (a + b) % MOD
print(b % MOD)                  # 输出方案数取模
""",
        cpp="""// P2071 爬楼梯（线性DP：每次1或2步，方案数对1e9+7取模）
#include <iostream>
using namespace std;
int main() {
    const long long MOD = 1000000007;
    int n;
    cin >> n;                   // 台阶数 n
    long long a = 1, b = 1;     // f[0]=1, f[1]=1
    for (int i = 2; i <= n; i++) { // 递推 f[i]=f[i-1]+f[i-2]
        long long c = (a + b) % MOD;
        a = b; b = c;
    }
    cout << b % MOD << endl;     // 输出方案数取模
    return 0;
}
""",
        java="""// P2071 爬楼梯（线性DP：每次1或2步，方案数对1e9+7取模）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        final long MOD = 1000000007L;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();              // 台阶数 n
        long a = 1, b = 1;                 // f[0]=1, f[1]=1
        for (int i = 2; i <= n; i++) {     // 递推 f[i]=f[i-1]+f[i-2]
            long c = (a + b) % MOD;
            a = b; b = c;
        }
        System.out.println(b % MOD);       // 输出方案数取模
    }
}
""",
    )
