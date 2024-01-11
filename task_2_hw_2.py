from collections import deque


def is_palindrome(input_str):
    # Видалити пробіли та зробити регістр нечутливим
    input_str = input_str.replace(" ", "").lower()

    char_queue = deque()

    # Додати символи до двосторонньої черги
    for char in input_str:
        char_queue.append(char)

    # Порівняти символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


# Приклад використання
user_input = input("Введіть рядок для перевірки на паліндром: ")
if is_palindrome(user_input):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")
