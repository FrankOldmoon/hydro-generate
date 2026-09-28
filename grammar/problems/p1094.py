# -*- coding: utf-8 -*-
"""P1094 队列操作模拟"""
from generate import make_problem


def build():
    data = [
        (6, [1, 2, 0, 3, 0, 0]),
        (2, [5, 0]),
        (6, [1, 2, 3, 0, 0, 0]),
        (6, [10, 20, 0, 30, 0, 0]),
        (6, [1, 0, 2, 0, 3, 0]),
        (6, [7, 8, 9, 0, 0, 0]),
        (2, [100, 0]),
        (8, [1, 2, 3, 4, 0, 0, 0, 0]),
        (4, [3, 0, 5, 0]),
        (6, [1, 2, 0, 0, 3, 0]),
    ]

    cases = []
    for n, ops in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in ops)
        queue = []
        out = ""
        for x in ops:
            if x == 0:
                out += f"{queue.pop(0)}\n"
            else:
                queue.append(x)
        cases.append((inp, out))
    return make_problem(
        "P1094", "队列操作模拟", ["入门", "队列"],
        cases=cases,
        desc_en="Given n operations: a positive integer x means enqueue x, 0 means "
                "dequeue and print the front element. The queue is guaranteed to "
                "be non-empty on every dequeue.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one non-negative integer (positive = enqueue, "
                 "0 = dequeue).",
        output_en="One line per dequeue: the dequeued value.",
        desc_zh="给定 n 个操作：正数 x 表示将 x 入队，0 表示出队并输出队首元素。保证"
                "出队时队列非空。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个非负整数（正数表示入队该值，"
                 "0 表示出队）。",
        output_zh="每次出队输出一个值，每行一个。",
        py=("# P1094 队列操作模拟（列表模拟队列：append 入队，pop(0) 出队）\n"
            "n = int(input())              # 操作数 n\n"
            "queue = []                    # 用列表模拟队列\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if x == 0:               # 出队\n"
            "        print(queue.pop(0))  # 队首出队\n"
            "    else:                    # 入队\n"
            "        queue.append(x)\n"),
        cpp=("// P1094 队列操作模拟\n"
             "#include <iostream>\n"
             "#include <queue>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    queue<int> q;            // 队列\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        if (x == 0) {        // 出队\n"
             "            cout << q.front() << endl;\n"
             "            q.pop();\n"
             "        } else {             // 入队\n"
             "            q.push(x);\n"
             "        }\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1094 队列操作模拟\n"
              "import java.util.Scanner;\n"
              "import java.util.LinkedList;\n"
              "import java.util.Queue;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        Queue<Integer> q = new LinkedList<>();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            if (x == 0) System.out.println(q.poll());  // 出队\n"
              "            else q.add(x);                              // 入队\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
