# -*- coding: utf-8 -*-
"""P2066 最大子段和"""
from generate import make_problem


def build():
    # (n, 数组a)，求连续子段最大和（至少选一个元素）
    data = [
        (5, [1, 2, 3, 4, 5]),
        (1, [-3]),
        (6, [-2, 1, -3, 4, -1, 2]),
        (4, [-1, -2, -3, -4]),
        (8, [2, -1, 3, -2, 4, 1, -3, 2]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, seed):
        v = seed
        a = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            a.append(v % 201 - 100)        # -100..100
        return a

    for n, seed in [(50, 5), (100, 13), (200, 27), (500, 41), (1000, 83)]:
        data.append((n, gen(n, seed)))

    cases = []
    for n, a in data:
        # 前缀和思想：最大子段和 = max(pre[j]-min_{i<j} pre[i])
        pre = 0
        min_pre = 0
        ans = -10**18
        for x in a:
            pre += x
            ans = max(ans, pre - min_pre)
            min_pre = min(min_pre, pre)
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        cases.append((inp, f"{ans}\n"))

    return make_problem(
        "P2066", "最大子段和", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given n integers, find the maximum sum of a contiguous subarray "
                "(at least one element must be chosen). Use the prefix sum idea: "
                "track the minimum prefix sum seen so far.",
        input_en="The first line contains n. The second line contains n "
                 "space-separated integers.",
        output_en="One integer, the maximum subarray sum.",
        desc_zh="给定 n 个数，求连续子段的最大和（至少选一个元素）。",
        input_zh="第一行一个整数 n；第二行 n 个用空格分隔的整数。",
        output_zh="一行一个整数，表示连续子段的最大和。",
        py=r"""# P2066 最大子段和（前缀和 + 维护最小前缀和）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # n 个整数
pre = 0                                # 当前前缀和
min_pre = 0                            # 已出现过的最小前缀和（含 pre[0]=0）
ans = -10**18
for x in a:
    pre += x                           # pre = pre[j]
    ans = max(ans, pre - min_pre)      # 以 j 结尾的最大子段和
    min_pre = min(min_pre, pre)        # 更新最小前缀和
print(ans)
""",
        cpp=r"""// P2066 最大子段和（前缀和 + 维护最小前缀和）
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    long long pre = 0;                 // 当前前缀和
    long long min_pre = 0;             // 已出现过的最小前缀和（含 pre[0]=0）
    long long ans = -1e18;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pre += x;                      // pre = pre[j]
        if (pre - min_pre > ans) ans = pre - min_pre;  // 以 j 结尾的最大子段和
        if (pre < min_pre) min_pre = pre;              // 更新最小前缀和
    }
    cout << ans << "\n";
    return 0;
}
""",
        java=r"""// P2066 最大子段和（前缀和 + 维护最小前缀和）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        long pre = 0;                  // 当前前缀和
        long minPre = 0;               // 已出现过的最小前缀和（含 pre[0]=0）
        long ans = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            pre += x;                  // pre = pre[j]
            if (pre - minPre > ans) ans = pre - minPre;  // 以 j 结尾的最大子段和
            if (pre < minPre) minPre = pre;              // 更新最小前缀和
        }
        System.out.println(ans);
    }
}
""",
    )
