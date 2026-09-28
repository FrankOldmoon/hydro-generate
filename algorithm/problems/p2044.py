# -*- coding: utf-8 -*-
"""P2044 直线分割平面"""
from generate import make_problem

def build():
    data=[1,2,3,4,5,6,7,8,10,20]
    cases=[]
    for n in data:
        ans=1+n+n*(n-1)//2
        cases.append((f"{n}\n", f"{ans}\n"))
    return make_problem(
        "P2044","直线分割平面",["算法","递推递归"],
        cases=cases,
        desc_en="n lines are drawn in the plane. Find the maximum number of regions they can divide the plane into.",
        input_en="One integer n.",
        output_en="The maximum number of regions.",
        desc_zh="求n条直线最多能把平面分成多少个区域。",
        input_zh="一个整数n。",
        output_zh="最多区域数。",
        py="""# P2044 直线分割平面
n = int(input())                      # 读取直线数 n
ans = 1 + n + n * (n - 1) // 2        # 最多区域数 = 1+n+n(n-1)/2
print(ans)                            # 输出区域数
""",
        cpp="""// P2044 直线分割平面
#include <iostream>
using namespace std;
int main() {
    long long n;
    cin >> n;                                  // 读取直线数 n
    long long ans = 1 + n + n * (n - 1) / 2;   // 最多区域数 = 1+n+n(n-1)/2
    cout << ans << endl;                       // 输出区域数
    return 0;
}
""",
        java="""// P2044 直线分割平面
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();                  // 读取直线数 n
        long ans = 1 + n + n * (n - 1) / 2;      // 最多区域数 = 1+n+n(n-1)/2
        System.out.println(ans);                 // 输出区域数
    }
}
""",
    )
