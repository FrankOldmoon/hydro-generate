# -*- coding: utf-8 -*-
"""P2059 跳石头"""
from generate import make_problem

def build():
    # (L, n, m, 石头位置列表，已升序)，求最短跳跃距离的最大值
    data=[(10,2,0,[3,6]),
          (10,2,1,[3,6]),
          (25,5,2,[2,11,14,17,21]),
          (5,0,0,[]),
          (100,3,3,[1,2,3]),
          (10,4,1,[1,2,3,4]),
          (20,5,2,[2,7,10,15,18]),
          (12,3,1,[4,5,8]),
          (8,2,0,[3,5]),
          (50,6,3,[5,10,20,25,30,40])]
    cases=[]
    for L,n,m,rocks in data:
        inp=f"{L} {n} {m}\n{' '.join(map(str,rocks))}\n"
        # 参考答案：从大到小枚举最短跳跃距离 d，贪心判定需移走石头数 <=m
        def feas(d):
            prev=0; removed=0
            for p in rocks:
                if p-prev<d:
                    removed+=1
                else:
                    prev=p
            if L-prev<d:
                removed+=1
            return removed<=m
        ans=1
        for d in range(L,0,-1):
            if feas(d):
                ans=d
                break
        cases.append((inp,f"{ans}\n"))
    return make_problem(
        "P2059","跳石头",["算法","二分查找"],
        cases=cases,
        desc_en="The start and end are separated by distance L. There are n rocks in between (sorted positions). You may remove at most m rocks. Maximize the minimum jumping distance.",
        input_en="First line: L, n, m. Second line: n integers, the sorted positions of rocks (strictly between 0 and L).",
        output_en="The maximum possible value of the minimum jumping distance.",
        desc_zh="起点到终点距离L，中间有n块石头(位置升序)，最多移走m块，求最短跳跃距离的最大值。",
        input_zh="第一行三个整数L、n、m。第二行n个升序整数表示石头位置(严格在0和L之间)。",
        output_zh="最短跳跃距离的最大值。",
        py="""# P2059 跳石头
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    it=iter(d)
    L=int(next(it)); n=int(next(it)); m=int(next(it))
    rocks=[int(next(it)) for _ in range(n)]
    # 判定：最短跳跃距离为 dist 时需移走多少块石头
    def feas(dist):
        prev=0; removed=0
        for p in rocks:
            if p-prev<dist:        # 间距不足，移走当前石头
                removed+=1
            else:
                prev=p
        if L-prev<dist:            # 终点前间距不足
            removed+=1
        return removed<=m
    lo,hi=1,L                       # 二分最短跳跃距离
    while lo<hi:
        mid=(lo+hi+1)//2            # 上取整避免死循环
        if feas(mid):               # 可行，尝试更大的距离
            lo=mid
        else:                       # 不可行，减小
            hi=mid-1
    print(lo)
main()
""",
        cpp="""// P2059 跳石头
#include <iostream>
#include <vector>
using namespace std;
int L,n,m;
vector<int> rocks;
bool feas(int dist){                // 最短跳跃距离为 dist 时需移走石头数
    int prev=0,removed=0;
    for(int i=0;i<n;i++){
        if(rocks[i]-prev<dist) removed++;  // 间距不足，移走
        else prev=rocks[i];
    }
    if(L-prev<dist) removed++;      // 终点前间距不足
    return removed<=m;
}
int main() {
    if(!(cin>>L>>n>>m)) return 0;
    rocks.resize(n);
    for(int i=0;i<n;i++) cin>>rocks[i];
    int lo=1,hi=L;                  // 二分最短跳跃距离
    while(lo<hi){
        int mid=(lo+hi+1)/2;        // 上取整避免死循环
        if(feas(mid)) lo=mid;       // 可行，尝试更大
        else hi=mid-1;              // 不可行，减小
    }
    cout<<lo<<endl;
    return 0;
}
""",
        java="""// P2059 跳石头
import java.util.Scanner;
public class Main {
    static int L,n,m;
    static int[] rocks;
    static boolean feas(int dist){  // 最短跳跃距离为 dist 时需移走石头数
        int prev=0,removed=0;
        for(int i=0;i<n;i++){
            if(rocks[i]-prev<dist) removed++;  // 间距不足，移走
            else prev=rocks[i];
        }
        if(L-prev<dist) removed++;  // 终点前间距不足
        return removed<=m;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        L=sc.nextInt(); n=sc.nextInt(); m=sc.nextInt();
        rocks=new int[n];
        for(int i=0;i<n;i++) rocks[i]=sc.nextInt();
        int lo=1,hi=L;              // 二分最短跳跃距离
        while(lo<hi){
            int mid=(lo+hi+1)/2;    // 上取整避免死循环
            if(feas(mid)) lo=mid;   // 可行，尝试更大
            else hi=mid-1;          // 不可行，减小
        }
        System.out.println(lo);
    }
}
""",
    )
