import os
import random

from stack import Stack


def first_task(array_of_brackets: str) -> bool:
    """
    Реализация с помощью стека
    :param array_of_brackets:
    :return:
    """
    if len(array_of_brackets) == 1:
        return False

    stack = []

    for bracket in array_of_brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if stack:
                stack.pop(0)
            else:
                return False

    return True if len(stack) == 0 else False


def first_task_better(array_of_brackets: str) -> bool:
    """Похожая реализация, но через словарь"""

    stack = []

    for bracket in array_of_brackets:
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if bracket == ')':
                if stack.pop() != '(':
                    return False
            elif bracket == ']':
                if stack.pop() != '[':
                    return False
            elif bracket == '}':
                if stack.pop() != '{':
                    return False

    return True



def second_task():
    stack = Stack()
    stack.push(1)
    stack.push(0)
    stack.push(-1)
    stack.push(2)
    stack.push(3)
    stack.push(5)

    print("Проходка 1", stack)
    print(stack.get_min())

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    print("Проходка 2", stack)
    print(stack.get_min())

    stack.pop()

    print("Проходка 3", stack)
    print(stack.get_min())

    stack.pop()

    print("Проходка 4", stack)
    print(stack.get_min())


def third_task(array_len: int, window_size: int) -> list:
    array = [random.randint(0, 10) for _ in range(array_len)]
    counter = 0
    max_value = 0
    max_values = []
    i = 0

    while i < array_len:
        if counter == window_size:
            i -= (window_size - 1)
            max_values.append(max_value)
            max_value = array[i]
            counter = 1
            i += 1
        else:
            max_value = max(max_value, array[i])
            counter += 1
            i += 1

    max_values.append(max_value)

    print(array)
    return max_values


def fourth_task(array_len: int) -> set:
    array = [random.randint(1, array_len - 1) for _ in range(array_len)]
    print(array)
    duplicates = set()

    for numbers in array:
        index = abs(numbers) % array_len
        if array[index] < 0:
            duplicates.add(abs(numbers))
        else:
            array[index] *= -1

    return duplicates


def fifth_task(matrix: list):
    rows_with_zero = set()
    columns_with_zero = set()

    for row in range(0, len(matrix)):
        for columns in range(0, len(matrix[row])):
            if matrix[row][columns] == 0:
                rows_with_zero.add(row)
                columns_with_zero.add(columns)

    for element in rows_with_zero:
        for columns in range(0, len(matrix[element])):
            matrix[element][columns] = 0

    for i in range(0, len(matrix)):
        for element in columns_with_zero:
            if len(matrix[i]) > element:
                matrix[i][element] = 0



if __name__ == '__main__':
    # print("Задание 1 а")
    # first_str = "((()))"
    # second_str = "((())))"
    # print(first_str, first_task(first_str))
    # print(second_str, first_task(second_str))
    #
    input()
    print("Задание 1 б")
    first_str = "{{(())}}[{()}]"
    second_str = "({)}"
    print(first_str, first_task_better(first_str))
    print(second_str, first_task_better(second_str))

    # input()
    # print("Задание 2")
    # second_task()
    # input()
    # print("Задание 3")
    # print(third_task(7, 3))
    # input()
    # print("Задание 4")
    # print(fourth_task(6))
    input()
    array = [
        [1, 2, 3, 0, 5],
        [1, 2, 3],
        [1, 2, 0, 3],
        [1, 4, 5, 6, 7, 8, 9]
    ]
    print("Задание 5")
    fifth_task(array)
    for i in range(len(array)):
        print(f"{array[i]}")
