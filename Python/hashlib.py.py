import hashlib
import time

def check_hash():  
    total_passw = 0
    
    target_hash = input('Введіть хеш: ')
    method = input('Введіть метод хешуваня: ')

    with open('#Підставити свою папку з паролями', 'r') as file:
        start_time = time.time()
        if method == 'md5':
            method_hash = hashlib.md5
        elif method == 'sha1':
            method_hash = hashlib.sha1
        elif method == 'sha256':
            method_hash = hashlib.sha256
        else:
            print("Неправильний метод хешування...")
            return
            
        found = False
        for passw in file:
            total_passw += 1
            passw = passw.strip()
            
            passw_hash = method_hash(passw.encode()).hexdigest()
            
            if passw_hash == target_hash:
                found = True
                print(f'Хеш: {passw_hash}')
                print(f'Хеш співпав, пароль: {passw}')
                break
        
        if not found:
            print('Пароль не знайдено')
            
        end_time = time.time()
        total_time = end_time - start_time    
        print(f'Всього перевірено паролей: {total_passw}')
        print(f'Час сканування: {total_time} sec') 

check_hash()
         