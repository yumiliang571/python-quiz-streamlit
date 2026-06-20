import html
import random

import streamlit as st


st.set_page_config(
    page_title="Python期末复习闯关",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =====================================================================
# 题库：题目取材自本课程的实验报告、随堂作业与课后作业
# 每题字段：难度 level / 知识点 topic / 题干 question /
#           选项 options / 正确答案 answer / 解析 explain
# 注意：answer 必须与 options 中某一项完全一致。
# =====================================================================
QUESTION_BANK = [
    # ----------------------------- 简单 -----------------------------
    {
        "level": "简单",
        "topic": "变量与赋值",
        "question": "不使用临时变量，交换两个变量 a、b 的值，正确写法是？",
        "options": ["a = b; b = a", "a, b = b, a", "swap(a, b)", "a == b"],
        "answer": "a, b = b, a",
        "explain": "Python 用 a, b = b, a 一行同时赋值：右边先打包成元组再解包，无需临时变量。",
    },
    {
        "level": "简单",
        "topic": "运算符",
        "question": "表达式 17 // 5 的结果是？",
        "options": ["3", "3.4", "2", "3.0"],
        "answer": "3",
        "explain": "// 是整除，只保留商的整数部分；17 / 5 才是 3.4。",
    },
    {
        "level": "简单",
        "topic": "运算符",
        "question": "表达式 17 % 5 的结果是？",
        "options": ["2", "3", "3.4", "0"],
        "answer": "2",
        "explain": "% 取余数：17 = 5×3 + 2，余数是 2。判断奇偶、辗转相除都靠它。",
    },
    {
        "level": "简单",
        "topic": "字符串",
        "question": "s = 'Python'，s[1] 的结果是？",
        "options": ["'P'", "'y'", "'t'", "'n'"],
        "answer": "'y'",
        "explain": "下标从 0 开始：s[0] 是 'P'，s[1] 是 'y'。",
    },
    {
        "level": "简单",
        "topic": "字符串",
        "question": "s = 'abc'，切片 s[::-1] 的结果是？",
        "options": ["'abc'", "'cba'", "'acb'", "报错"],
        "answer": "'cba'",
        "explain": "切片 [::-1] 步长为 -1，表示整个字符串倒序，是反转字符串的常用写法。",
    },
    {
        "level": "简单",
        "topic": "数据类型",
        "question": "type('123') 表示的数据类型是？",
        "options": ["int", "float", "str", "bool"],
        "answer": "str",
        "explain": "被引号包住就是字符串 str，哪怕里面写的是数字。",
    },
    {
        "level": "简单",
        "topic": "列表",
        "question": "lst = [5, 6, 7]，len(lst) 的结果是？",
        "options": ["2", "3", "5", "18"],
        "answer": "3",
        "explain": "len() 返回元素个数，列表有 3 个元素。",
    },
    {
        "level": "简单",
        "topic": "列表",
        "question": "lst = [10, 20, 30]，lst[-1] 的结果是？",
        "options": ["10", "20", "30", "报错"],
        "answer": "30",
        "explain": "负下标从末尾数起，-1 是最后一个元素 30。",
    },
    {
        "level": "简单",
        "topic": "函数",
        "question": "Python 中定义函数使用哪个关键字？",
        "options": ["def", "func", "function", "define"],
        "answer": "def",
        "explain": "用 def 定义函数，return 用来返回结果。",
    },
    {
        "level": "简单",
        "topic": "输出",
        "question": "n = 5，print(f'{n * n}') 会输出什么？",
        "options": ["n * n", "25", "55", "10"],
        "answer": "25",
        "explain": "f-string 里 {} 中的表达式会被计算，n * n = 25。",
    },

    # ----------------------------- 普通 -----------------------------
    {
        "level": "普通",
        "topic": "流程控制",
        "question": "range(2, 8, 2) 依次产生哪些整数？",
        "options": ["2, 4, 6", "2, 4, 6, 8", "2, 3, 4, 5, 6, 7", "2, 8"],
        "answer": "2, 4, 6",
        "explain": "range(start, stop, step) 含 start 不含 stop，步长 2：2, 4, 6（8 取不到）。",
    },
    {
        "level": "普通",
        "topic": "输入处理",
        "question": "'3,5,7'.split(',') 的结果是？",
        "options": ["[3, 5, 7]", "['3', '5', '7']", "'3 5 7'", "(3, 5, 7)"],
        "answer": "['3', '5', '7']",
        "explain": "split 切成字符串列表，元素仍是字符串！要参与计算得先用 int() 或 float() 转换——输入处理最常见的坑。",
    },
    {
        "level": "普通",
        "topic": "列表推导式",
        "question": "[i * i for i in range(1, 4)] 的结果是？",
        "options": ["[1, 4, 9]", "[1, 2, 3]", "[1, 4, 9, 16]", "[0, 1, 4]"],
        "answer": "[1, 4, 9]",
        "explain": "列表生成式对 1, 2, 3 各求平方得 1, 4, 9；range(1, 4) 不含 4。",
    },
    {
        "level": "普通",
        "topic": "列表",
        "question": "lst = [1, 2, 3]; lst.append([4, 5]) 之后，lst 是？",
        "options": ["[1, 2, 3, 4, 5]", "[1, 2, 3, [4, 5]]", "[1, 2, 3, 4]", "报错"],
        "answer": "[1, 2, 3, [4, 5]]",
        "explain": "append 把参数当成一个元素整体加进去，所以末尾是一个子列表；要展开成 4、5 得用 extend 或 +。",
    },
    {
        "level": "普通",
        "topic": "字典",
        "question": "d = {'a': 1, 'b': 2}，下面哪个会触发 KeyError？",
        "options": ["d['a']", "d['c']", "d.get('c')", "len(d)"],
        "answer": "d['c']",
        "explain": "键 'c' 不存在，用中括号取值会 KeyError；而 d.get('c') 返回 None，不报错。",
    },
    {
        "level": "普通",
        "topic": "循环",
        "question": "for i, v in enumerate(['a', 'b', 'c']): 第一次循环时 i 和 v 分别是？",
        "options": ["1 和 'a'", "0 和 'a'", "0 和 'b'", "'a' 和 0"],
        "answer": "0 和 'a'",
        "explain": "enumerate 默认从 0 开始配下标，第一次 i = 0、v = 'a'。",
    },
    {
        "level": "普通",
        "topic": "函数式",
        "question": "list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) 的结果是？",
        "options": ["[1, 3]", "[2, 4]", "[1, 2, 3, 4]", "[True, False, True, False]"],
        "answer": "[2, 4]",
        "explain": "filter 只保留让 lambda 返回 True 的元素，这里是偶数 2 和 4。",
    },
    {
        "level": "普通",
        "topic": "集合",
        "question": "set([1, 2, 2, 3, 3, 3]) 的结果是？",
        "options": ["[1, 2, 3]", "{1, 2, 3}", "{1, 2, 2, 3, 3, 3}", "(1, 2, 3)"],
        "answer": "{1, 2, 3}",
        "explain": "集合 set 自动去重，用花括号表示；常用来判断元素是否已经出现过。",
    },
    {
        "level": "普通",
        "topic": "统计",
        "question": "lst = [3, 9, 2, 8]，sum(1 for v in lst if v > 5) 的结果是？",
        "options": ["2", "17", "4", "5"],
        "answer": "2",
        "explain": "对每个大于 5 的元素计 1 再求和，相当于统计个数：9 和 8 共 2 个。",
    },
    {
        "level": "普通",
        "topic": "文件与异常",
        "question": "用 open() 打开一个不存在的文件，应该捕获哪个异常？",
        "options": ["ValueError", "FileNotFoundError", "KeyError", "TypeError"],
        "answer": "FileNotFoundError",
        "explain": "文件不存在时抛 FileNotFoundError，用 try ... except FileNotFoundError 捕获并友好提示。",
    },

    # ----------------------------- 挑战 -----------------------------
    {
        "level": "挑战",
        "topic": "排序",
        "question": "选择排序每一轮的核心操作是？",
        "options": [
            "相邻两个元素比较并不断交换",
            "在未排序部分找到最小值，放到当前位置",
            "随机交换两个元素",
            "把整个列表反转一次",
        ],
        "answer": "在未排序部分找到最小值，放到当前位置",
        "explain": "选择排序每轮在内层找到最小值的下标，内层结束后只交换一次；相邻比较、内层反复交换的是冒泡排序。",
    },
    {
        "level": "挑战",
        "topic": "排序",
        "question": "选择排序中，交换元素的语句应该写在哪里？",
        "options": [
            "写在内层 if 里面",
            "写在内层 for 循环外面（外层 for 之内）",
            "写在所有循环外面",
            "选择排序不需要交换",
        ],
        "answer": "写在内层 for 循环外面（外层 for 之内）",
        "explain": "内层只更新最小值下标 min_idx，内层结束后才交换一次。写进 if 里就变成冒泡了——这是最常考的区别。",
    },
    {
        "level": "挑战",
        "topic": "二维列表",
        "question": "执行 m = [[0]*3]*2; m[0][0] = 1 之后，m 是？",
        "options": [
            "[[1, 0, 0], [0, 0, 0]]",
            "[[1, 0, 0], [1, 0, 0]]",
            "[[1, 1, 1], [0, 0, 0]]",
            "报错",
        ],
        "answer": "[[1, 0, 0], [1, 0, 0]]",
        "explain": "[[0]*3]*2 让两行指向同一个列表，改一行另一行也跟着变！正确写法是 [[0]*3 for _ in range(2)]。",
    },
    {
        "level": "挑战",
        "topic": "二维列表",
        "question": "一个 2 行 4 列的矩阵，转置后变成几行几列？",
        "options": ["2 行 4 列", "4 行 2 列", "4 行 4 列", "2 行 2 列"],
        "answer": "4 行 2 列",
        "explain": "转置把行列互换：原 m[i][j] 变成新 result[j][i]，所以 2×4 变 4×2。",
    },
    {
        "level": "挑战",
        "topic": "二维列表",
        "question": "n×n 矩阵 matrix 的主对角线元素下标是？",
        "options": ["matrix[i][i]", "matrix[i][n-1-i]", "matrix[0][i]", "matrix[i][0]"],
        "answer": "matrix[i][i]",
        "explain": "主对角线行号等于列号，即 matrix[i][i]；副对角线才是 matrix[i][n-1-i]。",
    },
    {
        "level": "挑战",
        "topic": "二维列表",
        "question": "n×n 矩阵的副对角线（右上到左下）元素下标是？",
        "options": ["matrix[i][i]", "matrix[i][n-1-i]", "matrix[n-i][i]", "matrix[i][n+i]"],
        "answer": "matrix[i][n-1-i]",
        "explain": "副对角线满足 行号 + 列号 = n-1，所以列下标是 n-1-i。",
    },
    {
        "level": "挑战",
        "topic": "数论算法",
        "question": "辗转相除法 while b: a, b = b, a % b; return a，求 gcd(12, 18) 的结果是？",
        "options": ["2", "3", "6", "36"],
        "answer": "6",
        "explain": "(12,18)→(18,12)→(12,6)→(6,0)，b 为 0 时返回 a = 6。12 与 18 的最大公约数是 6。",
    },
    {
        "level": "挑战",
        "topic": "数论算法",
        "question": "已知 gcd(a, b)，求最小公倍数 lcm 的正确写法是？",
        "options": [
            "a * b / gcd(a, b)",
            "a * b // gcd(a, b)",
            "a + b - gcd(a, b)",
            "gcd(a, b) // (a * b)",
        ],
        "answer": "a * b // gcd(a, b)",
        "explain": "lcm = a*b/gcd，要用整除 // 得到整数；用 / 会得到带小数的 float。",
    },
    {
        "level": "挑战",
        "topic": "参数传递",
        "question": "def f(lst): lst.append(0)。执行 a = [1, 2]; f(a) 之后，a 是？",
        "options": ["[1, 2]", "[1, 2, 0]", "[0, 1, 2]", "None"],
        "answer": "[1, 2, 0]",
        "explain": "列表是可变对象，函数内对它 append 会直接改到原列表；而整数等不可变对象不会被函数改变。",
    },
    {
        "level": "挑战",
        "topic": "参数传递",
        "question": "def f(x): x += 1; return x。执行 a = 5; b = f(a) 之后，a 和 b 分别是？",
        "options": ["5 和 6", "6 和 6", "5 和 5", "6 和 5"],
        "answer": "5 和 6",
        "explain": "整数不可变，函数内 x += 1 只改局部副本并返回 6，原 a 仍是 5。可与上一题的列表对照记忆。",
    },
    {
        "level": "挑战",
        "topic": "递归",
        "question": "递归判断素数 def is_prime(num, i=2): 中，返回 True 的终止条件通常是？",
        "options": ["num == 0", "i * i > num", "i > num", "num % i == 0"],
        "answer": "i * i > num",
        "explain": "当 i 的平方已超过 num，说明没找到能整除的因子，num 是素数，返回 True；只需查到 √num 即可。",
    },
    {
        "level": "挑战",
        "topic": "去重算法",
        "question": "要给列表去重并保留原始顺序，用哪种结构记录“已出现过”最高效？",
        "options": [
            "再开一个 list，每次用 in 查找",
            "用 set 记录已出现的元素",
            "把所有元素拼成字符串",
            "用 sort 排序后再比较",
        ],
        "answer": "用 set 记录已出现的元素",
        "explain": "set 的成员判断 in 接近 O(1)，比在 list 里查找快；遍历时没见过就加入结果并记进 set，既去重又保序。",
    },

    # ------------------- 选择填空（代码补全）-------------------
    # 给出一段带 ____ 空白的代码，选正确选项补全；题目源自实验与作业。
    {
        "level": "普通",
        "topic": "代码填空·输入处理",
        "question": "键盘输入用逗号分隔的数字，求它们的和。____ 处应填什么？",
        "code": '''s = input("输入数字，用逗号分隔：")   # 例如 "3,5,7"
nums = [____ for v in s.split(",")]
print(sum(nums))                      # 期望输出 15''',
        "options": ["float(v)", "v", "str(v)", "v.split()"],
        "answer": "float(v)",
        "explain": "split 得到的是字符串列表，必须先转成数字（float 或 int）才能求和；直接对字符串求和会报错。",
    },
    {
        "level": "普通",
        "topic": "代码填空·文件异常",
        "question": "打开文件读取内容，文件不存在时给出提示。except 后的 ____ 应填什么？",
        "code": '''try:
    with open("data.txt", "r", encoding="utf-8") as f:
        print(f.read())
except ____:
    print("文件不存在！")''',
        "options": ["FileNotFoundError", "ValueError", "KeyError", "IndexError"],
        "answer": "FileNotFoundError",
        "explain": "文件不存在时抛出的是 FileNotFoundError，捕获它即可给出友好提示。",
    },
    {
        "level": "普通",
        "topic": "代码填空·循环累加",
        "question": "用循环累加 1 到 100 的和。range 的 ____ 应填什么？",
        "code": '''s = 0
for i in range(____):
    s += i
print(s)        # 期望输出 5050''',
        "options": ["1, 101", "1, 100", "0, 100", "1, 99"],
        "answer": "1, 101",
        "explain": "range 右端点取不到，要累加到 100 必须写 range(1, 101)。",
    },
    {
        "level": "普通",
        "topic": "代码填空·去重保序",
        "question": "去除列表重复元素并保留原始顺序。if 后的 ____ 应填什么？",
        "code": '''def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if ____:
            seen.add(item)
            result.append(item)
    return result''',
        "options": ["item not in seen", "item in seen", "item not in result", "item == seen"],
        "answer": "item not in seen",
        "explain": "只有没见过的元素才加入结果；用 set 的 not in 判断高效，既去重又保留顺序。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·选择排序",
        "question": "选择排序（升序）。内层找最小值的判断 ____ 应填什么？",
        "code": '''def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if ____:          # 找更小的
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr''',
        "options": ["arr[j] < arr[min_idx]", "arr[j] > arr[min_idx]", "arr[j] < arr[i]", "j < min_idx"],
        "answer": "arr[j] < arr[min_idx]",
        "explain": "要在未排序区找最小值，需比较 arr[j] 与当前最小 arr[min_idx]；写成 > 会变降序，比较 arr[i] 是常见错误。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·辗转相除",
        "question": "辗转相除法求最大公约数。循环体内 ____ 应填什么？",
        "code": '''def gcd(a, b):
    while b != 0:
        a, b = ____
    return a''',
        "options": ["b, a % b", "a % b, b", "b, a // b", "a, b % a"],
        "answer": "b, a % b",
        "explain": "新的 a 取旧 b，新的 b 取 a 除以 b 的余数，直到 b 为 0，此时 a 即最大公约数。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·矩阵转置",
        "question": "矩阵转置，把原矩阵行列互换。____ 处应填什么？",
        "code": '''def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            ____ = matrix[i][j]
    return result''',
        "options": ["result[j][i]", "result[i][j]", "result[i][i]", "matrix[j][i]"],
        "answer": "result[j][i]",
        "explain": "转置就是行列下标互换：原 matrix[i][j] 放到新 result[j][i]。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·二维列表初始化",
        "question": "创建 3 行 4 列、初值全 0 且各行互相独立的二维列表。____ 应填什么？",
        "code": '''rows, cols = 3, 4
matrix = ____
matrix[0][0] = 1
print(matrix)   # 期望只改到第 0 行''',
        "options": ["[[0]*cols for _ in range(rows)]", "[[0]*cols]*rows", "[0]*cols*rows", "[[0]*rows]*cols"],
        "answer": "[[0]*cols for _ in range(rows)]",
        "explain": "[[0]*cols]*rows 会让各行共享同一引用，改一行全变；必须用列表推导式生成相互独立的行。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·递归素数",
        "question": "递归判断 num 是否为素数。返回 True 的终止条件 ____ 应填什么？",
        "code": '''def is_prime(num, i=2):
    if num < 2:
        return False
    if ____:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i + 1)''',
        "options": ["i * i > num", "i > num", "num % i == 0", "i == num"],
        "answer": "i * i > num",
        "explain": "试除到 √num 即可；当 i*i > num 仍没找到因子，说明 num 是素数，返回 True。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·主对角线",
        "question": "求 n×n 矩阵主对角线元素之和。____ 应填什么？",
        "code": '''def diag_sum(matrix):
    n = len(matrix)
    s = 0
    for i in range(n):
        s += ____
    return s''',
        "options": ["matrix[i][i]", "matrix[i][n-1-i]", "matrix[0][i]", "matrix[i][0]"],
        "answer": "matrix[i][i]",
        "explain": "主对角线行号等于列号，累加 matrix[i][i]；若要副对角线则是 matrix[i][n-1-i]。",
    },
    {
        "level": "挑战",
        "topic": "代码填空·lambda 过滤",
        "question": "用 lambda + filter 删除列表里所有的 'A'。____ 应填什么？",
        "code": '''lst = list("ABCAAD")
result = list(filter(____, lst))
print("".join(result))   # 期望输出 BCD''',
        "options": ["lambda x: x != 'A'", "lambda x: x == 'A'", "lambda x: 'A'", "x != 'A'"],
        "answer": "lambda x: x != 'A'",
        "explain": "filter 保留让函数返回 True 的元素；要删掉 'A'，就保留 x != 'A' 的元素。",
    },

    # ============== 组员5 制作（新增挑战题：概念题 + 代码阅读题）==============
    {
        "level": "挑战",
        "topic": "排序",
        "author": "组员5",
        "question": "冒泡排序按升序排列时，第一轮完整比较结束后，哪个元素通常会被放到列表末尾？",
        "options": ["当前最大值", "当前最小值", "第一个元素", "随机元素"],
        "answer": "当前最大值",
        "explain": "升序冒泡排序每轮不断交换相邻逆序元素，第一轮会把当前最大值一路“冒泡”到末尾。",
    },
    {
        "level": "挑战",
        "topic": "递归",
        "author": "组员5",
        "question": "递归函数最容易出错的地方是什么？",
        "options": ["没有终止条件或没有向终止条件靠近", "函数名太短", "用了 return", "参数数量超过 1 个"],
        "answer": "没有终止条件或没有向终止条件靠近",
        "explain": "递归必须有明确终止条件，并且每次递归调用都要让问题规模变小，否则可能无限递归直到 RecursionError。",
    },
    {
        "level": "挑战",
        "topic": "二维列表",
        "author": "组员5",
        "question": "复制二维列表时，matrix[:] 的特点是？",
        "options": ["只复制外层列表，内层列表仍共享", "能完整深拷贝所有层", "会把二维列表转成一维列表", "一定会报错"],
        "answer": "只复制外层列表，内层列表仍共享",
        "explain": "matrix[:] 是浅拷贝，只新建外层列表；里面每一行仍然指向原来的列表，修改某一行内容会互相影响。",
    },
    {
        "level": "挑战",
        "topic": "字典排序",
        "author": "组员5",
        "question": "sorted(d.items(), key=lambda item: item[1]) 的排序依据是？",
        "options": ["按字典的值排序", "按字典的键排序", "按键值对数量排序", "按插入顺序反转"],
        "answer": "按字典的值排序",
        "explain": "d.items() 产生 (键, 值) 形式的元组，item[1] 取的是值，所以会按字典的值排序。",
    },
    {
        "level": "挑战",
        "topic": "文件与异常",
        "author": "组员5",
        "question": "try...except...else...finally 中，finally 代码块什么时候执行？",
        "options": ["无论是否发生异常都会执行", "只有发生异常才执行", "只有没有异常才执行", "只有 return 后才执行"],
        "answer": "无论是否发生异常都会执行",
        "explain": "finally 常用于关闭文件、释放资源等收尾操作，不管 try 中是否出错，通常都会执行。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·默认参数",
        "author": "组员5",
        "question": "阅读代码，程序两次 print 的输出分别是什么？",
        "code": '''def collect(x, box=[]):
    box.append(x)
    return box

print(collect(1))
print(collect(2))''',
        "options": ["[1] 和 [2]", "[1] 和 [1, 2]", "[1, 2] 和 [1, 2]", "报错"],
        "answer": "[1] 和 [1, 2]",
        "explain": "默认参数中的列表只会在函数定义时创建一次，两次调用共用同一个 box，所以第二次输出 [1, 2]。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·浅拷贝",
        "author": "组员5",
        "question": "阅读代码，print(a) 的输出是什么？",
        "code": '''a = [[1], [2]]
b = a[:]
b[0].append(9)
print(a)''',
        "options": ["[[1], [2]]", "[[1, 9], [2]]", "[[1], [2, 9]]", "[[9], [2]]"],
        "answer": "[[1, 9], [2]]",
        "explain": "a[:] 只复制外层列表，b[0] 和 a[0] 指向同一个内层列表；append(9) 会影响 a[0]。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·异常流程",
        "author": "组员5",
        "question": "阅读代码，输出顺序是什么？",
        "code": '''try:
    x = int("8")
except ValueError:
    print("E")
else:
    print("OK")
finally:
    print("END")''',
        "options": ["E → END", "OK → END", "只输出 OK", "只输出 END"],
        "answer": "OK → END",
        "explain": "int('8') 不会触发 ValueError，所以执行 else 输出 OK；finally 无论如何都会执行，继续输出 END。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·字典排序",
        "author": "组员5",
        "question": "阅读代码，print(result[0]) 的输出是什么？",
        "code": '''scores = {"Li": 88, "Wang": 95, "Zhao": 90}
result = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(result[0])''',
        "options": ["('Li', 88)", "('Wang', 95)", "('Zhao', 90)", "('Wang', 88)"],
        "answer": "('Wang', 95)",
        "explain": "lambda item: item[1] 表示按分数排序，reverse=True 表示降序，最高分是 Wang 的 95。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·二维列表",
        "author": "组员5",
        "question": "阅读代码，print(list(zip(*matrix))) 的输出是什么？",
        "code": '''matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))''',
        "options": ["[(1, 4), (2, 5), (3, 6)]", "[[1, 4], [2, 5], [3, 6]]", "[(1, 2, 3), (4, 5, 6)]", "[1, 4, 2, 5, 3, 6]"],
        "answer": "[(1, 4), (2, 5), (3, 6)]",
        "explain": "*matrix 会把两行拆开传给 zip，zip 按列配对，所以得到三组元组：(1,4)、(2,5)、(3,6)。",
    },
    {
        "level": "挑战",
        "topic": "代码阅读·递归",
        "author": "组员5",
        "question": "阅读代码，程序输出什么？",
        "code": '''def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(305))''',
        "options": ["8", "35", "305", "递归错误"],
        "answer": "8",
        "explain": "digit_sum 每次取个位并递归处理剩余数字：305 的各位数字和是 3 + 0 + 5 = 8。",
    },

    # ============== docx「简单题目模式」并入（简单模式）==============
    {
        "level": "简单", "topic": "变量命名",
        "question": "以下哪个是合法的变量名？",
        "options": ["1num", "num-1", "num_1", "num@1"],
        "answer": "num_1",
        "explain": "变量名只能由字母、数字、下划线组成，不能以数字开头，也不能含特殊符号。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "print(2 ** 3) 的输出是？",
        "options": ["5", "6", "8", "9"],
        "answer": "8",
        "explain": "** 是乘方（幂运算），2 的 3 次方 = 8。",
    },
    {
        "level": "简单", "topic": "注释",
        "question": "Python 单行注释使用哪个符号？",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#",
        "explain": "Python 用 # 作单行注释；// 是其他语言的写法。",
    },
    {
        "level": "简单", "topic": "列表",
        "question": "list1 = [1, 2, 3]，list1[0] 的值是？",
        "options": ["1", "2", "3", "报错"],
        "answer": "1",
        "explain": "列表下标从 0 开始，list1[0] 是第一个元素 1。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "下列哪个不是条件判断关键字？",
        "options": ["if", "elif", "else", "then"],
        "answer": "then",
        "explain": "Python 用 if / elif / else，没有 then。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "在循环中，跳出整个循环用哪个关键字？",
        "options": ["continue", "break", "pass", "return"],
        "answer": "break",
        "explain": "break 跳出整个循环；continue 只跳过本次、进入下一次。",
    },
    {
        "level": "简单", "topic": "类型转换",
        "question": "把字符串 '123' 转成整数，用哪个函数？",
        "options": ["str()", "int()", "float()", "bool()"],
        "answer": "int()",
        "explain": "int() 把内容转成整数；str() 转字符串、float() 转小数。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": "dict1 = {'name': 'Tom', 'age': 18}，取出年龄的写法是？",
        "options": ["dict1[0]", "dict1['age']", "dict1.age", "dict1(age)"],
        "answer": "dict1['age']",
        "explain": "字典通过键取值，用中括号写键名：dict1['age']。",
    },
    {
        "level": "简单", "topic": "数据类型",
        "question": "布尔值 True 对应的数字是？",
        "options": ["0", "1", "-1", "任意非 0 数"],
        "answer": "1",
        "explain": "True 等价于 1，False 等价于 0，可以参与运算。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "a = 10; b = 3，a % b 的结果是？",
        "options": ["1", "3", "0", "3.33"],
        "answer": "1",
        "explain": "% 取余数：10 除以 3 商 3 余 1。",
    },
    {
        "level": "简单", "topic": "字符串",
        "question": "字符串拼接使用哪个符号？",
        "options": ["+", "-", "*", "/"],
        "answer": "+",
        "explain": "+ 把两个字符串连接起来，如 'ab' + 'cd' = 'abcd'。",
    },
    {
        "level": "简单", "topic": "列表",
        "question": "定义一个空列表，正确的写法是？",
        "options": ["lst = []", "lst = {}", "lst = ()", "lst = 0"],
        "answer": "lst = []",
        "explain": "[] 是空列表；{} 是空字典，() 是空元组。",
    },
    {
        "level": "简单", "topic": "循环",
        "question": "for 循环常搭配哪个函数生成连续数字序列？",
        "options": ["range", "len", "input", "type"],
        "answer": "range",
        "explain": "range 生成连续整数序列，如 range(5) 是 0,1,2,3,4。",
    },

    # ====== 期末复习重点 PDF 出题（覆盖单选/判断/填空考点）======
    {
        "level": "普通", "topic": "随机模块",
        "question": "random.random() 生成的随机数范围是？",
        "options": ["[0, 1)", "[0, 1]", "(0, 1)", "[1, 10]"],
        "answer": "[0, 1)",
        "explain": "random.random() 返回 0（含）到 1（不含）之间的浮点数。",
    },
    {
        "level": "挑战", "topic": "随机模块",
        "question": "random.sample(pop, k) 的作用是？",
        "options": ["从序列中随机取 k 个不重复元素组成列表", "返回一个 0~1 的随机小数", "原地打乱序列", "返回最大的 k 个元素"],
        "answer": "从序列中随机取 k 个不重复元素组成列表",
        "explain": "sample 从序列里随机抽 k 个不重复元素，不改变原序列，常用于抽奖。",
    },
    {
        "level": "普通", "topic": "集合",
        "question": "创建一个空集合，正确的是？",
        "options": ["s = set()", "s = {}", "s = []", "s = ()"],
        "answer": "s = set()",
        "explain": "{} 创建的是空字典；空集合只能用 set()。",
    },
    {
        "level": "挑战", "topic": "集合运算",
        "question": "求两个集合的并集，用哪个运算符？",
        "options": ["|", "&", "-", "^"],
        "answer": "|",
        "explain": "并集 |（union）、交集 &（intersection）、差集 -、对称差 ^。",
    },
    {
        "level": "挑战", "topic": "集合运算",
        "question": "集合运算中，& 表示？",
        "options": ["交集", "并集", "差集", "对称差"],
        "answer": "交集",
        "explain": "& 是交集（两个集合都有的元素），对应方法 intersection()。",
    },
    {
        "level": "挑战", "topic": "del与clear",
        "question": "清空列表全部元素但保留列表对象本身，用？",
        "options": ["lst.clear()", "del lst", "lst.remove()", "lst.pop(all)"],
        "answer": "lst.clear()",
        "explain": "clear() 清空所有元素、容器还在；del lst 把整个变量都删掉。",
    },
    {
        "level": "普通", "topic": "文件操作",
        "question": "open 的模式 'a' 表示？",
        "options": ["追加写入（append）", "只读", "二进制", "新建并覆盖"],
        "answer": "追加写入（append）",
        "explain": "a = append 追加，从文件末尾写；r=read, w=write, b=binary。",
    },
    {
        "level": "普通", "topic": "文件操作",
        "question": "open 的模式 'w' 的特点是？",
        "options": ["覆盖写入（文件已存在则先清空）", "只读不能写", "追加到末尾", "文件不存在会报错"],
        "answer": "覆盖写入（文件已存在则先清空）",
        "explain": "w 模式打开会清空原内容再写；要保留旧内容追加得用 a。",
    },
    {
        "level": "挑战", "topic": "可变参数",
        "question": "函数形参 *args 会把多个位置参数收集成？",
        "options": ["元组", "列表", "字典", "字符串"],
        "answer": "元组",
        "explain": "* 前缀收集任意个位置参数，存为元组；** 收集关键字参数存为字典。",
    },
    {
        "level": "挑战", "topic": "可变参数",
        "question": "函数形参 **kwargs 会把关键字参数收集成？",
        "options": ["字典", "元组", "列表", "集合"],
        "answer": "字典",
        "explain": "** 前缀把 key=value 形式的关键字参数收集成字典。",
    },
    {
        "level": "普通", "topic": "可变性",
        "question": "下列哪个是不可变（immutable）数据类型？",
        "options": ["元组", "列表", "字典", "集合"],
        "answer": "元组",
        "explain": "不可变：数值、字符串、元组；可变：列表、字典、集合。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": "字典的键（key）必须满足什么？",
        "options": ["不可变且唯一", "可以重复", "必须是字符串", "必须是数字"],
        "answer": "不可变且唯一",
        "explain": "键必须是不可变类型（字符串、数字、元组）且唯一，值可以是任意类型。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst.pop() 不带参数时的行为是？",
        "options": ["移除并返回最后一个元素", "移除第一个元素", "清空列表", "返回列表长度"],
        "answer": "移除并返回最后一个元素",
        "explain": "pop() 默认移除并返回最后一个元素；pop(i) 移除指定位置。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst.insert(0, 5) 的作用是？",
        "options": ["在索引 0 处插入 5", "在末尾添加 5", "删除索引 0 的元素", "把第 0 个改成 5"],
        "answer": "在索引 0 处插入 5",
        "explain": "insert(位置, 元素) 在指定索引处插入，后面的元素依次后移。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'-'.join(['a', 'b', 'c']) 的结果是？",
        "options": ["'a-b-c'", "['a', 'b', 'c']", "'abc'", "'a,b,c'"],
        "answer": "'a-b-c'",
        "explain": "join 用分隔符把可迭代对象的元素连成一个字符串。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'  hi  '.strip() 的结果是？",
        "options": ["'hi'", "'  hi'", "'hi  '", "'  hi  '"],
        "answer": "'hi'",
        "explain": "strip() 去掉字符串首尾的空白字符。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'123'.isdigit() 的结果是？",
        "options": ["True", "False", "123", "报错"],
        "answer": "True",
        "explain": "isdigit() 判断字符串是否全是数字，全数字返回 True。",
    },
    {
        "level": "普通", "topic": "字符串格式化",
        "question": "'{} 和 {}'.format('A', 'B') 的结果是？",
        "options": ["'A 和 B'", "'{} 和 {}'", "'AB'", "报错"],
        "answer": "'A 和 B'",
        "explain": "format 按顺序把 {} 替换成参数。",
    },
    {
        "level": "挑战", "topic": "模块导入",
        "question": "from math import sqrt 的作用是？",
        "options": ["只引入 math 模块里的 sqrt 函数", "引入整个 math 模块", "定义一个 sqrt 函数", "删除 sqrt"],
        "answer": "只引入 math 模块里的 sqrt 函数",
        "explain": "from 模块 import 名字 只引入指定成员，可直接写 sqrt()；import math 则要写 math.sqrt()。",
    },
    {
        "level": "挑战", "topic": "函数返回",
        "question": "函数里写 return a, b，实际返回的是？",
        "options": ["一个元组 (a, b)", "两个独立的值", "一个列表 [a, b]", "报错"],
        "answer": "一个元组 (a, b)",
        "explain": "返回多个值时 Python 会打包成一个元组返回（本质仍是一个返回值）。",
    },
    {
        "level": "普通", "topic": "字符串运算符",
        "question": "'ab' * 3 的结果是？",
        "options": ["'ababab'", "'ab3'", "'aaabbb'", "报错"],
        "answer": "'ababab'",
        "explain": "字符串 * 整数 表示复制重复，'ab' 重复 3 次。",
    },
    {
        "level": "普通", "topic": "字符串运算符",
        "question": "'H' in 'Hello' 的结果是？",
        "options": ["True", "False", "0", "'H'"],
        "answer": "True",
        "explain": "in 判断子串是否存在，'H' 在 'Hello' 中，返回 True。",
    },
    {
        "level": "普通", "topic": "列表与元组",
        "question": "列表和元组最本质的区别是？",
        "options": ["列表可变、元组不可变", "列表用圆括号、元组用方括号", "元组能存数字、列表不能", "没有区别"],
        "answer": "列表可变、元组不可变",
        "explain": "本质区别是可变性：列表 [] 可增删改，元组 () 一旦创建不能改。",
    },
    {
        "level": "挑战", "topic": "排序",
        "question": "sorted(lst) 和 lst.sort() 的区别是？",
        "options": ["sorted 返回新列表不改原；sort 原地排序无返回", "完全一样", "sorted 原地改；sort 返回新列表", "两个都会报错"],
        "answer": "sorted 返回新列表不改原；sort 原地排序无返回",
        "explain": "sorted() 返回排好序的新列表、原列表不变；list.sort() 直接在原列表上排序，返回 None。",
    },

    # ====== 期末复习重点 PDF 出题（补充：例题 + 剩余考点）======
    {
        "level": "挑战", "topic": "代码阅读·lambda",
        "question": "阅读代码，print 输出什么？",
        "code": '''students = [{"name": "A", "age": 20, "grade": 85},
            {"name": "B", "age": 18, "grade": 92}]
best = max(students, key=lambda s: s["grade"])
print(best["name"])''',
        "options": ["B", "A", "92", "85"],
        "answer": "B",
        "explain": "max 用 key=lambda 取每人的 grade 作比较，最高分 92 是 B，所以输出 B 的名字。",
    },
    {
        "level": "挑战", "topic": "代码阅读·列表推导式",
        "question": "阅读代码，print(even) 输出什么？",
        "code": '''nums = [1, 2, 3]
squared = [x ** 2 for x in nums]
even = [x for x in squared if x % 2 == 0]
print(even)''',
        "options": ["[4]", "[1, 4, 9]", "[2]", "[4, 9]"],
        "answer": "[4]",
        "explain": "squared = [1, 4, 9]；再筛选偶数只剩 4，所以 even = [4]。",
    },
    {
        "level": "挑战", "topic": "代码阅读·列表方法",
        "question": "阅读代码，print(nums) 输出什么？",
        "code": '''nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
nums.remove(2)
print(nums)''',
        "options": ["[0, 1, 3, 4]", "[0, 1, 2, 3, 4]", "[1, 3, 4]", "[0, 1, 2, 4]"],
        "answer": "[0, 1, 3, 4]",
        "explain": "append(4)→[1,2,3,4]；insert(0,0)→[0,1,2,3,4]；remove(2) 删第一个 2→[0,1,3,4]。",
    },
    {
        "level": "挑战", "topic": "代码填空·递归",
        "question": "补全 Fibonacci 递归函数，____ 处应填什么？",
        "code": '''def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return ____

print(fib(6))''',
        "options": ["fib(n-1) + fib(n-2)", "fib(n-1) * fib(n-2)", "n-1 + n-2", "fib(n) + fib(n-1)"],
        "answer": "fib(n-1) + fib(n-2)",
        "explain": "Fibonacci 第 n 项 = 前两项之和，递归调用 fib(n-1) + fib(n-2)。",
    },
    {
        "level": "简单", "topic": "Python基础",
        "question": "Python 源程序文件的后缀名是？",
        "options": [".py", ".python", ".pt", ".pic"],
        "answer": ".py",
        "explain": "Python 源程序文件以 .py 为后缀。",
    },
    {
        "level": "简单", "topic": "类型转换",
        "question": "list('abc') 的结果是？",
        "options": ["['a', 'b', 'c']", "'abc'", "['abc']", "报错"],
        "answer": "['a', 'b', 'c']",
        "explain": "list() 把可迭代对象拆成元素列表，字符串会拆成单个字符。",
    },
    {
        "level": "普通", "topic": "切片",
        "question": "lst = [0, 1, 2, 3, 4]，lst[1:4] 的结果是？",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[0, 1, 2, 3]", "[2, 3, 4]"],
        "answer": "[1, 2, 3]",
        "explain": "切片 [1:4] 含起点 1 不含终点 4，取索引 1、2、3。",
    },
    {
        "level": "普通", "topic": "切片",
        "question": "lst = [0, 1, 2, 3, 4, 5]，lst[::2] 的结果是？",
        "options": ["[0, 2, 4]", "[1, 3, 5]", "[0, 1, 2]", "[5, 3, 1]"],
        "answer": "[0, 2, 4]",
        "explain": "[::2] 步长为 2，从头每隔一个取，得到索引 0、2、4。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst = [1, 2]; lst.extend([3, 4]) 后，lst 是？",
        "options": ["[1, 2, 3, 4]", "[1, 2, [3, 4]]", "[3, 4, 1, 2]", "[1, 2]"],
        "answer": "[1, 2, 3, 4]",
        "explain": "extend 把另一个列表的元素逐个加到末尾；append([3,4]) 才会变嵌套。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'aXbXc'.replace('X', '-') 的结果是？",
        "options": ["'a-b-c'", "'aXbXc'", "'abc'", "'a-bXc'"],
        "answer": "'a-b-c'",
        "explain": "replace 把所有匹配的子串都替换掉。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'abcabc'.count('a') 的结果是？",
        "options": ["2", "1", "3", "0"],
        "answer": "2",
        "explain": "count 统计子串出现次数，'a' 出现 2 次。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'hello'.find('l') 的结果是？",
        "options": ["2", "3", "-1", "1"],
        "answer": "2",
        "explain": "find 返回子串第一次出现的下标，第一个 'l' 在索引 2；找不到返回 -1。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'hello world'.title() 的结果是？",
        "options": ["'Hello World'", "'HELLO WORLD'", "'Hello world'", "'hello world'"],
        "answer": "'Hello World'",
        "explain": "title() 把每个单词的首字母都变大写。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'python'.startswith('py') 的结果是？",
        "options": ["True", "False", "'py'", "报错"],
        "answer": "True",
        "explain": "startswith 判断字符串是否以指定前缀开头，返回布尔值。",
    },
    {
        "level": "普通", "topic": "循环else",
        "question": "for 循环正常结束（没有被 break 中断）时，会执行 else 子句吗？",
        "options": ["会执行", "不会执行", "报错", "随机决定"],
        "answer": "会执行",
        "explain": "循环正常跑完会执行 else；若中途 break 退出，则不执行 else。",
    },
    {
        "level": "普通", "topic": "模块导入",
        "question": "import math 之后，调用平方根函数要写成？",
        "options": ["math.sqrt(x)", "sqrt(x)", "math(sqrt(x))", "import sqrt"],
        "answer": "math.sqrt(x)",
        "explain": "import math 要用 模块名.函数名；想直接写 sqrt() 得用 from math import sqrt。",
    },
    {
        "level": "普通", "topic": "类型转换",
        "question": "tuple([1, 2, 3]) 的结果是？",
        "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "报错"],
        "answer": "(1, 2, 3)",
        "explain": "tuple() 把可迭代对象转成元组。",
    },
    {
        "level": "挑战", "topic": "type与id",
        "question": "id() 函数返回的是？",
        "options": ["对象的唯一标识（内存地址）", "对象的类型", "对象的长度", "对象的值"],
        "answer": "对象的唯一标识（内存地址）",
        "explain": "id() 返回对象唯一标识（通常是内存地址），可判断两个变量是否指向同一对象；type() 才是看类型。",
    },
    {
        "level": "挑战", "topic": "文件模式",
        "question": "文件模式 'r+' 与 'w+' 的区别是？",
        "options": ["r+ 不清空原内容，w+ 会先清空", "完全一样", "r+ 只能读", "w+ 只能读"],
        "answer": "r+ 不清空原内容，w+ 会先清空",
        "explain": "两者都能读写；但 r+ 保留原内容，w+ 打开就清空原文件。",
    },

    # ===================================================================
    # 【扩充新增】取材自「扩充完整版」「普通模式题库」「Python入门60道」docx
    # 已逐题用 Python 校验答案；个别原题选项/答案有误处已按正确结果修正。
    # ===================================================================

    # ------------------------- 新增·简单 -------------------------
    {
        "level": "简单", "topic": "输出",
        "question": "Python 中把内容输出到控制台用哪个函数？",
        "options": ["print()", "input()", "output()", "show()"],
        "answer": "print()",
        "explain": "print() 负责输出显示；input() 是读取键盘输入。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "判断整数 num 是否为偶数，正确的条件是？",
        "options": ["num % 2 == 0", "num / 2 == 0", "num // 2 == 0", "num % 2 == 1"],
        "answer": "num % 2 == 0",
        "explain": "偶数除以 2 余 0，用 num % 2 == 0；== 1 判断的是奇数。",
    },
    {
        "level": "简单", "topic": "内置函数",
        "question": "len('study') 的返回值是？",
        "options": ["4", "5", "6", "0"],
        "answer": "5",
        "explain": "len() 返回字符个数，'study' 共 5 个字母。",
    },
    {
        "level": "简单", "topic": "输入处理",
        "question": "读入一个整数并能直接参与数学运算，正确写法是？",
        "options": ["int(input())", "input()", "float()", "str(input())"],
        "answer": "int(input())",
        "explain": "input() 读到的永远是字符串，要做整数运算得用 int(input()) 转换。",
    },
    {
        "level": "简单", "topic": "数据类型",
        "question": "下列属于浮点数（float）类型的是？",
        "options": ["2.56", "99", "-10", "False"],
        "answer": "2.56",
        "explain": "带小数点的是 float；99、-10 是 int，False 是 bool。",
    },
    {
        "level": "简单", "topic": "数据类型",
        "question": "下列哪一个是整型 int？",
        "options": ["88", "3.14", "'66'", "True"],
        "answer": "88",
        "explain": "88 是整数 int；3.14 是 float，'66' 是 str，True 是 bool。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "print(3 + 4 * 2) 的结果是？",
        "options": ["11", "14", "7", "9"],
        "answer": "11",
        "explain": "先乘除后加减：4*2=8，再 3+8=11。",
    },
    {
        "level": "简单", "topic": "字符串运算符",
        "question": "print('5' + '3') 的输出是？",
        "options": ["53", "8", "报错", "5 3"],
        "answer": "53",
        "explain": "引号里是字符串，+ 做拼接得到 '53'，不是数字相加。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "表示“大于等于”的运算符是？",
        "options": [">=", ">", "<", "=>"],
        "answer": ">=",
        "explain": ">= 表示大于等于；单个 = 是赋值，=> 在 Python 里不合法。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "a = 5，想让 a 增加 3，下列哪种写法是错误的（a 其实没变）？",
        "options": ["a + 3", "a += 3", "a = a + 3", "a = 3 + a"],
        "answer": "a + 3",
        "explain": "a + 3 只算出 8 却没赋回去，a 仍是 5；要写 a += 3 或 a = a + 3。",
    },
    {
        "level": "简单", "topic": "变量与赋值",
        "question": "同时给 a 赋 1、b 赋 2，正确的简写是？",
        "options": ["a, b = 1, 2", "a = 1 b = 2", "a := 1, b := 2", "a; b = 1; 2"],
        "answer": "a, b = 1, 2",
        "explain": "一行多赋值写成 a, b = 1, 2；写成 a=1 b=2 缺少分隔会报错。",
    },
    {
        "level": "简单", "topic": "运算符",
        "question": "判断两个值是否相等，使用哪个运算符？",
        "options": ["==", "=", "===", "=>"],
        "answer": "==",
        "explain": "== 比较是否相等；单个 = 是赋值，Python 没有 ===。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "下列哪个表达式的结果为 False？",
        "options": ["10 < 5", "5 > 2", "3 == 3", "2 != 3"],
        "answer": "10 < 5",
        "explain": "10 < 5 不成立，结果 False；其余三项都为 True。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "当条件成立时反复执行，使用哪个关键字？",
        "options": ["while", "if", "def", "return"],
        "answer": "while",
        "explain": "while 在条件为真时反复执行；for 用于遍历序列。",
    },
    {
        "level": "简单", "topic": "类型转换",
        "question": "print(int(7.9)) 的输出是？",
        "options": ["7", "8", "7.9", "报错"],
        "answer": "7",
        "explain": "int() 直接截掉小数部分（向 0 取整），不是四舍五入，所以是 7。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "not False 的结果是？",
        "options": ["True", "False", "0", "None"],
        "answer": "True",
        "explain": "not 取反，False 取反就是 True。",
    },
    {
        "level": "简单", "topic": "布尔值",
        "question": "bool('abc') 的结果是？",
        "options": ["True", "False", "'abc'", "0"],
        "answer": "True",
        "explain": "非空字符串为真，bool('abc') 是 True；只有空串 '' 才是 False。",
    },
    {
        "level": "简单", "topic": "布尔值",
        "question": "下列转成 bool 后结果为 True 的是？",
        "options": ["bool(-5)", "bool('')", "bool([])", "bool(0)"],
        "answer": "bool(-5)",
        "explain": "只有 0、空字符串、空容器为假；-5 非 0，bool(-5) 为 True。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "list(range(2, 7)) 的结果是？",
        "options": ["[2, 3, 4, 5, 6]", "[2, 3, 4, 5, 6, 7]", "[0, 1, 2, 3, 4, 5, 6]", "[2, 7]"],
        "answer": "[2, 3, 4, 5, 6]",
        "explain": "range(2, 7) 含 2 不含 7，得到 2、3、4、5、6。",
    },
    {
        "level": "简单", "topic": "布尔值",
        "question": "bool(set()) 的结果是？",
        "options": ["False", "True", "set()", "1"],
        "answer": "False",
        "explain": "空集合视为假，bool(set()) 为 False；非空集合才是 True。",
    },

    # ------------------------- 新增·普通 -------------------------
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'apple'.replace('p', 'm') 的结果是？",
        "options": ["ammle", "amle", "ample", "aMMle"],
        "answer": "ammle",
        "explain": "replace 替换全部匹配字符，'apple' 里两个 p 都变 m → 'ammle'。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": "dic = {'name': 'Tom', 'age': 18}，删除键 'age' 的正确语句是？",
        "options": ["del dic['age']", "del dic(age)", "remove dic['age']", "dic.popitem()"],
        "answer": "del dic['age']",
        "explain": "del 字典[键] 删除指定键值对；popitem() 删的是末尾一项，不一定是 age。",
    },
    {
        "level": "普通", "topic": "复合赋值",
        "question": "a = 5; a *= 3，执行后 a 的值是？",
        "options": ["15", "5", "8", "53"],
        "answer": "15",
        "explain": "a *= 3 等价于 a = a * 3，5×3 = 15。",
    },
    {
        "level": "普通", "topic": "布尔判断",
        "question": "下列表达式结果为 False 的是？",
        "options": ["7 >= 7 and ''", "10 > 2 or 3 < 1", "not 0", "bool([1, 2])"],
        "answer": "7 >= 7 and ''",
        "explain": "and 要两边都真；7>=7 为真但 '' 为假，结果取 '' 即假。其余都为 True。",
    },
    {
        "level": "普通", "topic": "流程控制",
        "question": "list(range(-2, 3)) 的结果是？",
        "options": ["[-2, -1, 0, 1, 2]", "[-2, -1, 0, 1, 2, 3]", "[0, 1, 2]", "[-2, -1]"],
        "answer": "[-2, -1, 0, 1, 2]",
        "explain": "range 可从负数开始，含 -2 不含 3，得到 -2,-1,0,1,2。",
    },
    {
        "level": "普通", "topic": "代码阅读·条件",
        "question": "阅读代码，输出是什么？",
        "code": '''score = 75
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")''',
        "options": ["B", "A", "C", "无输出"],
        "answer": "B",
        "explain": "75 不满足 >=90，但满足 >=60，走 elif 分支输出 B。",
    },
    {
        "level": "普通", "topic": "切片",
        "question": "lst = [10, 20, 30, 40, 50]，lst[1:-2] 的结果是？",
        "options": ["[20, 30]", "[20, 30, 40]", "[10, 20, 30]", "[30, 40]"],
        "answer": "[20, 30]",
        "explain": "-2 指倒数第 2 个（40）的位置，切片不含末端，取索引 1、2 → [20, 30]。",
    },
    {
        "level": "普通", "topic": "函数",
        "question": "定义一个无参数、无返回值的函数，正确写法是？",
        "options": ["def func(): pass", "function func():", "func = def()", "define func()"],
        "answer": "def func(): pass",
        "explain": "用 def 定义函数，函数体可用 pass 占位表示暂时什么都不做。",
    },
    {
        "level": "普通", "topic": "运算符",
        "question": "15 // 2 和 15 / 2 的结果分别是？",
        "options": ["7 和 7.5", "7.0 和 7", "7.5 和 7", "8 和 7.5"],
        "answer": "7 和 7.5",
        "explain": "// 整除得整数 7；/ 是真除法得浮点 7.5。",
    },
    {
        "level": "普通", "topic": "代码阅读·循环",
        "question": "阅读代码，打印出的数字是？",
        "code": '''for i in range(4):
    if i == 2:
        continue
    print(i)''',
        "options": ["0 1 3", "0 1 2 3", "2", "0 1"],
        "answer": "0 1 3",
        "explain": "i==2 时 continue 跳过本次 print，所以打印 0、1、3。",
    },
    {
        "level": "普通", "topic": "类型转换",
        "question": "下列哪行代码运行会直接报错？",
        "options": ["int('3.14')", "int('66')", "float('9.9')", "str(123)"],
        "answer": "int('3.14')",
        "explain": "int() 不能直接转带小数点的字符串，int('3.14') 抛 ValueError；需先 float('3.14')。",
    },
    {
        "level": "普通", "topic": "运算符",
        "question": "表达式 3 > 1 or 5 < 0 and 2 == 2 的结果是？",
        "options": ["True", "False", "0", "报错"],
        "answer": "True",
        "explain": "and 优先级高于 or：先算 5<0 and 2==2 为 False，再 True or False 为 True。",
    },
    {
        "level": "普通", "topic": "代码阅读·循环",
        "question": "阅读代码，最终打印 i 的值是？",
        "code": '''i = 0
while i < 3:
    i += 1
print(i)''',
        "options": ["3", "0", "2", "4"],
        "answer": "3",
        "explain": "i 从 0 每次 +1，到 3 时 3<3 不成立退出，print(i) 输出 3。",
    },
    {
        "level": "普通", "topic": "代码阅读·循环",
        "question": "阅读代码，输出结果是？",
        "code": '''for i in range(10):
    if i == 4:
        break
print(i)''',
        "options": ["4", "3", "9", "10"],
        "answer": "4",
        "explain": "i 到 4 时 break 跳出循环，此时 i 已是 4，print 输出 4。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst = [10, 20, 30]，执行 lst.pop(1) 的返回值和列表变化是？",
        "options": [
            "返回 20，列表变为 [10, 30]",
            "返回 10，列表变为 [20, 30]",
            "返回 30，删除末尾元素",
            "报错，pop 不能传参数",
        ],
        "answer": "返回 20，列表变为 [10, 30]",
        "explain": "pop(1) 删除并返回索引 1 的元素 20，列表剩 [10, 30]。",
    },
    {
        "level": "普通", "topic": "字符串",
        "question": "下列哪种写法可以表示跨多行的字符串？",
        "options": ["用三引号包裹", "用单引号包裹", "用 + 连接", "用逗号分隔"],
        "answer": "用三引号包裹",
        "explain": "三引号 ''' ''' 或三个双引号可写多行字符串；单引号、双引号只能写单行。",
    },
    {
        "level": "普通", "topic": "代码阅读·函数",
        "question": "阅读代码，打印结果是？",
        "code": '''def add(x, y):
    return x + y

res = add(2, 5)
print(res)''',
        "options": ["7", "25", "'7'", "None"],
        "answer": "7",
        "explain": "函数返回 2+5=7，print 输出整数 7（不是字符串 '7'）。",
    },
    {
        "level": "普通", "topic": "集合",
        "question": "关于集合 set，下列描述错误的是？",
        "options": ["可以通过 set[0] 取值", "元素不允许重复", "元素无序", "用 {} 或 set() 创建"],
        "answer": "可以通过 set[0] 取值",
        "explain": "集合无序、不支持下标，set[0] 会报错；它确实自动去重、无序。",
    },
    {
        "level": "普通", "topic": "字符串格式化",
        "question": "name = '小李'，要用 f-string 输出“我的名字：小李”，正确写法是？",
        "options": [
            'print(f"我的名字：{name}")',
            'print("我的名字：{name}")',
            'print(f"我的名字：name")',
            'print("我的名字：" + name)',
        ],
        "answer": 'print(f"我的名字：{name}")',
        "explain": "f-string 要加前缀 f 且变量放进 {} 中：f\"我的名字：{name}\"。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst = [1, 3, 5]，执行 lst.append([7, 9]) 后列表长度为？",
        "options": ["4", "3", "5", "6"],
        "answer": "4",
        "explain": "append 把 [7, 9] 当成一个元素加入，长度从 3 变 4（最后一项是子列表）。",
    },
    {
        "level": "普通", "topic": "元组",
        "question": "t = (8)，print(type(t)) 显示的类型是？",
        "options": ["int", "tuple", "list", "str"],
        "answer": "int",
        "explain": "(8) 只是加了括号的整数；单元素元组必须写成 (8,) 带逗号才是 tuple。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "要删除列表中下标为 3 的元素，正确操作是？",
        "options": ["del lst[3]", "lst.remove(3)", "lst.pop()", "clear(lst[3])"],
        "answer": "del lst[3]",
        "explain": "del lst[3] 按下标删；remove(3) 删的是“值为 3”的元素，含义不同。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": "d = {'a': 1, 'b': 2}，d.items() 返回的是？",
        "options": ["键值对组合", "所有键", "所有值", "字典长度"],
        "answer": "键值对组合",
        "explain": "items() 返回 (键, 值) 形式的键值对；keys() 只返回键，values() 只返回值。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": "只遍历字典中所有的“键”，使用哪个方法？",
        "options": ["d.keys()", "d.values()", "d.items()", "d.all()"],
        "answer": "d.keys()",
        "explain": "keys() 返回所有键；values() 返回所有值，items() 返回键值对。",
    },
    {
        "level": "普通", "topic": "循环",
        "question": "for i in range(len(lst)) 这种写法常用来做什么？",
        "options": ["获取列表下标", "直接取列表值", "生成随机数", "反转字符串"],
        "answer": "获取列表下标",
        "explain": "range(len(lst)) 生成 0..len-1，即每个元素的下标，再用 lst[i] 取值。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": "判断键 key 是否在字典 d 中，正确写法是？",
        "options": ["if key in d:", "if key == d:", "if key of d:", "if key is d:"],
        "answer": "if key in d:",
        "explain": "in 判断键是否存在，可避免直接取值触发 KeyError。",
    },
    {
        "level": "普通", "topic": "内置函数",
        "question": "max([3, 9, 1, 5]) 的返回值是？",
        "options": ["9", "1", "3", "5"],
        "answer": "9",
        "explain": "max() 返回最大值 9；对应 min() 返回最小值。",
    },
    {
        "level": "普通", "topic": "内置函数",
        "question": "min([3, 9, 1, 5]) 的返回值是？",
        "options": ["1", "9", "3", "5"],
        "answer": "1",
        "explain": "min() 返回最小值 1。",
    },
    {
        "level": "普通", "topic": "列表推导式",
        "question": "[x * 3 for x in range(4)] 的结果是？",
        "options": ["[0, 3, 6, 9]", "[1, 3, 6, 9]", "[3, 6, 9, 12]", "[0, 1, 2, 3]"],
        "answer": "[0, 3, 6, 9]",
        "explain": "range(4) 是 0,1,2,3，各乘 3 得 [0, 3, 6, 9]。",
    },
    {
        "level": "普通", "topic": "列表推导式",
        "question": "生成 1~10 之间的偶数列表，正确的推导式是？",
        "options": [
            "[x for x in range(1, 11) if x % 2 == 0]",
            "[x for x in range(1, 11) if x % 2 == 1]",
            "[x * 2 for x in range(10)]",
            "[x for x in range(1, 10)]",
        ],
        "answer": "[x for x in range(1, 11) if x % 2 == 0]",
        "explain": "加 if x%2==0 过滤偶数，range(1,11) 取 1~10，得到 [2, 4, 6, 8, 10]。",
    },
    {
        "level": "普通", "topic": "语法",
        "question": "pass 语句的作用是？",
        "options": ["占位，什么都不做", "终止循环", "返回数值", "跳过本次循环"],
        "answer": "占位，什么都不做",
        "explain": "pass 是空操作占位符，用在语法上需要语句但暂时不写内容的地方。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "'python'.upper() 的结果是？",
        "options": ["PYTHON", "python", "Python", "PyThOn"],
        "answer": "PYTHON",
        "explain": "upper() 把字母全部转大写；lower() 转小写。",
    },
    {
        "level": "普通", "topic": "内置函数",
        "question": "round(4.62, 1) 的结果是？",
        "options": ["4.6", "4.7", "5", "4"],
        "answer": "4.6",
        "explain": "round(x, 1) 保留 1 位小数，4.62 → 4.6。",
    },
    {
        "level": "普通", "topic": "集合",
        "question": "集合 set 的核心特点是？",
        "options": ["无序且元素不重复", "有序且允许重复", "支持下标索引取值", "只能存放数字"],
        "answer": "无序且元素不重复",
        "explain": "集合自动去重且无序，不能用下标取值。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst = [5, 1, 3]，执行 lst.sort() 后列表是？",
        "options": ["[1, 3, 5]", "[5, 3, 1]", "[5, 1, 3]", "不变"],
        "answer": "[1, 3, 5]",
        "explain": "sort() 原地升序排序，列表变为 [1, 3, 5]，返回值是 None。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "不带参数的 split() 默认按什么分割字符串？",
        "options": ["空格（空白字符）", "逗号", "换行", "句号"],
        "answer": "空格（空白字符）",
        "explain": "不带参数的 split() 按任意空白（空格/制表/换行）切分。",
    },
    {
        "level": "普通", "topic": "函数",
        "question": "在函数内部修改全局变量，需要先用哪个关键字声明？",
        "options": ["global", "local", "var", "static"],
        "answer": "global",
        "explain": "要在函数里给全局变量重新赋值，得先写 global 变量名，否则会被当成局部变量。",
    },
    {
        "level": "普通", "topic": "输出",
        "question": "print('test', end='') 与默认 print 相比，不会自动添加什么？",
        "options": ["换行符 \\n", "空格", "逗号", "制表符 \\t"],
        "answer": "换行符 \\n",
        "explain": "print 默认在末尾加换行符；end='' 取消换行，让下次输出接在同一行。",
    },

    # ------------------- 新增·挑战（算法与概念） -------------------
    {
        "level": "挑战", "topic": "算法",
        "question": "二分查找（折半查找）算法只能用于哪种数组？",
        "options": ["有序数组", "无序数组", "嵌套数组", "空数组"],
        "answer": "有序数组",
        "explain": "二分查找每次比较中间值来缩小范围，前提是数组已经有序。",
    },
    {
        "level": "挑战", "topic": "算法复杂度",
        "question": "时间复杂度 O(log n) 通常对应下列哪个算法？",
        "options": ["二分查找", "顺序遍历", "冒泡排序", "暴力枚举"],
        "answer": "二分查找",
        "explain": "二分查找每次把范围减半，比较次数约 log₂n，复杂度 O(log n)。",
    },
    {
        "level": "挑战", "topic": "算法复杂度",
        "question": "冒泡排序的时间复杂度是？",
        "options": ["O(n²)", "O(1)", "O(log n)", "O(n)"],
        "answer": "O(n²)",
        "explain": "冒泡排序两层嵌套循环，平均和最坏时间复杂度都是 O(n²)。",
    },
    {
        "level": "挑战", "topic": "排序",
        "question": "快速排序的核心思想是？",
        "options": ["选基准划分 + 分治递归", "相邻元素逐个交换", "从头到尾顺序查找", "递归累加求和"],
        "answer": "选基准划分 + 分治递归",
        "explain": "快排选一个基准，把更小/更大的元素分到两边（划分），再对两边递归，属于分治法。",
    },
    {
        "level": "挑战", "topic": "数论",
        "question": "完数（完美数）的定义是？",
        "options": ["所有真因数之和等于自身", "全部因数之和等于自身", "只能被 1 整除", "各位立方和等于自身"],
        "answer": "所有真因数之和等于自身",
        "explain": "完数等于它所有真因数（不含自身）之和，例如 6 = 1 + 2 + 3。",
    },
    {
        "level": "挑战", "topic": "字符串算法",
        "question": "回文字符串指的是？",
        "options": ["正读反读完全一致", "全部由数字组成", "长度一定是偶数", "不含大写字母"],
        "answer": "正读反读完全一致",
        "explain": "回文正读反读相同，如 'level'、'aba'；可用 s == s[::-1] 判断。",
    },
    {
        "level": "挑战", "topic": "集合",
        "question": "给列表去重，最快的数据结构转换是？",
        "options": ["转成集合 set", "转成元组", "转成字符串", "转成字典的值"],
        "answer": "转成集合 set",
        "explain": "set() 自动去重、查重接近 O(1)，list(set(lst)) 是最快的去重写法（不保序）。",
    },
    {
        "level": "挑战", "topic": "集合",
        "question": "“哈希去重”在 Python 中通常对应哪种数据结构？",
        "options": ["set", "list", "tuple", "str"],
        "answer": "set",
        "explain": "set/dict 底层是哈希表，成员判断快，适合去重和查重。",
    },
    {
        "level": "挑战", "topic": "算法",
        "question": "下列哪一项属于“空间换时间”的优化思路？",
        "options": ["用哈希表记录已遍历的值", "二分查找", "冒泡排序", "顺序循环逐个比较"],
        "answer": "用哈希表记录已遍历的值",
        "explain": "用额外的集合/字典记录已出现的值，用空间换取查找时间，是典型的空间换时间。",
    },
    {
        "level": "挑战", "topic": "应用",
        "question": "常见的密码强度校验，一般“不”要求下列哪一项？",
        "options": ["必须包含空格", "长度不少于 8 位", "包含大写字母", "包含数字"],
        "answer": "必须包含空格",
        "explain": "强密码常要求长度、大小写、数字、符号，但一般不要求“必须含空格”。",
    },
    {
        "level": "挑战", "topic": "应用",
        "question": "18 位身份证号的最后一位校验码，可能出现的特殊字符是？",
        "options": ["X", "Y", "Z", "Q"],
        "answer": "X",
        "explain": "校验码若计算结果为 10，用罗马数字 X 表示，所以末位可能是 X。",
    },
    {
        "level": "挑战", "topic": "算法",
        "question": "解决“三数之和”问题，常用的第一步操作是？",
        "options": ["先对数组排序", "先反转数组", "先转成集合", "先统计长度"],
        "answer": "先对数组排序",
        "explain": "先排序便于用双指针向中间逼近并跳过重复值，是三数之和的常用第一步。",
    },

    # ------------- 新增·代码阅读（挑战，源自「扩充完整版」表格代码）-------------
    {
        "level": "挑战", "topic": "代码阅读·变量赋值",
        "question": "阅读代码，print(b) 输出什么？",
        "code": '''a = 12
b = a
a = 50
print(b)''',
        "options": ["12", "50", "0", "报错"],
        "answer": "12",
        "explain": "b = a 时把 12 赋给 b；之后 a 改成 50 不影响已赋值的 b，输出 12。",
    },
    {
        "level": "挑战", "topic": "代码阅读·切片",
        "question": "阅读代码，print(s[:4]) 输出什么？",
        "code": '''s = "programming"
print(s[:4])''',
        "options": ["prog", "progr", "gram", "pro"],
        "answer": "prog",
        "explain": "s[:4] 取前 4 个字符（索引 0~3），得到 'prog'。",
    },
    {
        "level": "挑战", "topic": "代码阅读·参数传递",
        "question": "阅读代码，print(num) 输出什么？",
        "code": '''def add(x):
    x += 10

num = 20
add(num)
print(num)''',
        "options": ["20", "30", "10", "报错"],
        "answer": "20",
        "explain": "整数不可变，函数内 x += 10 只改局部副本，原 num 仍是 20。",
    },
    {
        "level": "挑战", "topic": "代码阅读·运算符",
        "question": "阅读代码，print(res) 输出什么？",
        "code": '''res = 14 // 3 + 2 ** 3
print(res)''',
        "options": ["12", "10", "13", "9"],
        "answer": "12",
        "explain": "先幂 2**3=8，再整除 14//3=4，最后 4+8=12（** 高于 //，// 高于 +）。",
    },
    {
        "level": "挑战", "topic": "代码阅读·循环",
        "question": "阅读代码，输出是什么？",
        "code": '''for i in range(4, 15, 5):
    print(i, end=" ")''',
        "options": ["4 9 14", "4 5 6", "5 10 15", "4 8 12"],
        "answer": "4 9 14",
        "explain": "从 4 起、步长 5：4、9、14（下一个 19≥15 停），end=' ' 同行空格分隔。",
    },
    {
        "level": "挑战", "topic": "代码阅读·递归",
        "question": "阅读代码，print(sum_all(5)) 输出什么？",
        "code": '''def sum_all(n):
    if n == 1:
        return 1
    return n + sum_all(n - 1)

print(sum_all(5))''',
        "options": ["15", "5", "10", "8"],
        "answer": "15",
        "explain": "1+2+3+4+5=15，递归到 n==1 返回 1，再逐层累加。",
    },
    {
        "level": "挑战", "topic": "代码阅读·列表推导式",
        "question": "阅读代码，print(new) 输出什么？",
        "code": '''lst = [4, 6, 8, 10]
new = [x // 2 for x in lst]
print(new)''',
        "options": ["[2, 3, 4, 5]", "[8, 12, 16, 20]", "[0, 0, 0, 0]", "[4, 6, 8, 10]"],
        "answer": "[2, 3, 4, 5]",
        "explain": "各元素整除 2：4→2, 6→3, 8→4, 10→5。",
    },
    {
        "level": "挑战", "topic": "代码阅读·转义字符",
        "question": "阅读代码，输出是什么？",
        "code": '''print("apple\\nbanana\\npear")''',
        "options": ["分三行输出三个单词", "一行输出全部文字", "原样输出 apple\\nbanana\\npear", "运行报错"],
        "answer": "分三行输出三个单词",
        "explain": "\\n 是换行符，apple、banana、pear 分三行输出。",
    },
    {
        "level": "挑战", "topic": "代码阅读·条件",
        "question": "阅读代码，输出是什么？",
        "code": '''x = 3
if x > 5:
    print("大")
else:
    print("小")''',
        "options": ["小", "大", "无输出", "报错"],
        "answer": "小",
        "explain": "3 > 5 不成立，走 else 输出“小”。",
    },
    {
        "level": "挑战", "topic": "代码阅读·循环",
        "question": "阅读代码，print(count) 输出什么？",
        "code": '''count = 0
for i in range(1, 4):
    count += 1
print(count)''',
        "options": ["3", "1", "4", "0"],
        "answer": "3",
        "explain": "range(1, 4) 循环 3 次，count 从 0 累加到 3。",
    },
    {
        "level": "挑战", "topic": "代码阅读·字典",
        "question": "阅读代码，print(d.get('z', 0)) 输出什么？",
        "code": '''d = {"x": 10, "y": 20}
print(d.get("z", 0))''',
        "options": ["0", "10", "20", "报错"],
        "answer": "0",
        "explain": "键 'z' 不存在，get 返回默认值 0，不会报错。",
    },
    {
        "level": "挑战", "topic": "代码阅读·交换",
        "question": "阅读代码，print(a, b) 输出什么？",
        "code": '''a, b = 7, 9
a, b = b, a
print(a, b)''',
        "options": ["9 7", "7 9", "7 7", "9 9"],
        "answer": "9 7",
        "explain": "a, b = b, a 同时交换，a 变 9、b 变 7。",
    },
    {
        "level": "挑战", "topic": "代码阅读·索引",
        "question": "阅读代码，print(word[-2]) 输出什么？",
        "code": '''word = "test"
print(word[-2])''',
        "options": ["s", "t", "e", "报错"],
        "answer": "s",
        "explain": "-2 是倒数第 2 个字符，'test' 倒数第二个是 's'。",
    },
    {
        "level": "挑战", "topic": "代码阅读·循环累加",
        "question": "阅读代码，print(total) 输出什么？",
        "code": '''total = 0
for i in [1, 2, 3]:
    total = total + i
print(total)''',
        "options": ["6", "3", "5", "0"],
        "answer": "6",
        "explain": "依次累加 1+2+3 = 6。",
    },
    {
        "level": "挑战", "topic": "代码阅读·布尔",
        "question": "阅读代码，输出是什么？",
        "code": '''flag = False
if not flag:
    print("yes")
else:
    print("no")''',
        "options": ["yes", "no", "无输出", "报错"],
        "answer": "yes",
        "explain": "not False 为 True，进入 if 输出 'yes'。",
    },

    # ===================================================================
    # 【第二批扩充·据「未更新题目筛查.md」补入】
    # 来源：Python入门60道 / 扩充完整版 / 普通模式题库 中"未发现同题"的题。
    # 概念重复的孪生题只保留一份；个别原题选项有误已修正。
    # ===================================================================

    # --------------------- 入门60道（简单）---------------------
    {
        "level": "简单", "topic": "输出",
        "question": '执行 print("hello")，控制台输出结果是？',
        "options": ["hello", '"hello"', "print", "无内容"],
        "answer": "hello",
        "explain": "print 输出引号里的内容本身、不带引号，结果是 hello。",
    },
    {
        "level": "简单", "topic": "变量与赋值",
        "question": "a = 8; print(a) 的运行结果是？",
        "options": ["8", "a", '"8"', "0"],
        "answer": "8",
        "explain": "print(a) 输出变量 a 的值 8（整数，不带引号）。",
    },
    {
        "level": "简单", "topic": "数据类型",
        "question": "下面哪一个是字符串类型的数据？",
        "options": ['"15"', "15", "True", "[1, 5]"],
        "answer": '"15"',
        "explain": "用引号括起来的才是字符串，\"15\" 是 str；15 是 int。",
    },
    {
        "level": "简单", "topic": "字符串运算符",
        "question": 'print("py" + "thon") 的结果是？',
        "options": ["python", "py thon", "py+thon", "报错"],
        "answer": "python",
        "explain": "+ 把两个字符串拼接起来，中间没有空格，结果是 python。",
    },
    {
        "level": "简单", "topic": "字符串",
        "question": 's = "abc"，取第一个字符的正确写法是？',
        "options": ["s[0]", "s[1]", "s[-1]", "s[3]"],
        "answer": "s[0]",
        "explain": "下标从 0 开始，第一个字符是 s[0]。",
    },
    {
        "level": "简单", "topic": "字符串方法",
        "question": 's = "a b c"，s.split() 的结果是？',
        "options": ['["a", "b", "c"]', '"abc"', '("a", "b", "c")', '{"a", "b", "c"}'],
        "answer": '["a", "b", "c"]',
        "explain": "split() 默认按空格切分，返回一个字符串列表。",
    },
    {
        "level": "简单", "topic": "字符串方法",
        "question": 's = "mm"，s.replace("m", "k") 的结果是？',
        "options": ["kk", "mk", "mm", "k"],
        "answer": "kk",
        "explain": "replace 替换全部匹配字符，两个 m 都变成 k。",
    },
    {
        "level": "简单", "topic": "内置函数",
        "question": "len([2, 4, 6, 8]) 的返回值是？",
        "options": ["4", "3", '"4"', "(4)"],
        "answer": "4",
        "explain": "len() 返回元素个数，列表有 4 个元素。",
    },
    {
        "level": "简单", "topic": "列表",
        "question": "[1, 2] + [3, 4] 的结果是？",
        "options": ["[1, 2, 3, 4]", "[1, 2, [3, 4]]", "[4, 3, 2, 1]", "报错"],
        "answer": "[1, 2, 3, 4]",
        "explain": "+ 把两个列表首尾拼接成一个新列表。",
    },
    {
        "level": "简单", "topic": "元组",
        "question": "空元组的正确写法是？",
        "options": ["()", "[]", "{}", '""'],
        "answer": "()",
        "explain": "() 是空元组；[] 是空列表，{} 是空字典。",
    },
    {
        "level": "简单", "topic": "元组",
        "question": "t = (5, 10)，t[0] 的值是？",
        "options": ["5", "10", "0", "(5)"],
        "answer": "5",
        "explain": "元组下标从 0 开始，t[0] 是第一个元素 5。",
    },
    {
        "level": "简单", "topic": "元组",
        "question": "t = (1, 2)，执行 t[0] = 9 会怎样？",
        "options": ["直接报错", "成功改成 (9, 2)", "自动转成列表", "返回 None"],
        "answer": "直接报错",
        "explain": "元组不可变，给元素重新赋值会抛 TypeError。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": "创建一个空字典的正确写法是？",
        "options": ["{}", "()", "[]", "0"],
        "answer": "{}",
        "explain": "{} 是空字典；空集合要用 set()，空列表是 []。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": 'd = {"name": "小红"}，取出 "小红" 的写法是？',
        "options": ['d["name"]', "d(name)", "d.name", "d-name"],
        "answer": 'd["name"]',
        "explain": "字典用中括号加键取值：d[\"name\"]。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": 'd = {}，d.get("age", 0) 的返回值是？',
        "options": ["0", "None", '"age"', "报错"],
        "answer": "0",
        "explain": "键不存在时 get 返回默认值 0，不会报错。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": "清空字典里所有键值对，用哪个方法？",
        "options": ["d.clear()", "del d", "d.pop()", "d.remove()"],
        "answer": "d.clear()",
        "explain": "clear() 清空所有键值对但保留字典对象；del d 把整个变量删掉。",
    },
    {
        "level": "简单", "topic": "集合运算",
        "question": "s1 = {1, 2}, s2 = {2, 3}，求两个集合的交集用哪个运算符？",
        "options": ["&", "|", "-", "+"],
        "answer": "&",
        "explain": "& 求交集（两个集合都有的元素）；| 求并集。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "5 == 5 的布尔结果是？",
        "options": ["True", "False", "5", "报错"],
        "answer": "True",
        "explain": "== 判断相等，5 等于 5，结果 True。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "9 > 12 的结果是？",
        "options": ["False", "True", "9", "12"],
        "answer": "False",
        "explain": "9 不大于 12，比较结果是 False。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "4 < 7 的结果是？",
        "options": ["True", "False", "11", "-3"],
        "answer": "True",
        "explain": "4 小于 7 成立，结果 True。",
    },
    {
        "level": "简单", "topic": "布尔判断",
        "question": "3 != 8 的结果是？",
        "options": ["True", "False", "0", "1"],
        "answer": "True",
        "explain": "!= 判断不相等，3 和 8 不相等，结果 True。",
    },
    {
        "level": "简单", "topic": "代码阅读·条件",
        "question": "阅读代码，输出是什么？",
        "code": '''num = 1
if num > 0:
    print("正数")''',
        "options": ["正数", "num", "1", "无输出"],
        "answer": "正数",
        "explain": "num = 1 满足 num > 0，进入 if 输出“正数”。",
    },
    {
        "level": "简单", "topic": "代码阅读·循环",
        "question": "阅读代码，打印出的内容是？",
        "code": '''for i in [1, 2]:
    print(i)''',
        "options": ["1 2", "i", "[1, 2]", "无输出"],
        "answer": "1 2",
        "explain": "for 遍历列表，依次打印元素 1 和 2。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "在循环中跳过本次剩余语句、直接进入下一轮，用哪个关键字？",
        "options": ["continue", "break", "return", "skip"],
        "answer": "continue",
        "explain": "continue 跳过本次剩余代码进入下一轮；break 是跳出整个循环。",
    },
    {
        "level": "简单", "topic": "变量命名",
        "question": "下面哪个是合法的 Python 变量名？",
        "options": ["num1", "1num", "num-1", "num@1"],
        "answer": "num1",
        "explain": "变量名由字母/数字/下划线组成、不能数字开头、不能含 - @ 等符号，num1 合法。",
    },
    {
        "level": "简单", "topic": "字符串",
        "question": 's = "cat"，取最后一个字符的写法是？',
        "options": ["s[-1]", "s[0]", "s[1]", "s[3]"],
        "answer": "s[-1]",
        "explain": "负下标从末尾数起，s[-1] 是最后一个字符 't'。",
    },
    {
        "level": "简单", "topic": "字典",
        "question": 'd = {"a": 1}，安全删除键 "a"（不存在也不报错）的写法是？',
        "options": ['d.pop("a", None)', 'del d["a"]', 'd.remove("a")', "d.popitem()"],
        "answer": 'd.pop("a", None)',
        "explain": "pop(键, 默认值) 删键并返回值，键不存在时返回默认值不报错；del 删不存在的键会报错。",
    },
    {
        "level": "简单", "topic": "代码阅读·条件",
        "question": "阅读代码，运行会怎样？",
        "code": '''if 5 > 0:
    print("ok")''',
        "options": ["会打印 ok", "不会打印", "报错", "输出空白"],
        "answer": "会打印 ok",
        "explain": "5 > 0 成立，执行 if 里的 print，输出 ok。",
    },
    {
        "level": "简单", "topic": "内置函数",
        "question": "len((6, 7, 8)) 的返回值是？",
        "options": ["3", "2", '"3"', "(3)"],
        "answer": "3",
        "explain": "len() 返回元素个数，元组有 3 个元素。",
    },

    # --------------------- 扩充完整版·简单 ---------------------
    {
        "level": "简单", "topic": "流程控制",
        "question": "list(range(5)) 里第一个数字是？",
        "options": ["0", "1", "5", "4"],
        "answer": "0",
        "explain": "range(5) 从 0 开始到 4，第一个是 0。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "下列哪个关键字用于条件判断？",
        "options": ["if", "for", "def", "while"],
        "answer": "if",
        "explain": "if 用于条件判断；for/while 是循环，def 用来定义函数。",
    },
    {
        "level": "简单", "topic": "字符串运算符",
        "question": 'print("hello" * 2) 的输出是？',
        "options": ["hellohello", "hello2", "hello hello", "报错"],
        "answer": "hellohello",
        "explain": "字符串 * 整数 是重复拼接，\"hello\" 重复 2 次且中间无空格。",
    },
    {
        "level": "简单", "topic": "流程控制",
        "question": "list(range(1, 10, 2)) 的结果是？",
        "options": ["[1, 3, 5, 7, 9]", "[2, 4, 6, 8, 10]", "[1, 2, 3, ..., 9]", "[1, 10, 2]"],
        "answer": "[1, 3, 5, 7, 9]",
        "explain": "从 1 开始、步长 2、不含 10，得到 1,3,5,7,9。",
    },
    {
        "level": "简单", "topic": "类型转换",
        "question": "把数字转成字符串，用哪个函数？",
        "options": ["str()", "int()", "float()", "len()"],
        "answer": "str()",
        "explain": "str() 转字符串；int() 转整数，float() 转小数。",
    },

    # --------------------- 扩充完整版·普通 ---------------------
    {
        "level": "普通", "topic": "数论",
        "question": "质数的正确定义是？",
        "options": [
            "只能被 1 和自身整除、且大于 1 的整数",
            "所有奇数都是质数",
            "能被 2 整除的数",
            "大于 0 的整数",
        ],
        "answer": "只能被 1 和自身整除、且大于 1 的整数",
        "explain": "质数大于 1 且只有 1 和它本身两个因数，如 2、3、5、7。",
    },
    {
        "level": "普通", "topic": "流程控制",
        "question": "continue 关键字的作用是？",
        "options": ["跳过本次循环，进入下一次", "直接结束整个循环", "退出函数", "没有作用"],
        "answer": "跳过本次循环，进入下一次",
        "explain": "continue 只结束本次迭代进入下一轮；break 才是跳出整个循环。",
    },
    {
        "level": "普通", "topic": "列表方法",
        "question": "lst = [1, 2, 3, 4]，lst.pop() 会删除哪个元素？",
        "options": ["4", "1", "2", "3"],
        "answer": "4",
        "explain": "pop() 不带参数时删除并返回最后一个元素 4。",
    },
    {
        "level": "普通", "topic": "函数",
        "question": "函数返回结果使用哪个关键字？",
        "options": ["return", "print", "def", "break"],
        "answer": "return",
        "explain": "return 把结果返回给调用处；print 只是打印，不等于返回。",
    },
    {
        "level": "普通", "topic": "元组",
        "question": "下列哪个是元组？",
        "options": ["(1, 2)", "[1, 2]", "{1, 2}", '"12"'],
        "answer": "(1, 2)",
        "explain": "圆括号是元组；[] 是列表，{} 是集合/字典。",
    },

    # --------------------- 扩充完整版·挑战 ---------------------
    {
        "level": "挑战", "topic": "递归",
        "question": "递归函数必不可少的结构是？",
        "options": ["终止条件（出口）", "for 循环", "列表", "字典"],
        "answer": "终止条件（出口）",
        "explain": "递归必须有终止条件，否则会无限递归直到 RecursionError。",
    },
    {
        "level": "挑战", "topic": "数论算法",
        "question": "求最大公约数最常用的算法是？",
        "options": ["欧几里得辗转相除法", "二分法", "冒泡排序", "递归求和"],
        "answer": "欧几里得辗转相除法",
        "explain": "辗转相除法（欧几里得算法）用 a, b = b, a % b 反复求余，直到余数为 0。",
    },

    # --------------------- 普通模式题库（普通）---------------------
    {
        "level": "普通", "topic": "元组",
        "question": "关于元组 t = (1, 2, 3)，下列说法正确的是？",
        "options": [
            "元组内的元素不可单独修改",
            "t[0] = 9 可以改第一个元素",
            "元组支持 append 添加元素",
            "空元组写作 t = {}",
        ],
        "answer": "元组内的元素不可单独修改",
        "explain": "元组不可变，不能改元素也不能 append；空元组是 ()，{} 是空字典。",
    },
    {
        "level": "普通", "topic": "字符串",
        "question": 's = "python"，取倒数第二个字符的写法是？',
        "options": ["s[-2]", "s[5]", "s[len(s)]", "s[-1]"],
        "answer": "s[-2]",
        "explain": "-2 表示倒数第二个字符（'o'）；s[len(s)] 会越界报错。",
    },
    {
        "level": "普通", "topic": "字典",
        "question": 'd = {"a": 1}，想取键 "b"、不存在时返回 0，推荐写法是？',
        "options": ['d.get("b", 0)', 'd["b"]', 'd.pop("b")', 'd["b"] or 0'],
        "answer": 'd.get("b", 0)',
        "explain": "get(键, 默认值) 取不到时返回默认值且不报错；d[\"b\"] 取不存在的键会 KeyError。",
    },
    {
        "level": "普通", "topic": "运算符",
        "question": "3 ** 3 的运算结果是？",
        "options": ["27", "9", "6", "33"],
        "answer": "27",
        "explain": "** 是幂运算，3 的 3 次方 = 27。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "要去掉字符串左右两侧的空格，用哪个方法？",
        "options": ["strip()", "lstrip()", "rstrip()", 'replace(" ", "")'],
        "answer": "strip()",
        "explain": "strip() 去掉首尾空白；lstrip/rstrip 只去一侧，replace 会把中间空格也删掉。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": '把 "apple,banana,orange" 按逗号切成列表，正确写法是？',
        "options": ['split(",")', "split()", 'split("、")', 'cut(",")'],
        "answer": 'split(",")',
        "explain": "split(\",\") 以逗号为分隔符切分；不带参数的 split() 按空格切。",
    },
    {
        "level": "普通", "topic": "字符串方法",
        "question": "判断一个字符串是否全部由数字组成，用哪个方法？",
        "options": ["isdigit()", "isalpha()", "isnumber()", "isspace()"],
        "answer": "isdigit()",
        "explain": "isdigit() 全是数字时返回 True；isalpha() 判断字母，isnumber() 不是字符串方法。",
    },
    {
        "level": "普通", "topic": "列表",
        "question": "把列表 [1, 2] 和 [3, 4] 拼接合并，用哪个运算符？",
        "options": ["+", "*", "&", "="],
        "answer": "+",
        "explain": "+ 把两个列表拼接成新列表 [1, 2, 3, 4]；* 是重复。",
    },
]


# 每个难度默认抽题量（可在侧边栏用滑块调整）
LEVEL_SIZE = {"简单": 10, "普通": 12, "挑战": 15}
DIFF_TAG = {"简单": "🌱 简单", "普通": "📘 普通", "挑战": "⚡ 挑战"}


# ===================================================================
# 主题样式：取自「界面设计描述词」清新蓝白主题
# 分色选项 A蓝 / B绿 / C橙 / D粉，渐变大标题，圆角卡片，柔和阴影
# ===================================================================
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(145deg, #f0f7ff 0%, #e6f0fa 100%); }
    .big-title {
        font-size: 34px; font-weight: 800; line-height: 1.2; letter-spacing: 0.5px;
        background: linear-gradient(135deg, #1a3b5d 0%, #3776AB 45%, #5A9FD4 70%, #7BB3E0 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        margin-bottom: 0.1rem;
    }
    .subtitle { color: #2c4a6e; font-size: 15px; margin-bottom: 0.2rem; }
    .quiz-card {
        background: rgba(255,255,255,0.75); border-radius: 28px; padding: 22px 26px 6px;
        box-shadow: 0 8px 32px rgba(60,100,177,0.06); border: 1px solid rgba(255,255,255,0.7);
        margin-top: 0.4rem;
    }
    .q-number { font-size: 17px; font-weight: 700; color: #1a3b5d;
        background: rgba(55,118,171,0.08); padding: 3px 16px; border-radius: 40px; }
    .q-tag { font-size: 13px; font-weight: 600; padding: 3px 14px; border-radius: 40px;
        background: rgba(90,159,212,0.12); color: #2c6b9e; margin-left: 8px; }
    .q-text { font-size: 20px; font-weight: 600; color: #0f2a44; line-height: 1.5; margin: 14px 0 6px; }
    /* 分色选项 A蓝 B绿 C橙 D粉 */
    div[role="radiogroup"] label {
        border-radius: 16px !important; padding: 11px 18px !important; margin-bottom: 10px !important;
        border: 2px solid transparent !important; box-shadow: 0 2px 6px rgba(0,0,0,0.02) !important;
        transition: all .15s !important; width: 100% !important;
    }
    div[role="radiogroup"] label:hover {
        transform: translateY(-2px) !important; box-shadow: 0 8px 20px rgba(60,100,177,0.10) !important;
    }
    div[role="radiogroup"] label:nth-of-type(1) { background: #E3F2FD !important; }
    div[role="radiogroup"] label:nth-of-type(2) { background: #E8F5E9 !important; }
    div[role="radiogroup"] label:nth-of-type(3) { background: #FFF3E0 !important; }
    div[role="radiogroup"] label:nth-of-type(4) { background: #FCE4EC !important; }
    /* 按钮 */
    .stButton > button { border-radius: 16px !important; font-weight: 600 !important;
        border: none !important; transition: all .2s !important; }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #3776AB, #4A8EC7) !important; color: #fff !important;
        box-shadow: 0 4px 16px rgba(55,118,171,0.20) !important; }
    .stButton > button[kind="primary"]:hover { transform: translateY(-2px) !important; }
    /* 侧边栏分数面板 */
    .score-panel { background: linear-gradient(135deg, rgba(55,118,171,0.06), rgba(90,159,212,0.10));
        border-radius: 18px; padding: 16px; margin: 8px 0 12px; border: 1px solid rgba(55,118,171,0.08); }
    .score-panel .row { display: flex; justify-content: space-between; align-items: center; padding: 2px 0; }
    .score-panel .label { font-size: 14px; color: #2c4a6e; font-weight: 500; }
    .score-panel .value { font-size: 22px; font-weight: 800; color: #3776AB; }
    .score-panel .sub { font-size: 13px; color: #4f7a9e; display: flex;
        justify-content: space-between; margin-top: 8px; }
    .score-panel .sub span { font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------- 抽题 / 评分逻辑 -----------------------------
def candidates_for(level):
    """该难度可抽的题池：简单只含简单；普通含简单+普通；挑战三档都有。"""
    allowed = ["简单"]
    if level in ("普通", "挑战"):
        allowed.append("普通")
    if level == "挑战":
        allowed.append("挑战")
    return [q for q in QUESTION_BANK if q["level"] in allowed]


def get_title(rate):
    """按正确率返回称号。"""
    if rate >= 1:
        return "Python 满分闯关王 🏆"
    if rate >= 0.8:
        return "基础很稳的同学 💪"
    if rate >= 0.6:
        return "正在升级的循环高手 🔁"
    return "需要再复习一轮的 Python 萌新 🌱"


def start_new_quiz(level, count):
    """生成一套新题并重置本轮所有进度。"""
    pool = candidates_for(level)
    count = max(1, min(count, len(pool)))
    st.session_state.quiz = random.sample(pool, count)
    st.session_state.level = level
    st.session_state.count = count
    st.session_state.idx = 0          # 当前第几题（从 0 起）
    st.session_state.answered = False  # 当前题是否已提交
    st.session_state.selected = None   # 当前题所选答案
    st.session_state.correct = 0
    st.session_state.wrong = 0
    st.session_state.topic_total = {}  # 各知识点出现次数
    st.session_state.topic_right = {}  # 各知识点答对次数
    st.session_state.completed = False
    st.session_state.quiz_id = st.session_state.get("quiz_id", 0) + 1


# ----------------------------- 初始化 -----------------------------
if "quiz" not in st.session_state:
    start_new_quiz("简单", LEVEL_SIZE["简单"])


# ----------------------------- 侧边栏 -----------------------------
with st.sidebar:
    st.markdown("### 🐍 Python 答题闯关")
    level = st.radio(
        "难度模式",
        ["简单", "普通", "挑战"],
        index=["简单", "普通", "挑战"].index(st.session_state.level),
    )
    pool_size = len(candidates_for(level))
    num = st.slider(
        "本次题量",
        min_value=1,
        max_value=pool_size,
        value=min(LEVEL_SIZE[level], pool_size),
        key=f"num_{level}",
        help="拖动调节这一次闯多少关；上限就是该难度题库的全部题量。",
    )
    # 切换难度或调节题量 → 自动换一套题
    if level != st.session_state.level or num != st.session_state.count:
        start_new_quiz(level, num)
        st.rerun()

    answered_n = st.session_state.correct + st.session_state.wrong
    total_n = len(st.session_state.quiz)
    acc = round(st.session_state.correct / answered_n * 100) if answered_n else 0
    st.markdown(
        f"""
        <div class="score-panel">
            <div class="row"><span class="label">⭐ 得分</span>
                <span class="value">{st.session_state.correct * 10}</span></div>
            <div class="sub">
                <span>✅ 正确 {st.session_state.correct}</span>
                <span>❌ 错误 {st.session_state.wrong}</span>
                <span>📝 {answered_n}/{total_n}</span>
            </div>
            <div class="sub"><span>正确率</span><span>{acc}%</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🔄 重新开始", use_container_width=True):
        start_new_quiz(level, num)
        st.rerun()

    with st.expander("📖 游戏规则", expanded=False):
        st.markdown(
            f"- 本轮共 **{total_n}** 道 Python 复习题\n"
            "- 选择答案后点「✅ 提交答案」\n"
            "- 正确 +10 分，错误不扣分\n"
            "- 看完解析点「➡️ 下一题」继续\n"
            "- 全部答完显示成绩和知识点得分图 🎉"
        )
    st.caption("知识点：变量·运算符·字符串·列表/字典/集合·循环·函数·递归·二维列表·排序·文件异常·算法")


# ----------------------------- 顶部标题区 -----------------------------
st.markdown('<div class="big-title">Python 期末复习闯关小游戏</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">📚 期末刷题神器 · 一题一关 · 边玩边学，轻松巩固 Python 基础</div>',
    unsafe_allow_html=True,
)
st.divider()


# ----------------------------- 主体：逐题闯关 -----------------------------
quiz = st.session_state.quiz
idx = st.session_state.idx

if st.session_state.completed or idx >= len(quiz):
    # ---------------- 完成界面 ----------------
    total = len(quiz)
    correct = st.session_state.correct
    rate = correct / total if total else 0
    st.markdown(
        f"""
        <div class="quiz-card" style="text-align:center; padding-bottom:24px;">
            <div style="font-size:52px;">🎉</div>
            <h2 style="color:#1a3b5d; margin:6px 0;">闯关完成！</h2>
            <p style="font-size:18px; color:#1a3b5d;">得分
                <span style="color:#3776AB; font-size:30px; font-weight:800;">{correct * 10}</span> 分</p>
            <p style="color:#3d5f7e;">✅ 正确 {correct} 题 · ❌ 错误 {st.session_state.wrong} 题 · 正确率 {round(rate * 100)}%</p>
            <p style="font-size:17px; color:#2c4a6e; margin-top:10px;">称号：{get_title(rate)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tr, tt = st.session_state.topic_right, st.session_state.topic_total
    if tt:
        st.subheader("📊 知识点得分率（%）")
        st.bar_chart({t: round(tr.get(t, 0) / tt[t] * 100, 1) for t in tt})
        missed = [t for t in tt if tr.get(t, 0) < tt[t]]
        if missed:
            st.warning("建议重点复习：" + "、".join(missed))
        else:
            st.balloons()

    if st.button("🔄 再来一轮", type="primary", use_container_width=True):
        start_new_quiz(st.session_state.level, st.session_state.count)
        st.rerun()

else:
    # ---------------- 答题界面 ----------------
    item = quiz[idx]
    qid = st.session_state.quiz_id
    st.markdown(
        f'<span class="q-number">📌 第 {idx + 1} / {len(quiz)} 题</span>'
        f'<span class="q-tag">{DIFF_TAG.get(item["level"], item["level"])}</span>'
        f'<span class="q-tag">{html.escape(item["topic"])}</span>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="q-text">{html.escape(item["question"])}</div>', unsafe_allow_html=True)
    if item.get("code"):
        st.code(item["code"], language="python")

    choice = st.radio(
        "选择答案",
        item["options"],
        index=None,
        key=f"opt_{qid}_{idx}",
        disabled=st.session_state.answered,
        label_visibility="collapsed",
    )

    col_submit, col_next = st.columns(2)
    with col_submit:
        if st.button(
            "✅ 提交答案",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.answered or choice is None,
        ):
            st.session_state.selected = choice
            st.session_state.answered = True
            topic = item["topic"]
            st.session_state.topic_total[topic] = st.session_state.topic_total.get(topic, 0) + 1
            if choice == item["answer"]:
                st.session_state.correct += 1
                st.session_state.topic_right[topic] = st.session_state.topic_right.get(topic, 0) + 1
            else:
                st.session_state.wrong += 1
            st.rerun()
    with col_next:
        is_last = idx == len(quiz) - 1
        if st.button(
            "🏁 查看成绩" if is_last else "➡️ 下一题",
            use_container_width=True,
            disabled=not st.session_state.answered,
        ):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.session_state.selected = None
            if st.session_state.idx >= len(quiz):
                st.session_state.completed = True
            st.rerun()

    # ---------------- 提交后：反馈 + 解析 ----------------
    if st.session_state.answered:
        if st.session_state.selected == item["answer"]:
            st.success("✅ 回答正确！+10 分")
        else:
            st.error(f"❌ 回答错误。正确答案：{item['answer']}")
        st.info("💡 " + item["explain"])

    st.markdown(
        '<div style="margin-top:14px; text-align:center; font-size:12px; color:#8aa9c9;">'
        '小组期末大作业 · Python 复习答题小游戏</div>',
        unsafe_allow_html=True,
    )
