import os
import time
from colorama import init, Fore, Style

import systemFiles.social_deanon as sd
import systemFiles.ip_deanon as idn
import systemFiles.phone_deanon as phd

init()

red = Fore.RED
reset = Style.RESET_ALL


os.system('cls||clear')
print('\n\n\n ██████╗░███████╗░█████╗░███╗░░██╗░█████╗░███╗░░██╗')
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
print(Style.BRIGHT + ' Разработчик:  nXoji     v0.1      Made in Ukraine' + reset)
time.sleep(2)


def main():
    while True:
        os.system('cls||clear')
        print('''
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
            idn.IpInfo()
        elif home_page == 3:
            idn.BSSIDinfo()
        elif home_page == 4:
            phd.PhoneNumber()
        else:
            print(red + ' Введите существующий пункт меню!' + reset)
            continue


if __name__ == '__main__':
    main()
