# -*- coding: utf-8 -*-
"""P2004 时钟加分钟"""
from generate import make_problem


def build():
    data = [
        (0, 0, 0), (0, 0, 60), (23, 59, 1), (23, 0, 120),
        (12, 30, 45), (6, 15, 100), (15, 45, 500), (10, 10, 1440),
        (23, 30, 30), (23, 59, 1441),
    ]

    def solve(h, m, k):
        total = (h * 60 + m + k) % (24 * 60)
        return f"{total // 60:02d}:{total % 60:02d}"

    cases = [(f"{h}\n{m}\n{k}\n", f"{solve(h, m, k)}\n") for h, m, k in data]
    return make_problem(
        "P2004", "时钟加分钟", ["算法", "模拟"],
        cases=cases,
        desc_en="Given a 24-hour clock time h:m and a non-negative integer k "
                "(minutes), output the time k minutes later, wrapping around at "
                "midnight, in HH:MM format.",
        input_en="Three lines: the hour h, the minute m, and the added minutes k, "
                 "each on one line. $0\\leq h\\leq 23$, $0\\leq m\\leq 59$, "
                 "$0\\leq k\\leq 100000$ .",
        output_en="One line: the resulting time in HH:MM format (24-hour, two "
                  "digits for each part).",
        desc_zh="给定 24 小时制时间 h:m 和非负整数 k（分钟），输出 k 分钟后的时间，"
                "超过 23:59 则从 00:00 重新开始，格式为 HH:MM。",
        input_zh="三行：依次为小时 h、分钟 m、增加的分钟数 k，每行一个整数。"
                 "$0\\leq h\\leq 23$，$0\\leq m\\leq 59$，$0\\leq k\\leq 100000$ 。",
        output_zh="一行，k 分钟后的时间，格式为 HH:MM（24 小时制，各两位）。",
        py=("# P2004 时钟加分钟\n"
            "# 把当前时间化为总分钟数，加 k 后对 1440 取模，再转回 HH:MM\n"
            "h = int(input())                      # 小时\n"
            "m = int(input())                      # 分钟\n"
            "k = int(input())                      # 增加的分钟数\n"
            "t = (h * 60 + m + k) % 1440           # 总分钟数模一天\n"
            "print('%02d:%02d' % (t // 60, t % 60)) # 输出 HH:MM\n"),
        cpp=("// P2004 时钟加分钟\n"
             "#include <cstdio>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int h, m, k;\n"
             "    scanf(\"%d %d %d\", &h, &m, &k);       // 小时、分钟、增加分钟数\n"
             "    int t = (h * 60 + m + k) % 1440;      // 总分钟数模一天\n"
             "    printf(\"%02d:%02d\\n\", t / 60, t % 60); // 输出 HH:MM\n"
             "    return 0;\n"
             "}\n"),
        java=("// P2004 时钟加分钟\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int h = sc.nextInt();           // 小时\n"
              "        int m = sc.nextInt();           // 分钟\n"
              "        int k = sc.nextInt();           // 增加的分钟数\n"
              "        int t = (h * 60 + m + k) % 1440; // 总分钟数模一天\n"
              "        System.out.printf(\"%02d:%02d%n\", t / 60, t % 60); // HH:MM\n"
              "    }\n"
              "}\n"),
    )
