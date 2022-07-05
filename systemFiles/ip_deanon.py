import requests
import ipaddress


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

        return r

    def output(self):
        default = self.defaultInfo()

        print(f''' =====================================
  IP adress:   {self.ip}
  Country:     {default["country"]}\n  CountryCode: {default["countryCode"]} 
  Region:      {default["region"]}\n  Region Name: {default["regionName"]}
  City:        {default["city"]}\n  Zip:         {default["zip"]}
  Latinude:    {default["lat"]}\n  Longitude:   {default["lon"]}
  Timezone:    {default["timezone"]}\n  ISP:         {default["isp"]}
  Org:         {default["org"]}\n  As:          {default["as"]}
 =====================================''')

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


def main():
    print(' Использование:\n n.IpInfo\n n.BSSIDinfo')


if __name__ == '__main__':
    main()
