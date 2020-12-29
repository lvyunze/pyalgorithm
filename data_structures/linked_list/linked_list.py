"""
单链表和双链表
"""
import inspect


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    # 链表查找
    def search(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        return self.search(node.next, data)

    # 获取数据
    def get_data(self):
        temp = self.head
        l_list = []
        while temp:
            l_list.append(temp.data)
            temp = temp.next
        return l_list

    # 在链表开头插入
    def insert_at_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # 结尾插入
    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    @staticmethod
    def get_code():
        return inspect.getsource(SinglyLinkedList)


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def get_data(self):
        temp = self.head
        l_list = []
        while temp:
            l_list.append(temp.data)
            temp = temp.next
        return l_list

    # 开头插入
    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    # 结尾插入
    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

    # 删除
    def delete(self, data):
        temp = self.head
        if temp.next is not None:
            # if head node is to be deleted
            if temp.data == data:
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while temp.next is not None:
                    if temp.data == data:
                        break
                    temp = temp.next
                if temp.next:
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return

        if temp is None:
            return

    @staticmethod
    def get_code():
        return inspect.getsource(DoublyLinkedList)


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        self.tail = None
        self.head = None

    def get_data(self):
        l_list = []
        current = self.tail
        while True:
            l_list.append(current.data)
            current = current.next
            if current == self.tail:
                break
        return l_list

    def insert(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    @staticmethod
    def get_code():
        return inspect.getsource(CircularLinkedList)


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)
    print(cll.get_data())
    print(cll.get_code())
