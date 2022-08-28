import pycountry
import phonenumbers
from phonenumbers import carrier, timezone, region_code_for_country_code


class PhoneNumber:
    def __init__(self):
        self.number = input('\n [+] Enter phone: ')
        self.number = self.number.replace('+', '')

        self.output()

    def default_info(self):
        try:
            phone_num = phonenumbers.parse(f'+{self.number}', None)
        except:
            raise ValueError('Номер введён не верно')

        country_iso = region_code_for_country_code(phone_num.country_code)
        country = pycountry.countries.get(alpha_2=country_iso)

        operator = carrier.name_for_number(phone_num, None)
        if operator == '':
            operator = 'Не найдено'

        timezone_info = timezone.time_zones_for_number(phone_num)
        if len(timezone_info) > 1:
            timezone_info = f'{len(timezone_info)} штук'
        elif len(timezone_info) == 1:
            timezone_info = ''.join(timezone_info)

        out = {
            'country': country.name,
            'operator': operator,
            'timezone': timezone_info
        }

        return out

    def output(self):
        data = self.default_info()

        print(f''' =====================================
   Номер:         +{self.number}
   Страна:        {data['country']}
   Оператор:      {data['operator']}
   Часовой пояс:  {data['timezone']}
 =====================================''')

        input()
