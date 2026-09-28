# -*- coding: utf-8 -*-
"""P2022 第k小元素"""
from generate import make_problem


def build():
    # (n, 数组, k)：升序后第 k 个（1-based）
    data = [
        (5, [3, 1, 2, 5, 4], 3),
        (8, [8, 7, 6, 5, 4, 3, 2, 1], 1),
        (1, [42], 1),
        (6, [1, 2, 3, 4, 5, 6], 6),
        (6, [6, 5, 4, 3, 2, 1], 2),
        (10, [4, 4, 1, 3, 2, 4, 1, 2, 5, 3], 5),
        (2, [100, -100], 2),
        (7, [5, 5, 5, 5, 5, 5, 5], 4),
        (9, [5, -3, 8, -1, 0, 7, -2, 6, 4], 9),
        (20, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4], 10),
    ]
    cases = []
    for n, a, k in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n{k}\n"
        b = sorted(a)                            # 升序排序
        out = f"{b[k - 1]}\n"                    # 第 k 小（1-based）
        cases.append((inp, out))
    return make_problem(
        "P2022", "第k小元素", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers and an integer k, output the k-th smallest "
                "element (1-based), i.e. the k-th element after sorting in "
                "ascending order.",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers. The third line contains an "
                 "integer k, satisfying $1\\leq n\\leq 100$, "
                 "$-1000\\leq a_i\\leq 1000$ and $1\\leq k\\leq n$ .",
        output_en="One line containing the k-th smallest element.",
        desc_zh="给定 n 个整数和整数 k，输出第 k 小的元素（1-based，即升序排序后第 k 个）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，第三行一个整数 k，满足 $1\\leq n\\leq 100$、$-1000\\leq a_i\\leq 1000$ 且 $1\\leq k\\leq n$ 。",
        output_zh="一行一个整数，表示第 k 小的元素。",
        py=r"""# P2022 第k小元素（升序排序后取第 k 个）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
k = int(input())                       # 待查询的 k（1-based）
a.sort()                               # 升序排序
print(a[k - 1])                        # 输出第 k 小（升序后第 k 个）
""",
        cpp=r"""// P2022 第k小元素（升序排序后取第 k 个）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    int a[105];
    for (int i = 0; i < n; i++) cin >> a[i];
    int k;
    cin >> k;                          // 待查询的 k
    sort(a, a + n);                    // 升序排序
    cout << a[k - 1] << endl;          // 输出第 k 小
    return 0;
}
""",
        java=r"""// P2022 第k小元素（升序排序后取第 k 个）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int k = sc.nextInt();          // 待查询的 k
        Arrays.sort(a);                // 升序排序
        System.out.println(a[k - 1]);  // 输出第 k 小
    }
}
""",
    )
