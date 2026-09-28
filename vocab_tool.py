# vocab_tool.py

import csv
import random
import os
import sys

# 解决路径问题
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import weekpath


def load_vocab(csv_path):
    """读取 CSV 文件，返回列表"""
    vocab_list = []
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_row = {}
            for key, value in row.items():
                if key is None:
                    continue
                cleaned_row[key.strip()] = value.strip() if isinstance(value, str) else value
            vocab_list.append(cleaned_row)
    return vocab_list


def make_question(correct_word, all_vocab):
    """生成一道选择题的数据"""
    # 【关键修改】这里的 "词语" 改成了你 CSV 里真正的列名 "词汇"
    answer = correct_word.get("词汇", "未知") 
    
    candidates = []
    for w in all_vocab:
        word = w.get("词汇") # 这里也要改
        if word and word != answer:
            candidates.append(word)

    # 去重
    candidates = list(set(candidates))

    # 如果词太少，补充几个常见的
    if len(candidates) < 3:
        candidates.extend(["苹果", "香蕉", "橘子"])
    
    # 随机抽 3 个干扰项
    distractors = random.sample(candidates, 3)

    options = [answer] + distractors
    random.shuffle(options)

    return {
        "answer": answer,
        "options": options
    }


def build_exercise_text(questions):
    """把题目格式化成文本"""
    lines = []
    lines.append("一、选词填空：请从 A、B、C、D 中选出最合适的词语。\n")

    for index, q in enumerate(questions, start=1):
        options = q["options"]
        option_labels = ["A", "B", "C", "D"]
        option_parts = []
        for label, word in zip(option_labels, options):
            option_parts.append(f"{label}. {word}")

        options_line = "  ".join(option_parts)
        lines.append(f"{index}. 选词填空：他是个（  ）。")
        lines.append(f"   {options_line}")
        lines.append("") 

    return "\n".join(lines)


def main():
    csv_path = weekpath.data_path("生词表.csv")
    output_path = os.path.join(weekpath.root_path(), "练习.txt")

    vocab_list = load_vocab(csv_path)
    print(f"共读取到 {len(vocab_list)} 个词条。")

    # 不加等级限制了，直接随机抽 5 个词
    sample_size = min(5, len(vocab_list))
    if sample_size == 0:
        print("错误：生词表是空的！")
        return
        
    selected_words = random.sample(vocab_list, sample_size)

    questions = []
    for word in selected_words:
        q = make_question(word, vocab_list)
        if q is not None:
            questions.append(q)

    if not questions:
        print("错误：生词表里的词太少，无法生成干扰项。")
        return

    exercise_text = build_exercise_text(questions)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(exercise_text)

    print(f"\n成功！练习题已生成到：{output_path}")
    print("\n练习题内容预览：\n")
    print(exercise_text)


if __name__ == "__main__":
    main()
