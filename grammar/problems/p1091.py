# -*- coding: utf-8 -*-
"""P1091 距离原点最近的点"""
from generate import make_problem


def build():
    data = [
        (3, [(1, 1), (3, 4), (0, 1)]),
        (1, [(0, 0)]),
        (2, [(1, 0), (0, 1)]),
        (4, [(3, 4), (1, 1), (5, 0), (2, 2)]),
        (3, [(0, 3), (4, 0), (0, 1)]),
        (2, [(-1, -1), (1, 1)]),
        (5, [(1, 5), (2, 3), (0, 1), (1, 1), (3, 0)]),
        (1, [(5, 5)]),
        (3, [(0, 0), (1, 0), (0, 1)]),
        (2, [(2, 1), (1, 0)]),
    ]

    cases = []
    for n, pts in data:
        inp = f"{n}\n" + "".join(f"{x} {y}\n" for x, y in pts)
        best = pts[0]
        best_d = best[0] ** 2 + best[1] ** 2
        for x, y in pts[1:]:
            d = x * x + y * y
            if d < best_d:
                best_d = d
                best = (x, y)
        cases.append((inp, f"{best[0]} {best[1]}\n"))
    return make_problem(
        "P1091", "距离原点最近的点", ["入门", "元组"],
        cases=cases,
        desc_en="Given n points with coordinates (x, y), find the point closest "
                "to the origin (0, 0). If tied, output the one that appears first.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain two space-separated integers x and y.",
        output_en="One line: the x and y of the closest point.",
        desc_zh="给定 n 个点的坐标 (x, y)，找出距离原点 (0,0) 最近的点。若距离相同，"
                "输出先出现的点。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行两个空格分隔的整数 x 和 y。",
        output_zh="一行，输出距离原点最近的点的坐标 x 和 y。",
        py=("# P1091 距离原点最近的点（元组存坐标，比较距离平方）\n"
            "n = int(input())              # 点的个数 n\n"
            "points = []\n"
            "for i in range(n):\n"
            "    x, y = map(int, input().split())\n"
            "    points.append((x, y))     # 元组存坐标\n"
            "best = points[0]\n"
            "best_d = best[0]**2 + best[1]**2  # 距离平方\n"
            "for x, y in points[1:]:\n"
            "    d = x*x + y*y\n"
            "    if d < best_d:            # 严格小于才更新（相同保留先出现的）\n"
            "        best_d = d\n"
            "        best = (x, y)\n"
            "print(best[0], best[1])\n"),
        cpp=("// P1091 距离原点最近的点\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <utility>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<pair<int,int>> pts;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x, y;\n"
             "        cin >> x >> y;\n"
             "        pts.push_back({x, y});\n"
             "    }\n"
             "    auto best = pts[0];\n"
             "    int bestD = best.first*best.first + best.second*best.second;\n"
             "    for (int i = 1; i < n; ++i) {\n"
             "        int d = pts[i].first*pts[i].first + pts[i].second*pts[i].second;\n"
             "        if (d < bestD) { bestD = d; best = pts[i]; }\n"
             "    }\n"
             "    cout << best.first << ' ' << best.second << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1091 距离原点最近的点\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] xs = new int[n], ys = new int[n];\n"
              "        for (int i = 0; i < n; ++i) { xs[i] = sc.nextInt(); ys[i] = sc.nextInt(); }\n"
              "        int bestIdx = 0;\n"
              "        int bestD = xs[0]*xs[0] + ys[0]*ys[0];\n"
              "        for (int i = 1; i < n; ++i) {\n"
              "            int d = xs[i]*xs[i] + ys[i]*ys[i];\n"
              "            if (d < bestD) { bestD = d; bestIdx = i; }\n"
              "        }\n"
              "        System.out.println(xs[bestIdx] + \" \" + ys[bestIdx]);\n"
              "    }\n"
              "}\n"),
    )
