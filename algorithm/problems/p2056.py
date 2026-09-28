# -*- coding: utf-8 -*-
"""P2056 第k小(二分答案)"""
from generate import make_problem

def build():
    # (n, k, L, R, 数组)；L=min, R=max，二分答案求第 k 小
    data=[(5,2,1,5,[3,1,4,1,5]),
          (5,3,1,5,[3,1,4,1,5]),
          (1,1,7,7,[7]),
          (6,1,5,5,[5,5,5,5,5,5]),
          (6,6,5,5,[5,5,5,5,5,5]),
          (8,4,10,80,[10,20,30,40,50,60,70,80]),
          (8,5,10,80,[10,20,30,40,50,60,70,80]),
          (10,7,1,5,[1,2,2,3,3,3,4,4,5,5]),
          (4,2,100,400,[100,200,300,400]),
          (7,1,3,9,[9,8,7,6,5,4,3])]
    cases=[]
    for n,k,L,R,a in data:
        inp=f"{n} {k}\n{L} {R}\n{' '.join(map(str,a))}\n"
        # 参考答案：排序后第 k 小(从1开始)
        out=sorted(a)[k-1]
        cases.append((inp,f"{out}\n"))
    return make_problem(
        "P2056","第k小",["算法","二分查找"],
        cases=cases,
        desc_en="Given n integers and k, and the value range [L, R], find the k-th smallest element.",
        input_en="First line: n and k. Second line: L and R (the value range). Third line: n integers.",
        output_en="The k-th smallest element.",
        desc_zh="给定n个数和k及值域[L,R]，求第k小的数。",
        input_zh="第一行两个整数n和k。第二行两个整数L和R表示值域。第三行n个整数。",
        output_zh="第k小的数。",
        py="""# P2056 第k小(二分答案)
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    it=iter(d)
    n=int(next(it)); k=int(next(it))
    L=int(next(it)); R=int(next(it))   # 值域 [L,R]
    a=[int(next(it)) for _ in range(n)]
    # 二分答案：找最小的 v 使 a 中 <=v 的个数 >=k
    lo,hi=L,R
    while lo<hi:
        mid=(lo+hi)//2
        cnt=sum(1 for v in a if v<=mid)  # 统计 <=mid 的个数
        if cnt>=k:                     # 个数足够，答案 <=mid
            hi=mid
        else:                          # 个数不足，答案 >mid
            lo=mid+1
    print(lo)                          # lo 即第 k 小
main()
""",
        cpp="""// P2056 第k小(二分答案)
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n,k;
    if(!(cin>>n>>k)) return 0;
    int L,R; cin>>L>>R;                // 值域 [L,R]
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    int lo=L,hi=R;                     // 二分答案
    while(lo<hi){
        int mid=(lo+hi)/2;
        int cnt=0;
        for(int i=0;i<n;i++) if(a[i]<=mid) cnt++;  // 统计 <=mid 的个数
        if(cnt>=k) hi=mid;            // 个数足够，答案 <=mid
        else lo=mid+1;                // 个数不足，答案 >mid
    }
    cout<<lo<<endl;                   // lo 即第 k 小
    return 0;
}
""",
        java="""// P2056 第k小(二分答案)
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt(),k=sc.nextInt();
        int L=sc.nextInt(),R=sc.nextInt();   // 值域 [L,R]
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();
        int lo=L,hi=R;                       // 二分答案
        while(lo<hi){
            int mid=(lo+hi)/2;
            int cnt=0;
            for(int i=0;i<n;i++) if(a[i]<=mid) cnt++;  // 统计 <=mid 的个数
            if(cnt>=k) hi=mid;              // 个数足够，答案 <=mid
            else lo=mid+1;                  // 个数不足，答案 >mid
        }
        System.out.println(lo);             // lo 即第 k 小
    }
}
""",
    )
