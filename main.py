import time
from colorama import init, Fore, Style

import social_deanon as sd
import ip_deanon as idn
import phone_deanon as phd

init()

red = Fore.RED
reset = Style.RESET_ALL


print('\n ██████╗░███████╗░█████╗░███╗░░██╗░█████╗░███╗░░██╗')
time.sleep(0.1)
print(' ██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░██║')
time.sleep(0.1)
print(' ██║░░██║█████╗░░███████║██╔██╗██║██║░░██║██╔██╗██║')
time.sleep(0.1)
print(' ██║░░██║██╔══╝░░██╔══██║██║╚████║██║░░██║██║╚████║')
time.sleep(0.1)
print(' ██████╔╝███████╗██║░░██║██║░╚███║╚█████╔╝██║░╚███║')
time.sleep(0.2)
print(' ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝')
time.sleep(0.2)
print(Style.BRIGHT + ' Разработчик:  H.I.M.     v0.1      Made in Ukraine' + reset)


def main():
	while True:
		print('''\n\n

 ╭━╮╭━┳━━━┳━╮╱╭┳╮╱╭╮
 ┃┃╰╯┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃╭╮╭╮┃╰━━┫╭╮╰╯┃┃╱┃┃
 ┃┃┃┃┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃┃┃┃┃┃╰━━┫┃╱┃┃┃╰━╯┃
 ╰╯╰╯╰┻━━━┻╯╱╰━┻━━━╯''')
		print(' Вы в главном меню\n 1) Проверка по нику\n 2) Проверка IP-adress\n 3) Проверка BSSID\n 4) Проверка по номеру телефона')
		print(' 0) ! ВЫХОД !')
		home_page = int(input('\n [+] Cделайте выбор: '))

		if home_page == 0:
			break
		elif home_page == 1:
			sd.SocialDeanon()
		elif home_page == 2:
			idn.IPinfo()
		elif home_page == 3:
			idn.BSSIDinfo()
		elif home_page == 4:
			phd.PhoneNumber()
		else:
			print(red + ' Введите существующий пункт меню!' + reset)
			continue



if __name__ == '__main__':
	main()