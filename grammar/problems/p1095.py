# -*- coding: utf-8 -*-
"""P1095 约瑟夫环"""
from generate import make_problem


def build():
    data = [
        (5, 3), (1, 1), (2, 1), (6, 2), (3, 1),
        (4, 2), (5, 1), (7, 3), (6, 4), (3, 2),
    ]

    def josephus(n, m):
        q = list(range(1, n + 1))
        result = []
        while q:
            for _ in range(m - 1):
                q.append(q.pop(0))
            result.append(q.pop(0))
        return result

    cases = []
    for n, m in data:
        inp = f"{n}\n{m}\n"
        out = "".join(f"{x}\n" for x in josephus(n, m))
        cases.append((inp, out))
    return make_problem(
        "P1095", "约瑟夫环", ["入门", "队列"],
        cases=cases,
        desc_en="n people numbered 1 to n stand in a circle. Starting from person "
                "1, count to m each time; the person who is counted out leaves "
                "the circle. Print the order of elimination.",
        input_en="Two lines: the first line contains n, the second line contains "
                 "m, satisfying $1\\leq n\\leq 1000$ and $1\\leq m\\leq 1000$ .",
        output_en="n lines: the elimination order.",
        desc_zh="n 个人编号 1 到 n 围成一圈，从 1 号开始报数，每次数到 m 的人出列。"
                "输出出列顺序。",
        input_zh="两行：第一行一个正整数 n，第二行一个正整数 m，满足 $1\\leq n\\leq 1000$ "
                 "且 $1\\leq m\\leq 1000$ 。",
        output_zh="n 行，按顺序输出出列人员的编号。",
        py=("# P1095 约瑟夫环（队列模拟报数出列）\n"
            "n = int(input())              # 人数 n\n"
            "m = int(input())              # 报数 m\n"
            "q = list(range(1, n + 1))     # 队列：1 到 n\n"
            "result = []\n"
            "while q:\n"
            "    for i in range(m - 1):   # 前 m-1 人重新排队\n"
            "        q.append(q.pop(0))\n"
            "    result.append(q.pop(0))  # 第 m 人出列\n"
            "for x in result:\n"
            "    print(x)\n"),
        cpp=("// P1095 约瑟夫环\n"
             "#include <iostream>\n"
             "#include <queue>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n, m;\n"
             "    cin >> n >> m;\n"
             "    queue<int> q;\n"
             "    for (int i = 1; i <= n; ++i) q.push(i);\n"
             "    while (!q.empty()) {\n"
             "        for (int i = 0; i < m - 1; ++i) {  // 前 m-1 人重新排队\n"
             "            q.push(q.front());\n"
             "            q.pop();\n"
             "        }\n"
             "        cout << q.front() << endl;  // 第 m 人出列\n"
             "        q.pop();\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1095 约瑟夫环\n"
              "import java.util.Scanner;\n"
              "import java.util.LinkedList;\n"
              "import java.util.Queue;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int m = sc.nextInt();\n"
              "        Queue<Integer> q = new LinkedList<>();\n"
              "        for (int i = 1; i <= n; ++i) q.add(i);\n"
              "        while (!q.isEmpty()) {\n"
              "            for (int i = 0; i < m - 1; ++i) {  // 前 m-1 人重新排队\n"
              "                q.add(q.poll());\n"
              "            }\n"
              "            System.out.println(q.poll());      // 第 m 人出列\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
