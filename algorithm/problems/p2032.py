# -*- coding: utf-8 -*-
"""P2032 最多不相交区间"""
from generate import make_problem


def build():
    # n 个区间 [起, 止]
    data = [
        (3, [(1, 3), (2, 5), (4, 6)]),
        (1, [(1, 2)]),
        (4, [(1, 2), (3, 4), (5, 6), (7, 8)]),
        (2, [(1, 5), (2, 3)]),
        (5, [(1, 10), (2, 3), (4, 5), (6, 7), (8, 9)]),
        (3, [(1, 3), (3, 5), (5, 7)]),
        (4, [(1, 4), (2, 3), (3, 6), (5, 7)]),
        (2, [(1, 2), (1, 2)]),
        (6, [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)]),
        (5, [(5, 8), (1, 2), (2, 3), (3, 4), (4, 5)]),
    ]
    cases = []
    for n, iv in data:
        inp = f"{n}\n" + "".join(f"{s} {e}\n" for s, e in iv)
        # 贪心：按右端点升序，能与上一个不相交就选
        iv_sorted = sorted(iv, key=lambda x: x[1])
        cnt = 0
        last = -10**18  # 上一个选中区间的右端点
        for s, e in iv_sorted:
            if s >= last:        # 与上一个不相交（端点相接视为不相交）
                cnt += 1
                last = e
        out = f"{cnt}\n"
        cases.append((inp, out))
    return make_problem(
        "P2032", "最多不相交区间", ["算法", "贪心"],
        cases=cases,
        desc_en="Given n intervals [start, end], select as many as possible so that "
                "no two selected intervals overlap. Two intervals that share only an "
                "endpoint are considered non-overlapping.",
        input_en="The first line contains an integer n. The following n lines each "
                 "contain two integers start and end.",
        output_en="One line containing the maximum number of mutually non-overlapping "
                  "intervals.",
        desc_zh="给定 n 个区间 [起, 止]，选出尽量多的区间使它们互不相交（仅在端点相接视为不相交）。",
        input_zh="第一行一个整数 n。接下来 n 行，每行两个整数 start 和 end 表示一个区间。",
        output_zh="一行一个整数，表示最多能选出的不相交区间数。",
        py=("# P2032 最多不相交区间（贪心：按右端点升序，能选就选）\n"
            "n = int(input())\n"
            "iv = []\n"
            "for _ in range(n):\n"
            "    s, e = map(int, input().split())\n"
            "    iv.append((s, e))\n"
            "iv.sort(key=lambda x: x[1])   # 按右端点升序排序\n"
            "cnt = 0\n"
            "last = -10**18                # 上一个选中区间的右端点\n"
            "for s, e in iv:\n"
            "    if s >= last:            # 与上一个不相交则选\n"
            "        cnt += 1\n"
            "        last = e\n"
            "print(cnt)\n"),
        cpp=("// P2032 最多不相交区间（贪心：按右端点升序）\n"
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
             "    sort(iv.begin(), iv.end(), [](auto a, auto b){ return a.second < b.second; });\n"
             "    int cnt = 0;\n"
             "    long long last = -1000000000000LL;  // 上一个选中区间的右端点\n"
             "    for (auto &p : iv) {\n"
             "        if (p.first >= last) {       // 不相交则选\n"
             "            cnt++;\n"
             "            last = p.second;\n"
             "        }\n"
             "    }\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2032 最多不相交区间（贪心：按右端点升序）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[][] iv = new int[n][2];\n"
              "        for (int i = 0; i < n; ++i) { iv[i][0] = sc.nextInt(); iv[i][1] = sc.nextInt(); }\n"
              "        Arrays.sort(iv, (a, b) -> Integer.compare(a[1], b[1]));  // 按右端点升序\n"
              "        int cnt = 0;\n"
              "        long last = -1000000000000L;  // 上一个选中区间的右端点\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            if (iv[i][0] >= last) {  // 不相交则选\n"
              "                cnt++;\n"
              "                last = iv[i][1];\n"
              "            }\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
