# -*- coding: utf-8 -*-
"""P2041 爬楼梯"""
from generate import make_problem

def build():
    data=[1,2,3,4,5,6,10,15,20,30]
    cases=[]
    for n in data:
        f=[0,1,2]
        for i in range(3,n+1): f.append(f[i-1]+f[i-2])
        cases.append((f"{n}\n", f"{f[n]}\n"))
    return make_problem(
        "P2041","爬楼梯",["算法","递推递归"],
        cases=cases,
        desc_en="There are n stairs. Each time you can climb 1 or 2 steps. Find the number of ways to reach the top.",
        input_en="One integer n.",
        output_en="The number of ways.",
        desc_zh="有n级台阶，每次走1或2级，求走到顶端共有多少种走法。",
        input_zh="一个整数n。",
        output_zh="走法总数。",
        py="""# P2041 爬楼梯
n = int(input())            # 读取台阶数 n
f = [0, 1, 2]               # f[1]=1, f[2]=2
for i in range(3, n + 1):   # 递推：f[i]=f[i-1]+f[i-2]
    f.append(f[i - 1] + f[i - 2])
print(f[n])                 # 输出走法总数
""",
        cpp="""// P2041 爬楼梯
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                      // 读取台阶数 n
    long long f[35];               // f[i] 表示走到第 i 级的走法数
    f[0] = 0; f[1] = 1; f[2] = 2;
    for (int i = 3; i <= n; i++)   // 递推：f[i]=f[i-1]+f[i-2]
        f[i] = f[i - 1] + f[i - 2];
    cout << f[n] << endl;          // 输出走法总数
    return 0;
}
""",
        java="""// P2041 爬楼梯
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 读取台阶数 n
        long[] f = new long[35];       // f[i] 表示走到第 i 级的走法数
        f[0] = 0; f[1] = 1; f[2] = 2;
        for (int i = 3; i <= n; i++)   // 递推：f[i]=f[i-1]+f[i-2]
            f[i] = f[i - 1] + f[i - 2];
        System.out.println(f[n]);      // 输出走法总数
    }
}
""",
    )
