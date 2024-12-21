from LxmlSoup import LxmlSoup
import requests
import schedule
import time

# Глобальные переменные
acondition = ''
atemperatura = ''
awind = ''
awni = ''
avosxod = ''
azaxod = ''
avlazhn = ''
adavlenie = ''


def update_weather_data():
    global acondition, atemperatura, awind, avni, avosxod, azaxod, avlazhn, adavlenie

    html = requests.get('https://ski-gv.ru/weather/1/').text  # получаем html код сайта
    soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

    links = soup.find_all('div', class_='weather-data')
    for i, link in enumerate(links):
        acondition = soup.find_all("span", class_="weather-condition")[i].text()
        atemperatura = soup.find_all("p", class_="weather-card__temp temp")[i].text()[0:3]
        veter = links[1].text().split()[3:]
        awind = ' '.join(veter)
        break

    icons = soup.find_all('div', class_='weather-card weather-card_type_full weather__current-part mobile-hidden')
    for i, link in enumerate(icons):
        weather_now_icon = soup.find_all("img", class_="weather-card__icon icon")[i]
        awni = weather_now_icon.get("src")
        break

    params = soup.find_all('ul', class_='weather-card__params params')
    for i, link in enumerate(params):
        norm_params = params[i].text()
        avosxod = norm_params.split()[0][6:]
        azaxod = norm_params.split()[1][5:]
        avlazhn = norm_params.split()[2][9:]
        adavlenie = norm_params.split()[3][8:]
        break


# Регистрация задачи обновления данных каждые 1 час
schedule.every(1).hour.do(update_weather_data)

if __name__ == '__main__':
    update_weather_data()
    while True:
        schedule.run_pending()
        time.sleep(1)
