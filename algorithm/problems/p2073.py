# -*- coding: utf-8 -*-
"""P2073 最长公共子序列"""
from generate import make_problem


def lcs(a, b):
    n, m = len(a), len(b)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[n][m]


def build():
    data = [
        ("ABCBDAB", "BDCABA"),
        ("ABC", "ABC"),
        ("ABC", "DEF"),
        ("A", "A"),
        ("AGGTAB", "GXTXAYB"),
        ("abcdef", "acef"),
        ("abcd", "abcd"),
        ("abcde", "edcba"),
        ("aabbaa", "abaaba"),
        ("abc", "ab"),
    ]
    cases = []
    for a, b in data:
        cases.append((f"{a}\n{b}\n", f"{lcs(a, b)}\n"))
    return make_problem(
        "P2073", "最长公共子序列", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given two strings a and b, find the length of their longest "
                "common subsequence.",
        input_en="Two lines, each containing a non-empty string of lowercase "
                 "letters (length up to 1000).",
        output_en="The length of the longest common subsequence.",
        desc_zh="给定两个字符串a和b，求它们的最长公共子序列的长度。",
        input_zh="两行，每行一个由小写字母组成的非空字符串（长度不超过1000）。",
        output_zh="最长公共子序列的长度。",
        py="""# P2073 最长公共子序列（线性DP）
a = input().strip()                   # 字符串 a
b = input().strip()                   # 字符串 b
n, m = len(a), len(b)
# f[i][j] 表示 a 前 i 个字符与 b 前 j 个字符的 LCS 长度
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:      # 字符相等，可接续
            f[i][j] = f[i - 1][j - 1] + 1
        else:                         # 否则取较大者
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
print(f[n][m])                        # 输出 LCS 长度
""",
        cpp="""// P2073 最长公共子序列（线性DP）
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string a, b;
    cin >> a >> b;                    // 字符串 a, b
    int n = a.size(), m = b.size();
    // f[i][j] 表示 a 前 i 个字符与 b 前 j 个字符的 LCS 长度
    vector<vector<int>> f(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (a[i - 1] == b[j - 1]) // 字符相等，可接续
                f[i][j] = f[i - 1][j - 1] + 1;
            else                      // 否则取较大者
                f[i][j] = max(f[i - 1][j], f[i][j - 1]);
    cout << f[n][m] << endl;          // 输出 LCS 长度
    return 0;
}
""",
        java="""// P2073 最长公共子序列（线性DP）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();         // 字符串 a
        String b = sc.next();         // 字符串 b
        int n = a.length(), m = b.length();
        // f[i][j] 表示 a 前 i 个字符与 b 前 j 个字符的 LCS 长度
        int[][] f = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (a.charAt(i - 1) == b.charAt(j - 1))  // 字符相等，可接续
                    f[i][j] = f[i - 1][j - 1] + 1;
                else                  // 否则取较大者
                    f[i][j] = Math.max(f[i - 1][j], f[i][j - 1]);
        System.out.println(f[n][m]);  // 输出 LCS 长度
    }
}
""",
    )
