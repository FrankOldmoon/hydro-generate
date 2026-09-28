# -*- coding: utf-8 -*-
"""P2093 区域填充"""
from generate import make_problem


def solve(grid, n, m, r, c, nc):
    # DFS 把与 (r,c) 连通的同色区域改为新色 nc
    grid = [list(row) for row in grid]
    old = grid[r][c]
    if old == nc:
        return grid
    stack = [(r, c)]
    grid[r][c] = nc
    while stack:
        cr, cc = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, ncc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= ncc < m and grid[nr][ncc] == old:
                grid[nr][ncc] = nc
                stack.append((nr, ncc))
    return grid


def build():
    data = [
        (3, 3, ["000", "000", "000"], 2, 2, '1'),
        (3, 3, ["000", "010", "000"], 2, 2, '2'),
        (4, 4, ["1111", "1221", "1221", "1111"], 2, 2, '3'),
        (3, 3, ["121", "222", "121"], 2, 2, '9'),
        (1, 1, ["5"], 1, 1, '7'),
        (1, 5, ["12345"], 1, 3, '9'),
        (5, 5, ["00000", "00000", "00000", "00000", "00000"], 1, 1, '5'),
        (5, 5, ["00000", "01110", "01110", "01110", "00000"], 1, 1, '2'),
        (4, 5, ["00100", "01110", "00100", "00000"], 2, 2, '8'),
        (3, 3, ["123", "456", "789"], 2, 2, '0'),
    ]
    cases = []
    for n, m, g, r, c, nc in data:
        inp = f"{n} {m}\n" + "\n".join(g) + f"\n{r} {c} {nc}\n"
        res = solve(g, n, m, r - 1, c - 1, nc)
        out = "\n".join("".join(row) for row in res) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2093", "区域填充", ["算法", "搜索"],
        cases=cases,
        desc_en=("Given an n*m grid whose cells are digits 0-9 (colors), a "
                 "starting cell (r,c) (1-indexed) and a new color, use flood "
                 "fill to change every cell connected to the starting cell by "
                 "up/down/left/right moves through cells of the same original "
                 "color into the new color. Output the grid after filling."),
        input_en=("The first line contains n and m. Then n lines follow, each "
                  "a string of m digits. The last line contains r, c and the "
                  "new color (a single digit). $1\\leq n,m\\leq 50$ ."),
        output_en="The n lines of the grid after flood fill.",
        desc_zh="给定 n×m 网格（每格为一个 0 到 9 的数字表示颜色）和起点 (r,c)（1 下标）及新颜色，用 DFS 把与起点上下左右连通且同色的区域全部改为新颜色，输出填充后的网格。",
        input_zh="第一行两个整数 n 和 m，接下来 n 行每行一个长度为 m 的数字串，最后一行三个值 r、c、新颜色（新颜色为一个数字），满足 $1\\leq n,m\\leq 50$ 。",
        output_zh="n 行，每行一个长度为 m 的字符串，表示填充后的网格。",
        py="""# P2093 区域填充
import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())            # 读入行数列数
grid = [list(input().strip()) for _ in range(n)]  # 读入网格
r, c, nc = input().split()                  # 读入起点和新颜色
r, c = int(r) - 1, int(c) - 1               # 转为 0 下标
old = grid[r][c]
if old != nc:                               # 颜色不同才填充
    stack = [(r, c)]
    grid[r][c] = nc
    while stack:                            # DFS 栈
        cr, cc = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, ncc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= ncc < m and grid[nr][ncc] == old:
                grid[nr][ncc] = nc
                stack.append((nr, ncc))
for row in grid:                            # 输出填充后的网格
    print("".join(row))
""",
        cpp="""// P2093 区域填充
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int n, m;
char grid[55][55];
int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
// DFS 填充与 (r,c) 连通的同色区域
void dfs(int r, int c, char oldc, char nc) {
    grid[r][c] = nc;
    for (int k = 0; k < 4; k++) {
        int nr = r + dr[k], ncc = c + dc[k];
        if (nr >= 0 && nr < n && ncc >= 0 && ncc < m && grid[nr][ncc] == oldc)
            dfs(nr, ncc, oldc, nc);
    }
}
int main() {
    cin >> n >> m;                          // 读入行数列数
    for (int i = 0; i < n; i++) cin >> grid[i];  // 读入网格
    int r, c; char nc;
    cin >> r >> c >> nc;                    // 读入起点和新颜色
    r--; c--;                               // 转为 0 下标
    char oldc = grid[r][c];
    if (oldc != nc) dfs(r, c, oldc, nc);    // 颜色不同才填充
    for (int i = 0; i < n; i++) cout << grid[i] << endl;  // 输出
    return 0;
}
""",
        java="""// P2093 区域填充
import java.util.*;
public class Main {
    static int n, m;
    static char[][] grid;
    static int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
    // DFS 填充与 (r,c) 连通的同色区域
    static void dfs(int r, int c, char oldc, char nc) {
        grid[r][c] = nc;
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], ncc = c + dc[k];
            if (nr >= 0 && nr < n && ncc >= 0 && ncc < m && grid[nr][ncc] == oldc)
                dfs(nr, ncc, oldc, nc);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); m = sc.nextInt();      // 读入行数列数
        grid = new char[n][m];
        for (int i = 0; i < n; i++) {            // 读入网格
            String s = sc.next();
            for (int j = 0; j < m; j++) grid[i][j] = s.charAt(j);
        }
        int r = sc.nextInt(), c = sc.nextInt();  // 读入起点
        String ncStr = sc.next();
        char nc = ncStr.charAt(0);               // 新颜色
        r--; c--;                                // 转为 0 下标
        char oldc = grid[r][c];
        if (oldc != nc) dfs(r, c, oldc, nc);     // 颜色不同才填充
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {            // 输出
            sb.append(new String(grid[i])).append('\\n');
        }
        System.out.print(sb);
    }
}
""",
    )
