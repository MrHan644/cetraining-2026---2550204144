from typing import Dict

def count_words(file_path: str) -> Dict[str, int]:
    """
    统计文本文件中每个英文单词出现次数
    :param file_path: 文本文件路径
    :return: 字典 {单词: 出现次数}
    """
    word_count = {}
    # 打开文件读取内容，统一小写避免区分 Hello/hello
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().lower()
    # 按空白分割所有单词
    word_list = content.split()
    for word in word_list:
        # 去除单词两侧标点符号
        clean_word = word.strip(".,!?\"'()[]")
        if clean_word:  # 排除空字符串
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1
    return word_count


# 程序入口，命令行传文件路径运行
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("用法: python word_count.py <文件路径>")
        else:
        res = count_words(sys.argv[1])
        # 循环打印每个单词和次数
        for word, count in res.items():
            print(f"{word}: {count}")