# -*- coding: utf-8 -*-
"""P2096 最少步数BFS"""
from collections import deque
from generate import make_problem


def solve(grid, n, m):
    # BFS 求从 S 到 E 的最少步数
    sr = sc = er = ec = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sr, sc = i, j
            elif grid[i][j] == 'E':
                er, ec = i, j
    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if r == er and c == ec:
            return dist[r][c]
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return -1


def build():
    grids = [
        (1, 3, ["S.E"]),
        (3, 3, ["S..", "...", "..E"]),
        (3, 3, ["S#.", ".#.", ".#E"]),
        (3, 3, ["S..", "###", "..E"]),
        (5, 5, ["S....", ".###.", ".....", ".###.", "....E"]),
        (5, 5, ["S....", ".....", ".....", ".....", "....E"]),
        (4, 4, ["S..#", "...#", "...#", "...E"]),
        (3, 4, ["S...", ".##.", "...E"]),
        (5, 5, ["S####", ".....", "####.", ".....", "....E"]),
        (5, 5, ["S...#", "####.", "....#", ".####", "....E"]),
    ]
    cases = []
    for n, m, g in grids:
        inp = f"{n} {m}\n" + "\n".join(g) + "\n"
        out = f"{solve(g, n, m)}\n"
        cases.append((inp, out))
    return make_problem(
        "P2096", "最少步数BFS", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m maze where '#' is a wall, '.' is a road, 'S' "
                 "is the start and 'E' is the end, find the minimum number of "
                 "steps from S to E moving up, down, left or right. If "
                 "unreachable, output -1."),
        input_en=("The first line contains n and m. Then n lines follow, each "
                  "a string of m characters ('#', '.', 'S' or 'E'). The maze "
                  "contains exactly one S and one E. $1\\leq n,m\\leq 50$ ."),
        output_en="One integer: the minimum steps, or -1 if unreachable.",
        desc_zh="给定 n×m 迷宫（'#' 墙、'.' 路、'S' 起点、'E' 终点），求从 S 走到 E 的最少步数，每步可向上、下、左、右移动一格，不可达输出 -1。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的字符串（含 '#'、'.'、'S'、'E'，恰有一个 S 和一个 E），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="一个整数，表示最少步数；若不可达输出 -1。",
        py="""# P2096 最少步数BFS
from collections import deque
n, m = map(int, input().split())            # 读入行数列数
grid = [input().strip() for _ in range(n)]  # 读入迷宫
sr = sc = er = ec = -1
for i in range(n):                          # 找起点 S 和终点 E
    for j in range(m):
        if grid[i][j] == 'S':
            sr, sc = i, j
        elif grid[i][j] == 'E':
            er, ec = i, j
dist = [[-1] * m for _ in range(n)]
dist[sr][sc] = 0
q = deque([(sr, sc)])
ans = -1
while q:                                    # BFS
    r, c = q.popleft()
    if r == er and c == ec:                 # 到达终点
        ans = dist[r][c]
        break
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
print(ans)
""",
        cpp="""// P2096 最少步数BFS
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
    int sr = -1, sc = -1, er = -1, ec = -1;
    for (int i = 0; i < n; i++)               // 找起点 S 和终点 E
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'S') { sr = i; sc = j; }
            else if (grid[i][j] == 'E') { er = i; ec = j; }
        }
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int,int>> q;
    dist[sr][sc] = 0;
    q.push(make_pair(sr, sc));
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    int ans = -1;
    while (!q.empty()) {                      // BFS
        pair<int,int> cur = q.front(); q.pop();
        int r = cur.first, c = cur.second;
        if (r == er && c == ec) { ans = dist[r][c]; break; }  // 到达终点
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m
                && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push(make_pair(nr, nc));
            }
        }
    }
    cout << ans << endl;
    return 0;
}
""",
        java="""// P2096 最少步数BFS
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
        int sr = -1, scol = -1, er = -1, ecol = -1;
        for (int i = 0; i < n; i++)               // 找起点 S 和终点 E
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'S') { sr = i; scol = j; }
                else if (grid[i][j] == 'E') { er = i; ecol = j; }
            }
        int[][] dist = new int[n][m];
        for (int[] t : dist) Arrays.fill(t, -1);
        Queue<int[]> q = new ArrayDeque<int[]>();
        dist[sr][scol] = 0;
        q.add(new int[]{sr, scol});
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        int ans = -1;
        while (!q.isEmpty()) {                    // BFS
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == er && c == ecol) { ans = dist[r][c]; break; }  // 到达终点
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m
                    && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
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
