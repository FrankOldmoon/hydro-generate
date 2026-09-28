# -*- coding: utf-8 -*-
"""P2060 借教室"""
from generate import make_problem

def build():
    # (n, m, 每天容量r, 订单列表[(s,t,d)])，二分求最多满足前几个订单
    data=[(3,3,[10,10,10],[(1,3,4),(1,3,4),(1,3,4)]),
          (3,2,[5,5,5],[(1,2,3),(2,3,3)]),
          (4,2,[2,2,2,2],[(1,4,2),(1,4,1)]),
          (5,1,[1,1,1,1,1],[(1,5,1)]),
          (5,1,[1,1,1,1,1],[(1,5,2)]),
          (4,4,[3,3,3,3],[(1,2,1),(3,4,1),(1,4,1),(2,3,1)]),
          (3,3,[2,2,2],[(1,1,2),(2,2,2),(3,3,2)]),
          (3,3,[2,2,2],[(1,1,2),(1,1,1),(1,1,1)]),
          (10,5,[5]*10,[(1,5,2),(3,8,2),(5,10,2),(1,10,1),(2,4,3)]),
          (6,4,[4,4,4,4,4,4],[(1,3,3),(4,6,3),(1,6,1),(2,5,2)])]
    cases=[]
    for n,m,r,orders in data:
        inp=f"{n} {m}\n{' '.join(map(str,r))}\n"+"".join(f"{s} {t} {dd}\n" for s,t,dd in orders)
        # 参考答案：判定前 k 个订单是否可满足(差分数组)，取最大可行 k
        def check(k):
            diff=[0]*(n+2)
            for j in range(k):
                s,t,dd=orders[j]
                diff[s]+=dd
                diff[t+1]-=dd
            cur=0
            for i in range(1,n+1):
                cur+=diff[i]
                if cur>r[i-1]:
                    return False
            return True
        ans=0
        for k in range(m+1):
            if check(k):
                ans=k
        cases.append((inp,f"{ans}\n"))
    return make_problem(
        "P2060","借教室",["算法","二分查找"],
        cases=cases,
        desc_en="There are n days, day i can lend r_i units. There are m orders; order j needs d_j units each day from day s_j to day t_j. Orders are processed in order. Find the maximum number of orders (a prefix) that can all be satisfied.",
        input_en="First line: n and m. Second line: n integers r_i. Next m lines: each s_j t_j d_j.",
        output_en="The maximum k such that the first k orders can all be satisfied (0 if even the first fails).",
        desc_zh="n天每天可借r个，m个订单按顺序各借若干天，求最多能满足前几个订单。",
        input_zh="第一行两个整数n和m。第二行n个整数表示每天可借数量r_i。接下来m行每行三个整数s_j t_j d_j表示订单。",
        output_zh="最多能满足前几个订单(从0到m)。",
        py="""# P2060 借教室
import sys
def main():
    d=sys.stdin.read().split()
    if not d:
        return
    it=iter(d)
    n=int(next(it)); m=int(next(it))
    r=[int(next(it)) for _ in range(n)]
    orders=[]
    for _ in range(m):
        s=int(next(it)); t=int(next(it)); dd=int(next(it))
        orders.append((s,t,dd))
    # 判定前 k 个订单是否可满足：差分数组统计每天需求
    def check(k):
        diff=[0]*(n+2)
        for j in range(k):
            s,t,dd=orders[j]
            diff[s]+=dd
            diff[t+1]-=dd
        cur=0
        for i in range(1,n+1):
            cur+=diff[i]
            if cur>r[i-1]:           # 某天需求超过容量
                return False
        return True
    lo,hi=0,m                         # 二分最大的可行前缀长度
    while lo<hi:
        mid=(lo+hi+1)//2              # 上取整避免死循环
        if check(mid):                # 前 mid 个可行，尝试更多
            lo=mid
        else:                         # 不可行，减少
            hi=mid-1
    print(lo)
main()
""",
        cpp="""// P2060 借教室
#include <iostream>
#include <vector>
using namespace std;
int n,m;
vector<int> r;
vector<pair<int,pair<int,int>>> ord;  // (s,(t,d))
bool check(int k){                    // 差分数组判定前 k 个订单
    vector<long long> diff(n+2,0);
    for(int j=0;j<k;j++){
        int s=ord[j].first,t=ord[j].second.first,dd=ord[j].second.second;
        diff[s]+=dd; diff[t+1]-=dd;
    }
    long long cur=0;
    for(int i=1;i<=n;i++){
        cur+=diff[i];
        if(cur>r[i-1]) return false;  // 某天需求超过容量
    }
    return true;
}
int main() {
    if(!(cin>>n>>m)) return 0;
    r.resize(n);
    for(int i=0;i<n;i++) cin>>r[i];
    ord.resize(m);
    for(int j=0;j<m;j++){
        int s,t,dd; cin>>s>>t>>dd;
        ord[j]=make_pair(s,make_pair(t,dd));
    }
    int lo=0,hi=m;                    // 二分最大的可行前缀长度
    while(lo<hi){
        int mid=(lo+hi+1)/2;          // 上取整避免死循环
        if(check(mid)) lo=mid;        // 可行，尝试更多
        else hi=mid-1;                // 不可行，减少
    }
    cout<<lo<<endl;
    return 0;
}
""",
        java="""// P2060 借教室
import java.util.Scanner;
public class Main {
    static int n,m;
    static int[] r;
    static int[][] ord;               // ord[j]={s,t,d}
    static boolean check(int k){      // 差分数组判定前 k 个订单
        long[] diff=new long[n+2];
        for(int j=0;j<k;j++){
            int s=ord[j][0],t=ord[j][1],dd=ord[j][2];
            diff[s]+=dd; diff[t+1]-=dd;
        }
        long cur=0;
        for(int i=1;i<=n;i++){
            cur+=diff[i];
            if(cur>r[i-1]) return false;  // 某天需求超过容量
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        n=sc.nextInt(); m=sc.nextInt();
        r=new int[n];
        for(int i=0;i<n;i++) r[i]=sc.nextInt();
        ord=new int[m][3];
        for(int j=0;j<m;j++){
            ord[j][0]=sc.nextInt();
            ord[j][1]=sc.nextInt();
            ord[j][2]=sc.nextInt();
        }
        int lo=0,hi=m;                // 二分最大的可行前缀长度
        while(lo<hi){
            int mid=(lo+hi+1)/2;      // 上取整避免死循环
            if(check(mid)) lo=mid;    // 可行，尝试更多
            else hi=mid-1;            // 不可行，减少
        }
        System.out.println(lo);
    }
}
""",
    )
