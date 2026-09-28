# -*- coding: utf-8 -*-
"""P2042 斐波那契第n项"""
from generate import make_problem

def build():
    MOD=1000000007
    data=[1,2,3,4,5,10,20,50,80,100]
    cases=[]
    for n in data:
        f=[0,1,1]
        for i in range(3,n+1): f.append((f[i-1]+f[i-2])%MOD)
        cases.append((f"{n}\n", f"{f[n]}\n"))
    return make_problem(
        "P2042","斐波那契第n项",["算法","递推递归"],
        cases=cases,
        desc_en="Let F(1)=F(2)=1 and F(n)=F(n-1)+F(n-2). Given n, find F(n) mod 1000000007.",
        input_en="One integer n.",
        output_en="F(n) mod 1000000007.",
        desc_zh="给定正整数n，求斐波那契数列第n项F(n)对1000000007取模的值，其中F(1)=F(2)=1。",
        input_zh="一个整数n。",
        output_zh="F(n) mod 1000000007 的值。",
        py="""# P2042 斐波那契第n项
MOD = 1000000007
n = int(input())                 # 读取 n
f = [0, 1, 1]                    # F(1)=F(2)=1
for i in range(3, n + 1):        # 递推：F(i)=F(i-1)+F(i-2)
    f.append((f[i - 1] + f[i - 2]) % MOD)
print(f[n])                      # 输出 F(n) mod 1e9+7
""",
        cpp="""// P2042 斐波那契第n项
#include <iostream>
using namespace std;
const int MOD = 1000000007;
int main() {
    int n;
    cin >> n;                          // 读取 n
    long long f[105];                  // f[i] = F(i) mod 1e9+7
    f[1] = 1; f[2] = 1;                // F(1)=F(2)=1
    for (int i = 3; i <= n; i++)       // 递推：F(i)=F(i-1)+F(i-2)
        f[i] = (f[i - 1] + f[i - 2]) % MOD;
    cout << f[n] << endl;              // 输出 F(n) mod 1e9+7
    return 0;
}
""",
        java="""// P2042 斐波那契第n项
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MOD = 1000000007;
        int n = sc.nextInt();              // 读取 n
        long[] f = new long[105];          // f[i] = F(i) mod 1e9+7
        f[1] = 1; f[2] = 1;                // F(1)=F(2)=1
        for (int i = 3; i <= n; i++)       // 递推：F(i)=F(i-1)+F(i-2)
            f[i] = (f[i - 1] + f[i - 2]) % MOD;
        System.out.println(f[n]);          // 输出 F(n) mod 1e9+7
    }
}
""",
    )
