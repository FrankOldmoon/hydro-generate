# -*- coding: utf-8 -*-
"""P2064 差分还原"""
from generate import make_problem


def build():
    # (n, 差分数组 d[1..n])，原数组 a[1]=d[1]，a[i]=a[i-1]+d[i]
    data = [
        (5, [1, 2, 3, 4, 5]),
        (1, [7]),
        (4, [3, -1, 2, -2]),
        (6, [0, 0, 0, 0, 0, 0]),
        (3, [10, -5, -3]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, seed):
        v = seed
        d = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            d.append(v % 201 - 100)        # -100..100
        return d

    for n, seed in [(50, 5), (100, 13), (200, 27), (500, 41), (1000, 83)]:
        data.append((n, gen(n, seed)))

    cases = []
    for n, d in data:
        # 原数组就是差分数组的前缀和：a[i] = d[1]+...+d[i]
        a = []
        cur = 0
        for i in range(n):
            cur += d[i]
            a.append(cur)
        inp = f"{n}\n{' '.join(map(str, d))}\n"
        cases.append((inp, " ".join(map(str, a)) + "\n"))

    return make_problem(
        "P2064", "差分还原", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given the difference array d of length n, restore the original "
                "array a where a[1]=d[1] and a[i]=a[i-1]+d[i] for i>1. That is, "
                "a is the prefix sum of d.",
        input_en="The first line contains n. The second line contains n "
                 "space-separated integers, the difference array d.",
        output_en="One line with n space-separated integers, the restored array a.",
        desc_zh="给定长度为 n 的差分数组 d，还原原数组 a，其中 a[1]=d[1]，a[i]=a[i-1]+d[i]。",
        input_zh="第一行一个整数 n；第二行 n 个用空格分隔的整数，表示差分数组 d。",
        output_zh="一行 n 个用空格分隔的整数，表示还原后的原数组 a。",
        py=r"""# P2064 差分还原（前缀和）
n = int(input())                       # 差分数组长度 n
d = list(map(int, input().split()))    # 差分数组 d
a = []
cur = 0
for i in range(n):
    cur += d[i]                        # 前缀和：a[i] = a[i-1] + d[i]
    a.append(cur)
print(" ".join(map(str, a)))           # 输出还原后的原数组
""",
        cpp=r"""// P2064 差分还原（前缀和）
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 差分数组长度 n
    long long cur = 0;
    for (int i = 1; i <= n; i++) {
        long long d;
        cin >> d;                      // 读入差分值 d[i]
        cur += d;                      // 前缀和：a[i] = a[i-1] + d[i]
        cout << cur;
        cout << (i == n ? "\n" : " ");
    }
    return 0;
}
""",
        java=r"""// P2064 差分还原（前缀和）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 差分数组长度 n
        StringBuilder sb = new StringBuilder();
        long cur = 0;
        for (int i = 1; i <= n; i++) {
            long d = sc.nextLong();    // 读入差分值 d[i]
            cur += d;                  // 前缀和：a[i] = a[i-1] + d[i]
            if (i > 1) sb.append(" ");
            sb.append(cur);
        }
        sb.append("\n");
        System.out.print(sb);
    }
}
""",
    )
