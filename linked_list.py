
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def make_list(self):
        """
        Goes through the linked list and pushes the node values
        into one list in the order they are structured within
        the linked list
        :return: list
        """
        temp = self.head
        temp_list = []
        while temp:
            temp_list.append(temp.data)
            temp = temp.next
        return temp_list


def linked_list_helper(head):

    temp_list = [head.data]

    if head is None:
        return

    while head.next is not None:
        if temp_list.count(head.next.data) < 2:
            temp_list.append(head.next.data)
            head = head.next
        else:
            head.next = head.next.next


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.push('B')
    l_list.push('A')
    l_list.push('B')
    l_list.push('E')
    l_list.push('E')
    l_list.push('B')
    l_list.push('E')

    print('\nInput\n-------')
    print(l_list.make_list())

    linked_list_helper(l_list.head)

    print('\nOutput\n-------')
    print(l_list.make_list())
