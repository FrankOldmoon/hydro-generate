# -*- coding: utf-8 -*-
"""P1023 点是否在矩形内（and 逻辑）"""
from generate import make_problem


def build():
    data = [
        (5, 5), (15, 5), (5, 15), (-1, 5), (0, 0),
        (10, 10), (11, 11), (3, 8), (10, 5), (5, 10),
    ]

    def pos(x, y):
        return "Inside" if (0 <= x <= 10 and 0 <= y <= 10) else "Outside"

    cases = [(f"{x}\n{y}\n", f"{pos(x, y)}\n") for x, y in data]
    return make_problem(
        "P1023", "点是否在矩形内", ["入门", "分支结构", "逻辑运算", "and"],
        cases=cases,
        desc_en="Given a point (x, y), print \"Inside\" if it lies inside or on "
                "the rectangle $[0,10]\\times[0,10]$ (i.e. $0\\leq x\\leq 10$ AND "
                "$0\\leq y\\leq 10$), otherwise print \"Outside\".",
        input_en="Two lines: each line contains one integer. Denote them x, y "
                 "from top to bottom, satisfying $-100\\leq x,y\\leq 100$ .",
        output_en="One line: \"Inside\" if $0\\leq x\\leq 10$ and $0\\leq y\\leq 10$, "
                  "otherwise \"Outside\".",
        desc_zh="给定一个点的坐标 (x, y)，若它在矩形 $[0,10]\\times[0,10]$ 内（含边界，即 "
                "$0\\leq x\\leq 10$ 且 $0\\leq y\\leq 10$）输出 \"Inside\"，否则输出 "
                "\"Outside\"。",
        input_zh="两行：每行一个整数，从上到下依次为 x、y，满足 $-100\\leq x,y\\leq 100$ 。",
        output_zh="一行，满足 $0\\leq x\\leq 10$ 且 $0\\leq y\\leq 10$ 输出 \"Inside\"，"
                   "否则输出 \"Outside\"。",
        py=("# P1023 点是否在矩形内（and 逻辑：横纵坐标同时落在区间内）\n"
            "x = int(input())               # 第一行：x\n"
            "y = int(input())               # 第二行：y\n"
            "if 0 <= x <= 10 and 0 <= y <= 10:   # and 逻辑：两个条件同时成立\n"
            "    print('Inside')\n"
            "else:\n"
            "    print('Outside')\n"),
        cpp=("// P1023 点是否在矩形内（and 逻辑）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int x, y;\n"
             "    cin >> x >> y;                 // 依次读入 x、y（每行一个）\n"
             "    if (x >= 0 && x <= 10 && y >= 0 && y <= 10) {  // and 逻辑\n"
             "        cout << \"Inside\" << endl;\n"
             "    } else {\n"
             "        cout << \"Outside\" << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1023 点是否在矩形内（and 逻辑）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int x = sc.nextInt();          // 第一行：x\n"
              "        int y = sc.nextInt();          // 第二行：y\n"
              "        if (x >= 0 && x <= 10 && y >= 0 && y <= 10) {  // and 逻辑\n"
              "            System.out.println(\"Inside\");\n"
              "        } else {\n"
              "            System.out.println(\"Outside\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
