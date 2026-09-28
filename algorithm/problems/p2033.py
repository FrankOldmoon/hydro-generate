# -*- coding: utf-8 -*-
"""P2033 最少选点覆盖"""
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
        # 贪心：按右端点升序，在右端点放点，跳过已覆盖的区间
        iv_sorted = sorted(iv, key=lambda x: x[1])
        cnt = 0
        last = -10**18  # 上一个放置的点的位置
        for s, e in iv_sorted:
            if s > last:        # 该区间不含已放置的点
                cnt += 1
                last = e        # 在右端点放点
        out = f"{cnt}\n"
        cases.append((inp, out))
    return make_problem(
        "P2033", "最少选点覆盖", ["算法", "贪心"],
        cases=cases,
        desc_en="Given n intervals, place the minimum number of points so that every "
                "interval contains at least one point.",
        input_en="The first line contains an integer n. The following n lines each "
                 "contain two integers start and end.",
        output_en="One line containing the minimum number of points needed.",
        desc_zh="给定 n 个区间，求最少放置多少个点，使得每个区间内都至少含有一个点。",
        input_zh="第一行一个整数 n。接下来 n 行，每行两个整数 start 和 end 表示一个区间。",
        output_zh="一行一个整数，表示最少需要的点数。",
        py=("# P2033 最少选点覆盖（贪心：按右端点升序，在右端点放点）\n"
            "n = int(input())\n"
            "iv = []\n"
            "for _ in range(n):\n"
            "    s, e = map(int, input().split())\n"
            "    iv.append((s, e))\n"
            "iv.sort(key=lambda x: x[1])   # 按右端点升序排序\n"
            "cnt = 0\n"
            "last = -10**18                # 上一个放置的点的位置\n"
            "for s, e in iv:\n"
            "    if s > last:            # 该区间不含已放的点\n"
            "        cnt += 1\n"
            "        last = e            # 在右端点放点\n"
            "print(cnt)\n"),
        cpp=("// P2033 最少选点覆盖（贪心：按右端点升序，在右端点放点）\n"
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
             "    long long last = -1000000000000LL;  // 上一个放置的点的位置\n"
             "    for (auto &p : iv) {\n"
             "        if (p.first > last) {       // 该区间不含已放的点\n"
             "            cnt++;\n"
             "            last = p.second;        // 在右端点放点\n"
             "        }\n"
             "    }\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2033 最少选点覆盖（贪心：按右端点升序，在右端点放点）\n"
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
              "        long last = -1000000000000L;  // 上一个放置的点的位置\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            if (iv[i][0] > last) {  // 该区间不含已放的点\n"
              "                cnt++;\n"
              "                last = iv[i][1];    // 在右端点放点\n"
              "            }\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
