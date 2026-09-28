# -*- coding: utf-8 -*-
"""P2065 区间加+单点查"""
from generate import make_problem


def build():
    # (n, 操作列表)，操作: (1,l,r,c) 区间加 c; (2,x) 查询位置 x 的值
    data = [
        (5, [(1, 1, 5, 1), (2, 3), (1, 2, 4, 2), (2, 2), (2, 5)]),
        (1, [(1, 1, 1, 9), (2, 1)]),
        (6, [(1, 1, 6, 3), (1, 3, 5, -1), (2, 1), (2, 3), (2, 6)]),
        (4, [(2, 2), (1, 2, 3, 10), (2, 2), (2, 4)]),
        (8, [(1, 1, 8, 1), (1, 1, 8, 1), (1, 1, 8, 1), (2, 5), (2, 1)]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, q, seed):
        v = seed
        ops = []
        for _ in range(q):
            v = (v * 1103515245 + 12345) % (1 << 31)
            if v % 2 == 0:             # 一半概率区间加
                v = (v * 1103515245 + 12345) % (1 << 31)
                l = v % n + 1
                v = (v * 1103515245 + 12345) % (1 << 31)
                r = v % n + 1
                if l > r:
                    l, r = r, l
                v = (v * 1103515245 + 12345) % (1 << 31)
                c = v % 201 - 100
                ops.append((1, l, r, c))
            else:                      # 一半概率单点查
                v = (v * 1103515245 + 12345) % (1 << 31)
                x = v % n + 1
                ops.append((2, x))
        return ops

    for n, q, seed in [(50, 40, 5), (100, 80, 17), (200, 150, 31),
                       (500, 300, 43), (1000, 600, 89)]:
        data.append((n, gen(n, q, seed)))

    cases = []
    for n, ops in data:
        # 暴力模拟作为期望输出：维护真实数组
        a = [0] * (n + 1)
        out = []
        for op in ops:
            if op[0] == 1:
                _, l, r, c = op
                for i in range(l, r + 1):
                    a[i] += c
            else:
                _, x = op
                out.append(str(a[x]))
        inp = f"{n} {len(ops)}\n"
        for op in ops:
            if op[0] == 1:
                inp += f"1 {op[1]} {op[2]} {op[3]}\n"
            else:
                inp += f"2 {op[1]}\n"
        cases.append((inp, "\n".join(out) + "\n" if out else "\n"))

    return make_problem(
        "P2065", "区间加+单点查", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="There are n elements initially all zero. Process q operations: "
                "'1 l r c' adds c to every element in [l,r] (1-based); '2 x' "
                "outputs the value at position x. Use a difference array plus "
                "prefix sum.",
        input_en="The first line contains n and q. Then q lines, each an "
                 "operation: either '1 l r c' or '2 x'.",
        output_en="For each type-2 operation, output the value at position x on "
                  "its own line.",
        desc_zh="给定 n 个初始为 0 的数，q 次操作：1 l r c 表示给区间 [l,r] 每个数加 c，2 x 表示查询位置 x 的值。",
        input_zh="第一行两个整数 n 和 q；接下来 q 行，每行一个操作：1 l r c 或 2 x。",
        output_zh="对于每个 2 x 操作，输出一行一个整数，表示位置 x 的值。",
        py=r"""# P2065 区间加+单点查（差分 + 前缀和）
import sys
input = sys.stdin.readline
n, q = map(int, input().split())        # 元素个数 n、操作数 q
d = [0] * (n + 2)                       # 差分数组，1-based
out = []
for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:                      # 区间加操作
        l, r, c = op[1], op[2], op[3]
        d[l] += c                       # 差分：左端点加 c
        d[r + 1] -= c                   # 差分：右端点后一位减 c
    else:                               # 单点查询操作
        x = op[1]
        v = 0
        for i in range(1, x + 1):       # 前缀和到 x 得到位置 x 的值
            v += d[i]
        out.append(str(v))
print("\n".join(out))
""",
        cpp=r"""// P2065 区间加+单点查（差分 + 前缀和）
#include <iostream>
using namespace std;
const int N = 1005;
long long d[N];
int main() {
    int n, q;
    cin >> n >> q;                      // 元素个数 n、操作数 q
    while (q--) {
        int t;
        cin >> t;
        if (t == 1) {                   // 区间加操作
            int l, r;
            long long c;
            cin >> l >> r >> c;
            d[l] += c;                  // 差分：左端点加 c
            d[r + 1] -= c;              // 差分：右端点后一位减 c
        } else {                        // 单点查询操作
            int x;
            cin >> x;
            long long v = 0;
            for (int i = 1; i <= x; i++)  // 前缀和到 x 得到位置 x 的值
                v += d[i];
            cout << v << "\n";
        }
    }
    return 0;
}
""",
        java=r"""// P2065 区间加+单点查（差分 + 前缀和）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), q = sc.nextInt();   // 元素个数 n、操作数 q
        long[] d = new long[n + 2];               // 差分数组
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int t = sc.nextInt();
            if (t == 1) {                         // 区间加操作
                int l = sc.nextInt(), r = sc.nextInt();
                long c = sc.nextLong();
                d[l] += c;                        // 差分：左端点加 c
                d[r + 1] -= c;                    // 差分：右端点后一位减 c
            } else {                              // 单点查询操作
                int x = sc.nextInt();
                long v = 0;
                for (int i = 1; i <= x; i++)      // 前缀和到 x 得到位置 x 的值
                    v += d[i];
                sb.append(v).append("\n");
            }
        }
        System.out.print(sb);
    }
}
""",
    )
