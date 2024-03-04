class LinkedList:
    """"Realisation single-linked list"""
    head = None
    length = 0
    isLoop = False

    class Node:
        def __init__(self, data, next_node=None):
            """"Realisation node element"""
            self.data = data
            self.next_node = next_node

    def __init__(self, data):
        self.length = len(data)
        if len(data) == 1:
            self.head = self.Node(data[0])

        else:
            self.head = self.Node(data[0])
            node = self.head

            for i in range(1, len(data)):
                node.next_node = self.Node(data[i])
                node = node.next_node

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            self.length += 1
            return data

        node = self.head

        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(data)
        self.length += 1
        return data

    def __str__(self):
        line = "["
        node = self.head
        if self.isLoop:
            line = "The linked list with loop.\n["
            i = 0

            while i < self.length-1:
                line += str(node.data) + ', '
                node = node.next_node
                i += 1
            line += str(node.data) + ']'
            return line

        while node.next_node:
            line += str(node.data) + ', '
            node = node.next_node

        line += str(node.data) + ']'
        return line

    def __getitem__(self, index):
        i = 0
        node = self.head

        while i < index:
            i += 1
            node = node.next_node

        return node.data

#    def __setitem__(self, data, index):
#    """Method that change item by index""""
#        i = 0
#        node = self.head
#
#        while i < index:
#            i += 1
#            node = node.next_node
#
#        node.data = data

    def insert(self, data, index):
        i = 0
        node = self.head
        prev_node = None
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        self.length += 1
        prev_node.next_node = self.Node(data, node)

    def remove(self, index):
        i = 0
        node = self.head
        prev_node = None
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        self.length -= 1
        prev_node.next_node = node.next_node.next_node

    def loop(self, index):
        """Create a loop (for last element)"""
        self.isLoop = True
        node = self.head
        link = self.head
        j = 0
        while node.next_node:
            if j == index:
                link = node
            node = node.next_node
            j += 1

        if j == index:
            link = node
        node.next_node = link

    def find_start_of_loop(self):
        slow = self.head.next_node
        fast = self.head.next_node.next_node
        while slow != fast:
            slow = slow.next_node
            fast = fast.next_node.next_node

        slow = self.head

        i = 0
        while slow != fast:
            slow = slow.next_node
            fast = fast.next_node
            i += 1

        return slow.data, i
