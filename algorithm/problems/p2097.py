# -*- coding: utf-8 -*-
"""P2097 全排列"""
from generate import make_problem


def solve(n):
    # DFS 生成 1..n 的所有全排列（字典序）
    res = []
    used = [False] * (n + 1)
    path = []

    def dfs():
        if len(path) == n:
            res.append(" ".join(map(str, path)))
            return
        for x in range(1, n + 1):
            if not used[x]:
                used[x] = True
                path.append(x)
                dfs()
                path.pop()
                used[x] = False

    dfs()
    return res


def build():
    ns = [1, 2, 3, 4, 5, 2, 3, 4, 5, 3]
    cases = []
    for n in ns:
        inp = f"{n}\n"
        out = "\n".join(solve(n)) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2097", "全排列", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an integer n, output all permutations of 1, 2, ..., n "
                 "in lexicographic order. Each permutation is on one line, "
                 "with numbers separated by single spaces."),
        input_en="One integer n. $1\\leq n\\leq 5$ .",
        output_en="All permutations of 1..n in lexicographic order, one per line.",
        desc_zh="给定整数 n，按字典序输出 1 到 n 的所有全排列，每个排列占一行，数之间用一个空格分隔。",
        input_zh="一行一个整数 n，满足 $1\\leq n\\leq 5$ 。",
        output_zh="若干行，每行一个全排列，按字典序输出。",
        py="""# P2097 全排列
n = int(input())                            # 读入 n
used = [False] * (n + 1)
path = []
out = []
def dfs():
    if len(path) == n:                      # 已选满 n 个
        out.append(" ".join(map(str, path)))
        return
    for x in range(1, n + 1):               # 字典序尝试每个数
        if not used[x]:
            used[x] = True
            path.append(x)
            dfs()                           # 递归
            path.pop()
            used[x] = False
dfs()
print("\\n".join(out))
""",
        cpp="""// P2097 全排列
#include <iostream>
#include <vector>
using namespace std;
int n;
bool used[10];
int path[10];
// DFS 生成全排列
void dfs(int dep) {
    if (dep == n) {                         // 已选满 n 个
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << path[i];
        }
        cout << '\\n';
        return;
    }
    for (int x = 1; x <= n; x++) {          // 字典序尝试每个数
        if (!used[x]) {
            used[x] = true;
            path[dep] = x;
            dfs(dep + 1);                   // 递归
            used[x] = false;
        }
    }
}
int main() {
    cin >> n;                               // 读入 n
    dfs(0);
    return 0;
}
""",
        java="""// P2097 全排列
import java.util.*;
public class Main {
    static int n;
    static boolean[] used;
    static int[] path;
    static StringBuilder sb = new StringBuilder();
    // DFS 生成全排列
    static void dfs(int dep) {
        if (dep == n) {                     // 已选满 n 个
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(path[i]);
            }
            sb.append('\\n');
            return;
        }
        for (int x = 1; x <= n; x++) {      // 字典序尝试每个数
            if (!used[x]) {
                used[x] = true;
                path[dep] = x;
                dfs(dep + 1);               // 递归
                used[x] = false;
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();                   // 读入 n
        used = new boolean[n + 1];
        path = new int[n];
        dfs(0);
        System.out.print(sb);
    }
}
""",
    )
