import requests

def IPinfo():
	query = input('\n [+] Ip For Scan: ')
	try:
		r = requests.get(f'http://ip-api.com/json/{query}').json()
		print(' =====================================')
		print(f'  IP adress:   {query}')
		print(f'  Country:     {r["country"]}\n  CountryCode: {r["countryCode"]}\n  Region:      {r["region"]}')
		print(f'  Region Name: {r["regionName"]}\n  City:        {r["city"]}\n  Zip:         {r["zip"]}\n  Latinude:    {r["lat"]}')
		print(f'  Longitude:   {r["lon"]}\n  Timezone:    {r["timezone"]}\n  ISP:         {r["isp"]}\n  Org:         {r["org"]}\n  As:          {r["as"]}')
		print(' =====================================')
	except:
		print(f' Не найдено!')
	input()


def BSSIDinfo():
	print('\n ============================')
	query = input(f'  BSSID: ')
	try:
		response = requests.get("https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)
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
			print(f'  Error code: {errorCode}\n  Error message: {errorMessage}')
			print(' ============================')
	except:
		print(f' НАПИШИ ВЕРНО!')
	input()


def main():
	print(' Использование:\n n.IPinfo\n n.IPtorrent\n n.BSSIDinfo')


if __name__ == '__main__':
	main()