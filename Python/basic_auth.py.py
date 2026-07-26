import base64

login = input('Введіть логін: ').strip()
password = input('Введіть пароль: ').strip()

text = f'{login}:{password}'

encoded = base64.b64encode(text.encode())

print(f'Authorization: Basic {encoded.decode()}')