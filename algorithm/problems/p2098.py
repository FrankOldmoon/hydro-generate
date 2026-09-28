# -*- coding: utf-8 -*-
"""P2098 组合枚举"""
from generate import make_problem


def solve(n, k):
    # DFS 生成从 1..n 中选 k 个的所有组合（字典序）
    res = []
    path = []

    def dfs(start):
        if len(path) == k:
            res.append(" ".join(map(str, path)))
            return
        for x in range(start, n + 1):
            path.append(x)
            dfs(x + 1)
            path.pop()

    dfs(1)
    return res


def build():
    data = [(3, 2), (4, 2), (5, 3), (5, 1), (6, 2),
            (7, 3), (4, 3), (5, 5), (6, 4), (8, 2)]
    cases = []
    for n, k in data:
        inp = f"{n} {k}\n"
        out = "\n".join(solve(n, k)) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2098", "组合枚举", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given integers n and k, output all ways of choosing k "
                 "distinct numbers from 1 to n, in lexicographic order. Each "
                 "combination is on one line, numbers in increasing order "
                 "separated by single spaces."),
        input_en="One line with two integers n and k. $1\\leq k\\leq n\\leq 10$ .",
        output_en="All combinations in lexicographic order, one per line.",
        desc_zh="给定整数 n 和 k，按字典序输出从 1 到 n 中选出 k 个数的所有组合，每个组合占一行，数按升序排列并用一个空格分隔。",
        input_zh="一行两个整数 n 和 k，满足 $1\\leq k\\leq n\\leq 10$ 。",
        output_zh="若干行，每行一个组合，按字典序输出。",
        py="""# P2098 组合枚举
n, k = map(int, input().split())            # 读入 n 和 k
path = []
out = []
def dfs(start):
    if len(path) == k:                      # 已选满 k 个
        out.append(" ".join(map(str, path)))
        return
    for x in range(start, n + 1):           # 从 start 开始枚举，保证升序
        path.append(x)
        dfs(x + 1)                          # 递归，下一个数更大
        path.pop()
dfs(1)
print("\\n".join(out))
""",
        cpp="""// P2098 组合枚举
#include <iostream>
using namespace std;
int n, k;
int path[10];
// DFS 生成组合
void dfs(int start, int dep) {
    if (dep == k) {                         // 已选满 k 个
        for (int i = 0; i < k; i++) {
            if (i) cout << ' ';
            cout << path[i];
        }
        cout << '\\n';
        return;
    }
    for (int x = start; x <= n; x++) {      // 从 start 开始枚举，保证升序
        path[dep] = x;
        dfs(x + 1, dep + 1);                // 递归，下一个数更大
    }
}
int main() {
    cin >> n >> k;                          // 读入 n 和 k
    dfs(1, 0);
    return 0;
}
""",
        java="""// P2098 组合枚举
import java.util.*;
public class Main {
    static int n, k;
    static int[] path;
    static StringBuilder sb = new StringBuilder();
    // DFS 生成组合
    static void dfs(int start, int dep) {
        if (dep == k) {                     // 已选满 k 个
            for (int i = 0; i < k; i++) {
                if (i > 0) sb.append(' ');
                sb.append(path[i]);
            }
            sb.append('\\n');
            return;
        }
        for (int x = start; x <= n; x++) {  // 从 start 开始枚举，保证升序
            path[dep] = x;
            dfs(x + 1, dep + 1);            // 递归，下一个数更大
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); k = sc.nextInt(); // 读入 n 和 k
        path = new int[k];
        dfs(1, 0);
        System.out.print(sb);
    }
}
""",
    )
