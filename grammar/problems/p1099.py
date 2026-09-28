# -*- coding: utf-8 -*-
"""P1099 递归判断2的幂"""
from generate import make_problem


def build():
    data = [1, 2, 3, 4, 8, 10, 16, 100, 256, 1024]

    def is_pow2(n):
        if n == 1:                  # 递归出口：1 是 2 的 0 次幂
            return True
        if n % 2 != 0:             # 奇数（>1）不是 2 的幂
            return False
        return is_pow2(n // 2)     # 继续除以 2 判断

    cases = [(f"{n}\n", f"{'Yes' if is_pow2(n) else 'No'}\n") for n in data]
    return make_problem(
        "P1099", "判断2的幂", ["入门", "递归"],
        cases=cases,
        desc_en="Given a positive integer n, determine whether n is a power of 2 "
                "(i.e., n = 1, 2, 4, 8, 16, ...). Print \"Yes\" or \"No\".",
        input_en="One line containing a positive integer n, satisfying "
                 "$1\\leq n\\leq 1000000000$ .",
        output_en="One line: \"Yes\" if n is a power of 2, otherwise \"No\".",
        desc_zh="给定一个正整数 n，判断 n 是否为 2 的幂（即 n = 1, 2, 4, 8, "
                "16, ...）。是输出 \"Yes\"，否则输出 \"No\"。",
        input_zh="一行一个正整数 n，满足 $1\\leq n\\leq 1000000000$ 。",
        output_zh="一行，是 2 的幂输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1099 递归判断2的幂（递归：不断除以2）\n"
            "def is_pow2(n):           # 定义递归函数\n"
            "    if n == 1:          # 递归出口：1 是 2^0\n"
            "        return True\n"
            "    if n % 2 != 0:     # 奇数（>1）不是 2 的幂\n"
            "        return False\n"
            "    return is_pow2(n // 2)  # 继续除以 2 判断\n"
            "\n"
            "n = int(input())          # 正整数 n\n"
            "if is_pow2(n):\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1099 递归判断2的幂\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "bool is_pow2(int n) {   // 递归判断 2 的幂\n"
             "    if (n == 1) return true;     // 递归出口\n"
             "    if (n % 2 != 0) return false; // 奇数不是\n"
             "    return is_pow2(n / 2);\n"
             "}\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    cout << (is_pow2(n) ? \"Yes\" : \"No\") << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1099 递归判断2的幂\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    static boolean isPow2(int n) {  // 递归判断 2 的幂\n"
              "        if (n == 1) return true;     // 递归出口\n"
              "        if (n % 2 != 0) return false; // 奇数不是\n"
              "        return isPow2(n / 2);\n"
              "    }\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        System.out.println(isPow2(n) ? \"Yes\" : \"No\");\n"
              "    }\n"
              "}\n"),
    )
