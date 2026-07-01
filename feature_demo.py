def calculate_average(numbers):
    """
    计算列表的平均值

    参数:
        numbers: 数字列表

    返回值:
        平均值（浮点数）
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 测试代码
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]
    result = calculate_average(test_list)
    print(f"列表 {test_list} 的平均值为: {result}")