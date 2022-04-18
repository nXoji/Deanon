import requests
import json

def PhoneNumber():
	phone = input(' [+] Enter phone: ')

	try:
		getInfo = f'https://htmlweb.ru/geo/api.php?json&telcod={phone}'
		infoPhone = requests.get( getInfo )
		    
		infoPhone = infoPhone.json()
		uty = requests.get('https://api.whatsapp.com/send?phone='+phone)
		if uty.status_code==200:
			utl2 = ' Есть'
		else:
			utl2 = ' Не неайден '

		country_id = infoPhone["country"]["id"]
		if country_id == 'RU':
			print( " ============================================== " )
			print( u"  Номер:       ", "+" + phone )
			print( u"  Страна:      ", infoPhone["country"]["english"] )
			print( u"  Регион:      ", infoPhone["region"]["english"] )
			print( u"  Округ:       ", infoPhone["region"]["okrug"] )
			print( u"  Оператор:    ", infoPhone["0"]["oper"] )
			print( u"  Часть света: ", infoPhone["country"]["location"] )
			print( "  WhatsApp:   ", utl2)
			print( " ============================================== " )

		elif country_id == 'US':
			print( " ==================================== " )
			print( u"  Номер:       ", "+" + phone )
			print( u"  Страна:      ", infoPhone["country"]["english"] )
			print( u"  Оператор:    ", infoPhone["0"]["oper"] )
			print( u"  Часть света: ", infoPhone["country"]["location"] )
			print( "  WhatsApp:   ", utl2)
			print( " ==================================== " )

		elif country_id == 'DE':
			print( " ==================================== " )
			print( u"  Номер:       ", "+" + phone )
			print( u"  Страна:      ", infoPhone["country"]["english"] )
			print( u"  Город:       ", infoPhone["0"]["english"])
			print( u"  Регион:      ", infoPhone["region"]["english"] )
			print( u"  Часть света: ", infoPhone["country"]["location"] )
			print( "  WhatsApp:   ", utl2)
			print( " ==================================== " )

		else:
			print( " ============================== " )
			print( u"  Номер:       ", "+" + phone )
			print( u"  Страна:      ", infoPhone["country"]["english"] )
			print( u"  Столица:     ", infoPhone["capital"]["english"])
			print( u"  Оператор:    ", infoPhone["0"]["oper_brand"] )
			print( u"  Часть света: ", infoPhone["country"]["location"] )
			print( "  WhatsApp:   ", utl2)
			print( " ============================== " )
	except:
		print(' ОШИБКА! Возможно вам надо воспользоваться vpn!')
	input()



def main():
	print(' Использование: \n n.PhoneNumber')
	PhoneNumber()


if __name__ == '__main__':
	main()