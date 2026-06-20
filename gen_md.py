"""从 app.py 的 QUESTION_BANK 自动生成「题库.md」（题库查阅版）。

用法：python gen_md.py
说明：用 ast 静态解析 app.py，不会启动 Streamlit；改题只需改 app.py 再重跑本脚本。
"""
import ast

LETTERS = ["A", "B", "C", "D", "E", "F"]
LEVEL_ORDER = ["简单", "普通", "挑战"]
LEVEL_TITLE = {"简单": "简单模式", "普通": "普通模式", "挑战": "挑战模式"}


def load_bank(path="app.py"):
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            getattr(t, "id", None) == "QUESTION_BANK" for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise RuntimeError("未在 app.py 中找到 QUESTION_BANK")


def main():
    bank = load_bank()
    total = len(bank)
    by_level = {lv: [q for q in bank if q["level"] == lv] for lv in LEVEL_ORDER}
    n_member5 = sum(1 for q in bank if q.get("author") == "组员5")
    counts = " + ".join(f"{LEVEL_TITLE[lv]} {len(by_level[lv])} 题" for lv in LEVEL_ORDER)

    lines = []
    lines.append("# Python 期末复习闯关题库\n")
    lines.append(
        "> 本文件由 `gen_md.py` 从 `app.py` 的题库**自动生成**，仅供查阅。"
        "改题请改 `app.py`，再重跑 `python gen_md.py`。\n"
    )
    lines.append(f"> 标 **〔组员5 制作〕** 的为组员5新增题（共 {n_member5} 道）。\n")
    lines.append(
        "题型：概念选择题 + 代码输出题 + 代码填空 + 代码阅读。"
        "取材自本课程实验/作业、《期末复习重点》(谭德健)，并整合了「普通模式题库」"
        "「Python入门60道」「扩充完整版」等题库 docx。"
        f"全库共 {total} 题（{counts}）。\n"
    )

    number = 0
    for lv in LEVEL_ORDER:
        lines.append(f"## {LEVEL_TITLE[lv]}\n")
        for q in by_level[lv]:
            number += 1
            tag = "　〔组员5 制作〕" if q.get("author") == "组员5" else ""
            lines.append(f"### {number}. {q['topic']}{tag}\n")
            lines.append(f"题目：{q['question']}\n")
            if q.get("code"):
                lines.append("```python")
                lines.append(q["code"])
                lines.append("```\n")
            for i, opt in enumerate(q["options"]):
                lines.append(f"- {LETTERS[i]}. {opt}")
            lines.append("")
            letter = LETTERS[q["options"].index(q["answer"])]
            lines.append(f"答案：{letter}\n")
            lines.append(f"解析：{q['explain']}\n")

    open("题库.md", "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
    print(f"题库.md 已生成：{total} 题（{counts}），组员5 题 {n_member5} 道。")


if __name__ == "__main__":
    main()
