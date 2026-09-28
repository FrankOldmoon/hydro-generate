# -*- coding: utf-8 -*-
"""P2100 最大连通块面积"""
from collections import deque
from generate import make_problem


def solve(grid, n, m):
    # 求最大 '1' 连通块的面积（格数）
    visited = [[False] * m for _ in range(n)]
    best = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                cnt = 0
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    cnt += 1
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                if cnt > best:
                    best = cnt
    return best


def build():
    grids = [
        (1, 1, ["1"]),
        (1, 5, ["10101"]),
        (3, 3, ["111", "101", "111"]),
        (3, 3, ["111", "000", "111"]),
        (5, 5, ["11111", "11111", "11111", "11111", "11111"]),
        (4, 4, ["1001", "0110", "0110", "1001"]),
        (5, 5, ["11000", "01100", "00110", "00011", "00001"]),
        (3, 3, ["000", "000", "000"]),
        (5, 5, ["11100", "11000", "00000", "00111", "00111"]),
        (4, 5, ["11111", "10001", "10001", "11111"]),
    ]
    cases = []
    for n, m, g in grids:
        inp = f"{n} {m}\n" + "\n".join(g) + "\n"
        out = f"{solve(g, n, m)}\n"
        cases.append((inp, out))
    return make_problem(
        "P2100", "最大连通块面积", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m grid where '1' is land and '0' is water, the "
                 "area of a land region is the number of land cells connected "
                 "up, down, left or right. Find the maximum area among all "
                 "land regions. If there is no land, output 0."),
        input_en=("The first line contains n and m. Then n lines follow, each "
                  "a string of m characters ('0' or '1'). "
                  "$1\\leq n,m\\leq 50$ ."),
        output_en="One integer: the maximum land region area.",
        desc_zh="给定 n×m 网格（'1' 为陆地，'0' 为水），上下左右相连的陆地区域的面积为其中陆地格数，求最大陆地区域的面积，若无陆地输出 0。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的字符串（仅含 '0' 和 '1'），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="一个整数，表示最大陆地区域的面积。",
        py="""# P2100 最大连通块面积
from collections import deque
n, m = map(int, input().split())            # 读入行数列数
grid = [input().strip() for _ in range(n)]  # 读入网格
visited = [[False] * m for _ in range(n)]
best = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and not visited[i][j]:
            cnt = 0
            q = deque([(i, j)])             # BFS 统计本块面积
            visited[i][j] = True
            while q:
                r, c = q.popleft()
                cnt += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            if cnt > best:                  # 更新最大值
                best = cnt
print(best)
""",
        cpp="""// P2100 最大连通块面积
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;                            // 读入行数列数
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];  // 读入网格
    vector<vector<bool>> vis(n, vector<bool>(m, false));
    int best = 0;
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (grid[i][j] == '1' && !vis[i][j]) {
                int cnt = 0;
                queue<pair<int,int>> q;       // BFS 统计本块面积
                q.push(make_pair(i, j));
                vis[i][j] = true;
                while (!q.empty()) {
                    pair<int,int> cur = q.front(); q.pop();
                    int r = cur.first, c = cur.second;
                    cnt++;
                    for (int k = 0; k < 4; k++) {
                        int nr = r + dr[k], nc = c + dc[k];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m
                            && grid[nr][nc] == '1' && !vis[nr][nc]) {
                            vis[nr][nc] = true;
                            q.push(make_pair(nr, nc));
                        }
                    }
                }
                if (cnt > best) best = cnt;   // 更新最大值
            }
    cout << best << endl;
    return 0;
}
""",
        java="""// P2100 最大连通块面积
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();   // 读入行数列数
        char[][] grid = new char[n][m];
        for (int i = 0; i < n; i++) {             // 读入网格
            String s = sc.next();
            for (int j = 0; j < m; j++) grid[i][j] = s.charAt(j);
        }
        boolean[][] vis = new boolean[n][m];
        int best = 0;
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (grid[i][j] == '1' && !vis[i][j]) {
                    int cnt = 0;
                    Queue<int[]> q = new ArrayDeque<int[]>();  // BFS 统计本块面积
                    q.add(new int[]{i, j});
                    vis[i][j] = true;
                    while (!q.isEmpty()) {
                        int[] cur = q.poll();
                        int r = cur[0], c = cur[1];
                        cnt++;
                        for (int k = 0; k < 4; k++) {
                            int nr = r + dr[k], nc = c + dc[k];
                            if (nr >= 0 && nr < n && nc >= 0 && nc < m
                                && grid[nr][nc] == '1' && !vis[nr][nc]) {
                                vis[nr][nc] = true;
                                q.add(new int[]{nr, nc});
                            }
                        }
                    }
                    if (cnt > best) best = cnt;   // 更新最大值
                }
        System.out.println(best);
    }
}
""",
    )
