# -*- coding: utf-8 -*-
"""P1044 去重后输出"""
from generate import make_problem


def build():
    data = [
        (5, [1, 2, 3, 2, 2]),
        (3, [1, 2, 3]),
        (4, [1, 1, 1, 1]),
        (6, [1, 2, 1, 3, 2, 4]),
        (1, [5]),
        (5, [5, 4, 3, 2, 1]),
        (4, [1, 2, 2, 3]),
        (3, [3, 3, 3]),
        (5, [1, 2, 3, 2, 1]),
        (2, [9, 9]),
    ]
    cases = []
    for n, arr in data:
        inp = f"{n}\n" + " ".join(str(x) for x in arr) + "\n"
        seen = []
        for x in arr:
            if x not in seen:
                seen.append(x)
        out = " ".join(str(x) for x in seen) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P1044", "去重后输出", ["入门", "列表", "一行全部"],
        cases=cases,
        desc_en="Given n on the first line and n integers on the second line "
                "(space-separated), remove duplicates keeping the first occurrence "
                "of each value, and print the result on one line (space-separated).",
        input_en="The first line contains a positive integer n. The second line "
                 "contains n space-separated integers, satisfying $1\\leq n\\leq 1000$ "
                 "and $-32768\\leq x_i\\leq 32767$ .",
        output_en="One line: the list after removing duplicates (first occurrence "
                  "kept), space-separated.",
        desc_zh="第一行为正整数 n，第二行为 n 个用空格分隔的整数，去重后（保留每个数第一次"
                "出现的顺序）在一行内输出（以空格分隔）。",
        input_zh="第一行一个正整数 n，第二行 n 个用空格分隔的整数，满足 $1\\leq n\\leq 1000$ "
                 "且 $-32768\\leq x_i\\leq 32767$ 。",
        output_zh="一行，去重后（保留首次出现顺序）以空格分隔输出。",
        py=("# P1044 去重后输出（保留首次出现顺序）\n"
            "n = int(input())                              # 个数 n\n"
            "a = list(map(int, input().split()))           # 一行读入整个列表\n"
            "b = []\n"
            "for x in a:                                   # 遍历原列表\n"
            "    if x not in b:                            # 未出现过则保留\n"
            "        b.append(x)\n"
            "print(' '.join(map(str, b)))                  # 空格分隔输出\n"),
        cpp=("// P1044 去重后输出（保留首次出现顺序）\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> a(n), b;\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    for (int x : a) {                        // 遍历原列表\n"
             "        bool seen = false;\n"
             "        for (int y : b) if (y == x) { seen = true; break; }\n"
             "        if (!seen) b.push_back(x);           // 未出现过则保留\n"
             "    }\n"
             "    for (int i = 0; i < (int)b.size(); ++i) { // 空格分隔输出\n"
             "        if (i) cout << ' ';\n"
             "        cout << b[i];\n"
             "    }\n"
             "    cout << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1044 去重后输出（保留首次出现顺序）\n"
              "import java.util.Scanner;\n"
              "import java.util.ArrayList;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        ArrayList<Integer> b = new ArrayList<>();\n"
              "        for (int x : a) {                   // 遍历原列表\n"
              "            if (!b.contains(x)) b.add(x);    // 未出现过则保留\n"
              "        }\n"
              "        for (int i = 0; i < b.size(); ++i) { // 空格分隔输出\n"
              "            if (i > 0) System.out.print(' ');\n"
              "            System.out.print(b.get(i));\n"
              "        }\n"
              "        System.out.println();\n"
              "    }\n"
              "}\n"),
    )
