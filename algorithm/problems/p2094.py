# -*- coding: utf-8 -*-
"""P2094 岛屿数量"""
from collections import deque
from generate import make_problem


def solve(grid, n, m):
    # 统计被水包围的陆地块数（即 '1' 的连通块个数）
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    return cnt


def build():
    grids = [
        (1, 1, ["1"]),
        (1, 3, ["010"]),
        (3, 3, ["010", "000", "010"]),
        (3, 3, ["111", "000", "111"]),
        (4, 4, ["1000", "0100", "0010", "0001"]),
        (5, 5, ["11111", "00000", "11111", "00000", "11111"]),
        (4, 4, ["1111", "1001", "1001", "1111"]),
        (5, 5, ["10101", "01010", "10101", "01010", "10101"]),
        (3, 3, ["000", "000", "000"]),
        (5, 5, ["11000", "01100", "00110", "00011", "00001"]),
    ]
    cases = []
    for n, m, g in grids:
        inp = f"{n} {m}\n" + "\n".join(g) + "\n"
        out = f"{solve(g, n, m)}\n"
        cases.append((inp, out))
    return make_problem(
        "P2094", "岛屿数量", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m grid where '1' is land and '0' is water, an "
                 "island is a group of land cells connected up, down, left or "
                 "right and surrounded by water. Find the number of islands."),
        input_en=("The first line contains n and m. Then n lines follow, each "
                  "a string of m characters ('0' or '1'). "
                  "$1\\leq n,m\\leq 50$ ."),
        output_en="One integer: the number of islands.",
        desc_zh="给定 n×m 网格（'1' 为陆地，'0' 为水），被水完全包围、上下左右相连的陆地块称为一座岛屿，求岛屿的数量。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的字符串（仅含 '0' 和 '1'），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="一个整数，表示岛屿的数量。",
        py="""# P2094 岛屿数量
from collections import deque
n, m = map(int, input().split())            # 读入行数列数
grid = [input().strip() for _ in range(n)]  # 读入网格
visited = [[False] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and not visited[i][j]:
            ans += 1                         # 发现新岛屿
            q = deque([(i, j)])
            visited[i][j] = True
            while q:                         # BFS 标记整座岛
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
print(ans)
""",
        cpp="""// P2094 岛屿数量
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
    int ans = 0;
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (grid[i][j] == '1' && !vis[i][j]) {
                ans++;                        // 发现新岛屿
                queue<pair<int,int>> q;
                q.push(make_pair(i, j));
                vis[i][j] = true;
                while (!q.empty()) {          // BFS 标记整座岛
                    pair<int,int> cur = q.front(); q.pop();
                    int r = cur.first, c = cur.second;
                    for (int k = 0; k < 4; k++) {
                        int nr = r + dr[k], nc = c + dc[k];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m
                            && grid[nr][nc] == '1' && !vis[nr][nc]) {
                            vis[nr][nc] = true;
                            q.push(make_pair(nr, nc));
                        }
                    }
                }
            }
    cout << ans << endl;
    return 0;
}
""",
        java="""// P2094 岛屿数量
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
        int ans = 0;
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (grid[i][j] == '1' && !vis[i][j]) {
                    ans++;                        // 发现新岛屿
                    Queue<int[]> q = new ArrayDeque<int[]>();
                    q.add(new int[]{i, j});
                    vis[i][j] = true;
                    while (!q.isEmpty()) {        // BFS 标记整座岛
                        int[] cur = q.poll();
                        int r = cur[0], c = cur[1];
                        for (int k = 0; k < 4; k++) {
                            int nr = r + dr[k], nc = c + dc[k];
                            if (nr >= 0 && nr < n && nc >= 0 && nc < m
                                && grid[nr][nc] == '1' && !vis[nr][nc]) {
                                vis[nr][nc] = true;
                                q.add(new int[]{nr, nc});
                            }
                        }
                    }
                }
        System.out.println(ans);
    }
}
""",
    )
