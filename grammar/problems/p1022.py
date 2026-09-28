# -*- coding: utf-8 -*-
"""P1022 判断非零（not 逻辑）"""
from generate import make_problem


def build():
    data = [0, 1, -1, 100, -100, 42, 32767, -32768, 999, -999]

    def ans(n):
        return "Zero" if n == 0 else "Nonzero"

    cases = [(f"{n}\n", f"{ans(n)}\n") for n in data]
    return make_problem(
        "P1022", "判断非零", ["入门", "分支结构", "逻辑运算", "not"],
        cases=cases,
        desc_en="Given an integer n, print \"Nonzero\" if n is NOT equal to 0, "
                "otherwise print \"Zero\".",
        input_en="One line containing an integer n, satisfying "
                 "$-32768\\leq n\\leq 32767$ .",
        output_en="One line: \"Nonzero\" if $n\\neq 0$, otherwise \"Zero\".",
        desc_zh="给定一个整数 n，若 n 不为 0 输出 \"Nonzero\"，否则输出 \"Zero\"。",
        input_zh="一行一个整数 n，满足 $-32768\\leq n\\leq 32767$ 。",
        output_zh="一行，$n\\neq 0$ 输出 \"Nonzero\"，否则输出 \"Zero\"。",
        py=("# P1022 判断非零（not 逻辑：对“等于 0”取反）\n"
            "n = int(input())            # 整数 n\n"
            "if not (n == 0):            # not 逻辑：n 不为 0\n"
            "    print('Nonzero')\n"
            "else:\n"
            "    print('Zero')\n"),
        cpp=("// P1022 判断非零（not 逻辑）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入整数 n\n"
             "    if (!(n == 0)) {         // not 逻辑：n 不为 0\n"
             "        cout << \"Nonzero\" << endl;\n"
             "    } else {\n"
             "        cout << \"Zero\" << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1022 判断非零（not 逻辑）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 整数 n\n"
              "        if (!(n == 0)) {        // not 逻辑：n 不为 0\n"
              "            System.out.println(\"Nonzero\");\n"
              "        } else {\n"
              "            System.out.println(\"Zero\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
