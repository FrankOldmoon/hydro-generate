# -*- coding: utf-8 -*-
"""P2061 一维区间和"""
from generate import make_problem


def build():
    # (n, 数组a, 查询列表[(l,r),...])，查询为 1-based 闭区间
    data = [
        (5, [1, 2, 3, 4, 5], [(1, 3), (2, 4), (1, 5)]),
        (1, [10], [(1, 1)]),
        (3, [-1, 5, -2], [(1, 3), (2, 2), (1, 1)]),
        (6, [1, 1, 1, 1, 1, 1], [(1, 6), (3, 4), (2, 5)]),
        (8, [2, -1, 3, -2, 4, 1, -3, 2], [(1, 8), (3, 6), (2, 5), (4, 4)]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, q, seed):
        v = seed
        a = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            a.append(v % 201 - 100)            # -100..100
        qs = []
        for _ in range(q):
            v = (v * 1103515245 + 12345) % (1 << 31)
            l = v % n + 1
            v = (v * 1103515245 + 12345) % (1 << 31)
            r = v % n + 1
            if l > r:
                l, r = r, l
            qs.append((l, r))
        return a, qs

    for n, q, seed in [(50, 20, 7), (100, 50, 13), (200, 100, 29),
                       (500, 200, 41), (1000, 500, 97)]:
        a, qs = gen(n, q, seed)
        data.append((n, a, qs))

    cases = []
    for n, a, qs in data:
        # 构造前缀和，pre[i] = a[0]+...+a[i-1]
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + a[i - 1]
        inp = f"{n}\n{' '.join(map(str, a))}\n{len(qs)}\n"
        out = []
        for l, r in qs:
            inp += f"{l} {r}\n"
            out.append(str(pre[r] - pre[l - 1]))  # 区间和
        cases.append((inp, "\n".join(out) + "\n"))

    return make_problem(
        "P2061", "一维区间和", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given n integers and q queries, each query asks for the sum of "
                "the subarray from index l to r (1-based, inclusive). Use a prefix "
                "sum array for O(1) per query.",
        input_en="The first line contains n. The second line contains n "
                 "space-separated integers. The third line contains q. Then q "
                 "lines follow, each containing two integers l and r.",
        output_en="q lines, each the sum of the queried interval.",
        desc_zh="给定 n 个数，q 次查询区间 [l,r] 的和，每个查询输出一行结果。",
        input_zh="第一行一个整数 n，第二行 n 个用空格分隔的整数，第三行一个整数 q，接下来 q 行每行两个整数 l 和 r。",
        output_zh="共 q 行，每行一个整数，表示对应区间 [l,r] 的和。",
        py=r"""# P2061 一维区间和（前缀和）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # n 个整数
q = int(input())                       # 查询数 q
pre = [0] * (n + 1)                    # 前缀和数组，pre[0]=0
for i in range(1, n + 1):              # 构造前缀和
    pre[i] = pre[i - 1] + a[i - 1]
out = []
for _ in range(q):                     # 处理每个查询
    l, r = map(int, input().split())   # 区间端点 1-based
    out.append(str(pre[r] - pre[l - 1]))  # 区间和 = pre[r]-pre[l-1]
print("\n".join(out))                  # 每行一个结果
""",
        cpp=r"""// P2061 一维区间和（前缀和）
#include <iostream>
using namespace std;
const int N = 1005;
long long a[N], pre[N];
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++)       // 构造前缀和
        pre[i] = pre[i - 1] + a[i];
    int q;
    cin >> q;                          // 查询数 q
    while (q--) {                      // 处理每个查询
        int l, r;
        cin >> l >> r;                 // 区间端点 1-based
        cout << pre[r] - pre[l - 1] << "\n";  // 区间和
    }
    return 0;
}
""",
        java=r"""// P2061 一维区间和（前缀和）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        long[] pre = new long[n + 1];  // 前缀和数组
        for (int i = 1; i <= n; i++)   // 构造前缀和
            pre[i] = pre[i - 1] + sc.nextLong();
        int q = sc.nextInt();          // 查询数 q
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {              // 处理每个查询
            int l = sc.nextInt(), r = sc.nextInt();  // 区间端点 1-based
            sb.append(pre[r] - pre[l - 1]).append("\n");  // 区间和
        }
        System.out.print(sb);
    }
}
""",
    )
