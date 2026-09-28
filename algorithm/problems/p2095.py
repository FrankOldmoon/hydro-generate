# -*- coding: utf-8 -*-
"""P2095 迷宫可达性"""
from generate import make_problem


def solve(grid, n, m):
    # DFS 判断从 (1,1) 能否到达 (n,m)
    if grid[0][0] == '#' or grid[n - 1][m - 1] == '#':
        return False
    visited = [[False] * m for _ in range(n)]
    stack = [(0, 0)]
    visited[0][0] = True
    while stack:
        r, c = stack.pop()
        if r == n - 1 and c == m - 1:
            return True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.' and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
    return False


def build():
    grids = [
        (1, 1, ["."]),
        (1, 3, ["..."]),
        (3, 3, ["...", "...", "..."]),
        (3, 3, [".#.", ".#.", ".#."]),
        (3, 3, ["...", "###", "..."]),
        (5, 5, [".....", ".###.", ".#.#.", ".###.", "....."]),
        (4, 4, ["....", ".##.", ".##.", "...."]),
        (5, 5, ["....#", "....#", "#####", "...#.", "...#."]),
        (5, 5, [".....", ".....", ".....", ".....", "....."]),
        (2, 2, [".#", "#."]),
    ]
    cases = []
    for n, m, g in grids:
        inp = f"{n} {m}\n" + "\n".join(g) + "\n"
        out = "Yes\n" if solve(g, n, m) else "No\n"
        cases.append((inp, out))
    return make_problem(
        "P2095", "迷宫可达性", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m maze where '#' is a wall and '.' is a road, "
                 "determine whether one can travel from the top-left cell "
                 "(1,1) to the bottom-right cell (n,m) moving up, down, left "
                 "or right. Print Yes if reachable, otherwise No."),
        input_en=("The first line contains n and m. Then n lines follow, each "
                  "a string of m characters ('#' or '.'). "
                  "$1\\leq n,m\\leq 50$ ."),
        output_en="Yes or No.",
        desc_zh="给定 n×m 迷宫（'#' 为墙，'.' 为路），判断能否从左上角 (1,1) 出发，每步向上、下、左、右移动一格，到达右下角 (n,m)，能到达输出 Yes，否则输出 No。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的字符串（仅含 '#' 和 '.'），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="一行，Yes 或 No。",
        py="""# P2095 迷宫可达性
n, m = map(int, input().split())            # 读入行数列数
grid = [input().strip() for _ in range(n)]  # 读入迷宫
visited = [[False] * m for _ in range(n)]
ans = "No"
if grid[0][0] != '#' and grid[n-1][m-1] != '#':
    stack = [(0, 0)]                        # DFS 栈
    visited[0][0] = True
    while stack:
        r, c = stack.pop()
        if r == n-1 and c == m-1:           # 到达终点
            ans = "Yes"
            break
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.' and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
print(ans)
""",
        cpp="""// P2095 迷宫可达性
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;                            // 读入行数列数
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];  // 读入迷宫
    vector<vector<bool>> vis(n, vector<bool>(m, false));
    string ans = "No";
    if (grid[0][0] != '#' && grid[n-1][m-1] != '#') {
        stack<pair<int,int>> st;             // DFS 栈
        st.push(make_pair(0, 0));
        vis[0][0] = true;
        int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
        while (!st.empty()) {
            pair<int,int> cur = st.top(); st.pop();
            int r = cur.first, c = cur.second;
            if (r == n-1 && c == m-1) { ans = "Yes"; break; }  // 到达终点
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m
                    && grid[nr][nc] == '.' && !vis[nr][nc]) {
                    vis[nr][nc] = true;
                    st.push(make_pair(nr, nc));
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
""",
        java="""// P2095 迷宫可达性
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();   // 读入行数列数
        char[][] grid = new char[n][m];
        for (int i = 0; i < n; i++) {             // 读入迷宫
            String s = sc.next();
            for (int j = 0; j < m; j++) grid[i][j] = s.charAt(j);
        }
        boolean[][] vis = new boolean[n][m];
        String ans = "No";
        if (grid[0][0] != '#' && grid[n-1][m-1] != '#') {
           Deque<int[]> st = new ArrayDeque<int[]>();  // DFS 栈
            st.push(new int[]{0, 0});
            vis[0][0] = true;
            int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
            while (!st.isEmpty()) {
                int[] cur = st.pop();
                int r = cur[0], c = cur[1];
                if (r == n-1 && c == m-1) { ans = "Yes"; break; }  // 到达终点
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m
                        && grid[nr][nc] == '.' && !vis[nr][nc]) {
                        vis[nr][nc] = true;
                        st.push(new int[]{nr, nc});
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
""",
    )
