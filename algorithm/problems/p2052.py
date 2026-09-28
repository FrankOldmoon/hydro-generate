# -*- coding: utf-8 -*-
"""P2052 第一个大于等于x"""
from generate import make_problem

def build():
    # (n, 升序数组, x)，求第一个 >=x 的位置(从1)，不存在输出 n+1
    data=[(5,[1,3,5,7,9],5),
          (5,[1,3,5,7,9],6),
          (5,[1,3,5,7,9],1),
          (5,[1,3,5,7,9],10),
          (5,[1,3,5,7,9],0),
          (6,[1,1,1,1,1,1],1),
          (6,[1,1,1,1,1,1],2),
          (1,[5],3),
          (1,[5],8),
          (8,[2,2,4,4,6,6,8,8],5)]
    cases=[]
    for n,a,x in data:
        inp=f"{n}\n{' '.join(map(str,a))}\n{x}\n"
        # 参考答案：第一个 >=x 的下标(0-based)，无则 n，位置=下标+1
        idx=n
        for i,v in enumerate(a):
            if v>=x:
                idx=i
                break
        cases.append((inp,f"{idx+1}\n"))
    return make_problem(
        "P2052","第一个大于等于x",["算法","二分查找"],
        cases=cases,
        desc_en="Given an array sorted in ascending order and an integer x, find the position (1-indexed) of the first element not less than x. If no such element exists, output n+1.",
        input_en="First line: integer n. Second line: n integers in ascending order. Third line: integer x.",
        output_en="The 1-indexed position of the first element >= x, or n+1 if none.",
        desc_zh="给定升序数组，查找第一个大于等于x的元素的位置(从1)，不存在输出n+1。",
        input_zh="第一行一个整数n。第二行n个升序整数。第三行一个整数x。",
        output_zh="第一个大于等于x的元素的位置(从1)，不存在则输出n+1。",
        py="""# P2052 第一个大于等于x
import sys
def main():
    d=sys.stdin.read().split()        # 读取全部 token
    if not d:
        return
    it=iter(d)
    n=int(next(it))                   # 元素个数
    a=[int(next(it)) for _ in range(n)]  # 升序数组
    x=int(next(it))                   # 目标值 x
    lo,hi=0,n                         # 在 [0,n] 中二分下界
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid]>=x:                 # mid 满足条件，答案在 mid 或左侧
            hi=mid
        else:                         # mid 不满足，答案在右侧
            lo=mid+1
    print(lo+1)                       # lo 为第一个 >=x 的下标，位置=下标+1
main()
""",
        cpp="""// P2052 第一个大于等于x
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    if(!(cin>>n)) return 0;           // 元素个数
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];   // 升序数组
    int x; cin>>x;                    // 目标值 x
    int lo=0,hi=n;                    // 在 [0,n] 中二分下界
    while(lo<hi){
        int mid=(lo+hi)/2;
        if(a[mid]>=x) hi=mid;         // mid 满足，答案在 mid 或左侧
        else lo=mid+1;                // mid 不满足，答案在右侧
    }
    cout<<lo+1<<endl;                 // 位置=下标+1，无则 n+1
    return 0;
}
""",
        java="""// P2052 第一个大于等于x
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt();               // 元素个数
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();  // 升序数组
        int x=sc.nextInt();               // 目标值 x
        int lo=0,hi=n;                    // 在 [0,n] 中二分下界
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(a[mid]>=x) hi=mid;         // mid 满足，答案在 mid 或左侧
            else lo=mid+1;                // mid 不满足，答案在右侧
        }
        System.out.println(lo+1);         // 位置=下标+1，无则 n+1
    }
}
""",
    )
