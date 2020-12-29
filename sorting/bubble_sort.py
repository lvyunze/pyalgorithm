"""
冒泡排序
"""
import inspect


def sort(_list: list) -> list:
    """
    :param _list: 需要排序的列表
    :return: 排序后的列表
    """
    for i in range(len(_list)):
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
    return _list


def improved_sort(_list: list) -> list:
    """
    改进的冒泡排序
    :param _list: 需要排序的列表
    :return: 排序后的列表
    """
    for i in range(len(_list)):
        stop = True
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                stop = False
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
        if stop:
            return _list
    return _list


def time_complexities() -> str:
    return "最好: O(n), " \
           "平均: O(n ^ 2), " \
           "最差: O(n ^ 2).\n\n" \
           "对于改进的冒泡排序算法:\n最佳: O(n); 平均: O(n * (n - 1) / 4); 最差: O(n ^ 2)"


# 获取源代码
def get_code():
    """
    获取排序源码
    """
    return inspect.getsource(sort)
