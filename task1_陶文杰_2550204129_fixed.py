import re
import os
from collections import Counter

def count_words(file_path):
    """
    统计文本文件中每个单词的出现次数

    参数:
        file_path (str): 文本文件的路径

    返回值:
        dict: 单词（小写）作为键，出现次数作为值的字典，按频次降序排列
        如果文件不存在，返回空字典并提示
    """

    # 1. 检查文件是否存在
    # 首先使用os.path.exists检查文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，打印提示信息并返回空字典
        print(f"错误：文件 '{file_path}' 不存在")
        return {}

    try:
        # 2. 打开文件并读取内容
        # 使用with语句自动管理文件资源，避免忘记关闭文件
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取整个文件内容
            content = file.read()

        # 3. 预处理文本内容
        # 将所有字母转为小写，方便统计（不区分大小写）
        content_lower = content.lower()

        # 4. 使用正则表达式提取单词
        # \w+ 匹配一个或多个字母、数字或下划线
        # 这个正则表达式会忽略标点符号和空白字符
        words = re.findall(r'\b\w+\b', content_lower)

        # 5. 使用Counter统计单词频次
        # Counter是collections模块中的工具类，专门用于计数
        word_counter = Counter(words)

        # 6. 按频次降序排列
        # 使用most_common()方法获取按频次降序排列的列表
        # 然后转换为字典
        sorted_words = dict(word_counter.most_common())

        # 7. 返回结果
        return sorted_words

    except FileNotFoundError:
        # 双重检查：虽然已经检查过文件存在，但这里处理打开文件时可能出现的异常
        print(f"错误：无法打开文件 '{file_path}'")
        return {}
    except UnicodeDecodeError:
        # 处理编码问题：如果文件不是UTF-8编码
        print(f"错误：文件 '{file_path}' 编码不是UTF-8")
        return {}
    except Exception as e:
        # 处理其他可能的异常
        print(f"处理文件时发生错误: {e}")
        return {}


# 测试代码
if __name__ == "__main__":
    # 测试用例1：使用我们刚才创建的sample.txt文件
    result = count_words("sample.txt")
    print("sample.txt中的单词统计:")
    for word, count in result.items():
        print(f"  '{word}': {count}次")

    print()

    # 测试用例2：不存在的文件
    result2 = count_words("nonexistent.txt")
    print("不存在的文件测试结果:", result2)
"