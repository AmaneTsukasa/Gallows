import string
from random_word import RandomWords


random_word = RandomWords()
rnd_word = random_word.get_random_word()


count = 5 + len(rnd_word)
secret_word = rnd_word[0]+ '*' * (len(rnd_word)-1)


print('Загаданное слово: ',rnd_word[0] + secret_word[1:])
while count > 0:
    count -= 1
    user_symb = input('Введите предпологаемую букву на английском: ').lower()
    while len(user_symb) != 1:
        print('Введите 1 букву!')
        user_symb = input('Введите предпологаемую букву на английском: ').lower()

    if user_symb not in string.ascii_lowercase:
        print('Опечатка, буква на русском')
        user_symb = input('Введите предпологаемую букву на английском: ').lower()

    if user_symb in rnd_word:
        print('Вы угадали!')
        for i, char in enumerate(rnd_word):
            if char == user_symb:
                secret_word = secret_word[:i] + char + secret_word[i+1:]

    else:
        print('Вы не угадали!')
        print('Осталось попыток: ', count)
    print(secret_word)


print(rnd_word)