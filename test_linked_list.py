import unittest

from linked_list import LinkedList, linked_list_helper


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def tearDown(self) -> None:
        self.linked_list.head = None

    def test_linked_list_push(self):
        """
        Test that it can add nodes to a linked list
        :return: void
        """
        data = "Z"
        self.linked_list.push(data)
        node_data = self.linked_list.head.data
        self.assertEqual(node_data, data)

    def test_linked_list_helper(self):
        """
        Test that it can delete elements that appear
        more than twice in a linked list
        :return: void
        """
        data = ['E', 'B', 'E', 'E', 'B', 'A', 'B']
        data_lifo = data[::-1]
        expected = ['E', 'B', 'E', 'B', 'A']
        for i in data_lifo:
            self.linked_list.push(i)

        linked_list_helper(self.linked_list.head)
        result = self.linked_list.make_list()
        self.assertEqual(result, expected)

    def test_linked_list_helper_with_two_letters(self):
        """
        Test that it can delete elements that appear
        more than twice in a linked list with two letters
        :return: void
        """
        data = ['E', 'B']
        data_lifo = data[::-1]
        expected = ['E', 'B']
        for i in data_lifo:
            self.linked_list.push(i)

        linked_list_helper(self.linked_list.head)
        result = self.linked_list.make_list()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
