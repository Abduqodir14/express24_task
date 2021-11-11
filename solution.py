import unittest


def addTwoNumbers(l1, l2):
    Rhead1 = reverseLL(l1)  # 3 -> 4 -> 2
    Rhead2 = reverseLL(l2)  # 4 -> 6 -> 5

    node1 = Rhead1
    node2 = Rhead2
    carry = 0
    newLL = None
    temp = None

    while node1 and node2:
        arith = node1.data + node2.data + carry

        carry = 0
        if arith >= 10:
            carry, arith = divmod(arith, 10)

        if newLL:
            temp.next = Node(arith)
            temp = temp.next
        else:
            newLL = Node(arith)
            temp = newLL

        node1, node2 = node1.next, node2.next

    return newLL


def reverseLL(head):
    prev = None
    node = head

    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next

    return prev


class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += " -> " + str(self.next)
        return string


class Test(unittest.TestCase):
    def test_addTwoNumbers(self):
        head1 = Node(2, Node(4, Node(3, None)))  # (2 -> 4 -> 3)
        head2 = Node(5, Node(6, Node(4, None)))  # (5 -> 6 -> 4)
        expected = Node(7, Node(0, Node(8, None)))  # (7 -> 0 -> 8)
        print("actual:", str(addTwoNumbers(head1, head2)))
        print("expected:", str(expected))


if __name__ == "__main__":
    unittest.main()
