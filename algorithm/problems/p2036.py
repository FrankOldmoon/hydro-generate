# -*- coding: utf-8 -*-
"""P2036 活动安排"""
from generate import make_problem


def build():
    # n 个活动 [开始, 结束]
    data = [
        (3, [(1, 4), (3, 5), (0, 6)]),
        (4, [(1, 3), (2, 4), (3, 5), (4, 6)]),
        (1, [(0, 1)]),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
        (6, [(0, 6), (1, 2), (3, 4), (5, 6), (2, 5), (4, 7)]),
        (3, [(1, 5), (6, 10), (2, 3)]),
        (2, [(1, 10), (2, 3)]),
        (4, [(0, 2), (1, 3), (2, 4), (3, 5)]),
        (5, [(0, 8), (1, 2), (2, 3), (4, 5), (6, 7)]),
        (3, [(1, 3), (3, 5), (5, 7)]),
    ]
    cases = []
    for n, iv in data:
        inp = f"{n}\n" + "".join(f"{s} {e}\n" for s, e in iv)
        # 贪心：按结束时间升序，能安排就安排
        iv_sorted = sorted(iv, key=lambda x: x[1])
        cnt = 0
        last = -10**18  # 上一个选中活动的结束时间
        for s, e in iv_sorted:
            if s >= last:        # 与上一个不冲突（端点相接视为不冲突）
                cnt += 1
                last = e
        out = f"{cnt}\n"
        cases.append((inp, out))
    return make_problem(
        "P2036", "活动安排", ["算法", "贪心"],
        cases=cases,
        desc_en="Given n activities, each with a start time and an end time, select "
                "the maximum number of activities such that no two selected "
                "activities overlap in time. Activities that only touch at an "
                "endpoint are considered non-overlapping.",
        input_en="The first line contains an integer n. The following n lines each "
                 "contain two integers start and end.",
        output_en="One line containing the maximum number of activities that can be "
                  "arranged.",
        desc_zh="给定 n 个活动 [开始, 结束]，求最多能安排多少个活动使其时间互不冲突（仅在端点相接视为不冲突）。",
        input_zh="第一行一个整数 n。接下来 n 行，每行两个整数 start 和 end 表示一个活动的开始与结束时间。",
        output_zh="一行一个整数，表示最多能安排的活动数。",
        py=("# P2036 活动安排（贪心：按结束时间升序，能安排就安排）\n"
            "n = int(input())\n"
            "iv = []\n"
            "for _ in range(n):\n"
            "    s, e = map(int, input().split())\n"
            "    iv.append((s, e))\n"
            "iv.sort(key=lambda x: x[1])   # 按结束时间升序排序\n"
            "cnt = 0\n"
            "last = -10**18                # 上一个选中活动的结束时间\n"
            "for s, e in iv:\n"
            "    if s >= last:            # 与上一个不冲突则安排\n"
            "        cnt += 1\n"
            "        last = e\n"
            "print(cnt)\n"),
        cpp=("// P2036 活动安排（贪心：按结束时间升序）\n"
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
             "    long long last = -1000000000000LL;  // 上一个选中活动的结束时间\n"
             "    for (auto &p : iv) {\n"
             "        if (p.first >= last) {       // 不冲突则安排\n"
             "            cnt++;\n"
             "            last = p.second;\n"
             "        }\n"
             "    }\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2036 活动安排（贪心：按结束时间升序）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[][] iv = new int[n][2];\n"
              "        for (int i = 0; i < n; ++i) { iv[i][0] = sc.nextInt(); iv[i][1] = sc.nextInt(); }\n"
              "        Arrays.sort(iv, (a, b) -> Integer.compare(a[1], b[1]));  // 按结束时间升序\n"
              "        int cnt = 0;\n"
              "        long last = -1000000000000L;  // 上一个选中活动的结束时间\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            if (iv[i][0] >= last) {  // 不冲突则安排\n"
              "                cnt++;\n"
              "                last = iv[i][1];\n"
              "            }\n"
              "        }\n"
              "        System.out.println(cnt);\n"
              "    }\n"
              "}\n"),
    )
