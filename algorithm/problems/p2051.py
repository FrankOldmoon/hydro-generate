# -*- coding: utf-8 -*-
"""P2051 有序查找"""
from generate import make_problem

def build():
    # (n, 升序数组, x)，数组元素互异保证位置唯一
    data=[(5,[1,3,5,7,9],5),
          (6,[1,2,3,4,5,6],1),
          (6,[1,2,3,4,5,6],6),
          (5,[2,4,6,8,10],5),
          (1,[7],7),
          (1,[7],3),
          (10,[1,4,7,10,13,16,19,22,25,28],22),
          (7,[10,20,30,40,50,60,70],65),
          (4,[100,200,300,400],400),
          (8,[3,6,9,12,15,18,21,24],15)]
    cases=[]
    for n,a,x in data:
        inp=f"{n}\n{' '.join(map(str,a))}\n{x}\n"
        # 参考答案：x 在数组中则输出位置(从1)，否则输出0
        idx=a.index(x)+1 if x in a else 0
        cases.append((inp,f"{idx}\n"))
    return make_problem(
        "P2051","有序查找",["算法","二分查找"],
        cases=cases,
        desc_en="Given an array sorted in ascending order and an integer x, find the position of x (1-indexed). Output 0 if x does not appear.",
        input_en="First line: integer n. Second line: n integers in ascending order. Third line: integer x.",
        output_en="The 1-indexed position of x, or 0 if not found.",
        desc_zh="给定升序数组和x，查找x的位置(从1)，不存在输出0。",
        input_zh="第一行一个整数n。第二行n个升序整数。第三行一个整数x。",
        output_zh="x的位置(从1开始)，不存在则输出0。",
        py="""# P2051 有序查找
import sys
def main():
    d=sys.stdin.read().split()        # 读取全部 token
    if not d:
        return
    it=iter(d)
    n=int(next(it))                   # 元素个数
    a=[int(next(it)) for _ in range(n)]  # 升序数组
    x=int(next(it))                   # 待查找的 x
    lo,hi=0,n-1
    pos=-1
    while lo<=hi:                     # 二分查找
        mid=(lo+hi)//2
        if a[mid]==x:                 # 找到 x
            pos=mid
            break
        elif a[mid]<x:                # 往右半区间找
            lo=mid+1
        else:                         # 往左半区间找
            hi=mid-1
    print(pos+1 if pos!=-1 else 0)    # 输出位置(从1)或0
main()
""",
        cpp="""// P2051 有序查找
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    if(!(cin>>n)) return 0;           // 读取元素个数
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];   // 升序数组
    int x; cin>>x;                    // 待查找的 x
    int lo=0,hi=n-1,pos=-1;
    while(lo<=hi){                    // 二分查找
        int mid=(lo+hi)/2;
        if(a[mid]==x){pos=mid;break;} // 找到 x
        else if(a[mid]<x) lo=mid+1;   // 往右半区间找
        else hi=mid-1;                // 往左半区间找
    }
    cout<<(pos==-1?0:pos+1)<<endl;    // 输出位置(从1)或0
    return 0;
}
""",
        java="""// P2051 有序查找
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n=sc.nextInt();               // 元素个数
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();  // 升序数组
        int x=sc.nextInt();               // 待查找的 x
        int lo=0,hi=n-1,pos=-1;
        while(lo<=hi){                    // 二分查找
            int mid=(lo+hi)/2;
            if(a[mid]==x){pos=mid;break;} // 找到 x
            else if(a[mid]<x) lo=mid+1;   // 往右半区间找
            else hi=mid-1;                // 往左半区间找
        }
        System.out.println(pos==-1?0:pos+1);  // 输出位置(从1)或0
    }
}
""",
    )
