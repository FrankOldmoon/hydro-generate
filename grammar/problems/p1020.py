# -*- coding: utf-8 -*-
"""P1020 判断正负零（三分支）"""
from generate import make_problem


def build():
    data = [5, -5, 0, 100, -1, 32767, -32768, 42, -42, 1]

    def cls(n):
        return "Positive" if n > 0 else ("Zero" if n == 0 else "Negative")

    cases = [(f"{n}\n", f"{cls(n)}\n") for n in data]
    return make_problem(
        "P1020", "判断正负零", ["入门", "分支结构", "三分支"],
        cases=cases,
        desc_en="Given an integer n, print \"Positive\" if n is positive, "
                "\"Zero\" if n is zero, or \"Negative\" if n is negative.",
        input_en="One line containing an integer n, satisfying "
                 "$-32768\\leq n\\leq 32767$ .",
        output_en="One line: \"Positive\" if $n>0$, \"Zero\" if $n=0$, "
                  "\"Negative\" if $n<0$.",
        desc_zh="给定一个整数 n，正数输出 \"Positive\"，零输出 \"Zero\"，负数输出 \"Negative\"。",
        input_zh="一行一个整数 n，满足 $-32768\\leq n\\leq 32767$ 。",
        output_zh="一行：$n>0$ 输出 \"Positive\"，$n=0$ 输出 \"Zero\"，$n<0$ 输出 \"Negative\"。",
        py=("# P1020 判断正负零（三分支：if-elif-else）\n"
            "n = int(input())            # 整数 n\n"
            "if n > 0:                   # 三分支：正数\n"
            "    print('Positive')\n"
            "elif n == 0:                # 零\n"
            "    print('Zero')\n"
            "else:                       # 负数\n"
            "    print('Negative')\n"),
        cpp=("// P1020 判断正负零（三分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入整数 n\n"
             "    if (n > 0)               // 三分支：正数\n"
             "        cout << \"Positive\" << endl;\n"
             "    else if (n == 0)         // 零\n"
             "        cout << \"Zero\" << endl;\n"
             "    else                     // 负数\n"
             "        cout << \"Negative\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1020 判断正负零（三分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 整数 n\n"
              "        if (n > 0)              // 三分支：正数\n"
              "            System.out.println(\"Positive\");\n"
              "        else if (n == 0)        // 零\n"
              "            System.out.println(\"Zero\");\n"
              "        else                    // 负数\n"
              "            System.out.println(\"Negative\");\n"
              "    }\n"
              "}\n"),
    )
