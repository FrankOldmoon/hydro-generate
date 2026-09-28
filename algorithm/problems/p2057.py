# -*- coding: utf-8 -*-
"""P2057 木材切割"""
from generate import make_problem

def build():
    # (n, M, 高度列表)，求最大锯片高度 h 使截得总长 >=M
    data=[(4,7,[10,10,10,10]),
          (3,15,[5,6,7]),
          (1,2,[10]),
          (5,100,[20,30,40,50,60]),
          (5,1,[1,2,3,4,5]),
          (6,50,[10,10,10,10,10,10]),
          (2,10,[100,100]),
          (4,8,[5,5,5,5]),
          (1,0,[5]),
          (5,200,[100,200,150,50,80])]
    cases=[]
    for n,M,h in data:
        inp=f"{n} {M}\n{' '.join(map(str,h))}\n"
        # 参考答案：从高到低枚举 h，找最大的使总截得 >=M
        mx=max(h)
        ans=0
        for hh in range(mx,-1,-1):
            s=sum(v-hh for v in h if v>hh)
            if s>=M:
                ans=hh
                break
        cases.append((inp,f"{ans}\n"))
    return make_problem(
        "P2057","木材切割",["算法","二分查找"],
        cases=cases,
        desc_en="There are n trees with given heights. Choose a saw blade height h; each tree yields max(0, height-h) wood. Find the maximum h such that the total wood obtained is at least M.",
        input_en="First line: n and M. Second line: n integers, the tree heights.",
        output_en="The maximum saw blade height h.",
        desc_zh="n棵树给定高度，锯片高度h时每棵树截得max(0,高度-h)，求使截得木材总长大于等于M的最大锯片高度。",
        input_zh="第一行两个整数n和M。第二行n个整数表示各树高度。",
        output_zh="最大的锯片高度h。",
        py="""# P2057 木材切割
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    it=iter(d)
    n=int(next(it)); M=int(next(it))
    a=[int(next(it)) for _ in range(n)]
    mx=max(a)
    # 二分最大 h，使 sum(max(0,a[i]-h)) >= M
    lo,hi=0,mx
    while lo<hi:
        mid=(lo+hi+1)//2              # 上取整避免死循环
        s=sum(v-mid for v in a if v>mid)  # 截得总长
        if s>=M:                      # 可行，尝试更高的 h
            lo=mid
        else:                         # 不可行，降低 h
            hi=mid-1
    print(lo)
main()
""",
        cpp="""// P2057 木材切割
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n; long long M;
    if(!(cin>>n>>M)) return 0;
    vector<long long> a(n);
    long long mx=0;
    for(int i=0;i<n;i++){ cin>>a[i]; if(a[i]>mx) mx=a[i]; }
    long long lo=0,hi=mx;             // 二分最大 h
    while(lo<hi){
        long long mid=(lo+hi+1)/2;    // 上取整避免死循环
        long long s=0;
        for(int i=0;i<n;i++) if(a[i]>mid) s+=a[i]-mid;  // 截得总长
        if(s>=M) lo=mid;              // 可行，尝试更高
        else hi=mid-1;                // 不可行，降低
    }
    cout<<lo<<endl;
    return 0;
}
""",
        java="""// P2057 木材切割
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt();
        long M=sc.nextLong();
        long[] a=new long[n];
        long mx=0;
        for(int i=0;i<n;i++){ a[i]=sc.nextLong(); if(a[i]>mx) mx=a[i]; }
        long lo=0,hi=mx;              // 二分最大 h
        while(lo<hi){
            long mid=(lo+hi+1)/2;     // 上取整避免死循环
            long s=0;
            for(int i=0;i<n;i++) if(a[i]>mid) s+=a[i]-mid;  // 截得总长
            if(s>=M) lo=mid;          // 可行，尝试更高
            else hi=mid-1;            // 不可行，降低
        }
        System.out.println(lo);
    }
}
""",
    )
