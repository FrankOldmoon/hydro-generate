# -*- coding: utf-8 -*-
"""P1025 三角形判断与分类（嵌套分支）"""
from generate import make_problem


def build():
    data = [
        (3, 4, 5), (3, 3, 3), (3, 3, 4), (1, 1, 2), (5, 5, 8),
        (3, 4, 8), (6, 6, 6), (4, 5, 6), (1, 2, 3), (7, 7, 7),
    ]

    def kind(a, b, c):
        s = sorted([a, b, c])
        x, y, z = s  # x <= y <= z
        if x + y <= z:           # 不能构成三角形
            return "NotTriangle"
        # 内层分支：判断三角形类型
        if a == b == c:
            return "Equilateral"
        if a == b or b == c or a == c:
            return "Isosceles"
        return "Scalene"

    cases = [(f"{a}\n{b}\n{c}\n", f"{kind(a, b, c)}\n") for a, b, c in data]
    return make_problem(
        "P1025", "三角形判断与分类", ["入门", "分支结构", "嵌套分支"],
        cases=cases,
        desc_en="Given three integers a, b, c (side lengths), determine: if they "
                "cannot form a triangle (i.e. the sum of the two smaller sides is "
                "not greater than the largest side), print \"NotTriangle\"; "
                "otherwise print \"Equilateral\" if all three sides are equal, "
                "\"Isosceles\" if exactly two sides are equal, or \"Scalene\" if "
                "all three sides differ.",
        input_en="Three lines: each line contains one integer. Denote them a, b, "
                 "c from top to bottom, satisfying $1\\leq a,b,c\\leq 32767$ .",
        output_en="One line: \"NotTriangle\", \"Equilateral\", \"Isosceles\", or "
                  "\"Scalene\" according to the rules above.",
        desc_zh="给定三个整数 a、b、c（三条边的长度），判断：若不能构成三角形（较短两边之和不大于"
                "最长边）输出 \"NotTriangle\"；否则三边相等输出 \"Equilateral\"，恰有两边相等输出 "
                "\"Isosceles\"，三边互不相等输出 \"Scalene\"。",
        input_zh="三行：每行一个整数，从上到下依次为 a、b、c，满足 $1\\leq a,b,c\\leq 32767$ 。",
        output_zh="一行：按上述规则输出 \"NotTriangle\"/\"Equilateral\"/\"Isosceles\"/"
                  "\"Scalene\" 之一。",
        py=("# P1025 三角形判断与分类（嵌套分支：外层判合法性，内层判类型）\n"
            "a = int(input())          # 第一行：a\n"
            "b = int(input())          # 第二行：b\n"
            "c = int(input())          # 第三行：c\n"
            "s = sorted([a, b, c])      # 排序：s[0] <= s[1] <= s[2]\n"
            "if s[0] + s[1] <= s[2]:    # 外层分支：不能构成三角形\n"
            "    print('NotTriangle')\n"
            "else:                      # 能构成三角形，进入内层分支\n"
            "    if a == b == c:        # 内层：三边相等\n"
            "        print('Equilateral')\n"
            "    elif a == b or b == c or a == c:   # 内层：恰有两边相等\n"
            "        print('Isosceles')\n"
            "    else:                  # 内层：三边互不相等\n"
            "        print('Scalene')\n"),
        cpp=("// P1025 三角形判断与分类（嵌套分支）\n"
             "#include <iostream>\n"
             "#include <algorithm>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int a, b, c;\n"
             "    cin >> a >> b >> c;          // 依次读入 a、b、c（每行一个）\n"
             "    int s[3] = {a, b, c};\n"
             "    sort(s, s + 3);              // 排序：s[0] <= s[1] <= s[2]\n"
             "    if (s[0] + s[1] <= s[2]) {   // 外层分支：不能构成三角形\n"
             "        cout << \"NotTriangle\" << endl;\n"
             "    } else {                     // 能构成三角形，进入内层分支\n"
             "        if (a == b && b == c)    // 内层：三边相等\n"
             "            cout << \"Equilateral\" << endl;\n"
             "        else if (a == b || b == c || a == c)   // 内层：恰有两边相等\n"
             "            cout << \"Isosceles\" << endl;\n"
             "        else                     // 内层：三边互不相等\n"
             "            cout << \"Scalene\" << endl;\n"
             "    }\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1025 三角形判断与分类（嵌套分支）\n"
              "import java.util.Scanner;\n"
              "import java.util.Arrays;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int a = sc.nextInt();      // 第一行：a\n"
              "        int b = sc.nextInt();      // 第二行：b\n"
              "        int c = sc.nextInt();      // 第三行：c\n"
              "        int[] s = {a, b, c};\n"
              "        Arrays.sort(s);            // 排序：s[0] <= s[1] <= s[2]\n"
              "        if (s[0] + s[1] <= s[2]) { // 外层分支：不能构成三角形\n"
              "            System.out.println(\"NotTriangle\");\n"
              "        } else {                   // 能构成三角形，进入内层分支\n"
              "            if (a == b && b == c)  // 内层：三边相等\n"
              "                System.out.println(\"Equilateral\");\n"
              "            else if (a == b || b == c || a == c)   // 内层：恰有两边相等\n"
              "                System.out.println(\"Isosceles\");\n"
              "            else                   // 内层：三边互不相等\n"
              "                System.out.println(\"Scalene\");\n"
              "        }\n"
              "    }\n"
              "}\n"),
    )
