# -*- coding: utf-8 -*-
"""P1064 统计单词数"""
from generate import make_problem


def build():
    data = [
        "hello world", "a b c", "hello", "one two three four",
        "i love programming very much", "x y", "alpha beta gamma",
        "single", "red green blue yellow", "foo bar baz qux quux",
    ]
    cases = [(f"{line}\n", f"{len(line.split())}\n") for line in data]
    return make_problem(
        "P1064", "统计单词数", ["入门", "字符串"],
        cases=cases,
        desc_en="Given a line containing several words separated by single spaces, "
                "print the number of words.",
        input_en="One line containing words separated by single spaces (no leading "
                 "or trailing spaces), the total length not exceeding 1000 "
                 "characters.",
        output_en="One line: the number of words.",
        desc_zh="给定一行由若干单词组成的字符串（单词之间用一个空格分隔），输出单词的个数。",
        input_zh="一行字符串，包含若干用单个空格分隔的单词（无前导/后置空格），总长度不超过 "
                 "1000 个字符。",
        output_zh="一行，输出单词的个数。",
        py=("# P1064 统计单词数（split 按空格切分后计数）\n"
            "line = input()            # 一行若干单词（空格分隔）\n"
            "words = line.split()      # 切分成单词列表\n"
            "print(len(words))         # 单词个数\n"),
        cpp=("// P1064 统计单词数\n"
             "#include <iostream>\n"
             "#include <string>\n"
             "#include <sstream>\n"
             "using namespace std;\n"
             "int main() {\n"
             "    string line;\n"
             "    getline(cin, line);          // 读入整行\n"
             "    istringstream iss(line);\n"
             "    string word;\n"
             "    int cnt = 0;\n"
             "    while (iss >> word) ++cnt;   // 逐个读取单词计数\n"
             "    cout << cnt << endl;\n"
             "    return 0;\n"
             "}\n"),
        java=("// P1064 统计单词数\n"
              "import java.util.Scanner;\n"
              "public class Main {\n"
              "    public static void main(String[] args) {\n"
              "        Scanner sc = new Scanner(System.in);\n"
              "        String line = sc.nextLine();        // 读入整行\n"
              "        String[] words = line.split(\"\\\\s+\"); // 按空格切分\n"
              "        System.out.println(words.length);     // 单词个数\n"
              "    }\n"
              "}\n"),
    )
