# -*- coding: utf-8 -*-
"""P2030 最小差值对"""
from generate import make_problem


def build():
    # (n, 数组)：任意两数差绝对值的最小值 = 排序后相邻元素差的最小值
    data = [
        (5, [3, 1, 2, 5, 4]),
        (8, [8, 7, 6, 5, 4, 3, 2, 1]),
        (2, [100, -100]),
        (6, [1, 2, 3, 4, 5, 6]),
        (5, [1, 5, 9, 2, 6]),
        (2, [0, 0]),
        (5, [5, 5, 5, 5, 5]),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4]),
        (5, [10, 20, 15, 35, 25]),
        (10, [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        b = sorted(a)                            # 升序排序
        mn = min(b[i + 1] - b[i] for i in range(n - 1))  # 相邻差最小值
        out = f"{mn}\n"
        cases.append((inp, out))
    return make_problem(
        "P2030", "最小差值对", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers, find the minimum absolute difference between "
                "any two numbers. After sorting, this equals the minimum "
                "difference between adjacent elements.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying $2\\leq n\\leq "
                 "100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing the minimum absolute difference between any "
                  "two numbers.",
        desc_zh="给定 n 个整数，求任意两数之差的绝对值的最小值（排序后相邻元素差的最小值即为答案）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $2\\leq n\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行一个整数，表示任意两数之差的绝对值的最小值。",
        py=r"""# P2030 最小差值对（排序后相邻元素差的最小值即任意两数差绝对值的最小值）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
a.sort()                               # 升序排序
ans = a[1] - a[0]
for i in range(1, n - 1):              # 扫描相邻元素取最小差
    d = a[i + 1] - a[i]
    if d < ans:
        ans = d
print(ans)                             # 输出最小差值
""",
        cpp=r"""// P2030 最小差值对（排序后相邻元素差的最小值即任意两数差绝对值的最小值）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);                    // 升序排序
    int ans = a[1] - a[0];
    for (int i = 1; i < n - 1; i++) {  // 扫描相邻元素取最小差
        int d = a[i + 1] - a[i];
        if (d < ans) ans = d;
    }
    cout << ans << endl;               // 输出最小差值
    return 0;
}
""",
        java=r"""// P2030 最小差值对（排序后相邻元素差的最小值即任意两数差绝对值的最小值）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        Arrays.sort(a);                // 升序排序
        int ans = a[1] - a[0];
        for (int i = 1; i < n - 1; i++) {  // 扫描相邻元素取最小差
            int d = a[i + 1] - a[i];
            if (d < ans) ans = d;
        }
        System.out.println(ans);       // 输出最小差值
    }
}
""",
    )
