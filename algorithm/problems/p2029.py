# -*- coding: utf-8 -*-
"""P2029 成绩排名"""
from generate import make_problem


def build():
    # 每组：[(姓名, 语文, 数学, 英语)]，按总分降序，同分按姓名字典序升序
    data = [
        [("Alice", 90, 80, 70), ("Bob", 70, 80, 90), ("Carol", 80, 80, 80)],
        [("Alice", 100, 100, 100), ("Bob", 50, 50, 50), ("Carol", 80, 80, 80)],
        [("Tom", 60, 60, 60)],
        [("Dave", 90, 90, 90), ("Eve", 90, 90, 90), ("Amy", 90, 90, 90), ("Bob", 90, 90, 90)],
        [("Zac", 90, 90, 90), ("Amy", 80, 90, 100), ("Ben", 100, 100, 100), ("Leo", 0, 0, 0)],
        [("Ann", 50, 50, 50), ("Ben", 50, 50, 51)],
        [("Cara", 70, 80, 90), ("Dave", 90, 80, 70), ("Eve", 80, 80, 80),
         ("Frank", 100, 100, 100), ("Grace", 0, 0, 0)],
        [("Sam", 85, 85, 85), ("Amy", 85, 85, 85)],
        [("Xena", 100, 0, 0), ("Yara", 0, 100, 0), ("Zara", 0, 0, 100)],
        [("Ann", 100, 100, 100), ("Bob", 100, 100, 99), ("Cath", 99, 100, 100),
         ("Dan", 0, 0, 0), ("Eve", 50, 50, 50), ("Fay", 50, 50, 50)],
    ]
    cases = []
    for students in data:
        n = len(students)
        inp = f"{n}\n" + "\n".join(f"{nm} {c} {m} {e}" for nm, c, m, e in students) + "\n"
        arr = [(nm, c + m + e) for nm, c, m, e in students]
        arr.sort(key=lambda x: (-x[1], x[0]))   # 总分降序，同分姓名升序
        out = "\n".join(f"{nm} {tot}" for nm, tot in arr) + "\n"
        cases.append((inp, out))
    return make_problem(
        "P2029", "成绩排名", ["算法", "排序"],
        cases=cases,
        desc_en="Given n students, each on a line as \"name chinese math english\", "
                "sort by total score descending. Students with the same total are "
                "sorted by name in ascending lexicographic order. Output each "
                "student as \"name total\" per line.",
        input_en="The first line contains a positive integer n. Then n lines "
                 "follow, each containing a name and three non-negative integer "
                 "scores separated by spaces, satisfying $1\\leq n\\leq 100$, "
                 "$0\\leq score\\leq 100$ and the name consists of letters only.",
        output_en="n lines, each containing \"name total\" in the sorted order.",
        desc_zh="给定 n 个学生（每行\"姓名 语文 数学 英语\"），按总分降序输出，每行输出\"姓名 总分\"，同分按姓名字典序升序排列。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个姓名和三个用空格分隔的非负整数成绩，满足 $1\\leq n\\leq 100$、$0\\leq 成绩\\leq 100$ 且姓名仅由字母组成。",
        output_zh="共 n 行，每行\"姓名 总分\"，按总分降序输出，同分按姓名字典序升序。",
        py=r"""# P2029 成绩排名（按总分降序，同分按姓名字典序升序）
n = int(input())                       # 学生人数 n
stu = []
for _ in range(n):
    parts = input().split()
    name = parts[0]                    # 姓名
    total = int(parts[1]) + int(parts[2]) + int(parts[3])  # 总分
    stu.append((name, total))
stu.sort(key=lambda x: (-x[1], x[0]))  # 总分降序，同分姓名升序
for name, total in stu:
    print(name, total)                 # 每行输出"姓名 总分"
""",
        cpp=r"""// P2029 成绩排名（按总分降序，同分按姓名字典序升序）
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
struct Stu { string name; int total; };
bool cmp(const Stu &a, const Stu &b) {
    if (a.total != b.total) return a.total > b.total;  // 总分降序
    return a.name < b.name;            // 同分姓名字典序升序
}
int main() {
    int n;
    cin >> n;                          // 学生人数 n
    Stu s[105];
    for (int i = 0; i < n; i++) {
        int c, m, e;
        cin >> s[i].name >> c >> m >> e;
        s[i].total = c + m + e;        // 总分
    }
    sort(s, s + n, cmp);               // 排序
    for (int i = 0; i < n; i++)
        cout << s[i].name << ' ' << s[i].total << endl;  // 每行"姓名 总分"
    return 0;
}
""",
        java=r"""// P2029 成绩排名（按总分降序，同分按姓名字典序升序）
import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();          // 学生人数 n
        String[] names = new String[n];
        Integer[] idx = new Integer[n];
        int[] total = new int[n];
        for (int i = 0; i < n; i++) {
            names[i] = sc.next();      // 姓名
            int c = sc.nextInt(), m = sc.nextInt(), e = sc.nextInt();
            total[i] = c + m + e;      // 总分
            idx[i] = i;
        }
        // 按总分降序，同分按姓名字典序升序
        Arrays.sort(idx, new Comparator<Integer>() {
            public int compare(Integer x, Integer y) {
                if (total[x] != total[y]) return total[y] - total[x];
                return names[x].compareTo(names[y]);
            }
        });
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int t = idx[i];
            sb.append(names[t]).append(' ').append(total[t]).append('\n');
        }
        System.out.print(sb);
    }
}
""",
    )
