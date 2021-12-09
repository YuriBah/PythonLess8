import re

def email_parse(email_adress):
    dom = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    final = dom.match(email_adress)
    if not final:
        raise ValueError(f'Адрес не валиден: {email_adress}')
    return final.groupdict()

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))