# -*- coding: utf-8 -*-
"""P1084 统计数字出现次数"""
from generate import make_problem


def build():
    data = [
        (5, [123, 1122, 0, 555, 1001], 1),
        (1, [0], 0),
        (3, [111, 222, 333], 3),
        (1, [123456], 7),
        (4, [2020, 2002, 2200, 2222], 2),
        (2, [98765, 56789], 5),
        (1, [100000], 0),
        (3, [7, 77, 777], 7),
        (2, [1234321, 1111], 1),
        (1, [9999], 9),
    ]

    def count_digit(x, d):
        if x == 0:                  # 0 这个数本身含一个数字 0
            return 1 if d == 0 else 0
        cnt = 0
        while x > 0:
            if x % 10 == d:         # 末位等于 d
                cnt += 1
            x //= 10                # 去掉末位
        return cnt

    cases = []
    for n, nums, d in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums) + f"{d}\n"
        out = "".join(f"{count_digit(x, d)}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1084", "统计数字出现次数", ["入门", "函数"],
        cases=cases,
        desc_en="Given n non-negative integers and a digit d (0-9), print how "
                "many times d appears in each number.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain a non-negative integer. The last line "
                 "contains a digit d (0-9).",
        output_en="n lines: the count of digit d in each number.",
        desc_zh="给定 n 个非负整数和一个数字 d（0-9），输出每个数中数字 d 出现的次数。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个非负整数。最后一行一个数字 d"
                 "（0-9）。",
        output_zh="n 行，每行输出对应数中数字 d 出现的次数。",
        py=("# P1084 统计数字出现次数（自定义函数逐位判断）\n"
            "def count_digit(x, d):  # 定义统计数字 d 出现次数的函数\n"
            "    if x == 0:          # 0 这个数本身含一个数字 0\n"
            "        return 1 if d == 0 else 0\n"
            "    cnt = 0\n"
            "    while x > 0:        # 逐位处理\n"
            "        if x % 10 == d: # 末位等于 d\n"
            "            cnt += 1\n"
            "        x //= 10        # 去掉末位\n"
            "    return cnt\n"
            "\n"
            "n = int(input())        # 个数 n\n"
            "nums = []\n"
            "for i in range(n):\n"
            "    nums.append(int(input()))\n"
            "d = int(input())        # 待统计的数字 d\n"
            "for x in nums:\n"
            "    print(count_digit(x, d))\n"),
        cpp=("// P1084 统计数字出现次数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int count_digit(int x, int d) {  // 统计数字 d 出现次数\n"
             "    if (x == 0) return (d == 0) ? 1 : 0;  // 0 含一个 0\n"
             "    int cnt = 0;\n"
             "    while (x > 0) {\n"
             "        if (x % 10 == d) ++cnt;\n"
             "        x /= 10;\n"
             "    }\n"
             "    return cnt;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    int a[1000];\n"
             "    for (int i = 0; i < n; ++i) cin >> a[i];\n"
             "    int d;\n"
             "    cin >> d;\n"
             "    for (int i = 0; i < n; ++i)\n"
             "        cout << count_digit(a[i], d) << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1084 统计数字出现次数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static int countDigit(int x, int d) {  // 统计数字 d 出现次数\n"
              "        if (x == 0) return (d == 0) ? 1 : 0;  // 0 含一个 0\n"
              "        int cnt = 0;\n"
              "        while (x > 0) {\n"
              "            if (x % 10 == d) ++cnt;\n"
              "            x /= 10;\n"
              "        }\n"
              "        return cnt;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        int[] a = new int[n];\n"
              "        for (int i = 0; i < n; ++i) a[i] = sc.nextInt();\n"
              "        int d = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i)\n"
              "            System.out.println(countDigit(a[i], d));\n"
              "    }\n"
              "}\n"),
    )
