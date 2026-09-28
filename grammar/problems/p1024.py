# -*- coding: utf-8 -*-
"""P1024 3或5的倍数（or 逻辑）"""
from generate import make_problem


def build():
    data = [3, 5, 15, 7, 2, 9, 10, 11, 30, 1]

    def ans(n):
        return "Yes" if (n % 3 == 0 or n % 5 == 0) else "No"

    cases = [(f"{n}\n", f"{ans(n)}\n") for n in data]
    return make_problem(
        "P1024", "3或5的倍数", ["入门", "分支结构", "逻辑运算", "or"],
        cases=cases,
        desc_en="Given an integer n, print \"Yes\" if n is a multiple of 3 OR a "
                "multiple of 5, otherwise print \"No\".",
        input_en="One line containing an integer n, satisfying "
                 "$-100000\\leq n\\leq 100000$ .",
        output_en="One line: \"Yes\" if $n\\bmod 3=0$ or $n\\bmod 5=0$, "
                  "otherwise \"No\".",
        desc_zh="给定一个整数 n，若 n 是 3 的倍数或 5 的倍数，输出 \"Yes\"，否则输出 \"No\"。",
        input_zh="一行一个整数 n，满足 $-100000\\leq n\\leq 100000$ 。",
        output_zh="一行，$n\\bmod 3=0$ 或 $n\\bmod 5=0$ 输出 \"Yes\"，否则输出 \"No\"。",
        py=("# P1024 3或5的倍数（or 逻辑：满足任一条件即可）\n"
            "n = int(input())            # 整数 n\n"
            "if n % 3 == 0 or n % 5 == 0:   # or 逻辑：是 3 或 5 的倍数\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')\n"),
        cpp=("// P1024 3或5的倍数（or 逻辑）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入整数 n\n"
             "    if (n % 3 == 0 || n % 5 == 0) {  // or 逻辑\n"
             "        cout << \"Yes\" << endl;\n"
             "    } else {\n"
             "        cout << \"No\" << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1024 3或5的倍数（or 逻辑）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 整数 n\n"
              "        if (n % 3 == 0 || n % 5 == 0) {  // or 逻辑\n"
              "            System.out.println(\"Yes\");\n"
              "        } else {\n"
              "            System.out.println(\"No\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
