import schedule
import random
import time


webcams = ('Средняя станция г. Большевик', 'Вершина г. Большевик', 'Входная группа г. Большевик',
           'Вершина г. Большевик 2', 'Долина туристов')


event_location = random.choice(webcams)
reward = random.choice(range(500, 1001, 50))  # Рандомное вознаграждение от 500 до 1000, кратное 50
notification = f"Новое событие! Отправляйтесь к камере: {event_location} и запишите видео в наш чат!\nВознаграждение первому кто запишет видео: {reward} рублей на карту ски-пасс"


# # Планирование запуска события через случайные интервалы
# def schedule_random_event():
#     delay = random.randint(1800, 3600)  # Устанавливаем задержку в секундах (например, от 10 до 60 секунд)
#     time.sleep(delay)
#     event()
#     schedule_random_event()  # Рекурсивно вызываем функцию для бесконечного цикла


# Запуск
# schedule_random_event()
