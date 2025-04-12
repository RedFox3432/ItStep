import requests as r
from bs4 import BeautifulSoup as bs

class MinFin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
        else:
            print('Не вдалося підключитися до сайту')

    def getInfo(self):
        valute = []
        valuteTag = self.soup.find_all('tr', class_='sc-1x32wa2-4 dKDsVV')[:5]
        if not valuteTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return valute

        for i in valuteTag:
            nameValute = i.find('a', class_='sc-1x32wa2-7 ciClTw')
            name = nameValute.text.strip() if nameValute else 'Назва валюти відсутня'
            Valute = i.find_all('td')
            if len(Valute) > 2:
                buyValute = Valute[1]
                buy = buyValute.text.strip().replace(',', '.') if buyValute else 'Курс купівлі відсутній'
                sellValute = Valute[2]
                sell = sellValute.text.strip().replace(',', '.') if sellValute else 'Курс продажі відсутній'

                valute.append({
                    'Назва': name,
                    'Купівля': buy,
                    'Продаж': sell
                })
        return valute

    def showInfo(self, txt):
        print('\033[32m№\tНазва\t\tКупівля\t\tПродаж')
        print('-' * 60 + '\033[0m')
        for num, item in enumerate(txt, 1):
            print(f"{num}\t{item['Назва']:<10}\t{item['Купівля']:<10}\t{item['Продаж']}")

url = "https://minfin.com.ua/ua/currency/"
obj = MinFin(url)
obj.auditSite()
txt = obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')
