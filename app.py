import random

import streamlit as st


st.set_page_config(
    page_title="Python期末复习闯关",
    page_icon="🐍",
    layout="centered",
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
]


LEVEL_SIZE = {"简单": 5, "普通": 8, "挑战": 10}


def candidates_for(level):
    """该难度可抽的题池：简单只含简单；普通含简单+普通；挑战三档都有。"""
    allowed = ["简单"]
    if level in ("普通", "挑战"):
        allowed.append("普通")
    if level == "挑战":
        allowed.append("挑战")
    return [q for q in QUESTION_BANK if q["level"] in allowed]


def build_quiz(level, count):
    """从该难度题池里随机抽 count 道题（不超过题池上限）。"""
    pool = candidates_for(level)
    count = max(1, min(count, len(pool)))
    return random.sample(pool, count)


def get_title(score, total):
    """根据得分率返回称号。"""
    rate = score / total if total else 0
    if rate == 1:
        return "Python 满分闯关王 🏆"
    if rate >= 0.8:
        return "基础很稳的同学 💪"
    if rate >= 0.6:
        return "正在升级的循环高手 🔁"
    return "需要再复习一轮的 Python 萌新 🌱"


def start_new_quiz(level, count):
    """生成一套新题；quiz_id +1 让单选框的 key 变化，自动清掉上一轮的选择。"""
    st.session_state.quiz = build_quiz(level, count)
    st.session_state.current_level = level
    st.session_state.current_count = count
    st.session_state.submitted = False
    st.session_state.quiz_id += 1


# ----------------------- 初始化会话状态 -----------------------
if "quiz_id" not in st.session_state:
    st.session_state.quiz_id = 0
if "current_level" not in st.session_state:
    st.session_state.current_level = "简单"
if "current_count" not in st.session_state:
    st.session_state.current_count = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "quiz" not in st.session_state:
    st.session_state.quiz = []


st.title("🐍 Python 期末复习闯关")
st.caption("题目取材自本课程的实验、随堂与课后作业。选难度 → 答题 → 自动评分 + 解析 + 知识点得分。")

with st.sidebar:
    st.header("闯关设置")
    level = st.radio("选择难度", ["简单", "普通", "挑战"], horizontal=True)
    pool_size = len(candidates_for(level))
    num = st.slider(
        "本次题量",
        min_value=1,
        max_value=pool_size,
        value=min(LEVEL_SIZE[level], pool_size),
        key=f"num_{level}",
        help="拖动调节这一次要复习多少题；上限就是该难度题库的全部题量。",
    )
    st.caption(f"{level}模式题库共 {pool_size} 题，本次抽 {num} 题")
    st.write("知识点：变量、运算符、字符串、列表/字典/集合、循环、函数、递归、二维列表、排序、文件异常")
    if st.button("🔄 重新抽题", use_container_width=True):
        start_new_quiz(level, num)

# 切换难度或调节题量，就自动换一套题
if st.session_state.current_level != level or st.session_state.current_count != num:
    start_new_quiz(level, num)
# 首次进入、或被重置后还没有题，则生成一套
if not st.session_state.quiz:
    start_new_quiz(level, num)

st.subheader(f"{level}模式：共 {len(st.session_state.quiz)} 题")

qid = st.session_state.quiz_id
with st.form("quiz_form"):
    for index, item in enumerate(st.session_state.quiz, start=1):
        st.markdown(f"**第 {index} 题　[{item['topic']}]**")
        st.write(item["question"])
        if item.get("code"):                 # 代码填空题：展示带 ____ 的代码块
            st.code(item["code"], language="python")
        st.radio(
            "选择答案",
            item["options"],
            index=None,                  # 默认不选，必须自己作答
            key=f"q_{qid}_{index}",       # key 含 quiz_id，换题后自动失效，不会串选项
            label_visibility="collapsed",
        )
        st.divider()
    submitted = st.form_submit_button("提交答案", use_container_width=True)

if submitted:
    st.session_state.submitted = True

if st.session_state.submitted:
    score = 0
    unanswered = 0
    topic_total = {}
    topic_right = {}

    for index, item in enumerate(st.session_state.quiz, start=1):
        user_answer = st.session_state.get(f"q_{qid}_{index}")
        if user_answer is None:
            unanswered += 1
        is_right = user_answer == item["answer"]
        score += int(is_right)
        topic_total[item["topic"]] = topic_total.get(item["topic"], 0) + 1
        topic_right[item["topic"]] = topic_right.get(item["topic"], 0) + int(is_right)

    total = len(st.session_state.quiz)
    if unanswered:
        st.warning(f"有 {unanswered} 题没作答，已按答错计算。")
    st.success(f"得分：{score} / {total}　称号：{get_title(score, total)}")
    st.progress(score / total)

    st.subheader("每题解析")
    for index, item in enumerate(st.session_state.quiz, start=1):
        user_answer = st.session_state.get(f"q_{qid}_{index}")
        is_right = user_answer == item["answer"]
        status = "✅ 答对" if is_right else "❌ 答错"
        with st.expander(f"第 {index} 题：{status}"):
            st.write(f"你的答案：{user_answer if user_answer is not None else '未作答'}")
            st.write(f"正确答案：{item['answer']}")
            st.info(item["explain"])

    st.subheader("知识点得分率（%）")
    chart_data = {
        topic: round(topic_right[topic] / topic_total[topic] * 100, 1)
        for topic in topic_total
    }
    st.bar_chart(chart_data)

    missed = [t for t in topic_total if topic_right[t] < topic_total[t]]
    if missed:
        st.warning("建议重点复习：" + "、".join(missed))
    else:
        st.balloons()
