import string
from random import sample, choice
import secrets
specSmb = ["@", "#", "$", "%", "&"]

dlina = int(input("Введите длину пароля \n"))

slognost = int(input("Выберете сложность пароля:\n" 
                     "1 - для пароля и строчных букв\n" 
                     "2 - для пароля из строчных и прописных букв\n" 
                     "3 - для строчных и прописных букв и цифр\n" ))

kolvo = int(input("Введите количество паролей \n"))

if slognost == 1:
    alphabet = string.ascii_lowercase
elif slognost == 2:
    alphabet = string.ascii_letters
else:
    alphabet = string.ascii_letters + string.digits

for pwd in range(kolvo):
    pwd = ''.join(secrets.choice(alphabet) for i in range(dlina))
    print(pwd)




