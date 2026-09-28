# -*- coding: utf-8 -*-
"""P2063 区间加值"""
from generate import make_problem


def build():
    # (n, 操作列表[(l,r,c),...])，初始数组全 0，对 [l,r] 每个数加 c
    data = [
        (5, [(1, 5, 1), (2, 4, 2)]),
        (1, [(1, 1, 5)]),
        (6, [(1, 6, 3), (3, 5, -1), (2, 3, 4)]),
        (4, [(1, 4, 0), (2, 3, 10)]),
        (7, [(1, 7, 1), (1, 7, 1), (1, 7, 1)]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, q, seed):
        v = seed
        ops = []
        for _ in range(q):
            v = (v * 1103515245 + 12345) % (1 << 31)
            l = v % n + 1
            v = (v * 1103515245 + 12345) % (1 << 31)
            r = v % n + 1
            if l > r:
                l, r = r, l
            v = (v * 1103515245 + 12345) % (1 << 31)
            c = v % 201 - 100            # -100..100
            ops.append((l, r, c))
        return ops

    for n, q, seed in [(50, 20, 5), (100, 50, 17), (200, 100, 31),
                       (500, 200, 43), (1000, 500, 89)]:
        data.append((n, gen(n, q, seed)))

    cases = []
    for n, ops in data:
        # 用差分数组还原最终数组
        d = [0] * (n + 2)                # 1-based，多一位给 r+1
        for l, r, c in ops:
            d[l] += c
            d[r + 1] -= c                # 差分：[l,r] 加 c
        a = []
        cur = 0
        for i in range(1, n + 1):
            cur += d[i]                  # 前缀和还原
            a.append(cur)
        inp = f"{n} {len(ops)}\n"
        for l, r, c in ops:
            inp += f"{l} {r} {c}\n"
        cases.append((inp, " ".join(map(str, a)) + "\n"))

    return make_problem(
        "P2063", "区间加值", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="There are n elements initially all zero. Perform q operations: "
                "each adds c to every element in [l,r] (1-based). Output the "
                "final array. Use a difference array.",
        input_en="The first line contains n and q. Then q lines, each with three "
                 "integers l r c.",
        output_en="One line with n space-separated integers, the final array.",
        desc_zh="给定 n 个初始为 0 的数，q 次操作给区间 [l,r] 每个数加 c，输出最终数组。",
        input_zh="第一行两个整数 n 和 q；接下来 q 行每行三个整数 l r c，表示给 [l,r] 每个数加 c。",
        output_zh="一行 n 个用空格分隔的整数，表示最终数组。",
        py=r"""# P2063 区间加值（差分数组）
n, q = map(int, input().split())        # 元素个数 n、操作数 q
d = [0] * (n + 2)                       # 差分数组，1-based，多一位给 r+1
for _ in range(q):
    l, r, c = map(int, input().split())  # 对 [l,r] 每个数加 c
    d[l] += c                           # 差分：左端点加 c
    d[r + 1] -= c                       # 差分：右端点后一位减 c
a = []
cur = 0
for i in range(1, n + 1):
    cur += d[i]                         # 前缀和还原原数组
    a.append(cur)
print(" ".join(map(str, a)))            # 输出最终数组
""",
        cpp=r"""// P2063 区间加值（差分数组）
#include <iostream>
using namespace std;
const int N = 1005;
long long d[N];
int main() {
    int n, q;
    cin >> n >> q;                      // 元素个数 n、操作数 q
    while (q--) {
        int l, r;
        long long c;
        cin >> l >> r >> c;             // 对 [l,r] 每个数加 c
        d[l] += c;                      // 差分：左端点加 c
        d[r + 1] -= c;                  // 差分：右端点后一位减 c
    }
    long long cur = 0;
    for (int i = 1; i <= n; i++) {
        cur += d[i];                    // 前缀和还原原数组
        cout << cur;
        cout << (i == n ? "\n" : " ");
    }
    return 0;
}
""",
        java=r"""// P2063 区间加值（差分数组）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), q = sc.nextInt();   // 元素个数 n、操作数 q
        long[] d = new long[n + 2];               // 差分数组
        while (q-- > 0) {
            int l = sc.nextInt(), r = sc.nextInt();
            long c = sc.nextLong();               // 对 [l,r] 每个数加 c
            d[l] += c;                            // 差分：左端点加 c
            d[r + 1] -= c;                        // 差分：右端点后一位减 c
        }
        StringBuilder sb = new StringBuilder();
        long cur = 0;
        for (int i = 1; i <= n; i++) {
            cur += d[i];                          // 前缀和还原原数组
            if (i > 1) sb.append(" ");
            sb.append(cur);
        }
        sb.append("\n");
        System.out.print(sb);
    }
}
""",
    )
