# -*- coding: utf-8 -*-
"""P2076 最长不下降子序列"""
from generate import make_problem


def lis_nd(a):
    n = len(a)
    if n == 0:
        return 0
    f = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] <= a[i] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1
    return max(f)


def build():
    data = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [1, 2, 2, 3, 3, 4],
        [3, 1, 4, 1, 5, 9, 2],
        [1, 3, 5, 2, 4, 6, 7, 8],
        [2, 2, 2, 3, 3, 2, 2],
        [10, 9, 2, 5, 3, 7, 101, 18, 4, 6],
        [1, 2, 3, 1, 2, 3, 4, 5],
        [7, 7, 7, 7, 7],
    ]
    cases = []
    for a in data:
        inp = f"{len(a)}\n" + " ".join(map(str, a)) + "\n"
        cases.append((inp, f"{lis_nd(a)}\n"))
    return make_problem(
        "P2076", "最长不下降子序列", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given a sequence of n integers, find the length of its longest "
                "non-decreasing subsequence (equal elements are allowed).",
        input_en="The first line contains n (1 <= n <= 1000). The second line "
                 "contains n integers separated by spaces.",
        output_en="The length of the longest non-decreasing subsequence.",
        desc_zh="给定n个整数组成的序列，求其最长不下降子序列（允许相等）的长度。",
        input_zh="第一行一个整数n（1 <= n <= 1000），第二行n个空格分隔的整数。",
        output_zh="最长不下降子序列的长度。",
        py="""# P2076 最长不下降子序列（线性DP：f[i]=max(f[j]+1), a[j]<=a[i]）
n = int(input())                      # 序列长度 n
a = list(map(int, input().split()))   # 读取序列
f = [1] * n                           # f[i] 表示以 a[i] 结尾的最长不下降子序列长度
for i in range(n):
    for j in range(i):
        if a[j] <= a[i] and f[j] + 1 > f[i]:  # 非严格不下降才可接续
            f[i] = f[j] + 1
print(max(f))                         # 输出最长不下降子序列长度
""",
        cpp="""// P2076 最长不下降子序列（线性DP：f[i]=max(f[j]+1), a[j]<=a[i]）
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 序列长度 n
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<int> f(n, 1);               // f[i] 表示以 a[i] 结尾的最长不下降子序列长度
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (a[j] <= a[i] && f[j] + 1 > f[i])  // 非严格不下降才可接续
                f[i] = f[j] + 1;
    cout << *max_element(f.begin(), f.end()) << endl;
    return 0;
}
""",
        java="""// P2076 最长不下降子序列（线性DP：f[i]=max(f[j]+1), a[j]<=a[i]）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 序列长度 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int[] f = new int[n];          // f[i] 表示以 a[i] 结尾的最长不下降子序列长度
        int ans = 0;
        for (int i = 0; i < n; i++) {
            f[i] = 1;
            for (int j = 0; j < i; j++)
                if (a[j] <= a[i] && f[j] + 1 > f[i])  // 非严格不下降才可接续
                    f[i] = f[j] + 1;
            if (f[i] > ans) ans = f[i];
        }
        System.out.println(ans);
    }
}
""",
    )
