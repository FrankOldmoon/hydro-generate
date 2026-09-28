# -*- coding: utf-8 -*-
"""P2040 截断木材"""
from generate import make_problem


def build():
    # (n 棵树的高度列表, 需要长度 M)
    data = [
        (4, [10, 15, 20, 15], 7),
        (3, [10, 10, 10], 5),
        (4, [20, 15, 10, 17], 7),
        (4, [4, 42, 40, 26], 20),
        (1, [10], 3),
        (3, [100, 200, 150], 50),
        (2, [5, 5], 2),
        (6, [10, 20, 30, 40, 50, 60], 30),
        (3, [8, 8, 8], 6),
        (4, [10, 20, 30, 40], 15),
    ]
    cases = []
    for n, trees, M in data:
        inp = f"{n}\n{' '.join(map(str, trees))}\n{M}\n"
        # 二分贪心：找最大锯片高度使截得木材 >= M
        lo, hi = 0, max(trees)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            wood = sum(max(0, x - mid) for x in trees)
            if wood >= M:        # 木材够，尝试更高
                ans = mid
                lo = mid + 1
            else:                # 木材不够，降低锯片
                hi = mid - 1
        out = f"{ans}\n"
        cases.append((inp, out))
    return make_problem(
        "P2040", "截断木材", ["算法", "贪心"],
        cases=cases,
        desc_en="There are n trees, each with a height. A saw at height h cuts every "
                "tree taller than h, producing max(0, height_i - h) units of wood. "
                "Find the maximum saw height h such that the total wood cut is at "
                "least M.",
        input_en="The first line contains an integer n. The second line contains n "
                 "space-separated integers, the tree heights. The third line contains "
                 "an integer M, the required amount of wood.",
        output_en="One line containing the maximum saw height.",
        desc_zh="有 n 棵树，给定每棵树的高度，在高度 h 处锯下后每棵树可得 max(0, 树高-h) 木材，求使总木材不少于 M 的最大锯片高度 h。",
        input_zh="第一行一个整数 n。第二行 n 个空格分隔的整数，表示树的高度。第三行一个整数 M 表示需要的木材量。",
        output_zh="一行一个整数，表示最大的锯片高度。",
        py=("# P2040 截断木材（二分贪心：找最大锯片高度使木材 >= M）\n"
            "n = int(input())\n"
            "h = list(map(int, input().split()))\n"
            "M = int(input())\n"
            "lo, hi = 0, max(h)\n"
            "ans = 0\n"
            "while lo <= hi:\n"
            "    mid = (lo + hi) // 2\n"
            "    wood = sum(x - mid for x in h if x > mid)  # 截得木材\n"
            "    if wood >= M:        # 木材够，尝试更高\n"
            "        ans = mid\n"
            "        lo = mid + 1\n"
            "    else:                # 木材不够，降低锯片\n"
            "        hi = mid - 1\n"
            "print(ans)\n"),
        cpp=("// P2040 截断木材（二分贪心：找最大锯片高度使木材 >= M）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n; cin >> n;\n"
             "    vector<int> h(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> h[i];\n"
             "    long long M; cin >> M;\n"
             "    int hi = *max_element(h.begin(), h.end());\n"
             "    int lo = 0, ans = 0;\n"
             "    while (lo <= hi) {\n"
             "        int mid = (lo + hi) / 2;\n"
             "        long long wood = 0;\n"
             "        for (int x : h)\n"
             "            if (x > mid) wood += x - mid;  // 截得木材\n"
             "        if (wood >= M) {       // 木材够，尝试更高\n"
             "            ans = mid;\n"
             "            lo = mid + 1;\n"
             "        } else {              // 木材不够，降低锯片\n"
             "            hi = mid - 1;\n"
             "        }\n"
             "    }\n"
             "    cout << ans << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2040 截断木材（二分贪心：找最大锯片高度使木材 >= M）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] h = new int[n];\n"
              "        int hi = 0;\n"
              "        for (int i = 0; i < n; ++i) { h[i] = sc.nextInt(); if (h[i] > hi) hi = h[i]; }\n"
              "        long M = sc.nextLong();\n"
              "        int lo = 0, ans = 0;\n"
              "        while (lo <= hi) {\n"
              "            int mid = (lo + hi) / 2;\n"
              "            long wood = 0;\n"
              "            for (int x : h)\n"
              "                if (x > mid) wood += x - mid;  // 截得木材\n"
              "            if (wood >= M) {       // 木材够，尝试更高\n"
              "                ans = mid;\n"
              "                lo = mid + 1;\n"
              "            } else {              // 木材不够，降低锯片\n"
              "                hi = mid - 1;\n"
              "            }\n"
              "        }\n"
              "        System.out.println(ans);\n"
              "    }\n"
              "}\n"),
    )
