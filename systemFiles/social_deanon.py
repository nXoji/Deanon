import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA


class SocialDeanon:
    def __init__(self):
        self.nickname = input('\n [+] Enter nickname: ')
        self.nickname = self.nickname.replace('@', '')

        self.output()

    def telegram(self):
        url = f'https://t.me/{self.nickname}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quote = soup.find('div', class_="tgme_page_description")

        temp = quote.text.strip()

        if temp != f"If you have Telegram, you can contact @{self.nickname} right away.":
            return f"  {url}\n"
        else:
            return ""

    def availability(self):
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

        for req_url in req_list:
            social_req = req_url + self.nickname

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

        return req_answer

    def output(self):
        req_answer = self.availability()

        q = int(len(self.nickname))
        if q <= 5:
            ravno = ' ========================================='
        elif q > 5 and q <= 12:
            ravno = ' ================================================'
        elif q > 12:
            ravno = ' ============================================================='
        else:
            ravno = 'ERROR'

        a = len(req_answer)
        if a >= 1:
            print(ravno)
            print('  Результат:')
            for b in req_answer:
                print('  ' + b)
        else:
            print('\n Этот ник в социальных сетях не найден!')

        print(self.telegram(), end="")
        print(ravno)

        input()
