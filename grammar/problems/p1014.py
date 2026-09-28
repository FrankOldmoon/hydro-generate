# -*- coding: utf-8 -*-
"""P1014 时分秒转换"""
from generate import make_problem


def build():
    data = [3661, 3600, 60, 1, 0, 86399, 7200, 90, 36000, 54321]
    cases = [(f"{n}\n", f"{n // 3600}\n{(n % 3600) // 60}\n{n % 60}\n") for n in data]
    return make_problem(
        "P1014", "时分秒转换", ["入门", "数学"],
        cases=cases,
        desc_en="Given a non-negative integer n (the number of seconds), convert "
                "it into hours, minutes and seconds. Print the hours on the first "
                "line, the minutes on the second line, and the seconds on the third "
                "line.",
        input_en="One line containing a non-negative integer n (the number of "
                 "seconds), satisfying $0\\leq n\\leq 100000$ .",
        output_en="Three lines: the first line is the hours $\\lfloor n/3600\\rfloor$, "
                  "the second line is the minutes $\\lfloor (n\\bmod 3600)/60\\rfloor$, "
                  "the third line is the seconds $n\\bmod 60$.",
        desc_zh="给定一个非负整数 n（表示秒数），将其换算为时、分、秒。第一行输出时，"
                "第二行输出分，第三行输出秒。",
        input_zh="一行一个非负整数 n（秒数），满足 $0\\leq n\\leq 100000$ 。",
        output_zh="三行：第一行为时 $\\lfloor n/3600\\rfloor$，第二行为分 "
                  "$\\lfloor (n\\bmod 3600)/60\\rfloor$，第三行为秒 $n\\bmod 60$。",
        py=("# P1014 时分秒转换（整除与取余）\n"
            "n = int(input())          # 秒数 n\n"
            "print(n // 3600)          # 第一行：时\n"
            "print((n % 3600) // 60)   # 第二行：分\n"
            "print(n % 60)             # 第三行：秒\n"),
        cpp=("// P1014 时分秒转换\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                       // 读入秒数 n\n"
             "    cout << n / 3600 << endl;       // 第一行：时\n"
             "    cout << (n % 3600) / 60 << endl; // 第二行：分\n"
             "    cout << n % 60 << endl;          // 第三行：秒\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1014 时分秒转换\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();          // 秒数 n\n"
              "        System.out.println(n / 3600);        // 第一行：时\n"
              "        System.out.println((n % 3600) / 60);  // 第二行：分\n"
              "        System.out.println(n % 60);           // 第三行：秒\n"
              "    }\n"
              "}\n"),
    )
