# -*- coding: utf-8 -*-
"""P1086 集合去重排序"""
from generate import make_problem


def build():
    data = [
        (5, [3, 1, 2, 3, 1]),
        (1, [5]),
        (3, [1, 1, 1]),
        (4, [4, 3, 2, 1]),
        (6, [1, 2, 3, 1, 2, 3]),
        (1, [0]),
        (5, [5, 4, 3, 2, 1]),
        (7, [1, 1, 2, 2, 3, 3, 4]),
        (2, [10, 10]),
        (8, [3, 3, 3, 2, 2, 1, 1, 1]),
    ]

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        s = sorted(set(nums))
        out = f"{len(s)}\n" + "".join(f"{x}\n" for x in s)
        cases.append((inp, out))
    return make_problem(
        "P1086", "集合去重排序", ["入门", "集合"],
        cases=cases,
        desc_en="Given n integers, remove duplicates, then print the "
                "count and the unique values in ascending order.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain an integer.",
        output_en="The first line is the count of unique values k. The following "
                  "k lines are the unique values in ascending order.",
        desc_zh="给定 n 个整数，去重后先输出去重后的个数，再按升序输出。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个整数。",
        output_zh="第一行输出去重后的个数 k。接下来 k 行升序输出去重后的整数。",
        py=("# P1086 集合去重排序（set 去重 + sorted 排序）\n"
            "n = int(input())              # 个数 n\n"
            "s = set()                     # 创建空集合\n"
            "for i in range(n):\n"
            "    s.add(int(input()))       # 加入集合（自动去重）\n"
            "result = sorted(s)            # 升序排序\n"
            "print(len(result))            # 去重后个数\n"
            "for x in result:\n"
            "    print(x)\n"),
        cpp=("// P1086 集合去重排序\n"
             "#include <iostream>\n"
             "#include <set>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    set<int> s;               // set 自动去重并排序\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        s.insert(x);\n"
             "    }\n"
             "    cout << s.size() << endl;\n"
             "    for (int x : s) cout << x << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1086 集合去重排序\n"
              "import java.util.Scanner;\n"
              "import java.util.TreeSet;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        TreeSet<Integer> s = new TreeSet<>();  // 自动去重排序\n"
              "        for (int i = 0; i < n; ++i) s.add(sc.nextInt());\n"
              "        System.out.println(s.size());\n"
              "        for (int x : s) System.out.println(x);\n"
              "    }\n"
              "}\n"),
    )
