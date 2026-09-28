# -*- coding: utf-8 -*-
"""P2050 分解因数个数"""
from generate import make_problem

def count_div(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return cnt

def build():
    data=[1,2,6,12,100,97,1000,360,1000000,999983]
    cases=[]
    for n in data:
        cases.append((f"{n}\n", f"{count_div(n)}\n"))
    return make_problem(
        "P2050","分解因数个数",["算法","递推递归"],
        cases=cases,
        desc_en="Given a positive integer n, find the number of its positive divisors (including 1 and n).",
        input_en="One integer n.",
        output_en="The number of positive divisors.",
        desc_zh="给定正整数n，求n的正因数个数（包括1和n本身）。",
        input_zh="一个整数n。",
        output_zh="因数个数。",
        py="""# P2050 分解因数个数
n = int(input())            # 读取 n
cnt = 0
i = 1
while i * i <= n:           # 枚举到 sqrt(n)
    if n % i == 0:          # i 是因数
        cnt += 1
        if i != n // i:     # 配对的另一个因数
            cnt += 1
    i += 1
print(cnt)                  # 输出因数个数
""",
        cpp="""// P2050 分解因数个数
#include <iostream>
using namespace std;
int main() {
    long long n;
    cin >> n;                       // 读取 n
    long long cnt = 0;
    for (long long i = 1; i * i <= n; i++) {  // 枚举到 sqrt(n)
        if (n % i == 0) {           // i 是因数
            cnt++;
            if (i != n / i)         // 配对的另一个因数
                cnt++;
        }
    }
    cout << cnt << endl;            // 输出因数个数
    return 0;
}
""",
        java="""// P2050 分解因数个数
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();             // 读取 n
        long cnt = 0;
        for (long i = 1; i * i <= n; i++) { // 枚举到 sqrt(n)
            if (n % i == 0) {               // i 是因数
                cnt++;
                if (i != n / i)             // 配对的另一个因数
                    cnt++;
            }
        }
        System.out.println(cnt);            // 输出因数个数
    }
}
""",
    )
