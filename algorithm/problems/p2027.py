# -*- coding: utf-8 -*-
"""P2027 逆序对个数"""
from generate import make_problem


def build():
    # (n, 数组)：统计逆序对个数 i<j 且 a[i]>a[j]
    data = [
        (5, [3, 1, 2, 5, 4]),
        (8, [8, 7, 6, 5, 4, 3, 2, 1]),
        (1, [42]),
        (6, [1, 2, 3, 4, 5, 6]),
        (6, [6, 5, 4, 3, 2, 1]),
        (5, [5, 5, 5, 5, 5]),
        (2, [100, -100]),
        (7, [3, 1, 3, 1, 3, 1, 3]),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4]),
        (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        # 暴力 O(n^2) 统计，作为标准答案（与归并排序结果一致）
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] > a[j]:
                    cnt += 1
        out = f"{cnt}\n"
        cases.append((inp, out))
    return make_problem(
        "P2027", "逆序对个数", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers, count the number of inversion pairs. A pair "
                "(i, j) is an inversion when i < j and a[i] > a[j]. A merge-sort "
                "based approach is recommended.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying "
                 "$1\\leq n\\leq 100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing the number of inversion pairs.",
        desc_zh="给定 n 个整数，统计逆序对个数（满足 i<j 且 a[i]>a[j] 的数对数目），可用归并排序思想求解。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行一个整数，表示逆序对的个数。",
        py=r"""# P2027 逆序对个数（归并排序思想：合并时统计逆序对）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
tmp = [0] * n                          # 归并辅助数组

def merge_sort(l, r):                  # 统计 [l,r) 内逆序对数并排序
    if r - l <= 1:
        return 0
    mid = (l + r) // 2
    cnt = merge_sort(l, mid) + merge_sort(mid, r)
    i, j, p = l, mid, l
    while i < mid and j < r:           # 双指针合并
        if a[i] <= a[j]:
            tmp[p] = a[i]
            i += 1
        else:
            tmp[p] = a[j]
            j += 1
            cnt += mid - i             # 左侧剩余元素均与 a[j] 构成逆序对
        p += 1
    while i < mid:
        tmp[p] = a[i]
        i += 1
        p += 1
    while j < r:
        tmp[p] = a[j]
        j += 1
        p += 1
    for t in range(l, r):
        a[t] = tmp[t]
    return cnt

print(merge_sort(0, n))                # 输出逆序对个数
""",
        cpp=r"""// P2027 逆序对个数（归并排序思想：合并时统计逆序对）
#include <iostream>
using namespace std;
int a[105], tmp[105];
long long merge_sort(int l, int r) {   // 统计 [l,r) 内逆序对数并排序
    if (r - l <= 1) return 0;
    int mid = (l + r) / 2;
    long long cnt = merge_sort(l, mid) + merge_sort(mid, r);
    int i = l, j = mid, p = l;
    while (i < mid && j < r) {         // 双指针合并
        if (a[i] <= a[j]) tmp[p++] = a[i++];
        else { tmp[p++] = a[j++]; cnt += mid - i; }  // 左侧剩余均构成逆序对
    }
    while (i < mid) tmp[p++] = a[i++];
    while (j < r) tmp[p++] = a[j++];
    for (int t = l; t < r; t++) a[t] = tmp[t];
    return cnt;
}
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << merge_sort(0, n) << endl;  // 输出逆序对个数
    return 0;
}
""",
        java=r"""// P2027 逆序对个数（归并排序思想：合并时统计逆序对）
import java.util.Scanner;
public class Main {
    static int[] a, tmp;
    static long mergeSort(int l, int r) {  // 统计 [l,r) 内逆序对数并排序
        if (r - l <= 1) return 0;
        int mid = (l + r) / 2;
        long cnt = mergeSort(l, mid) + mergeSort(mid, r);
        int i = l, j = mid, p = l;
        while (i < mid && j < r) {     // 双指针合并
            if (a[i] <= a[j]) tmp[p++] = a[i++];
            else { tmp[p++] = a[j++]; cnt += mid - i; }  // 左侧剩余均构成逆序对
        }
        while (i < mid) tmp[p++] = a[i++];
        while (j < r) tmp[p++] = a[j++];
        for (int t = l; t < r; t++) a[t] = tmp[t];
        return cnt;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        a = new int[n]; tmp = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        System.out.println(mergeSort(0, n));  // 输出逆序对个数
    }
}
""",
    )
