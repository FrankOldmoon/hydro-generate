# -*- coding: utf-8 -*-
"""P2070 前缀和统计"""
from generate import make_problem


def build():
    # (n, k, 数组a)，求有多少对 (i,j) 使 pre[j]-pre[i-1] 恰好等于 k
    # 其中 pre[0]=0，pre[t]=a[1]+...+a[t]，1<=i<=j<=n
    data = [
        (5, 6, [1, 2, 3, 4, 5]),
        (1, 1, [1]),
        (4, 0, [1, -1, 2, -2]),
        (6, 3, [1, 2, 0, 0, 1, 2]),
        (5, 5, [5, 5, 5, 5, 5]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, seed):
        v = seed
        a = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            a.append(v % 15 - 7)          # -7..7
        k = (seed * 3 % 9) - 4            # k 在 -4..4
        return a, k

    for n, seed in [(50, 5), (100, 13), (200, 27), (500, 41), (1000, 83)]:
        a, k = gen(n, seed)
        data.append((n, k, a))

    cases = []
    for n, k, a in data:
        # 前缀和 + 哈希表：统计 pre[j]-pre[i-1]=k 的 (i,j) 对数
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1                        # pre[0]=0 已出现
        pre = 0
        ans = 0
        for x in a:
            pre += x                      # pre = pre[j]
            ans += cnt[pre - k]           # 找到 pre[i-1]=pre[j]-k 的个数
            cnt[pre] += 1                 # 当前前缀和加入计数
        inp = f"{n} {k}\n{' '.join(map(str, a))}\n"
        cases.append((inp, f"{ans}\n"))

    return make_problem(
        "P2070", "前缀和统计", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given n integers and an integer k, let pre[0]=0 and "
                "pre[t]=a[1]+...+a[t]. Count the number of pairs (i,j) with "
                "1<=i<=j<=n such that pre[j]-pre[i-1] equals k (i.e. the number "
                "of subarrays summing to k). Use prefix sums with a hash map.",
        input_en="The first line contains n and k. The second line contains n "
                 "space-separated integers.",
        output_en="One integer, the number of pairs (i,j) with pre[j]-pre[i-1]=k.",
        desc_zh="给定 n 个数和整数 k，求有多少对 (i,j) 使前缀和 pre[j]-pre[i-1] 恰好等于 k（即子数组和为 k 的方案数）。",
        input_zh="第一行两个整数 n 和 k；第二行 n 个用空格分隔的整数。",
        output_zh="一行一个整数，表示满足 pre[j]-pre[i-1]=k 的 (i,j) 对数。",
        py=r"""# P2070 前缀和统计（前缀和 + 哈希表）
from collections import defaultdict
n, k = map(int, input().split())        # 元素个数 n、目标值 k
a = list(map(int, input().split()))     # n 个整数
cnt = defaultdict(int)                  # 记录各前缀和出现次数
cnt[0] = 1                              # pre[0]=0 已出现一次
pre = 0
ans = 0
for x in a:
    pre += x                            # pre = pre[j]
    ans += cnt[pre - k]                 # pre[i-1]=pre[j]-k 的个数即为合法 (i,j) 对数
    cnt[pre] += 1                       # 当前前缀和加入计数
print(ans)
""",
        cpp=r"""// P2070 前缀和统计（前缀和 + 哈希表）
#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    int n;
    long long k;
    cin >> n >> k;                      // 元素个数 n、目标值 k
    unordered_map<long long, long long> cnt;  // 记录各前缀和出现次数
    cnt[0] = 1;                         // pre[0]=0 已出现一次
    long long pre = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pre += x;                       // pre = pre[j]
        ans += cnt[pre - k];            // pre[i-1]=pre[j]-k 的个数即为合法 (i,j) 对数
        cnt[pre]++;                     // 当前前缀和加入计数
    }
    cout << ans << "\n";
    return 0;
}
""",
        java=r"""// P2070 前缀和统计（前缀和 + 哈希表）
import java.util.Scanner;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();           // 元素个数 n
        long k = sc.nextLong();         // 目标值 k
        HashMap<Long, Long> cnt = new HashMap<>();  // 记录各前缀和出现次数
        cnt.put(0L, 1L);                // pre[0]=0 已出现一次
        long pre = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            pre += x;                   // pre = pre[j]
            ans += cnt.getOrDefault(pre - k, 0L);  // 合法 (i,j) 对数
            cnt.merge(pre, 1L, Long::sum);         // 当前前缀和加入计数
        }
        System.out.println(ans);
    }
}
""",
    )
