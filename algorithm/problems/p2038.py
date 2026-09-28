# -*- coding: utf-8 -*-
"""P2038 合并果子"""
import heapq
from generate import make_problem


def build():
    # n 堆果子的重量
    data = [
        (3, [1, 2, 3]),
        (1, [5]),
        (4, [1, 2, 3, 4]),
        (5, [5, 5, 5, 5, 5]),
        (2, [1, 10]),
        (3, [10, 20, 30]),
        (4, [1, 1, 1, 1]),
        (6, [1, 2, 3, 4, 5, 6]),
        (3, [1, 1, 10]),
        (5, [1, 2, 3, 4, 10]),
    ]
    cases = []
    for n, piles in data:
        inp = f"{n}\n{' '.join(map(str, piles))}\n"
        # 贪心：用小顶堆，每次合并最小的两堆
        h = list(piles)
        heapq.heapify(h)
        total = 0
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            s = a + b
            total += s
            heapq.heappush(h, s)
        out = f"{total}\n"
        cases.append((inp, out))
    return make_problem(
        "P2038", "合并果子", ["算法", "贪心"],
        cases=cases,
        desc_en="There are n piles of fruit, each with a given weight. Each time you "
                "merge two piles, the cost equals the sum of their weights. Find the "
                "minimum total cost to merge all piles into one.",
        input_en="The first line contains an integer n. The second line contains n "
                 "space-separated integers, the weights of the piles.",
        output_en="One line containing the minimum total merging cost.",
        desc_zh="有 n 堆果子，每堆有一定重量，每次合并两堆的代价为两堆重量之和，求把所有果子合并成一堆的最小总代价。",
        input_zh="第一行一个整数 n。第二行 n 个空格分隔的整数，表示每堆果子的重量。",
        output_zh="一行一个整数，表示最小总代价。",
        py=("# P2038 合并果子（贪心：小顶堆，每次合并最小的两堆）\n"
            "import heapq\n"
            "n = int(input())\n"
            "h = list(map(int, input().split()))\n"
            "heapq.heapify(h)               # 建小顶堆\n"
            "total = 0\n"
            "while len(h) > 1:\n"
            "    a = heapq.heappop(h)       # 最小堆\n"
            "    b = heapq.heappop(h)       # 次小堆\n"
            "    s = a + b\n"
            "    total += s                # 合并代价\n"
            "    heapq.heappush(h, s)      # 新堆入堆\n"
            "print(total)\n"),
        cpp=("// P2038 合并果子（贪心：小顶堆，每次合并最小的两堆）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "#include <queue>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n; cin >> n;\n"
             "    priority_queue<int, vector<int>, greater<int>> pq;  // 小顶堆\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x; cin >> x;\n"
             "        pq.push(x);\n"
             "    }\n"
             "    long long total = 0;\n"
             "    while (pq.size() > 1) {\n"
             "        int a = pq.top(); pq.pop();  // 最小堆\n"
             "        int b = pq.top(); pq.pop();  // 次小堆\n"
             "        total += a + b;              // 合并代价\n"
             "        pq.push(a + b);               // 新堆入堆\n"
             "    }\n"
             "    cout << total << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2038 合并果子（贪心：小顶堆，每次合并最小的两堆）\n"
              "import java.util.Scanner;\n"
              "import java.util.PriorityQueue;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        PriorityQueue<Integer> pq = new PriorityQueue<>();  // 小顶堆\n"
              "        for (int i = 0; i < n; ++i) pq.add(sc.nextInt());\n"
              "        long total = 0;\n"
              "        while (pq.size() > 1) {\n"
              "            int a = pq.poll();  // 最小堆\n"
              "            int b = pq.poll();  // 次小堆\n"
              "            total += a + b;    // 合并代价\n"
              "            pq.add(a + b);     // 新堆入堆\n"
              "        }\n"
              "        System.out.println(total);\n"
              "    }\n"
              "}\n"),
    )
