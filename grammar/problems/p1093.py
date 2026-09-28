# -*- coding: utf-8 -*-
"""P1093 删除相邻重复元素"""
from generate import make_problem


def build():
    data = [
        (7, [1, 2, 2, 3, 3, 2, 1]),
        (4, [1, 1, 2, 2]),
        (6, [1, 2, 3, 3, 2, 1]),
        (1, [5]),
        (2, [1, 2]),
        (5, [1, 1, 1, 1, 1]),
        (3, [1, 2, 1]),
        (8, [1, 2, 2, 1, 3, 3, 4, 4]),
        (4, [1, 2, 3, 3]),
        (6, [1, 1, 2, 3, 3, 2]),
    ]

    def solve(nums):
        stack = []
        for x in nums:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        return stack

    cases = []
    for n, nums in data:
        inp = f"{n}\n" + "".join(f"{x}\n" for x in nums)
        result = solve(nums)
        out = f"{len(result)}\n" + "".join(f"{x}\n" for x in result)
        cases.append((inp, out))
    return make_problem(
        "P1093", "删除相邻重复元素", ["入门", "栈"],
        cases=cases,
        desc_en="Given n integers, repeatedly remove adjacent equal pairs until no "
                "adjacent duplicates remain. Print the count and the remaining "
                "elements in order.",
        input_en="The first line contains a positive integer n. The following n "
                 "lines each contain an integer.",
        output_en="The first line is the count k of remaining elements. The "
                  "following k lines are the remaining elements in order.",
        desc_zh="给定 n 个整数，不断删除相邻相同的元素对，直到没有相邻重复为止。先输出"
                "剩余元素个数，再按顺序输出剩余元素。",
        input_zh="第一行一个正整数 n。接下来 n 行，每行一个整数。",
        output_zh="第一行输出剩余元素个数 k。接下来 k 行按顺序输出剩余元素。",
        py=("# P1093 删除相邻重复元素（栈模拟消除）\n"
            "n = int(input())              # 个数 n\n"
            "stack = []                    # 用列表模拟栈\n"
            "for i in range(n):\n"
            "    x = int(input())\n"
            "    if stack and stack[-1] == x:  # 栈顶与当前相同\n"
            "        stack.pop()          # 消除一对\n"
            "    else:\n"
            "        stack.append(x)      # 不同则入栈\n"
            "print(len(stack))            # 剩余个数\n"
            "for x in stack:\n"
            "    print(x)\n"),
        cpp=("// P1093 删除相邻重复元素\n"
             "#include <iostream>\n"
             "#include <vector>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    int n;\n"
             "    cin >> n;\n"
             "    vector<int> st;          // 用 vector 模拟栈\n"
             "    for (int i = 0; i < n; ++i) {\n"
             "        int x;\n"
             "        cin >> x;\n"
             "        if (!st.empty() && st.back() == x) st.pop_back();\n"
             "        else st.push_back(x);\n"
             "    }\n"
             "    cout << st.size() << endl;\n"
             "    for (int x : st) cout << x << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1093 删除相邻重复元素\n"
              "import java.util.Scanner;\n"
              "import java.util.ArrayDeque;\n"
              "import java.util.Deque;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        int n = sc.nextInt();\n"
              "        Deque<Integer> st = new ArrayDeque<>();\n"
              "        for (int i = 0; i < n; ++i) {\n"
              "            int x = sc.nextInt();\n"
              "            if (!st.isEmpty() && st.peek() == x) st.pop();\n"
              "            else st.push(x);\n"
              "        }\n"
              "        // 输出（栈底到栈顶）\n"
              "        int[] arr = new int[st.size()];\n"
              "        int sz = st.size();\n"
              "        for (int i = sz - 1; i >= 0; --i) arr[i] = st.pop();\n"
              "        System.out.println(sz);\n"
              "        for (int x : arr) System.out.println(x);\n"
              "    }\n"
              "}\n"),
    )
