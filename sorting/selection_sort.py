"""
选择排序
"""
import inspect


def sort(_list: list) -> list:
    """
    :param _list: 整数排序列表
    :return: 排序后的列表
    """

    # For iterating n - 1 times
    for i in range(len(_list) - 1):
        minimum = i

        # Compare i and i + 1 element
        for j in range(i + 1, len(_list)):
            if _list[j] < _list[minimum]:
                minimum = j
        if minimum != i:
            _list[i], _list[minimum] = _list[minimum], _list[i]
    return _list


def time_complexities():
    return "最好: O(n ^ 2), 平均: O(n ^ 2), 最差: O(n ^ 2)"


# 获取源代码
def get_code():
    return inspect.getsource(sort)
