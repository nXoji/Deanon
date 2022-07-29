import pycountry
import phonenumbers
from phonenumbers import carrier, timezone, region_code_for_country_code


class PhoneNumber:
    def __init__(self):
        self.number = input('\n [+] Enter phone: ')
        self.number = self.number.replace('+', '')

        self.output()

    def defaultInfo(self):
        try:
            phoneNum = phonenumbers.parse(f'+{self.number}', None)
        except:
            raise ValueError('Номер введён не верно')

        countryIso = region_code_for_country_code(phoneNum.country_code)
        country = pycountry.countries.get(alpha_2=countryIso)

        operator = carrier.name_for_number(phoneNum, None)
        if operator == '':
            operator = 'Не найдено'

        timezoneInfo = timezone.time_zones_for_number(phoneNum)
        if len(timezoneInfo) > 1:
            timezoneInfo = f'{len(timezoneInfo)} штук'
        elif len(timezoneInfo) == 1:
            timezoneInfo = ''.join(timezoneInfo)

        out = {
            'country': country.name,
            'operator': operator,
            'timezone': timezoneInfo
        }

        return out

    def output(self):
        data = self.defaultInfo()

        print(f''' =====================================
   Номер:         +{self.number}
   Страна:        {data['country']}
   Оператор:      {data['operator']}
   Часовой пояс:  {data['timezone']}
 =====================================''')

        input()
