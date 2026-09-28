# -*- coding: utf-8 -*-
"""P2069 区间和等于目标"""
from generate import make_problem


def build():
    # (n, target, 数组a)，求和恰好等于 target 的连续区间个数
    data = [
        (5, 9, [2, 7, 1, 8, 3]),
        (1, 4, [4]),
        (4, 0, [1, -1, 1, -1]),
        (6, 3, [1, 2, 3, 1, 2, 3]),
        (7, 6, [1, 2, 3, 0, 3, 2, 1]),
    ]

    # 线性同余生成器补充更大的数据
    def gen(n, seed):
        v = seed
        a = []
        for _ in range(n):
            v = (v * 1103515245 + 12345) % (1 << 31)
            a.append(v % 21 - 10)          # -10..10
        target = (seed * 7 % 11) - 5       # target 在 -5..5
        return a, target

    for n, seed in [(50, 5), (100, 13), (200, 27), (500, 41), (1000, 83)]:
        a, target = gen(n, seed)
        data.append((n, target, a))

    cases = []
    for n, target, a in data:
        # 前缀和 + 哈希表：区间 [i,j] 和等于 target 等价于 pre[j]-pre[i-1]=target
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        ans = 0
        for x in a:
            pre += x
            ans += cnt[pre - target]
            cnt[pre] += 1
        inp = f"{n} {target}\n{' '.join(map(str, a))}\n"
        cases.append((inp, f"{ans}\n"))

    return make_problem(
        "P2069", "区间和等于目标", ["算法", "前缀和与差分"],
        cases=cases,
        desc_en="Given n integers and a target value, count the number of "
                "contiguous intervals whose sum equals target. Use prefix sums "
                "with a hash map.",
        input_en="The first line contains n and target. The second line contains "
                 "n space-separated integers.",
        output_en="One integer, the number of intervals with sum equal to target.",
        desc_zh="给定 n 个数和目标值 target，求有多少个连续区间的和等于 target。",
        input_zh="第一行两个整数 n 和 target；第二行 n 个用空格分隔的整数。",
        output_zh="一行一个整数，表示和等于 target 的连续区间个数。",
        py=r"""# P2069 区间和等于目标（前缀和 + 哈希表）
from collections import defaultdict
n, target = map(int, input().split())   # 元素个数 n、目标值 target
a = list(map(int, input().split()))     # n 个整数
cnt = defaultdict(int)                  # 记录各前缀和出现次数
cnt[0] = 1                              # pre[0]=0 出现一次
pre = 0
ans = 0
for x in a:
    pre += x                            # pre = pre[j]
    ans += cnt[pre - target]            # 区间 [i,j] 和为 target 当且仅当 pre[i-1]=pre[j]-target
    cnt[pre] += 1                       # 记录当前前缀和
print(ans)
""",
        cpp=r"""// P2069 区间和等于目标（前缀和 + 哈希表）
#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    int n;
    long long target;
    cin >> n >> target;                 // 元素个数 n、目标值 target
    unordered_map<long long, long long> cnt;  // 记录各前缀和出现次数
    cnt[0] = 1;                         // pre[0]=0 出现一次
    long long pre = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pre += x;                       // pre = pre[j]
        ans += cnt[pre - target];       // 区间 [i,j] 和为 target 当且仅当 pre[i-1]=pre[j]-target
        cnt[pre]++;                     // 记录当前前缀和
    }
    cout << ans << "\n";
    return 0;
}
""",
        java=r"""// P2069 区间和等于目标（前缀和 + 哈希表）
import java.util.Scanner;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();           // 元素个数 n
        long target = sc.nextLong();    // 目标值 target
        HashMap<Long, Long> cnt = new HashMap<>();  // 记录各前缀和出现次数
        cnt.put(0L, 1L);                // pre[0]=0 出现一次
        long pre = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            pre += x;                   // pre = pre[j]
            ans += cnt.getOrDefault(pre - target, 0L);  // 合法区间数
            cnt.merge(pre, 1L, Long::sum);              // 记录当前前缀和
        }
        System.out.println(ans);
    }
}
""",
    )
