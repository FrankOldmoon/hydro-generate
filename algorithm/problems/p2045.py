# -*- coding: utf-8 -*-
"""P2045 骨牌铺满"""
from generate import make_problem

def build():
    data=[1,2,3,4,5,6,8,12,18,25]
    cases=[]
    for n in data:
        f=[0,1,2]
        for i in range(3,n+1): f.append(f[i-1]+f[i-2])
        cases.append((f"{n}\n", f"{f[n]}\n"))
    return make_problem(
        "P2045","骨牌铺满",["算法","递推递归"],
        cases=cases,
        desc_en="Tile a 2*n rectangle with 1*2 dominoes. Find the number of tilings.",
        input_en="One integer n.",
        output_en="The number of tilings.",
        desc_zh="用1×2骨牌铺满2×n的矩形，求共有多少种不同的铺法。",
        input_zh="一个整数n。",
        output_zh="铺法总数。",
        py="""# P2045 骨牌铺满
n = int(input())            # 读取列数 n
f = [0, 1, 2]               # f[1]=1, f[2]=2
for i in range(3, n + 1):   # 递推：f[i]=f[i-1]+f[i-2]
    f.append(f[i - 1] + f[i - 2])
print(f[n])                 # 输出铺法数
""",
        cpp="""// P2045 骨牌铺满
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                        // 读取列数 n
    long long f[30];                 // f[i] 表示 2×i 的铺法数
    f[0] = 0; f[1] = 1; f[2] = 2;
    for (int i = 3; i <= n; i++)     // 递推：f[i]=f[i-1]+f[i-2]
        f[i] = f[i - 1] + f[i - 2];
    cout << f[n] << endl;            // 输出铺法数
    return 0;
}
""",
        java="""// P2045 骨牌铺满
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 读取列数 n
        long[] f = new long[30];       // f[i] 表示 2×i 的铺法数
        f[0] = 0; f[1] = 1; f[2] = 2;
        for (int i = 3; i <= n; i++)   // 递推：f[i]=f[i-1]+f[i-2]
            f[i] = f[i - 1] + f[i - 2];
        System.out.println(f[n]);      // 输出铺法数
    }
}
""",
    )
