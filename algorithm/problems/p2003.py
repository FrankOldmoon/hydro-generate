# -*- coding: utf-8 -*-
"""P2003 某年第几天"""
from generate import make_problem


def build():
    data = [
        (2000, 3, 1), (1900, 3, 1), (2000, 1, 1), (2000, 12, 31),
        (2001, 12, 31), (2004, 2, 29), (2003, 2, 28), (1996, 7, 1),
        (2020, 3, 1), (2023, 11, 15),
    ]

    def is_leap(y):
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

    def solve(y, mo, d):
        days = [31, 29 if is_leap(y) else 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        return sum(days[:mo - 1]) + d

    cases = [(f"{y}\n{mo}\n{d}\n", f"{solve(y, mo, d)}\n") for y, mo, d in data]
    return make_problem(
        "P2003", "某年第几天", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a date (year, month, day), determine which day of the year "
                "it is. Note the leap year rule: a year is a leap year if it is "
                "divisible by 400, or divisible by 4 but not by 100.",
        input_en="Three lines: the year, the month and the day, each on one line. "
                 "The date is a valid Gregorian date with "
                 "$1\\leq \\text{year}\\leq 9999$ .",
        output_en="One line: the day-of-year number (1-based).",
        desc_zh="给定一个日期（年、月、日），求该日是该年的第几天。注意闰年规则：能被 400 "
                "整除，或能被 4 整除但不能被 100 整除的年份为闰年。",
        input_zh="三行：依次为年、月、日，每行一个整数。保证是合法的格里高利历日期，"
                 "$1\\leq \\text{年}\\leq 9999$ 。",
        output_zh="一行，该日是该年的第几天（从 1 开始）。",
        py=("# P2003 某年第几天\n"
            "# 读入年月日，累加本月之前各月天数，再加上当日，注意闰年二月\n"
            "y = int(input())                       # 年\n"
            "mo = int(input())                      # 月\n"
            "d = int(input())                       # 日\n"
            "days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n"
            "if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):  # 闰年二月 29 天\n"
            "    days[1] = 29\n"
            "print(sum(days[:mo - 1]) + d)          # 前 mo-1 月天数 + 当日\n"),
        cpp=("// P2003 某年第几天\n"
             "#include <iostream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int y, mo, d;\n"
             "    cin >> y >> mo >> d;             // 年、月、日\n"
             "    int days[] = {0,31,28,31,30,31,30,31,31,30,31,30,31}; // 下标 1..12\n"
             "    bool leap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);\n"
             "    if (leap) days[2] = 29;          // 闰年二月 29 天\n"
             "    int s = 0;\n"
             "    for (int i = 1; i < mo; ++i) s += days[i]; // 前 mo-1 月\n"
             "    s += d;                           // 加当日\n"
             "    cout << s << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2003 某年第几天\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int y = sc.nextInt();        // 年\n"
              "        int mo = sc.nextInt();       // 月\n"
              "        int d = sc.nextInt();        // 日\n"
              "        int[] days = {0,31,28,31,30,31,30,31,31,30,31,30,31};\n"
              "        boolean leap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);\n"
              "        if (leap) days[2] = 29;      // 闰年二月 29 天\n"
              "        int s = 0;\n"
              "        for (int i = 1; i < mo; ++i) s += days[i]; // 前 mo-1 月\n"
              "        s += d;                       // 加当日\n"
              "        System.out.println(s);\n"
              "    }\n"
              "}\n"),
    )
