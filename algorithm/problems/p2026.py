# -*- coding: utf-8 -*-
"""P2026 求排名"""
from generate import make_problem


def build():
    # (n, 数组)：紧凑排名，相同数排名相同，按原顺序输出
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
        (8, [10, 20, 10, 30, 20, 10, 40, 30]),
    ]
    cases = []
    for n, a in data:
        inp = f"{n}\n{' '.join(map(str, a))}\n"
        uniq = sorted(set(a))                    # 升序排序并去重
        rank = {v: i + 1 for i, v in enumerate(uniq)}  # 值→紧凑排名（1-based）
        out = ' '.join(str(rank[v]) for v in a) + '\n'  # 按原顺序输出排名
        cases.append((inp, out))
    return make_problem(
        "P2026", "求排名", ["算法", "排序"],
        cases=cases,
        desc_en="Given n integers, output the ascending rank of each number in the "
                "original input order. Ranks start from 1, equal numbers share the "
                "same rank, and ranks are compact (e.g. 1, 1, 3).",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying "
                 "$1\\leq n\\leq 100$ and $-1000\\leq a_i\\leq 1000$ .",
        output_en="One line containing n ranks corresponding to the input order, "
                  "separated by spaces.",
        desc_zh="给定 n 个整数，按原输入顺序输出每个数的升序排名（排名从 1 开始，相同数排名相同，紧凑排名如 1,1,3）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 100$ 且 $-1000\\leq a_i\\leq 1000$ 。",
        output_zh="一行 n 个用空格分隔的整数，表示按原输入顺序每个数的升序排名。",
        py=r"""# P2026 求排名（排序去重建立值到紧凑排名的映射，按原顺序输出）
n = int(input())                       # 元素个数 n
a = list(map(int, input().split()))    # 读入 n 个整数
uniq = sorted(set(a))                  # 升序排序并去重
rank = {v: i + 1 for i, v in enumerate(uniq)}  # 值→紧凑排名（1-based）
print(' '.join(str(rank[v]) for v in a))       # 按原顺序输出每个数的排名
""",
        cpp=r"""// P2026 求排名（排序去重后二分查找排名，按原顺序输出）
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;                          // 元素个数 n
    int a[105], b[105];
    for (int i = 0; i < n; i++) { cin >> a[i]; b[i] = a[i]; }
    sort(b, b + n);                    // 升序排序
    int k = 0;                         // 就地去重
    for (int i = 0; i < n; i++)
        if (i == 0 || b[i] != b[i - 1]) b[k++] = b[i];
    for (int i = 0; i < n; i++) {      // 按原顺序输出每个数的排名
        int p = lower_bound(b, b + k, a[i]) - b;  // 二分查找值的位置
        if (i) cout << ' ';
        cout << (p + 1);               // 排名 = 位置 + 1
    }
    cout << endl;
    return 0;
}
""",
        java=r"""// P2026 求排名（排序去重后二分查找排名，按原顺序输出）
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 元素个数 n
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) { a[i] = sc.nextInt(); b[i] = a[i]; }
        Arrays.sort(b);                // 升序排序
        int k = 0;                     // 就地去重
        for (int i = 0; i < n; i++)
            if (i == 0 || b[i] != b[i - 1]) b[k++] = b[i];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {  // 按原顺序输出每个数的排名
            int p = Arrays.binarySearch(b, 0, k, a[i]);  // 二分查找值的位置
            if (i > 0) sb.append(' ');
            sb.append(p + 1);          // 排名 = 位置 + 1
        }
        sb.append('\n');
        System.out.print(sb);
    }
}
""",
    )
