#   Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def encode(stroka):
    encoding = ''
    i = 0
    while i < len(stroka):
        count = 1
        while i + 1 < len(stroka) and stroka[i] == stroka[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + stroka[i]
        i += 1
    return encoding

if __name__ == '__main__':
    stroka = input('Введите строку для кодировки: ')
    print(encode(stroka))