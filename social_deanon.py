import requests
from colorama import init, Fore, Style

red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA

def SocialDeanon():
	nickname = input('\n [+] Введите никнейм для деанона: ')

	req_list = [
	'https://www.instagram.com/',
	'https://github.com/',
	'https://rt.pornhub.com/users/',
	'https://ok.ru/',
	'https://vk.com/',
	'https://soundcloud.com/',
	'https://www.tumblr.com/blog/view/',
	'https://twitter.com/',
	'https://ask.fm/',
	'https://znanija.com/app/profile/',
	'https://www.deviantart.com/',
	'https://www.flickr.com/',
	'https://ru.linkedin.com/in/',
	'https://myspace.com/',
	'https://www.pinterest.com/',
	'https://www.reddit.com/r/',
	'https://www.reddit.com/user/'
	]

	req_answer = []

	i = 1
	for req_url in req_list:
		social_req = req_url + nickname

		try:
			res = requests.get(social_req)
			if res:
			    print(green, ' ', social_req)
			    req_answer.append(social_req)
			else:
			    print(red, ' ', social_req)
		except:
			print(magenta, ' ', social_req)
	print(Style.RESET_ALL)

	q = int(len( nickname ))
	if q <= 5:
		ravno = ' ========================================='
	elif q > 5 and q <= 12:
		ravno = ' ================================================'
	elif q > 12:
		ravno - ' ============================================================='
	else: 
		ravno = 'ERROR'

	a = len( req_answer )
	if a >= 1:
		print( ravno )
		print('  Результат:')
		for b in req_answer:
			print('  ' + b)
		print( ravno )
	else:
		print('\n Этот ник в социальных сетях не найден!')
	input()

	
def main():
	print("""Использование:
		N.SocialDeanon""")


if __name__ == '__main__':
	main()