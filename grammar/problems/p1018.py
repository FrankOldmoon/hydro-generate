# -*- coding: utf-8 -*-
"""P1018 判断奇偶"""
from generate import make_problem


def build():
    data = [2, 3, 0, 100, 7, -1, -2, 99, 256, 42]
    cases = [(f"{n}\n", f"{'Even' if n % 2 == 0 else 'Odd'}\n") for n in data]
    return make_problem(
        "P1018", "判断奇偶", ["入门", "分支结构", "双分支"],
        cases=cases,
        desc_en="Given an integer n, print \"Even\" if n is even, otherwise print "
                "\"Odd\".",
        input_en="One line containing an integer n, satisfying "
                 "$-100000\\leq n\\leq 100000$ .",
        output_en="One line containing \"Even\" if n is even, otherwise \"Odd\".",
        desc_zh="给定一个整数 n，是偶数输出 \"Even\"，是奇数输出 \"Odd\"。",
        input_zh="一行一个整数 n，满足 $-100000\\leq n\\leq 100000$ 。",
        output_zh="一行，偶数输出 \"Even\"，奇数输出 \"Odd\"。",
        py=("# P1018 判断奇偶（双分支：if-else）\n"
            "n = int(input())            # 整数 n\n"
            "if n % 2 == 0:              # 双分支：能被 2 整除为偶数\n"
            "    print('Even')           # 偶数\n"
            "else:\n"
            "    print('Odd')            # 奇数\n"),
        cpp=("// P1018 判断奇偶（双分支）\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;                // 读入整数 n\n"
             "    if (n % 2 == 0)          // 双分支：能被 2 整除为偶数\n"
             "        cout << \"Even\" << endl;\n"
             "    else\n"
             "        cout << \"Odd\" << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1018 判断奇偶（双分支）\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();   // 整数 n\n"
              "        if (n % 2 == 0)         // 双分支：偶数\n"
              "            System.out.println(\"Even\");\n"
              "        else\n"
              "            System.out.println(\"Odd\");\n"
              "    }\n"
              "}\n"),
    )
