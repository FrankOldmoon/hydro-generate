# -*- coding: utf-8 -*-
"""P2079 最长回文子序列"""
from generate import make_problem


def lps(s):
    n = len(s)
    if n == 0:
        return 0
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                f[i][j] = (f[i + 1][j - 1] if length > 2 else 0) + 2
            else:
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
    return f[0][n - 1]


def build():
    data = [
        "bbbab",
        "cbbd",
        "a",
        "abcba",
        "abcdef",
        "aaa",
        "abacaba",
        "abcde",
        "aabbaa",
        "abac",
    ]
    cases = []
    for s in data:
        cases.append((f"{s}\n", f"{lps(s)}\n"))
    return make_problem(
        "P2079", "最长回文子序列", ["算法", "线性DP"],
        cases=cases,
        desc_en="Given a string s, find the length of its longest palindromic "
                "subsequence.",
        input_en="One line containing a non-empty string of lowercase letters "
                 "(length up to 1000).",
        output_en="The length of the longest palindromic subsequence.",
        desc_zh="给定一个字符串s，求其最长回文子序列的长度。",
        input_zh="一行一个由小写字母组成的非空字符串（长度不超过1000）。",
        output_zh="最长回文子序列的长度。",
        py="""# P2079 最长回文子序列（动态规划）
s = input().strip()                   # 字符串 s
n = len(s)
# f[i][j] 表示 s[i..j] 内最长回文子序列长度
f = [[0] * n for _ in range(n)]
for i in range(n):
    f[i][i] = 1                       # 单字符回文长度为1
for length in range(2, n + 1):        # 按区间长度递推
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j]:              # 两端相等，可同时加入
            f[i][j] = (f[i + 1][j - 1] if length > 2 else 0) + 2
        else:                         # 否则舍去一端取较大者
            f[i][j] = max(f[i + 1][j], f[i][j - 1])
print(f[0][n - 1])                    # 输出最长回文子序列长度
""",
        cpp="""// P2079 最长回文子序列（动态规划）
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string s;
    cin >> s;                         // 字符串 s
    int n = s.size();
    // f[i][j] 表示 s[i..j] 内最长回文子序列长度
    vector<vector<int>> f(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) f[i][i] = 1;  // 单字符回文长度为1
    for (int len = 2; len <= n; len++) {      // 按区间长度递推
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1;
            if (s[i] == s[j])                  // 两端相等，可同时加入
                f[i][j] = (len > 2 ? f[i + 1][j - 1] : 0) + 2;
            else                               // 否则舍去一端取较大者
                f[i][j] = max(f[i + 1][j], f[i][j - 1]);
        }
    }
    cout << f[0][n - 1] << endl;      // 输出最长回文子序列长度
    return 0;
}
""",
        java="""// P2079 最长回文子序列（动态规划）
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();         // 字符串 s
        int n = s.length();
        // f[i][j] 表示 s[i..j] 内最长回文子序列长度
        int[][] f = new int[n][n];
        for (int i = 0; i < n; i++) f[i][i] = 1;  // 单字符回文长度为1
        for (int len = 2; len <= n; len++) {      // 按区间长度递推
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j))    // 两端相等，可同时加入
                    f[i][j] = (len > 2 ? f[i + 1][j - 1] : 0) + 2;
                else                               // 否则舍去一端取较大者
                    f[i][j] = Math.max(f[i + 1][j], f[i][j - 1]);
            }
        }
        System.out.println(f[0][n - 1]);  // 输出最长回文子序列长度
    }
}
""",
    )
