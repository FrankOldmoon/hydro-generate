# -*- coding: utf-8 -*-
"""P2055 整数平方根"""
from generate import make_problem
import math

def build():
    # n 取值适中(<=1e9)，避免 C++ long long 在二分中 mid*mid 溢出
    data=[0,1,2,4,9,15,16,99,1000000,1000000000]
    cases=[]
    for n in data:
        inp=f"{n}\n"
        # 参考答案：floor(sqrt(n))
        out=math.isqrt(n)
        cases.append((inp,f"{out}\n"))
    return make_problem(
        "P2055","整数平方根",["算法","二分查找"],
        cases=cases,
        desc_en="Given a non-negative integer n, compute floor(sqrt(n)).",
        input_en="One non-negative integer n (n <= 10^9).",
        output_en="floor(sqrt(n)).",
        desc_zh="给定非负整数n，求floor(sqrt(n))，即整数平方根(下取整)。",
        input_zh="一个非负整数n(n不超过10^9)。",
        output_zh="floor(sqrt(n))的值。",
        py="""# P2055 整数平方根
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    n=int(d[0])                      # 读取 n
    lo,hi=0,n                         # 在 [0,n] 中二分最大的 r 满足 r*r<=n
    while lo<hi:
        mid=(lo+hi+1)//2              # 上取整避免死循环
        if mid*mid<=n:                # mid 可行，尝试更大
            lo=mid
        else:                         # mid 过大
            hi=mid-1
    print(lo)                         # lo 即为 floor(sqrt(n))
main()
""",
        cpp="""// P2055 整数平方根
#include <iostream>
using namespace std;
int main() {
    long long n;
    if(!(cin>>n)) return 0;          // 读取 n
    long long lo=0,hi=n;             // 在 [0,n] 中二分最大的 r 满足 r*r<=n
    while(lo<hi){
        long long mid=(lo+hi+1)/2;   // 上取整避免死循环
        if(mid*mid<=n) lo=mid;       // mid 可行，尝试更大
        else hi=mid-1;               // mid 过大
    }
    cout<<lo<<endl;                  // lo 即为 floor(sqrt(n))
    return 0;
}
""",
        java="""// P2055 整数平方根
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextLong()) return;
        long n=sc.nextLong();            // 读取 n
        long lo=0,hi=n;                  // 在 [0,n] 中二分最大的 r 满足 r*r<=n
        while(lo<hi){
            long mid=(lo+hi+1)/2;        // 上取整避免死循环
            if(mid*mid<=n) lo=mid;       // mid 可行，尝试更大
            else hi=mid-1;               // mid 过大
        }
        System.out.println(lo);          // lo 即为 floor(sqrt(n))
    }
}
""",
    )
