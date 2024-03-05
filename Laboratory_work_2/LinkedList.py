class LinkedList:

    head = None
    length= 0

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.prev = previous

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
        """Создаем словарь, проходим по списку, копируя каждый элемент. При первой 
        проходке мы создим односвязный список, который связан так:
        последний элемент -> элемент -> элемент -> первый элемент
        При второй проходке, мы с конца, для каждого элемента добавляем
        через метод next ссылку на последующий, тем самым у нас образуется
        начальный элемент, который уже ссылается на следующий, который в свою очередь
        на следующий и т.д., => образуется цепочка.
        Возвращаем первое значение, которое является связным списком.
        
        Сложность выполнения:
            (1) Первый перебор через while будет по n элементам => O(n)
            (2) Второй перебор через while будет по n элементам => O(n)
            
            (3) Так же у нас 14 строк => O(14*1) = O(1)
            
            из (1), (2), (3) => O(n) * O(n) + O(1) = O(2*n) + O(1) = O(n + 1) = O(n)
        """
        if not self.head:
            return None

        mapping = {}
        node = self.head
        node_copy = self.Node(node.data)
        mapping[node] = node_copy
        prev = node

        while node.next:
            node = node.next
            node_copy = self.Node(node.data, previous=prev)
            mapping[node] = node_copy
            prev = node

        while node.prev:
            node_copy = node
            node = node.prev
            mapping[node].next = mapping[node_copy]

        head_copy = mapping[node]

        return head_copy

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
