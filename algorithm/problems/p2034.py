# -*- coding: utf-8 -*-
"""P2034 区间合并"""
from generate import make_problem


def build():
    # n 个区间 [起, 止]，相接视为可合并
    data = [
        (3, [(1, 3), (2, 5), (4, 6)]),
        (1, [(1, 2)]),
        (4, [(1, 2), (3, 4), (5, 6), (7, 8)]),
        (2, [(1, 5), (2, 3)]),
        (5, [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]),
        (4, [(1, 3), (2, 4), (5, 7), (6, 8)]),
        (4, [(1, 4), (2, 3), (3, 6), (8, 10)]),
        (2, [(1, 2), (1, 2)]),
        (6, [(1, 2), (3, 5), (4, 6), (8, 9), (10, 12), (11, 13)]),
        (3, [(1, 3), (3, 5), (5, 7)]),
    ]
    cases = []
    for n, iv in data:
        inp = f"{n}\n" + "".join(f"{s} {e}\n" for s, e in iv)
        # 贪心：按起点升序，重叠或相接则合并
        iv_sorted = sorted(iv, key=lambda x: x[0])
        cnt = 0
        cur_r = -10**18  # 当前合并区间的右端点
        for s, e in iv_sorted:
            if cnt == 0 or s > cur_r:   # 新区间组（不相接）
                cnt += 1
                cur_r = e
            else:                       # 与当前组重叠或相接，合并
                if e > cur_r:
                    cur_r = e
        out = f"{cnt}\n"
        cases.append((inp, out))
    return make_problem(
        "P2034", "区间合并", ["算法", "贪心"],
        cases=cases,
        desc_en="Given n intervals, merge all intervals that overlap or touch, then "
                "output the number of intervals after merging.",
        input_en="The first line contains an integer n. The following n lines each "
                 "contain two integers start and end.",
        output_en="One line containing the number of intervals after merging.",
        desc_zh="给定 n 个区间，把所有重叠或相接的区间合并后，输出合并后的区间数。",
        input_zh="第一行一个整数 n。接下来 n 行，每行两个整数 start 和 end 表示一个区间。",
        output_zh="一行一个整数，表示合并后的区间数。",
        py=("# P2034 区间合并（贪心：按起点升序，重叠或相接则合并）\n"
            "n = int(input())\n"
            "iv = []\n"
            "for _ in range(n):\n"
            "    s, e = map(int, input().split())\n"
            "    iv.append((s, e))\n"
            "iv.sort(key=lambda x: x[0])    # 按起点升序排序\n"
            "cnt = 0\n"
            "cur_r = -10**18               # 当前合并区间的右端点\n"
            "for s, e in iv:\n"
            "    if cnt == 0 or s > cur_r: # 新区间组\n"
            "        cnt += 1\n"
            "        cur_r = e\n"
            "    elif e > cur_r:           # 重叠或相接，扩展右端点\n"
            "        cur_r = e\n"
            "print(cnt)\n"),
        cpp=("// P2034 区间合并（贪心：按起点升序，重叠或相接则合并）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n; cin >> n;\n"
             "    vector<pair<int,int>> iv;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int s, e; cin >> s >> e;\n"
             "        iv.push_back({s, e});\n"
             "    }\n"
             "    sort(iv.begin(), iv.end());  // 按起点升序\n"
             "    int cnt = 0;\n"
             "    long long cur_r = -1000000000000LL;  // 当前合并区间的右端点\n"
             "    for (auto &p : iv) {\n"
             "        if (cnt == 0 || p.first > cur_r) {  // 新区间组\n"
             "            cnt++;\n"
             "            cur_r = p.second;\n"
             "        } else if (p.second > cur_r) {       // 重叠或相接，扩展\n"
             "            cur_r = p.second;\n"
             "        }\n"
             "    }\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2034 区间合并（贪心：按起点升序，重叠或相接则合并）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[][] iv = new int[n][2];\n"
              "        for (int i = 0; i < n; ++i) { iv[i][0] = sc.nextInt(); iv[i][1] = sc.nextInt(); }\n"
              "        Arrays.sort(iv, (a, b) -> Integer.compare(a[0], b[0]));  // 按起点升序\n"
              "        int cnt = 0;\n"
              "        long cur_r = -1000000000000L;  // 当前合并区间的右端点\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            if (cnt == 0 || iv[i][0] > cur_r) {  // 新区间组\n"
              "                cnt++;\n"
              "                cur_r = iv[i][1];\n"
              "            } else if (iv[i][1] > cur_r) {       // 重叠或相接，扩展\n"
              "                cur_r = iv[i][1];\n"
              "            }\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
