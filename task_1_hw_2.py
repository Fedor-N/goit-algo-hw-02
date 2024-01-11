import queue
# Створити чергу заявок
request_queue = queue.Queue()
# Функція для генерації нових заявок


def generate_request():
    new_request = f"Request-{request_queue.qsize() + 1}"
    request_queue.put(new_request)
    print(f"Згенеровано новий запит: {new_request}")
# Функція для обробки заявок


def process_request():
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"Обробка запиту: {processed_request}")
    else:
        print("Черга порожня. Немає запитів для обробки.")


# Головний цикл програми
while True:
    user_input = input(
        "Натисніть «g», щоб створити запит, «p», щоб обробити запит, або «q», щоб вийти: ")

    if user_input == 'g':
        generate_request()
    elif user_input == 'p':
        process_request()
    elif user_input == 'q':
        print("Вихід з програми. До побачення!")
        break
    else:
        print("Неправильні дані. Введіть «g», «p» або «q».")
