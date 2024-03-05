from LinkedList import LinkedList

a = LinkedList()
b = LinkedList()

a.append(1)
a.append(2)
a.append(3)

b.head = a.copy()

print(a)
print(b.reverse())
