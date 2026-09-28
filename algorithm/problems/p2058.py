# -*- coding: utf-8 -*-
"""P2058 数列分段"""
from generate import make_problem

def build():
    # (n, m, 数组)，分成 m 个连续段，求最大段和的最小值
    data=[(5,2,[1,2,3,4,5]),
          (4,2,[4,2,4,5]),
          (1,1,[7]),
          (3,3,[1,2,3]),
          (3,1,[1,2,3]),
          (6,3,[1,1,1,1,1,1]),
          (5,5,[10,20,30,40,50]),
          (5,1,[10,20,30,40,50]),
          (8,3,[2,3,4,1,5,6,2,1]),
          (4,2,[7,2,5,6])]
    cases=[]
    for n,m,a in data:
        inp=f"{n} {m}\n{' '.join(map(str,a))}\n"
        # 参考答案：暴力枚举最大段和 X，贪心判定最少段数是否 <=m
        def feas(X):
            seg=1; cur=0
            for v in a:
                if cur+v<=X:
                    cur+=v
                else:
                    seg+=1; cur=v
            return seg<=m
        ans=sum(a)
        for X in range(max(a), sum(a)+1):
            if feas(X):
                ans=X
                break
        cases.append((inp,f"{ans}\n"))
    return make_problem(
        "P2058","数列分段",["算法","二分查找"],
        cases=cases,
        desc_en="Given n positive integers and an integer m, split them into m consecutive segments. Minimize the maximum segment sum.",
        input_en="First line: n and m. Second line: n positive integers.",
        output_en="The minimum possible value of the maximum segment sum.",
        desc_zh="给定n个正整数和段数m，将其分成m个连续段，求最大段和的最小值。",
        input_zh="第一行两个整数n和m。第二行n个正整数。",
        output_zh="最大段和的最小值。",
        py="""# P2058 数列分段
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    it=iter(d)
    n=int(next(it)); m=int(next(it))
    a=[int(next(it)) for _ in range(n)]
    # 判定：限制每段和不超过 X 时，贪心求最少段数是否 <=m
    def feas(X):
        seg=1; cur=0
        for v in a:
            if cur+v<=X:
                cur+=v
            else:
                seg+=1; cur=v
        return seg<=m
    lo,hi=max(a),sum(a)              # 二分最大段和
    while lo<hi:
        mid=(lo+hi)//2
        if feas(mid):                # 可行，尝试更小的最大段和
            hi=mid
        else:                        # 不可行，增大
            lo=mid+1
    print(lo)
main()
""",
        cpp="""// P2058 数列分段
#include <iostream>
#include <vector>
using namespace std;
int n,m;
vector<int> a;
bool feas(long long X){             // 限制每段和不超过 X 时贪心求最少段数
    long long seg=1,cur=0;
    for(int i=0;i<n;i++){
        if(cur+a[i]<=X) cur+=a[i];
        else { seg++; cur=a[i]; }
    }
    return seg<=m;
}
int main() {
    if(!(cin>>n>>m)) return 0;
    a.resize(n);
    long long s=0,mx=0;
    for(int i=0;i<n;i++){ cin>>a[i]; s+=a[i]; if(a[i]>mx) mx=a[i]; }
    long long lo=mx,hi=s;            // 二分最大段和
    while(lo<hi){
        long long mid=(lo+hi)/2;
        if(feas(mid)) hi=mid;        // 可行，尝试更小
        else lo=mid+1;               // 不可行，增大
    }
    cout<<lo<<endl;
    return 0;
}
""",
        java="""// P2058 数列分段
import java.util.Scanner;
public class Main {
    static int n,m;
    static int[] a;
    static boolean feas(long X){     // 限制每段和不超过 X 时贪心求最少段数
        long seg=1,cur=0;
        for(int i=0;i<n;i++){
            if(cur+a[i]<=X) cur+=a[i];
            else { seg++; cur=a[i]; }
        }
        return seg<=m;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        n=sc.nextInt(); m=sc.nextInt();
        a=new int[n];
        long s=0,mx=0;
        for(int i=0;i<n;i++){ a[i]=sc.nextInt(); s+=a[i]; if(a[i]>mx) mx=a[i]; }
        long lo=mx,hi=s;              // 二分最大段和
        while(lo<hi){
            long mid=(lo+hi)/2;
            if(feas(mid)) hi=mid;     // 可行，尝试更小
            else lo=mid+1;            // 不可行，增大
        }
        System.out.println(lo);
    }
}
""",
    )
