# -*- coding: utf-8 -*-
"""P2053 最后一个小于等于x"""
from generate import make_problem

def build():
    # (n, 升序数组, x)，求最后一个 <=x 的位置(从1)，不存在输出 0
    data=[(5,[1,3,5,7,9],5),
          (5,[1,3,5,7,9],6),
          (5,[1,3,5,7,9],0),
          (5,[1,3,5,7,9],9),
          (5,[1,3,5,7,9],10),
          (6,[1,1,1,1,1,1],1),
          (6,[1,1,1,1,1,1],0),
          (1,[5],5),
          (1,[5],4),
          (8,[2,2,4,4,6,6,8,8],5)]
    cases=[]
    for n,a,x in data:
        inp=f"{n}\n{' '.join(map(str,a))}\n{x}\n"
        # 参考答案：统计 <=x 的元素个数 cnt；位置=cnt，cnt=0 则无(输出0)
        cnt=sum(1 for v in a if v<=x)
        cases.append((inp,f"{cnt}\n"))
    return make_problem(
        "P2053","最后一个小于等于x",["算法","二分查找"],
        cases=cases,
        desc_en="Given an array sorted in ascending order and an integer x, find the position (1-indexed) of the last element not greater than x. If no such element exists, output 0.",
        input_en="First line: integer n. Second line: n integers in ascending order. Third line: integer x.",
        output_en="The 1-indexed position of the last element <= x, or 0 if none.",
        desc_zh="给定升序数组，查找最后一个小于等于x的元素的位置(从1)，不存在输出0。",
        input_zh="第一行一个整数n。第二行n个升序整数。第三行一个整数x。",
        output_zh="最后一个小于等于x的元素的位置(从1)，不存在则输出0。",
        py="""# P2053 最后一个小于等于x
import sys
def main():
    d=sys.stdin.read().split()        # 读取全部 token
    if not d:
        return
    it=iter(d)
    n=int(next(it))                   # 元素个数
    a=[int(next(it)) for _ in range(n)]  # 升序数组
    x=int(next(it))                   # 目标值 x
    lo,hi=0,n                         # 在 [0,n] 中二分
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid]<=x:                 # mid 满足 <=x，答案在 mid 右侧
            lo=mid+1
        else:                         # mid 不满足，答案在 mid 或左侧
            hi=mid
    # lo 为第一个 >x 的下标，即 <=x 的元素个数，恰好为最后一个 <=x 的位置
    print(lo)
main()
""",
        cpp="""// P2053 最后一个小于等于x
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    if(!(cin>>n)) return 0;           // 元素个数
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];   // 升序数组
    int x; cin>>x;                    // 目标值 x
    int lo=0,hi=n;                    // 在 [0,n] 中二分
    while(lo<hi){
        int mid=(lo+hi)/2;
        if(a[mid]<=x) lo=mid+1;       // mid 满足 <=x，答案在 mid 右侧
        else hi=mid;                  // mid 不满足，答案在 mid 或左侧
    }
    // lo 为 <=x 的元素个数，恰好为最后一个 <=x 的位置(从1)，0 表示无
    cout<<lo<<endl;
    return 0;
}
""",
        java="""// P2053 最后一个小于等于x
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt();               // 元素个数
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();  // 升序数组
        int x=sc.nextInt();               // 目标值 x
        int lo=0,hi=n;                    // 在 [0,n] 中二分
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(a[mid]<=x) lo=mid+1;       // mid 满足 <=x，答案在 mid 右侧
            else hi=mid;                  // mid 不满足，答案在 mid 或左侧
        }
        // lo 为 <=x 的元素个数，即最后一个 <=x 的位置(从1)，0 表示无
        System.out.println(lo);
    }
}
""",
    )
