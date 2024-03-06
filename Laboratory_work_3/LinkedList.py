class LinkedList:

    head = None
    class Node:

        def __init__(self, data, prev=None, next=None):
            self.prev = prev
            self.next = next
            self.data = data

    def append(self, data):

        if not self.head:
            self.head = self.Node(data)
            return data

        node = self.head

        while node.next:
            node = node.next

        node.next = self.Node(data)
        node.next.prev = node

        return data

    def __str__(self):

        if not self.head:
            return '[]'

        line = '['
        node = self.head
        while node.next:
            line += str(node.data) + ', '
            node = node.next
        line += str(node.data) + ']'

        return line

    def reverse(self):
        """Print reverse linked list"""

        if not self.head:
            return []

        node = self.head
        while node.next:
            node = node.next

        line = '['

        while node.prev:
            line += str(node.data) + ', '
            node = node.prev

        line += str(node.data) + ']'

        return line

    def del_duplicate(self):
        """Deleate all dublicate elements"""

        if not self.head:
            return None

        node = self.head
        while node:
            node_sup = node
            while node_sup.next:
                if node.data == node_sup.next.data:
                    node_sup.next = node_sup.next.next
                    if node_sup.next:
                        node_sup.next.prev = node_sup
                else:
                    node_sup = node_sup.next
            node = node.next
        return node





