# -*- coding: utf-8 -*-
"""P2078 编辑距离"""
from generate import make_problem


def edit(a, b):
    n, m = len(a), len(b)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        f[i][0] = i
    for j in range(m + 1):
        f[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[n][m]


def build():
    data = [
        ("horse", "ros"),
        ("intention", "execution"),
        ("abc", "abc"),
        ("abc", "abcd"),
        ("abcd", "abc"),
        ("kitten", "sitting"),
        ("sunday", "saturday"),
        ("a", "b"),
        ("abc", "def"),
        ("distance", "difference"),
    ]
    cases = []
    for a, b in data:
        cases.append((f"{a}\n{b}\n", f"{edit(a, b)}\n"))
    return make_problem(
        "P2078", "编辑距离", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given two strings a and b, you may insert, delete, or replace one "
                "character each operation. Find the minimum number of operations to "
                "turn a into b.",
        input_en="Two lines, each containing a non-empty string of lowercase "
                 "letters (length up to 1000).",
        output_en="The minimum number of operations (edit distance).",
        desc_zh="给定两个字符串a和b，每次可以插入、删除或替换一个字符，求把a变成b所需的最少操作数。",
        input_zh="两行，每行一个由小写字母组成的非空字符串（长度不超过1000）。",
        output_zh="最少操作数（编辑距离）。",
        py="""# P2078 编辑距离（线性DP）
a = input().strip()                   # 字符串 a
b = input().strip()                   # 字符串 b
n, m = len(a), len(b)
# f[i][j] 表示 a 前 i 个字符变成 b 前 j 个字符的最少操作数
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):                # a 前 i 个变成空串：删 i 次
    f[i][0] = i
for j in range(m + 1):                # 空串变成 b 前 j 个：插 j 次
    f[0][j] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:      # 字符相同无需操作
            f[i][j] = f[i - 1][j - 1]
        else:                         # 取删/插/换的最小值 +1
            f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
print(f[n][m])                        # 输出编辑距离
""",
        cpp="""// P2078 编辑距离（线性DP）
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string a, b;
    cin >> a >> b;                    // 字符串 a, b
    int n = a.size(), m = b.size();
    // f[i][j] 表示 a 前 i 个字符变成 b 前 j 个字符的最少操作数
    vector<vector<int>> f(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; i++) f[i][0] = i;      // a 前 i 个变成空串
    for (int j = 0; j <= m; j++) f[0][j] = j;      // 空串变成 b 前 j 个
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (a[i - 1] == b[j - 1])              // 字符相同无需操作
                f[i][j] = f[i - 1][j - 1];
            else                                   // 取删/插/换的最小值 +1
                f[i][j] = 1 + min(min(f[i - 1][j], f[i][j - 1]), f[i - 1][j - 1]);
    cout << f[n][m] << endl;        // 输出编辑距离
    return 0;
}
""",
        java="""// P2078 编辑距离（线性DP）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();         // 字符串 a
        String b = sc.next();         // 字符串 b
        int n = a.length(), m = b.length();
        // f[i][j] 表示 a 前 i 个字符变成 b 前 j 个字符的最少操作数
        int[][] f = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) f[i][0] = i;  // a 前 i 个变成空串
        for (int j = 0; j <= m; j++) f[0][j] = j;  // 空串变成 b 前 j 个
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (a.charAt(i - 1) == b.charAt(j - 1))  // 字符相同无需操作
                    f[i][j] = f[i - 1][j - 1];
                else                                    // 取删/插/换的最小值 +1
                    f[i][j] = 1 + Math.min(Math.min(f[i - 1][j], f[i][j - 1]), f[i - 1][j - 1]);
        System.out.println(f[n][m]);  // 输出编辑距离
    }
}
""",
    )
