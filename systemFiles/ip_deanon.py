import socket
import threading
import requests
import ipaddress
from bs4 import BeautifulSoup


class IpInfo:
    def __init__(self):
        self.ip = input('\n [+] IP For Scan: ')

        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            raise ValueError('IP адресс введён неверно')

        self.output()

    def defaultInfo(self):
        r = requests.get(f'http://ip-api.com/json/{self.ip}').json()
        host = socket.getnameinfo((self.ip, 0), socket.NI_NAMEREQD)

        out = {
            'api': r,
            'host': host
        }

        return out

    def openPorts(self):
        openPortsList = []

        def scan_port(ip, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                sock.connect((ip, port))
                openPortsList.append(str(port))
                sock.close()
            except:
                pass

        for i in range(65535):
            thread_ = threading.Thread(target=scan_port, args=(self.ip, i))
            thread_.start()

        return openPortsList

    def csgo(self):
        url = f'https://www.gametracker.com/search/csgo/?query={self.ip}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.find_all('tr')

        texts = trs[1].find_all('a')
        text = texts[1].text
        result = text.strip()

        if result != "Teams":
            return result
        else:
            return "Не найдено"

    def minecraft(self):
        url = f'https://mc-servera.net/search?q={self.ip}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('a', class_='s-link')

        if len(quotes) == 0:
            return "Не найдено"
        elif len(quotes) == 1:
            return quotes.text
        elif len(quotes) > 1:
            return f"{quotes[0].text} и {len(quotes) - 1} других"

    def unturned(self):
        url = f'https://www.trackyserver.com/unturned-server/1?s={self.ip}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('h4', class_='no-margin')

        if len(quotes) == 0:
            return "Не найдено"
        elif len(quotes) == 1:
            return quotes.text
        elif len(quotes) > 1:
            return f"{quotes[0].text} и {len(quotes) - 1} других"

    def arma(self):
        url = f'https://www.gametracker.com/search/arma3/?query={self.ip}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.find_all('tr')

        texts = trs[1].find_all('a')
        text = texts[1].text
        result = text.strip()

        if result != "Teams":
            return result
        else:
            return "Не найдено"

    def output(self):

        def len_design():
            list = [len(self.csgo()), len(self.minecraft()),
                    len(self.unturned()), len(self.arma())]
            max_len = max(list)

            return 14 + max_len + 1

        default = self.defaultInfo()
        api = default['api']
        host = default['host']

        openPorts = self.openPorts()

        print(' ' + "="*len_design() + f'''
  IP adress:   {self.ip}
  Country:     {api["country"]}
  Region:      {api["region"]}\n  Region Name: {api["regionName"]}
  City:        {api["city"]}\n  Zip:         {api["zip"]}
  Latinude:    {api["lat"]}\n  Longitude:   {api["lon"]}
  Timezone:    {api["timezone"]}\n  ISP:         {api["isp"]}
  Org:         {api["org"]}\n  As:          {api["as"]}
  Host:        {host[0]}\n  Open ports:  {', '.join(openPorts)}
  Minecraft:   {self.minecraft()}\n  CS:GO:       {self.csgo()}
  Unturned:    {self.unturned()}\n  Arma 3:      {self.arma()}
 ''' + "="*len_design())

        input()


def BSSIDinfo():
    print('\n ============================')
    query = input(f'  BSSID: ')
    try:
        response = requests.get(
            "https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)
        data = response.json()
        status = data["result"]
        if status == 200:
            lat = data["data"]["lat"]
            lon = data["data"]["lon"]
            print(f'  Latinude: {lat}\n  Longitude: {lon}')
            print(' =============================')
        else:
            errorCode = data["message"]
            errorMessage = data["desc"]
            print(
                f'  Error code: {errorCode}\n  Error message: {errorMessage}')
            print(' ============================')
    except:
        print(f' НАПИШИ ВЕРНО!')
    input()
