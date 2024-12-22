from LxmlSoup import LxmlSoup
import requests
import schedule
import time

# Глобальные переменные для второго парсера
condition = ''
temperatura = ''
wind = ''
wni = ''
vosxod = ''
zaxod = ''
vlazhn = ''
davlenie = ''

img_open = 'https://ski-gv.ru/resources/images/icons/enabled.svg'
img_closed = 'https://ski-gv.ru/resources/images/icons/icon/close-trass.svg'


def update_weather_data_2():
    global condition, temperatura, wind, wni, vosxod, zaxod, vlazhn, davlenie

    html = requests.get('https://ski-gv.ru/weather/0/').text  # получаем html код сайта
    soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

    links = soup.find_all('div', class_='weather-data')
    for i, link in enumerate(links):
        condition = soup.find_all("span", class_="weather-condition")[i].text()
        temperatura = soup.find_all("p", class_="weather-card__temp temp")[i].text()[0:-4]
        veter = links[1].text().split()[3:]
        wind = ' '.join(veter)
        break

    icons = soup.find_all('div', class_='weather-card weather-card_type_full weather__current-part mobile-hidden')
    for i, link in enumerate(icons):
        weather_now_icon = soup.find_all("img", class_="weather-card__icon icon")[i]
        wni = weather_now_icon.get("src")
        break

    params = soup.find_all('ul', class_='weather-card__params params')
    for i, link in enumerate(params):
        norm_params = params[i].text()
        vosxod = norm_params.split()[0][6:]
        zaxod = norm_params.split()[1][5:]
        vlazhn = norm_params.split()[2][9:]
        davlenie = norm_params.split()[3][8:]
        break

update_weather_data_2()

# Регистрация задачи обновления данных каждые 1 час
schedule.every(1).hour.do(update_weather_data_2)

if __name__ == '__main__':
    update_weather_data_2()
    while True:
        schedule.run_pending()
        time.sleep(1)
