# -*- coding: utf-8 -*-
"""P2047 递归求gcd"""
from generate import make_problem

def g(a, b):
    return a if b == 0 else g(b, a % b)

def build():
    data=[(12,8),(100,75),(17,5),(1071,462),(48,36),
          (1000000,1000),(1,1),(0,7),(7,0),(999999937,999999937)]
    cases=[]
    for a,b in data:
        cases.append((f"{a}\n{b}\n", f"{g(a,b)}\n"))
    return make_problem(
        "P2047","求最大公约数",["算法","递推递归"],
        cases=cases,
        desc_en="Given two non-negative integers a and b, find their greatest common divisor.",
        input_en="Two integers a and b, one per line.",
        output_en="gcd(a, b).",
        desc_zh="给定两个非负整数a、b，求它们的最大公约数。",
        input_zh="两行，每行一个整数，依次为a、b。",
        output_zh="a和b的最大公约数。",
        py="""# P2047 递归求gcd
def gcd(a, b):                          # 辗转相除递归求最大公约数
    return a if b == 0 else gcd(b, a % b)
a = int(input())                        # 读取 a
b = int(input())                        # 读取 b
print(gcd(a, b))                        # 输出 gcd(a, b)
""",
        cpp="""// P2047 递归求gcd
#include <iostream>
using namespace std;
long long gcd(long long a, long long b) {   // 辗转相除递归
    return b == 0 ? a : gcd(b, a % b);
}
int main() {
    long long a, b;
    cin >> a >> b;                          // 读取 a, b
    cout << gcd(a, b) << endl;              // 输出 gcd(a, b)
    return 0;
}
""",
        java="""// P2047 递归求gcd
import java.util.Scanner;
public class Main {
    static long gcd(long a, long b) {       // 辗转相除递归
        return b == 0 ? a : gcd(b, a % b);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();             // 读取 a
        long b = sc.nextLong();             // 读取 b
        System.out.println(gcd(a, b));      // 输出 gcd(a, b)
    }
}
""",
    )
