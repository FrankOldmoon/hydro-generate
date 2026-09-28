# -*- coding: utf-8 -*-
"""P2037 排队接水"""
from generate import make_problem


def build():
    # n 个人的接水时间
    data = [
        (3, [3, 1, 2]),
        (1, [5]),
        (5, [1, 2, 3, 4, 5]),
        (4, [5, 5, 5, 5]),
        (2, [10, 1]),
        (6, [6, 5, 4, 3, 2, 1]),
        (3, [2, 4, 1]),
        (4, [10, 20, 30, 40]),
        (5, [3, 1, 4, 1, 5]),
        (2, [3, 7]),
    ]
    cases = []
    for n, t in data:
        inp = f"{n}\n{' '.join(map(str, t))}\n"
        # 贪心：按接水时间升序，总等待时间 = sum (n-1-i)*t[i]
        ts = sorted(t)
        total = 0
        for i in range(n):
            total += (n - 1 - i) * ts[i]   # 第 i 人之后有 n-1-i 人等待
        out = f"{total}\n"
        cases.append((inp, out))
    return make_problem(
        "P2037", "排队接水", ["算法", "贪心"],
        cases=cases,
        desc_en="n people need to fetch water one by one at a single tap. Each person "
                "i has a water-fetching time t_i. Determine the queuing order that "
                "minimizes the average waiting time, and output the total waiting "
                "time under that order (the waiting time of the person being served "
                "is 0).",
        input_en="The first line contains an integer n. The second line contains n "
                 "space-separated integers, the water-fetching times.",
        output_en="One line containing the minimum total waiting time.",
        desc_zh="n 个人排队在一个水龙头接水，每人接水时间为 t_i，求使平均等待时间最短的排队顺序下的总等待时间（正在接水的人等待时间为 0）。",
        input_zh="第一行一个整数 n。第二行 n 个空格分隔的整数，表示每个人的接水时间。",
        output_zh="一行一个整数，表示最小总等待时间。",
        py=("# P2037 排队接水（贪心：按接水时间升序，总等待时间最小）\n"
            "n = int(input())\n"
            "t = list(map(int, input().split()))\n"
            "t.sort()                       # 按接水时间升序\n"
            "total = 0\n"
            "for i in range(n):\n"
            "    total += (n - 1 - i) * t[i]  # 第 i 人之后有 n-1-i 人等待\n"
            "print(total)\n"),
        cpp=("// P2037 排队接水（贪心：按接水时间升序）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n; cin >> n;\n"
             "    vector<int> t(n);\n"
             "    for (int i = 0; i < n; ++i) cin >> t[i];\n"
             "    sort(t.begin(), t.end());   // 按接水时间升序\n"
             "    long long total = 0;\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        total += (long long)(n - 1 - i) * t[i];  // 之后有 n-1-i 人等待\n"
             "    cout << total << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2037 排队接水（贪心：按接水时间升序）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] t = new int[n];\n"
              "        for (int i = 0; i < n; ++i) t[i] = sc.nextInt();\n"
              "        Arrays.sort(t);  // 按接水时间升序\n"
              "        long total = 0;\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            total += (long)(n - 1 - i) * t[i];  // 之后有 n-1-i 人等待\n"
              "        System.out.println(total);\n"
              "    }\n"
              "}\n"),
    )
