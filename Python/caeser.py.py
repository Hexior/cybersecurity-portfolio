


import base64

print('1 - Encode\n2 - Decode')
user = input('Введіть метод: ')

if user == '1':
    text = input('Введіть текс для кодування: ')
    
    encoded = base64.b64encode(text.encode())
    print(f'{text} ---> {encoded.decode()}')

elif user == '2':
    text = input('Введіть Base64: ')
    
    decoded = base64.b64decode(text.encode())
    print(f'{text} ---> {decoded}')

else:
    print('Такого методу не існує...')
    
