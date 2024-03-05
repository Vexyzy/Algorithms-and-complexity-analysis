class LinkedList:

    head = None
    length= 0

    class Node:

        def __init__(self, data, next=None, previous=None, random=None ):
            self.data = data
            self.next = next
            self.random = random

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            self.length += 1
            return data

        node = self.head

        while node.next:
            node = node.next

        node.next = self.Node(data, previous=node)
        self.length += 1

    def copy(self):
        """Первой проходкой метод коппирует элементы списка (data) и вставляет
        между изначальными элементами скопированные. Т.е получается вместо массива 1 -> 2 -> 3
        получается 1 -> 1 -> 2 -> 2 -> 3 -> 3. Второй проходкой метод расставляет "рандом"
        ссылки для всех нечетных (отсчет с 0) элементов нового списка, опираясь на "рандом"
        ссылки четных(отсчет с 0) элеменотов, т.е. если 1[0] -> 3[4], то 1[1] -> 3[5], как видим,
        "рандом" сылки для новых элементов стоят на +1 по индексу "рандом" ссылок изначальных
        элементов. Третей проходной метод разъеденяет копированные элемента от исходных, нечетные
        отправляются в переменную head_copy и в исходном меняются ссылки на последующий элемент,
        путем удаления следующей ссылки, т.е 1 -> 1 -> 2 ... будет ввести 1 -> 2..., а скопированный
        список будет выглядеть 1 -> ...

        (1) 3 цикла => O(3*n) = O(n)
        (2) 20 команд => O(20*1) = O(20) = O(1)

        Из (1) и (2) => O(n) + O(1) = O(n+1) = O(n)
        """

        if not self.head:
            return None

        node = self.head
        while node:
            node_copy = self.Node(node.data)
            node_copy.next = node.next
            node.next = node_copy
            node = node_copy.next

        node = self.head
        while node:
            node.next.random = node.random.next
            node = node.next.next

        node = self.head
        head_copy = self.Node(node.next.data, random=node.next.random)
        node_copy = head_copy
        while node:
            if not node.next.next:
                node.next = None
                break;
            node.next = node.next.next
            node_copy.next = node.next.next
            node_copy.next.random = node_copy
            node = node.next
            node_copy = node_copy.next

        return head_copy

    def random(self, index, random_position):
        if not self.head:
            return None

        node = self.head
        i = 0
        while i < random_position:
            node = node.next
            i += 1

        random_position = node
        i = 0
        node = self.head
        while i < index:
            node = node.next
            i += 1

        node.random = random_position

    def __str__(self):
        if not self.head:
            return "[]"

        node = self.head
        line = '['

        while node.next:
            line += str(node.data) + ', '
            node = node.next

        line += str(node.data) + ']'
        return line
    def __getitem__(self, index):
        if not self.head:
            return "[]"
        i = 0
        node = self.head
        while i < index:
            node = node.next
            i += 1
        return node
    def reverse(self):

        node = self.head
        line = '['

        while node.next:
            node = node.next

        while node.prev:
            line += str(node.data) + ', '
            node = node.prev

        line += str(node.data) + ']'
        return line
