# -*- coding: utf-8 -*-
"""P2021 数组去重并排序"""
from generate import make_problem


def build():
    # (n, 数组)：去重后升序输出，第一行个数，第二行元素
    data = [
        (5, [3, 1, 2, 3, 1]),
        (3, [5, 5, 5]),
        (1, [42]),
        (8, [8, 7, 6, 5, 4, 3, 2, 1]),
        (6, [1, 2, 3, 4, 5, 6]),
        (10, [4, 4, 1, 3, 2, 4, 1, 2, 5, 3]),
        (2, [100, -100]),
        (7, [5, 5, 5, 5, 5, 5, 5]),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4]),
        (20, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        s = sorted(set(a))                       # 去重后升序
        out = f"{len(s)}\n{' '.join(map(str, s))}\n"
        cases.append((inp, out))
    return make_problem(
        "P2021", "数组去重并排序", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers, remove duplicates and output the remaining "
                "values in ascending order. The first line is the count k of "
                "distinct values, and the second line contains the k values in "
                "ascending order separated by spaces.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying "
                 "$1\\leq n\\leq 100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="Two lines: the first line is the count k of distinct values; "
                  "the second line contains the k values in ascending order "
                  "separated by spaces.",
        desc_zh="给定 n 个整数，去重后升序输出。第一行输出去重后个数 k，第二行输出 k 个升序整数。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="两行：第一行一个整数 k 表示去重后元素个数；第二行 k 个用空格分隔的整数，按升序排列。",
        py=r"""# P2021 数组去重并排序（先去重再升序排序）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
s = sorted(set(a))                     # 去重后升序排序
print(len(s))                          # 第一行：去重后元素个数
print(' '.join(map(str, s)))           # 第二行：升序输出
""",
        cpp=r"""// P2021 数组去重并排序（先排序再去重）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);                    // 先升序排序
    int k = 0;
    for (int i = 0; i < n; i++) {      // 去重：保留每个值的首次出现
        if (i == 0 || a[i] != a[i - 1]) a[k++] = a[i];
    }
    cout << k << endl;                 // 第一行：去重后个数
    for (int i = 0; i < k; i++) {      // 第二行：升序输出
        if (i) cout << ' ';
        cout << a[i];
    }
    cout << endl;
    return 0;
}
""",
        java=r"""// P2021 数组去重并排序（先排序再去重）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        Arrays.sort(a);                // 先升序排序
        int k = 0;
        int[] tmp = new int[n];
        for (int i = 0; i < n; i++) {  // 去重：保留每个值首次出现
            if (i == 0 || a[i] != a[i - 1]) tmp[k++] = a[i];
        }
        StringBuilder sb = new StringBuilder();
        sb.append(k).append('\n');     // 第一行：去重后个数
        for (int i = 0; i < k; i++) {  // 第二行：升序输出
            if (i > 0) sb.append(' ');
            sb.append(tmp[i]);
        }
        sb.append('\n');
        System.out.print(sb);
    }
}
""",
    )
