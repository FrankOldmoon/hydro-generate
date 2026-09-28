# -*- coding: utf-8 -*-
"""P1019 成绩是否及格"""
from generate import make_problem


def build():
    data = [60, 59, 100, 0, 75, 90, 1, 80, 33, 99]
    cases = [(f"{s}\n", f"{'Pass' if s >= 60 else 'Fail'}\n") for s in data]
    return make_problem(
        "P1019", "成绩是否及格", ["入门", "分支结构", "双分支"],
        cases=cases,
        desc_en="Given an integer score s (0 to 100), print \"Pass\" if s is at "
                "least 60, otherwise print \"Fail\".",
        input_en="One line containing an integer s (the score), satisfying "
                 "$0\\leq s\\leq 100$ .",
        output_en="One line containing \"Pass\" if $s\\geq 60$, otherwise \"Fail\".",
        desc_zh="给定一个整数成绩 s（0 到 100），及格（s 不低于 60）输出 \"Pass\"，否则输出 \"Fail\"。",
        input_zh="一行一个整数 s（成绩），满足 $0\\leq s\\leq 100$ 。",
        output_zh="一行，及格（$s\\geq 60$）输出 \"Pass\"，否则输出 \"Fail\"。",
        py=("# P1019 成绩是否及格（双分支：if-else）\n"
            "s = int(input())            # 成绩 s\n"
            "if s >= 60:                 # 双分支：不低于 60 为及格\n"
            "    print('Pass')           # 及格\n"
            "else:\n"
            "    print('Fail')           # 不及格\n"),
        cpp=("// P1019 成绩是否及格（双分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int s;\n"
             "    cin >> s;                // 读入成绩 s\n"
             "    if (s >= 60)             // 双分支：不低于 60 为及格\n"
             "        cout << \"Pass\" << endl;\n"
             "    else\n"
             "        cout << \"Fail\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1019 成绩是否及格（双分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int s = sc.nextInt();   // 成绩 s\n"
              "        if (s >= 60)            // 双分支：不低于 60 为及格\n"
              "            System.out.println(\"Pass\");\n"
              "        else\n"
              "            System.out.println(\"Fail\");\n"
              "    }\n"
              "}\n"),
    )
