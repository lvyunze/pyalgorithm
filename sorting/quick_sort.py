"""
快速排序
"""
import inspect


def sort(_list: list) -> list:
    """
    快速排序
    :param _list:整数列表
    :return: 排序后的列表
    """
    if len(_list) <= 1:
        return list(_list)
    pivot = _list[len(_list) // 2]
    left = [x for x in _list if x < pivot]
    middle = [x for x in _list if x == pivot]
    right = [x for x in _list if x > pivot]
    return sort(left) + middle + sort(right)


# 返回时间复杂度
def time_complexities() -> str:
    return '''最好: O(nlogn), 平均: O(nlogn), 最差: O(n ^ 2)'''


# 获取源代码
def get_code() -> str:
    """
    获取排序源码
    """
    return inspect.getsource(sort)