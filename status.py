import schedule
from LxmlSoup import LxmlSoup
import requests
import time

# URL страницы
url = "https://ski-gv.ru/hills/1/1/"

# Получаем HTML страницы
response = requests.get(url)
if response.status_code == 200:
    html = response.text
else:
    print("Не удалось получить данные с сайта")
    exit()
# Создаем экземпляр LxmlSoup
soup = LxmlSoup(html)


status_lw = ''

hill_blocks = [block for block in soup.find_all("div") if
               "scheme-select__option track-option option" in block.get("class", "")]
if hill_blocks:
    # Берем первый блок с трассой
    hill_block = hill_blocks[0]
    # Статус трассы
    track_status_elem = next((p for p in hill_block.find_all("p") if "track-status" in p.get("class", "")), None)
    if track_status_elem:
        status_text = track_status_elem.text().strip() if callable(
            track_status_elem.text) else track_status_elem.text.strip()
        status_class = track_status_elem.get("class", "")
        if "track-status_opened" in status_class:
            status_lw = "открыта"
        elif "track-status_closed" in status_class:
            status_lw = f"закрыта: {status_text}"
        else:
            status_lw = f"Неизвестно: {status_text}"
    else:
        status_lw = "Статус не найден"



# Регистрация задачи обновления данных каждые 1 час
# schedule.every(1).hour.do(status())

# if __name__ == '__main__':
#     status()
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
