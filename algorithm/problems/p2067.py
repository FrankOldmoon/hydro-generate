# -*- coding: utf-8 -*-
"""P2067 和为k的子数组"""
from generate import make_problem


def build():
    # (n, k, 数组a)，求和恰好等于 k 的连续子数组个数
    data = [
        (5, 3, [1, 2, 3, 4, 5]),
        (1, 7, [7]),
        (3, 0, [1, -1, 0]),
        (4, 2, [1, 1, 1, 1]),
        (6, 5, [2, 3, 1, 2, 4, 1]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, seed):
        v = seed
        a = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            a.append(v % 21 - 10)          # -10..10，便于出现多个等于 k 的子数组
        k = (seed % 11) - 5                # k 在 -5..5
        return a, k

    for n, seed in [(50, 5), (100, 13), (200, 27), (500, 41), (1000, 83)]:
        a, k = gen(n, seed)
        data.append((n, k, a))

    cases = []
    for n, k, a in data:
        # 前缀和 + 哈希表：pre[j]-pre[i-1]=k 等价于统计之前 pre[j]-k 的出现次数
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        ans = 0
        for x in a:
            pre += x
            ans += cnt[pre - k]
            cnt[pre] += 1
        inp = f"{n} {k}\n{' '.join(map(str, a))}\n"
        cases.append((inp, f"{ans}\n"))

    return make_problem(
        "P2067", "和为k的子数组", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given n integers and an integer k, count the number of "
                "contiguous subarrays whose sum is exactly k. Use prefix sums "
                "with a hash map.",
        input_en="The first line contains n and k. The second line contains n "
                 "space-separated integers.",
        output_en="One integer, the number of subarrays with sum k.",
        desc_zh="给定 n 个数和整数 k，求有多少个连续子数组的和恰好等于 k。",
        input_zh="第一行两个整数 n 和 k；第二行 n 个用空格分隔的整数。",
        output_zh="一行一个整数，表示和等于 k 的连续子数组个数。",
        py=r"""# P2067 和为k的子数组（前缀和 + 哈希表）
from collections import defaultdict
n, k = map(int, input().split())        # 元素个数 n、目标和 k
a = list(map(int, input().split()))     # n 个整数
cnt = defaultdict(int)                  # 记录各前缀和出现次数
cnt[0] = 1                              # pre[0]=0 出现一次
pre = 0
ans = 0
for x in a:
    pre += x                            # pre = pre[j]
    ans += cnt[pre - k]                 # 之前 pre[j]-k 的出现次数即为以 j 结尾的合法子数组数
    cnt[pre] += 1                       # 记录当前前缀和
print(ans)
""",
        cpp=r"""// P2067 和为k的子数组（前缀和 + 哈希表）
#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    int n;
    long long k;
    cin >> n >> k;                      // 元素个数 n、目标和 k
    unordered_map<long long, long long> cnt;  // 记录各前缀和出现次数
    cnt[0] = 1;                         // pre[0]=0 出现一次
    long long pre = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pre += x;                       // pre = pre[j]
        ans += cnt[pre - k];            // 之前 pre[j]-k 的出现次数即为以 j 结尾的合法子数组数
        cnt[pre]++;                     // 记录当前前缀和
    }
    cout << ans << "\n";
    return 0;
}
""",
        java=r"""// P2067 和为k的子数组（前缀和 + 哈希表）
import java.util.Scanner;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();           // 元素个数 n
        long k = sc.nextLong();         // 目标和 k
        HashMap<Long, Long> cnt = new HashMap<>();  // 记录各前缀和出现次数
        cnt.put(0L, 1L);                // pre[0]=0 出现一次
        long pre = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            pre += x;                   // pre = pre[j]
            ans += cnt.getOrDefault(pre - k, 0L);  // 以 j 结尾的合法子数组数
            cnt.merge(pre, 1L, Long::sum);         // 记录当前前缀和
        }
        System.out.println(ans);
    }
}
""",
    )
