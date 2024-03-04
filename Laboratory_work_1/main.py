from LinkedList import LinkedList

# make linkedList
a = LinkedList([2, 3, 2, 3, 3, 5, 3, 4, 2, 3])
a.loop(4)

if a.isLoop:
    print(f"Значение начального узела петли: {a.find_start_of_loop()[0]}"
          f"\nИндекс начального узела петли: {a.find_start_of_loop()[1]}")
else:
    print("В списке нету петли")
