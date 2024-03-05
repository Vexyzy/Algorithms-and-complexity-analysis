from LinkedList import LinkedList

a = LinkedList()
b = LinkedList()

a.append(1)
a.append(2)
a.append(3)

a.random(0, 2)
a.random(1, 0)
a.random(2, 1)

b.head = a.copy()


print(a)
print(b)
print(a == b)
print(a[0].random == a[2])
print(b[2].random == b[1])




