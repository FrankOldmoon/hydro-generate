# -*- coding: utf-8 -*-
"""P2025 众数"""
from generate import make_problem


def build():
    # (n, 数组)：出现次数最多的数，多个众数取值最小
    data = [
        (5, [3, 1, 2, 3, 1]),
        (3, [5, 5, 5]),
        (1, [42]),
        (6, [1, 2, 3, 4, 5, 6]),
        (6, [6, 5, 4, 3, 2, 1]),
        (10, [4, 4, 1, 3, 2, 4, 1, 2, 5, 3]),
        (2, [100, -100]),
        (7, [5, 5, 5, 5, 5, 5, 5]),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4]),
        (20, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        b = sorted(a)                            # 升序排序，便于统计连续相同值
        mode, best, cur = b[0], 1, 1
        for i in range(1, n):                    # 统计连续相同元素
            if b[i] == b[i - 1]:
                cur += 1
            else:
                cur = 1
            if cur > best:                       # 严格大于才更新，保证众数相同取最小值
                best = cur
                mode = b[i]
        out = f"{mode}\n"
        cases.append((inp, out))
    return make_problem(
        "P2025", "众数", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers, output the mode (the value that appears most "
                "frequently). If multiple values share the maximum frequency, "
                "output the smallest one.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying "
                 "$1\\leq n\\leq 100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing the mode.",
        desc_zh="给定 n 个整数，输出出现次数最多的数（若存在多个众数，取值最小的那个）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行一个整数，表示众数（多个众数时取值最小者）。",
        py=r"""# P2025 众数（排序后统计连续相同元素，取出现最多且值最小者）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
a.sort()                               # 升序排序，便于统计连续相同值
mode = a[0]
best = 1
cur = 1
for i in range(1, n):                  # 扫描统计连续相同元素
    if a[i] == a[i - 1]:
        cur += 1
    else:
        cur = 1
    if cur > best:                     # 严格大于才更新，保证众数相同取最小值
        best = cur
        mode = a[i]
print(mode)                            # 输出众数
""",
        cpp=r"""// P2025 众数（排序后统计连续相同元素，取出现最多且值最小者）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);                    // 升序排序
    int mode = a[0], best = 1, cur = 1;
    for (int i = 1; i < n; i++) {      // 统计连续相同元素
        if (a[i] == a[i - 1]) cur++;
        else cur = 1;
        if (cur > best) {              // 严格大于才更新，众数相同取最小值
            best = cur;
            mode = a[i];
        }
    }
    cout << mode << endl;              // 输出众数
    return 0;
}
""",
        java=r"""// P2025 众数（排序后统计连续相同元素，取出现最多且值最小者）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        Arrays.sort(a);                // 升序排序
        int mode = a[0], best = 1, cur = 1;
        for (int i = 1; i < n; i++) {  // 统计连续相同元素
            if (a[i] == a[i - 1]) cur++;
            else cur = 1;
            if (cur > best) {          // 严格大于才更新，众数相同取最小值
                best = cur;
                mode = a[i];
            }
        }
        System.out.println(mode);      // 输出众数
    }
}
""",
    )
