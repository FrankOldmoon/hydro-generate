# -*- coding: utf-8 -*-
"""P2028 合并有序数组"""
from generate import make_problem


def build():
    # (n, 升序数组a, m, 升序数组b)：双指针归并
    data = [
        (3, [1, 3, 5], 3, [2, 4, 6]),
        (3, [1, 2, 3], 3, [4, 5, 6]),
        (3, [4, 5, 6], 3, [1, 2, 3]),
        (1, [42], 1, [7]),
        (1, [7], 1, [42]),
        (2, [1, 1], 3, [1, 1, 1]),
        (4, [1, 3, 5, 7], 4, [2, 4, 6, 8]),
        (5, [10, 20, 30, 40, 50], 3, [5, 25, 100]),
        (3, [-5, 0, 5], 3, [-3, 3, 8]),
        (6, [1, 2, 2, 3, 3, 4], 4, [2, 3, 3, 5]),
    ]
    cases = []
    for n, a, m, b in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}\n"
        i = j = 0
        res = []
        while i < n and j < m:                    # 双指针取较小者
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:])                         # 处理剩余元素
        res.extend(b[j:])
        out = ' '.join(map(str, res)) + '\n'
        cases.append((inp, out))
    return make_problem(
        "P2028", "合并有序数组", ["算法", "排序"],
        cases=cases,
        desc_en="Given two arrays sorted in ascending order, merge them into one "
                "ascending array and output the result.",
        input_en="The first line contains a positive integer n and the second line "
                 "contains n ascending integers. The third line contains a positive "
                 "integer m and the fourth line contains m ascending integers, "
                 "satisfying $1\\leq n, m\\leq 100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing the n+m integers of the merged ascending "
                  "array, separated by spaces.",
        desc_zh="给定两个升序数组，合并为一个升序数组并输出。",
        input_zh="第一行一个正整数 n，第二行 n 个升序整数；第三行一个正整数 m，第四行 m 个升序整数，满足 $1\\leq n, m\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行 n+m 个用空格分隔的整数，表示合并后的升序数组。",
        py=r"""# P2028 合并有序数组（双指针归并两个升序数组）
n = int(input())                       # 第一个数组长度 n
a = list(map(int, input().split()))    # n 个升序整数
m = int(input())                       # 第二个数组长度 m
b = list(map(int, input().split()))    # m 个升序整数
i = j = 0
res = []
while i < n and j < m:                 # 双指针取较小者
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
res.extend(a[i:])                      # 处理剩余元素
res.extend(b[j:])
print(' '.join(map(str, res)))         # 输出合并后的升序数组
""",
        cpp=r"""// P2028 合并有序数组（双指针归并两个升序数组）
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 第一个数组长度 n
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    int m;
    cin >> m;                          // 第二个数组长度 m
    int b[105];
    for (int i = 0; i < m; i++) cin >> b[i];
    int c[210], k = 0;
    int i = 0, j = 0;
    while (i < n && j < m) {           // 双指针取较小者
        if (a[i] <= b[j]) c[k++] = a[i++];
        else c[k++] = b[j++];
    }
    while (i < n) c[k++] = a[i++];     // 处理剩余元素
    while (j < m) c[k++] = b[j++];
    for (int t = 0; t < k; t++) {      // 输出合并后的升序数组
        if (t) cout << ' ';
        cout << c[t];
    }
    cout << endl;
    return 0;
}
""",
        java=r"""// P2028 合并有序数组（双指针归并两个升序数组）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 第一个数组长度 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int m = sc.nextInt();          // 第二个数组长度 m
        int[] b = new int[m];
        for (int i = 0; i < m; i++) b[i] = sc.nextInt();
        int[] c = new int[n + m];
        int i = 0, j = 0, k = 0;
        while (i < n && j < m) {       // 双指针取较小者
            if (a[i] <= b[j]) c[k++] = a[i++];
            else c[k++] = b[j++];
        }
        while (i < n) c[k++] = a[i++]; // 处理剩余元素
        while (j < m) c[k++] = b[j++];
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < k; t++) {  // 输出合并后的升序数组
            if (t > 0) sb.append(' ');
            sb.append(c[t]);
        }
        sb.append('\n');
        System.out.print(sb);
    }
}
""",
    )
