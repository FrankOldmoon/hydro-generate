# -*- coding: utf-8 -*-
"""P1077 判断素数"""
from generate import make_problem


def build():
    data = [
        (5, [2, 3, 4, 5, 6]),
        (1, [1]),
        (3, [7, 8, 9]),
        (1, [2]),
        (4, [11, 13, 15, 17]),
        (2, [97, 100]),
        (1, [25]),
        (3, [1, 0, 2]),
        (6, [2, 3, 5, 7, 11, 13]),
        (3, [49, 50, 51]),
    ]

    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        out = "".join(f"{'Yes' if is_prime(x) else 'No'}\n" for x in nums)
        cases.append((inp, out))
    return make_problem(
        "P1077", "判断素数", ["入门", "函数"],
        cases=cases,
        desc_en="Given n and n positive integers, determine whether each is prime. "
                "Print \"Yes\" if prime, otherwise \"No\".",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain one non-negative integer.",
        output_en="n lines: \"Yes\" if the number is prime, otherwise \"No\".",
        desc_zh="给定 n 及 n 个非负整数，判断每个数是否为素数。是输出 \"Yes\"，否则输出 "
                "\"No\"。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个非负整数。",
        output_zh="n 行，素数输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1077 判断素数（自定义函数判断素数）\n"
            "def is_prime(x):              # 定义判断素数的函数\n"
            "    if x < 2:\n"
            "        return False\n"
            "    if x == 2:\n"
            "        return True\n"
            "    if x % 2 == 0:\n"
            "        return False\n"
            "    i = 3\n"
            "    while i * i <= x:        # 只需检查到 sqrt(x)\n"
            "        if x % i == 0:\n"
            "            return False\n"
            "        i += 2\n"
            "    return True\n"
            "\n"
            "n = int(input())              # 个数 n\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if is_prime(x):\n"
            "        print('Yes')\n"
            "    else:\n"
            "        print('No')\n"),
        cpp=("// P1077 判断素数\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_prime(int x) {         // 判断素数\n"
             "    if (x < 2) return false;\n"
             "    if (x == 2) return true;\n"
             "    if (x % 2 == 0) return false;\n"
             "    for (int i = 3; i * i <= x; i += 2)\n"
             "        if (x % i == 0) return false;\n"
             "    return true;\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        cout << (is_prime(x) ? \"Yes\" : \"No\") << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1077 判断素数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isPrime(int x) {  // 判断素数\n"
              "        if (x < 2) return false;\n"
              "        if (x == 2) return true;\n"
              "        if (x % 2 == 0) return false;\n"
              "        for (int i = 3; i * i <= x; i += 2)\n"
              "            if (x % i == 0) return false;\n"
              "        return true;\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            System.out.println(isPrime(x) ? \"Yes\" : \"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
