# -*- coding: utf-8 -*-
"""P1021 成绩等级评定（多分支：5 个分支）"""
from generate import make_problem


def build():
    data = [95, 85, 75, 65, 55, 100, 0, 90, 80, 60]

    def grade(s):
        if s >= 90:
            return "A"
        elif s >= 80:
            return "B"
        elif s >= 70:
            return "C"
        elif s >= 60:
            return "D"
        else:
            return "F"

    cases = [(f"{s}\n", f"{grade(s)}\n") for s in data]
    return make_problem(
        "P1021", "成绩等级评定", ["入门", "分支结构", "多分支"],
        cases=cases,
        desc_en="Given an integer score s (0 to 100), print its grade: \"A\" if "
                "$s\\geq 90$, \"B\" if $80\\leq s<90$, \"C\" if $70\\leq s<80$, "
                "\"D\" if $60\\leq s<70$, otherwise \"F\".",
        input_en="One line containing an integer s (the score), satisfying "
                 "$0\\leq s\\leq 100$ .",
        output_en="One line: \"A\"/\"B\"/\"C\"/\"D\"/\"F\" according to the rules above.",
        desc_zh="给定一个整数成绩 s（0 到 100），输出等级：$s\\geq 90$ 为 \"A\"，"
                "$80\\leq s<90$ 为 \"B\"，$70\\leq s<80$ 为 \"C\"，$60\\leq s<70$ 为 "
                "\"D\"，否则为 \"F\"。",
        input_zh="一行一个整数 s（成绩），满足 $0\\leq s\\leq 100$ 。",
        output_zh="一行：按上述规则输出 \"A\"/\"B\"/\"C\"/\"D\"/\"F\" 之一。",
        py=("# P1021 成绩等级评定（多分支：if-elif-...-else，共 5 个分支）\n"
            "s = int(input())            # 成绩 s\n"
            "if s >= 90:                 # A 档\n"
            "    print('A')\n"
            "elif s >= 80:               # B 档\n"
            "    print('B')\n"
            "elif s >= 70:               # C 档\n"
            "    print('C')\n"
            "elif s >= 60:               # D 档\n"
            "    print('D')\n"
            "else:                       # F 档（不及格）\n"
            "    print('F')\n"),
        cpp=("// P1021 成绩等级评定（多分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int s;\n"
             "    cin >> s;                // 读入成绩 s\n"
             "    if (s >= 90)             // A 档\n"
             "        cout << \"A\" << endl;\n"
             "    else if (s >= 80)        // B 档\n"
             "        cout << \"B\" << endl;\n"
             "    else if (s >= 70)        // C 档\n"
             "        cout << \"C\" << endl;\n"
             "    else if (s >= 60)        // D 档\n"
             "        cout << \"D\" << endl;\n"
             "    else                     // F 档\n"
             "        cout << \"F\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1021 成绩等级评定（多分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int s = sc.nextInt();   // 成绩 s\n"
              "        if (s >= 90)             // A 档\n"
              "            System.out.println(\"A\");\n"
              "        else if (s >= 80)        // B 档\n"
              "            System.out.println(\"B\");\n"
              "        else if (s >= 70)        // C 档\n"
              "            System.out.println(\"C\");\n"
              "        else if (s >= 60)        // D 档\n"
              "            System.out.println(\"D\");\n"
              "        else                     // F 档\n"
              "            System.out.println(\"F\");\n"
              "    }\n"
              "}\n"),
    )
