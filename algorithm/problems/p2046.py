# -*- coding: utf-8 -*-
"""P2046 快速幂"""
from generate import make_problem

def build():
    data=[(2,10,1000000007),(3,5,100),(7,0,1000000007),(5,1,100),
          (0,5,1000),(2,30,1000000000),(2,1000000000,1000000007),
          (10,9,1000000007),(123456,789,1000000007),(999999937,2,1000000007)]
    cases=[]
    for a,b,m in data:
        ans=pow(a,b,m)
        cases.append((f"{a}\n{b}\n{m}\n", f"{ans}\n"))
    return make_problem(
        "P2046","快速幂",["算法","递推递归"],
        cases=cases,
        desc_en="Given a, b, m, compute a^b mod m using fast exponentiation.",
        input_en="Three integers a, b, m, one per line.",
        output_en="a^b mod m.",
        desc_zh="给定a、b、m，求a的b次方对m取模的值。",
        input_zh="三行，每行一个整数，依次为a、b、m。",
        output_zh="a^b mod m 的值。",
        py="""# P2046 快速幂
a = int(input())               # 读取 a
b = int(input())               # 读取 b
m = int(input())               # 读取 m
ans = 1                        # 快速幂结果
base = a % m
t = b
while t > 0:                   # 逐位处理 b
    if t & 1:                  # 当前位为 1 则累乘
        ans = ans * base % m
    base = base * base % m     # 底数平方
    t >>= 1
print(ans % m)                 # 输出 a^b mod m
""",
        cpp="""// P2046 快速幂
#include <iostream>
using namespace std;
int main() {
    long long a, b, m;
    cin >> a >> b >> m;                // 读取 a, b, m
    long long ans = 1, base = a % m;   // 快速幂初始化
    while (b > 0) {                    // 逐位处理 b
        if (b & 1)                     // 当前位为 1 则累乘
            ans = ans * base % m;
        base = base * base % m;        // 底数平方
        b >>= 1;
    }
    cout << ans % m << endl;           // 输出 a^b mod m
    return 0;
}
""",
        java="""// P2046 快速幂
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();        // 读取 a
        long b = sc.nextLong();        // 读取 b
        long m = sc.nextLong();        // 读取 m
        long ans = 1, base = a % m;    // 快速幂初始化
        while (b > 0) {                // 逐位处理 b
            if ((b & 1) == 1)          // 当前位为 1 则累乘
                ans = ans * base % m;
            base = base * base % m;    // 底数平方
            b >>= 1;
        }
        System.out.println(ans % m);   // 输出 a^b mod m
    }
}
""",
    )
