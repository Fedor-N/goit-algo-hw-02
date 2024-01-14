import queue
import threading
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок


def generate_request():
    while not exit_flag:
        new_request = f"Request-{request_queue.qsize() + 1}"
        request_queue.put(new_request)
        print(f"New request generated: {new_request}")
        time.sleep(2)  # Затримка для емуляції інтервалу між заявками

# Функція для обробки заявок


def process_request():
    while not exit_flag:
        if not request_queue.empty():
            processed_request = request_queue.get()
            print(f"Processing request: {processed_request}")
            time.sleep(1)  # Затримка для емуляції часу обробки заявки
        else:
            print("Queue is empty. No requests to process.")
            time.sleep(2)  # Затримка для уникнення постійного опитування черги


# Головний цикл програми
exit_flag = False
try:
    # Запуск потоків для генерації та обробки заявок
    generate_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)

    generate_thread.start()
    process_thread.start()

    # Очікуємо завершення виконання
    generate_thread.join()
    process_thread.join()

except KeyboardInterrupt:
    print("Exiting the program. Goodbye!")
    exit_flag = True  # Встановлюємо флаг вихідного сигналу для завершення потоків
