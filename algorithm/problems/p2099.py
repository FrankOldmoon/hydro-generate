# -*- coding: utf-8 -*-
"""P2099 马的遍历"""
from collections import deque
from generate import make_problem


def solve(n):
    # BFS 求马从 (1,1) 到各格的最少步数
    dist = [[-1] * n for _ in range(n)]
    if n == 0:
        return dist
    dist[0][0] = 0
    q = deque([(0, 0)])
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
             (2, 1), (2, -1), (-2, 1), (-2, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


def build():
    ns = [1, 2, 3, 4, 5, 3, 4, 5, 6, 8]
    cases = []
    for n in ns:
        inp = f"{n}\n"
        d = solve(n)
        out = "\n".join(" ".join(str(x) for x in row) for row in d) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2099", "马的遍历", ["算法", "搜索"],
        cases=cases,
        desc_en=("On an n*n chessboard, a knight starts at the top-left cell "
                 "(1,1) and moves in the eight L-shaped chess knight moves. "
                 "Find the minimum number of moves to reach every cell. If a "
                 "cell is unreachable, output -1. Print the n*n answer "
                 "matrix, numbers in a row separated by single spaces."),
        input_en="One integer n. $1\\leq n\\leq 50$ .",
        output_en="n rows, each with n integers separated by single spaces: the minimum moves, or -1.",
        desc_zh="在 n×n 棋盘上，马从左上角 (1,1) 出发，按国际象棋走日字（八个方向），求到达每个格子的最少步数，不可达输出 -1，按 n×n 矩阵输出，每行数之间用空格分隔。",
        input_zh="一行一个整数 n，满足 $1\\leq n\\leq 50$ 。",
        output_zh="n 行，每行 n 个整数（空格分隔），表示到各格的最少步数，不可达为 -1。",
        py="""# P2099 马的遍历
from collections import deque
n = int(input())                            # 读入 n
dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1)]  # 马的八个日字方向
while q:                                    # BFS
    r, c = q.popleft()
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
for row in dist:                            # 输出矩阵
    print(" ".join(map(str, row)))
""",
        cpp="""// P2099 马的遍历
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;                               // 读入 n
    vector<vector<int>> dist(n, vector<int>(n, -1));
    queue<pair<int,int>> q;
    int dr[8] = {1, 1, -1, -1, 2, 2, -2, -2};  // 马的八个日字方向
    int dc[8] = {2, -2, 2, -2, 1, -1, 1, -1};
    if (n > 0) {
        dist[0][0] = 0;
        q.push(make_pair(0, 0));
    }
    while (!q.empty()) {                    // BFS
        pair<int,int> cur = q.front(); q.pop();
        int r = cur.first, c = cur.second;
        for (int k = 0; k < 8; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push(make_pair(nr, nc));
            }
        }
    }
    for (int i = 0; i < n; i++) {           // 输出矩阵
        for (int j = 0; j < n; j++) {
            if (j) cout << ' ';
            cout << dist[i][j];
        }
        cout << '\\n';
    }
    return 0;
}
""",
        java="""// P2099 马的遍历
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();               // 读入 n
        int[][] dist = new int[n][n];
        for (int[] t : dist) Arrays.fill(t, -1);
        Queue<int[]> q = new ArrayDeque<int[]>();
        int[] dr = {1, 1, -1, -1, 2, 2, -2, -2};  // 马的八个日字方向
        int[] dc = {2, -2, 2, -2, 1, -1, 1, -1};
        if (n > 0) {
            dist[0][0] = 0;
            q.add(new int[]{0, 0});
        }
        while (!q.isEmpty()) {              // BFS
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int k = 0; k < 8; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {       // 输出矩阵
            for (int j = 0; j < n; j++) {
                if (j > 0) sb.append(' ');
                sb.append(dist[i][j]);
            }
            sb.append('\\n');
        }
        System.out.print(sb);
    }
}
""",
    )
