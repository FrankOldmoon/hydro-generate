# -*- coding: utf-8 -*-
"""P2023 中位数"""
from generate import make_problem


def build():
    # (n, 数组)：n 为奇数，输出升序后正中间元素
    data = [
        (5, [3, 1, 2, 5, 4]),
        (7, [8, 7, 6, 5, 4, 3, 2]),
        (1, [42]),
        (3, [1, 2, 3]),
        (3, [3, 2, 1]),
        (9, [4, 4, 1, 3, 2, 4, 1, 2, 5]),
        (5, [100, -100, 0, 50, -50]),
        (7, [5, 5, 5, 5, 5, 5, 5]),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4]),
        (15, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        b = sorted(a)                            # 升序排序
        out = f"{b[n // 2]}\n"                   # 正中间元素即中位数
        cases.append((inp, out))
    return make_problem(
        "P2023", "中位数", ["算法", "排序"],
        cases=cases,
        desc_en="Given an odd integer n and n integers, output the median, i.e. "
                "the middle element after sorting in ascending order.",
        input_en="The first line contains an odd positive integer n. The second "
                 "line contains n space-separated integers, satisfying "
                 "$1\\leq n\\leq 99$ (n is odd) and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing the median.",
        desc_zh="给定奇数 n 和 n 个整数，输出中位数（升序排序后正中间那个元素）。",
        input_zh="第一行一个正奇数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 99$（n 为奇数）且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行一个整数，表示中位数。",
        py=r"""# P2023 中位数（升序排序后取正中间元素）
n = int(input())                       # 元素个数 n（奇数）
a = list(map(int, input().split()))    # 读入 n 个整数
a.sort()                               # 升序排序
print(a[n // 2])                       # 正中间元素即中位数
""",
        cpp=r"""// P2023 中位数（升序排序后取正中间元素）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n（奇数）
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);                    // 升序排序
    cout << a[n / 2] << endl;          // 正中间元素即中位数
    return 0;
}
""",
        java=r"""// P2023 中位数（升序排序后取正中间元素）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n（奇数）
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        Arrays.sort(a);                // 升序排序
        System.out.println(a[n / 2]);  // 正中间元素即中位数
    }
}
""",
    )
