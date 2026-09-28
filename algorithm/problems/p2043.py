# -*- coding: utf-8 -*-
"""P2043 汉诺塔步数"""
from generate import make_problem

def build():
    data=[1,2,3,4,5,6,10,15,20,30]
    cases=[]
    for n in data:
        f=0
        for i in range(1,n+1): f=2*f+1
        cases.append((f"{n}\n", f"{f}\n"))
    return make_problem(
        "P2043","汉诺塔步数",["算法","递推递归"],
        cases=cases,
        desc_en="Move n disks in the Tower of Hanoi from one peg to another. Find the minimum number of moves.",
        input_en="One integer n.",
        output_en="The minimum number of moves (2^n - 1).",
        desc_zh="求n个盘子的汉诺塔从一根柱子全部移到另一根柱子所需的最少移动步数。",
        input_zh="一个整数n。",
        output_zh="最少移动步数。",
        py="""# P2043 汉诺塔步数
n = int(input())            # 读取盘子数 n
f = 0                       # f 表示 n 盘的最少步数
for i in range(1, n + 1):   # 递推：f(i)=2*f(i-1)+1
    f = 2 * f + 1
print(f)                    # 输出 2^n - 1
""",
        cpp="""// P2043 汉诺塔步数
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                       // 读取盘子数 n
    long long f = 0;                // f 表示 n 盘的最少步数
    for (int i = 1; i <= n; i++)    // 递推：f(i)=2*f(i-1)+1
        f = 2 * f + 1;
    cout << f << endl;              // 输出 2^n - 1
    return 0;
}
""",
        java="""// P2043 汉诺塔步数
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 读取盘子数 n
        long f = 0;                    // f 表示 n 盘的最少步数
        for (int i = 1; i <= n; i++)   // 递推：f(i)=2*f(i-1)+1
            f = 2 * f + 1;
        System.out.println(f);         // 输出 2^n - 1
    }
}
""",
    )
