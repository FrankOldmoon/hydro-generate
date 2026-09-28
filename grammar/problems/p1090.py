# -*- coding: utf-8 -*-
"""P1090 坐标排序"""
from generate import make_problem


def build():
    data = [
        (3, [(1, 2), (3, 1), (1, 1)]),
        (1, [(0, 0)]),
        (4, [(3, 3), (2, 2), (1, 1), (0, 0)]),
        (2, [(1, 5), (1, 3)]),
        (5, [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]),
        (3, [(0, 5), (0, 0), (0, 3)]),
        (4, [(-1, 2), (1, -1), (-1, -1), (1, 2)]),
        (2, [(10, 20), (5, 15)]),
        (6, [(2, 1), (2, 2), (1, 1), (1, 2), (3, 1), (3, 2)]),
        (3, [(1, 1), (2, 2), (1, 2)]),
    ]

    cases = []
    for n, pts in data:
        inp = f"{n}\n" + "".join(f"{x} {y}\n" for x, y in pts)
        sorted_pts = sorted(pts)
        out = "".join(f"{x} {y}\n" for x, y in sorted_pts)
        cases.append((inp, out))
    return make_problem(
        "P1090", "坐标排序", ["入门", "元组"],
        cases=cases,
        desc_en="Given n points with coordinates (x, y), sort them by x ascending. "
                "If x values are equal, sort by y ascending.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain two space-separated integers x and y.",
        output_en="n lines: the sorted coordinates, each line containing x and y.",
        desc_zh="给定 n 个点的坐标 (x, y)，按 x 升序排序，x 相同则按 y 升序排序后输出。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行两个空格分隔的整数 x 和 y。",
        output_zh="n 行，每行两个空格分隔的整数，表示排序后的坐标。",
        py=("# P1090 坐标排序（元组排序：先按 x 再按 y）\n"
            "n = int(input())              # 点的个数 n\n"
            "points = []\n"
            "for i in range(n):\n"
            "    x, y = map(int, input().split())\n"
            "    points.append((x, y))     # 用元组存储坐标\n"
            "points.sort()                 # 元组排序：先比 x，再比 y\n"
            "for x, y in points:\n"
            "    print(x, y)\n"),
        cpp=("// P1090 坐标排序\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<pair<int,int>> pts;   // pair 存坐标\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x, y;\n"
             "        cin >> x >> y;\n"
             "        pts.push_back({x, y});\n"
             "    }\n"
             "    sort(pts.begin(), pts.end());  // pair 排序：先 first 再 second\n"
             "    for (auto &p : pts)\n"
             "        cout << p.first << ' ' << p.second << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1090 坐标排序\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[][] pts = new int[n][2];\n"
              "        for (int i = 0; i < n; ++i) { pts[i][0] = sc.nextInt(); pts[i][1] = sc.nextInt(); }\n"
              "        Arrays.sort(pts, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            System.out.println(pts[i][0] + \" \" + pts[i][1]);\n"
              "    }\n"
              "}\n"),
    )
