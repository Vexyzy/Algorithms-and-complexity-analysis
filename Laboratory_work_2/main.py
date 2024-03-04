from LinkedList import LinkedList

a = LinkedList()

a.append(5)
a.append(6)
a.append(7)

b = LinkedList()

node = a.head

b.append(a.head.data)
while node.next:
    b.append(node.next.data)
    node = node.next

print(b)
