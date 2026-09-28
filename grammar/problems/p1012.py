# -*- coding: utf-8 -*-
"""P1012 鸡兔同笼"""
from generate import make_problem


def build():
    data = [
        (10, 26), (5, 16), (3, 8), (8, 24), (1, 2),
        (1, 4), (10, 20), (10, 40), (20, 56), (100, 280),
    ]
    cases = []
    for h, l in data:
        r = (l - 2 * h) // 2   # 兔的数量
        c = h - r              # 鸡的数量
        cases.append((f"{h}\n{l}\n", f"{c}\n{r}\n"))
    return make_problem(
        "P1012", "鸡兔同笼", ["入门", "数学"],
        cases=cases,
        desc_en="A cage contains some chickens and rabbits. Given the total number "
                "of heads h and the total number of legs l, print the number of "
                "chickens and rabbits. Chickens have 2 legs, rabbits have 4 legs. "
                "The input is guaranteed to have a valid solution.",
        input_en="Two lines: the first line contains integer h (total heads), the "
                 "second line contains integer l (total legs), satisfying "
                 "$1\\leq h\\leq 1000$ and $1\\leq l\\leq 10000$ . The input is "
                 "guaranteed to have a valid solution.",
        output_en="Print two lines: the first line is the number of chickens, the "
                  "second line is the number of rabbits.",
        desc_zh="一个笼子里有若干只鸡和兔。已知头的总数 h 和腿的总数 l，输出鸡和兔的数量。鸡有 2 条腿，兔有 4 条腿。数据保证一定有解。",
        input_zh="两行：第一行一个整数 h（头的总数），第二行一个整数 l（腿的总数），满足 $1\\leq h\\leq 1000$ 且 $1\\leq l\\leq 10000$ 。数据保证一定有解。",
        output_zh="输出两行：第一行为鸡的数量，第二行为兔的数量。",
        py=("# P1012 鸡兔同笼\n"
            "# 每行一个整数，依次读入头数 h 和腿数 l，输出鸡、兔数量\n"
            "h = int(input())   # 头的总数 h\n"
            "l = int(input())   # 腿的总数 l\n"
            "r = (l - 2 * h) // 2   # 兔的数量：r = (l-2h)/2\n"
            "c = h - r              # 鸡的数量：c = h-r\n"
            "print(c)               # 第一行：鸡\n"
            "print(r)               # 第二行：兔\n"),
        cpp=("// P1012 鸡兔同笼\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int h, l;\n"
             "    cin >> h >> l;             // 依次读入头数 h 和腿数 l（每行一个）\n"
             "    int r = (l - 2 * h) / 2;   // 兔的数量\n"
             "    int c = h - r;             // 鸡的数量\n"
             "    cout << c << endl;         // 第一行：鸡\n"
             "    cout << r << endl;         // 第二行：兔\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1012 鸡兔同笼\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int h = sc.nextInt();   // 头的总数 h\n"
              "        int l = sc.nextInt();   // 腿的总数 l\n"
              "        int r = (l - 2 * h) / 2;   // 兔的数量\n"
              "        int c = h - r;             // 鸡的数量\n"
              "        System.out.println(c);    // 第一行：鸡\n"
              "        System.out.println(r);    // 第二行：兔\n"
              "    }\n"
              "}\n"),
    )
