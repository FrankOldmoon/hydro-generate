# -*- coding: utf-8 -*-
"""P2077 打家劫舍"""
from generate import make_problem


def rob(a):
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    prev2 = a[0]
    prev1 = max(a[0], a[1])
    for i in range(2, n):
        cur = max(prev1, prev2 + a[i])
        prev2 = prev1
        prev1 = cur
    return prev1


def build():
    data = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [1],
        [2, 1, 1, 2],
        [5, 3],
        [10, 1, 1, 10],
        [2, 4, 6, 8, 10],
        [1, 2, 3, 4, 5, 6],
        [0, 0, 0],
        [100, 1, 1, 100],
    ]
    cases = []
    for a in data:
        inp = f"{len(a)}\n" + " ".join(map(str, a)) + "\n"
        cases.append((inp, f"{rob(a)}\n"))
    return make_problem(
        "P2077", "打家劫舍", ["算法", "线性DP"],
        cases=cases,
        desc_en="There are n rooms in a row, each with some money. You cannot rob "
                "two adjacent rooms. Find the maximum amount of money you can rob.",
        input_en="The first line contains n (1 <= n <= 100000). The second line "
                 "contains n non-negative integers (the money in each room).",
        output_en="The maximum amount of money that can be robbed.",
        desc_zh="一排n个房间，每个房间有一定金钱，不能同时偷相邻两个房间，求能偷到的最大金钱。",
        input_zh="第一行一个整数n（1 <= n <= 100000），第二行n个非负整数表示每个房间的金钱。",
        output_zh="能偷到的最大金钱数。",
        py="""# P2077 打家劫舍（线性DP：f[i]=max(f[i-1], f[i-2]+a[i])）
n = int(input())                      # 房间数 n
a = list(map(int, input().split()))   # 每个房间的金钱
if n == 1:
    print(a[0])                       # 只有一个房间
else:
    prev2 = a[0]                      # f[0]
    prev1 = max(a[0], a[1])           # f[1]
    for i in range(2, n):
        cur = max(prev1, prev2 + a[i])  # 偷或不偷当前房间
        prev2 = prev1
        prev1 = cur
    print(prev1)                      # 输出最大金钱
""",
        cpp="""// P2077 打家劫舍（线性DP：f[i]=max(f[i-1], f[i-2]+a[i]）
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                         // 房间数 n
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    if (n == 1) {
        cout << a[0] << endl;         // 只有一个房间
        return 0;
    }
    long long prev2 = a[0];           // f[0]
    long long prev1 = max(a[0], a[1]); // f[1]
    for (int i = 2; i < n; i++) {
        long long cur = max(prev1, prev2 + a[i]);  // 偷或不偷当前房间
        prev2 = prev1;
        prev1 = cur;
    }
    cout << prev1 << endl;            // 输出最大金钱
    return 0;
}
""",
        java="""// P2077 打家劫舍（线性DP：f[i]=max(f[i-1], f[i-2]+a[i]）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();         // 房间数 n
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();
        if (n == 1) {
            System.out.println(a[0]); // 只有一个房间
            return;
        }
        long prev2 = a[0];            // f[0]
        long prev1 = Math.max(a[0], a[1]);  // f[1]
        for (int i = 2; i < n; i++) {
            long cur = Math.max(prev1, prev2 + a[i]);  // 偷或不偷当前房间
            prev2 = prev1;
            prev1 = cur;
        }
        System.out.println(prev1);    // 输出最大金钱
    }
}
""",
    )
