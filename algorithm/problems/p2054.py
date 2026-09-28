# -*- coding: utf-8 -*-
"""P2054 查找插入位置"""
from generate import make_problem

def build():
    # (n, 升序数组, x)，求 x 应插入的位置(从1)，使插入后仍升序(即下界)
    data=[(5,[1,3,5,7,9],5),
          (5,[1,3,5,7,9],6),
          (5,[1,3,5,7,9],1),
          (5,[1,3,5,7,9],10),
          (5,[1,3,5,7,9],0),
          (4,[2,4,6,8],3),
          (4,[2,4,6,8],8),
          (1,[5],5),
          (1,[5],9),
          (7,[10,20,30,40,50,60,70],25)]
    cases=[]
    for n,a,x in data:
        inp=f"{n}\n{' '.join(map(str,a))}\n{x}\n"
        # 参考答案：第一个 >=x 的下标(0-based)，无则 n，插入位置=下标+1
        idx=n
        for i,v in enumerate(a):
            if v>=x:
                idx=i
                break
        cases.append((inp,f"{idx+1}\n"))
    return make_problem(
        "P2054","查找插入位置",["算法","二分查找"],
        cases=cases,
        desc_en="Given an array sorted in ascending order and an integer x, find the position (1-indexed) where x should be inserted so that the array remains sorted.",
        input_en="First line: integer n. Second line: n integers in ascending order. Third line: integer x.",
        output_en="The 1-indexed insertion position of x (in range 1..n+1).",
        desc_zh="给定升序数组，查找x应插入的位置(从1)，使插入后数组仍保持升序。",
        input_zh="第一行一个整数n。第二行n个升序整数。第三行一个整数x。",
        output_zh="x应插入的位置(从1开始，取值1到n+1)。",
        py="""# P2054 查找插入位置
import sys
def main():
    d=sys.stdin.read().split()        # 读取全部 token
    if not d:
        return
    it=iter(d)
    n=int(next(it))                   # 元素个数
    a=[int(next(it)) for _ in range(n)]  # 升序数组
    x=int(next(it))                   # 待插入的 x
    lo,hi=0,n                         # 在 [0,n] 中二分下界
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid]>=x:                 # 插入点在 mid 或左侧
            hi=mid
        else:                         # 插入点在 mid 右侧
            lo=mid+1
    print(lo+1)                       # 插入位置=下标+1
main()
""",
        cpp="""// P2054 查找插入位置
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    if(!(cin>>n)) return 0;           // 元素个数
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];   // 升序数组
    int x; cin>>x;                    // 待插入的 x
    int lo=0,hi=n;                    // 在 [0,n] 中二分下界
    while(lo<hi){
        int mid=(lo+hi)/2;
        if(a[mid]>=x) hi=mid;         // 插入点在 mid 或左侧
        else lo=mid+1;                // 插入点在 mid 右侧
    }
    cout<<lo+1<<endl;                 // 插入位置=下标+1
    return 0;
}
""",
        java="""// P2054 查找插入位置
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt();               // 元素个数
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();  // 升序数组
        int x=sc.nextInt();               // 待插入的 x
        int lo=0,hi=n;                    // 在 [0,n] 中二分下界
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(a[mid]>=x) hi=mid;         // 插入点在 mid 或左侧
            else lo=mid+1;                // 插入点在 mid 右侧
        }
        System.out.println(lo+1);         // 插入位置=下标+1
    }
}
""",
    )
