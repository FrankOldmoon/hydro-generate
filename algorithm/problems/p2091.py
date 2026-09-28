# -*- coding: utf-8 -*-
"""P2091 迷宫最短路"""
from collections import deque
from generate import make_problem


def solve(grid, n, m):
    # BFS 求左上 (1,1) 到右下 (n,m) 的最少步数
    if grid[0][0] == '#' or grid[n - 1][m - 1] == '#':
        return -1
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:
            return dist[r][c]
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return -1


def build():
    grids = [
        (1, 1, ["."]),
        (1, 5, ["....."]),
        (3, 3, ["...", ".#.", "..."]),
        (3, 3, [".#.", ".#.", ".#."]),
        (5, 5, [".....", ".....", ".....", ".....", "....."]),
        (5, 5, [".....", ".###.", ".....", ".###.", "....."]),
        (4, 5, [".....", ".##..", "...#.", "....."]),
        (3, 4, ["....", ".##.", "...."]),
        (5, 5, [".....", "####.", ".....", ".####", "....."]),
        (5, 5, ["....#", "###.#", "#....", "#.###", "#...."]),
    ]
    cases = []
    for n, m, g in grids:
        inp = f"{n} {m}\n" + "\n".join(g) + "\n"
        out = f"{solve(g, n, m)}\n"
        cases.append((inp, out))
    return make_problem(
        "P2091", "迷宫最短路", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m maze where '#' is a wall and '.' is a road, "
                 "find the minimum number of steps to go from the top-left "
                 "cell (1,1) to the bottom-right cell (n,m), moving up, down, "
                 "left or right one cell per step. If it is unreachable, "
                 "output -1."),
        input_en=("The first line contains two integers n and m. Then n lines "
                  "follow, each being a string of m characters ('#' or '.'). "
                  "$1\\leq n,m\\leq 50$ ."),
        output_en="One integer: the minimum number of steps, or -1 if unreachable.",
        desc_zh="给定 n×m 迷宫（'#' 为墙，'.' 为路），求从左上角 (1,1) 走到右下角 (n,m) 的最少步数，每步可向上、下、左、右移动一格，不可达输出 -1。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的字符串（仅含 '#' 和 '.'），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="一个整数，表示最少步数；若不可达输出 -1。",
        py="""# P2091 迷宫最短路
from collections import deque
n, m = map(int, input().split())            # 读入行数列数
grid = [input().strip() for _ in range(n)]  # 读入迷宫
# 起点或终点是墙则不可达
if grid[0][0] == '#' or grid[n-1][m-1] == '#':
    print(-1)
else:
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 0
    q = deque([(0, 0)])                     # BFS 队列
    ans = -1
    while q:
        r, c = q.popleft()
        if r == n-1 and c == m-1:           # 到达终点
            ans = dist[r][c]
            break
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # 四方向
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    print(ans)
""",
        cpp="""// P2091 迷宫最短路
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;                            // 读入行数列数
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];  // 读入迷宫
    // 起点或终点是墙则不可达
    if (grid[0][0] == '#' || grid[n-1][m-1] == '#') {
        cout << -1 << endl;
        return 0;
    }
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int,int>> q;
    dist[0][0] = 0;
    q.push(make_pair(0, 0));                  // BFS 起点
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    int ans = -1;
    while (!q.empty()) {
        pair<int,int> cur = q.front(); q.pop();
        int r = cur.first, c = cur.second;
        if (r == n-1 && c == m-1) { ans = dist[r][c]; break; }  // 到达终点
        for (int k = 0; k < 4; k++) {         // 四方向
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m
                && grid[nr][nc] == '.' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push(make_pair(nr, nc));
            }
        }
    }
    cout << ans << endl;
    return 0;
}
""",
        java="""// P2091 迷宫最短路
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
        // 起点或终点是墙则不可达
        if (grid[0][0] == '#' || grid[n-1][m-1] == '#') {
            System.out.println(-1);
            return;
        }
        int[][] dist = new int[n][m];
        for (int[] t : dist) Arrays.fill(t, -1);
        Queue<int[]> q = new ArrayDeque<int[]>();
        dist[0][0] = 0;
        q.add(new int[]{0, 0});                   // BFS 起点
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        int ans = -1;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == n-1 && c == m-1) { ans = dist[r][c]; break; }  // 到达终点
            for (int k = 0; k < 4; k++) {         // 四方向
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m
                    && grid[nr][nc] == '.' && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        System.out.println(ans);
    }
}
""",
    )
