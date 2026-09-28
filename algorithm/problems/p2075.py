# -*- coding: utf-8 -*-
"""P2075 最大子段和"""
from generate import make_problem


def kadane(a):
    cur = a[0]
    best = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def build():
    data = [
        [1, 2, 3, 4, 5],
        [-1, -2, -3],
        [5, 4, -1, 7, 8],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [-5],
        [2, -1, 2, -1, 2],
        [3, -2, 3, -2, 3],
        [10, -1, 10, -1, 10],
        [1, -2, 3, -4, 5, -6, 7],
    ]
    cases = []
    for a in data:
        inp = f"{len(a)}\n" + " ".join(map(str, a)) + "\n"
        cases.append((inp, f"{kadane(a)}\n"))
    return make_problem(
        "P2075", "最大子段和", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given n integers, find the maximum sum of a contiguous subarray "
                "(must be non-empty).",
        input_en="The first line contains n (1 <= n <= 100000). The second line "
                 "contains n integers separated by spaces.",
        output_en="The maximum contiguous subarray sum.",
        desc_zh="给定n个整数，求其连续子段（非空）的最大和。",
        input_zh="第一行一个整数n（1 <= n <= 100000），第二行n个空格分隔的整数。",
        output_zh="连续子段的最大和。",
        py="""# P2075 最大子段和（线性DP / Kadane）
n = int(input())                      # 元素个数 n
a = list(map(int, input().split()))   # 读取序列
cur = a[0]                            # 以当前元素结尾的最大子段和
best = a[0]                           # 全局最优
for x in a[1:]:
    cur = max(x, cur + x)             # 要么另起，要么接续
    best = max(best, cur)             # 更新全局最优
print(best)                           # 输出最大子段和
""",
        cpp="""// P2075 最大子段和（线性DP / Kadane）
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                         // 元素个数 n
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    long long cur = a[0];             // 以当前元素结尾的最大子段和
    long long best = a[0];            // 全局最优
    for (int i = 1; i < n; i++) {
        cur = max(a[i], cur + a[i]);  // 要么另起，要么接续
        best = max(best, cur);        // 更新全局最优
    }
    cout << best << endl;             // 输出最大子段和
    return 0;
}
""",
        java="""// P2075 最大子段和（线性DP / Kadane）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();         // 元素个数 n
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();
        long cur = a[0];              // 以当前元素结尾的最大子段和
        long best = a[0];             // 全局最优
        for (int i = 1; i < n; i++) {
            cur = Math.max(a[i], cur + a[i]);  // 要么另起，要么接续
            best = Math.max(best, cur);        // 更新全局最优
        }
        System.out.println(best);     // 输出最大子段和
    }
}
""",
    )
