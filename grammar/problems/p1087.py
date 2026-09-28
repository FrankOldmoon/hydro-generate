# -*- coding: utf-8 -*-
"""P1087 两个集合的交集"""
from generate import make_problem


def build():
    data = [
        (3, [1, 2, 3], 3, [2, 3, 4]),
        (1, [1], 1, [1]),
        (2, [1, 2], 2, [3, 4]),
        (4, [1, 2, 3, 4], 2, [2, 4]),
        (3, [1, 1, 2], 3, [1, 2, 2]),
        (1, [5], 1, [5]),
        (5, [1, 2, 3, 4, 5], 3, [3, 4, 5]),
        (3, [1, 2, 3], 3, [1, 2, 3]),
        (4, [10, 20, 30, 40], 2, [20, 40]),
        (2, [1, 3], 2, [3, 1]),
    ]

    cases = []
    for n, a, m, b in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in a)
        inp += f"{m}\n" + "".join(f"{x}\n" for x in b)
        inter = sorted(set(a) & set(b))
        out = f"{len(inter)}\n" + "".join(f"{x}\n" for x in inter)
        cases.append((inp, out))
    return make_problem(
        "P1087", "两个集合的交集", ["入门", "集合"],
        cases=cases,
        desc_en="Given two groups of integers, find their intersection (common "
                "elements), print the count and the values in ascending order.",
        input_en="The first line contains n, followed by n integers. Then a line "
                 "with m, followed by m integers.",
        output_en="The first line is the intersection size k. The following k "
                  "lines are the intersection elements in ascending order.",
        desc_zh="给定两组整数，求它们的交集（共同拥有的元素），先输出交集大小，再升序输出。",
        input_zh="第一行一个正整数 n，接下来 n 行每行一个整数（第一组）。然后一行正整数 "
                 "m，接下来 m 行每行一个整数（第二组）。",
        output_zh="第一行输出交集大小 k。接下来 k 行升序输出交集元素。",
        py=("# P1087 两个集合的交集（& 运算求交集）\n"
            "n = int(input())              # 第一组个数 n\n"
            "a = set()\n"
            "for i in range(n):\n"
            "    a.add(int(input()))\n"
            "m = int(input())              # 第二组个数 m\n"
            "b = set()\n"
            "for i in range(m):\n"
            "    b.add(int(input()))\n"
            "inter = sorted(a & b)         # 交集后排序\n"
            "print(len(inter))             # 交集大小\n"
            "for x in inter:\n"
            "    print(x)\n"),
        cpp=("// P1087 两个集合的交集\n"
             "#include <iostream>\n"
             "#include <set>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    set<int> a;\n"
             "    for (int i = 0; i < n; ++i) { int x; cin >> x; a.insert(x); }\n"
             "    int m;\n"
             "    cin >> m;\n"
             "    set<int> b;\n"
             "    for (int i = 0; i < m; ++i) { int x; cin >> x; b.insert(x); }\n"
             "    set<int> inter;\n"
             "    for (int x : a)              // 遍历 a\n"
             "        if (b.count(x)) inter.insert(x);  // 在 b 中则加入交集\n"
             "    cout << inter.size() << endl;\n"
             "    for (int x : inter) cout << x << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1087 两个集合的交集\n"
              "import java.util.Scanner;\n"
              "import java.util.TreeSet;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        TreeSet<Integer> a = new TreeSet<>();\n"
              "        for (int i = 0; i < n; ++i) a.add(sc.nextInt());\n"
              "        int m = sc.nextInt();\n"
              "        TreeSet<Integer> b = new TreeSet<>();\n"
              "        for (int i = 0; i < m; ++i) b.add(sc.nextInt());\n"
              "        a.retainAll(b);              // 交集：a 保留 b 中也有的\n"
              "        System.out.println(a.size());\n"
              "        for (int x : a) System.out.println(x);\n"
              "    }\n"
              "}\n"),
    )
