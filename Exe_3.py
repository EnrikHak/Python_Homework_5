#   Создайте программу для игры в ""Крестики-нолики"".

from decimal import setcontext


dask = [['*' , '*' , '*'], ['*' , '*' , '*'], ['*' , '*' , '*']]

#       Вариант 2


print(dask[0])
print(dask[1])
print(dask[2])
j = None
k = None
section = ''
stop = False

for i in range(9):
    if stop == True:
        break
    if i % 2 == 0:
        print()
        print('Первый игрок делает ход')
        n = int(input('Выберите строку (1-3): '))
        m = int(input('Выберите столбец (1-3): '))
        if n and m == j and k:
            print('Клетка занята!')
            section != 'X'
            n = int(input('Выберите строку еще раз (1-3): '))
            m = int(input('Выберите столбец еще раз (1-3): '))
            section = 'X'
        else:
            section = 'X'
        
        dask[n-1][m-1] = section
        print(dask[0])
        print(dask[1])
        print(dask[2])
    else:
        print()
        print('Второй игрок делает ход')
        j = int(input('Выберите строку (1-3): '))
        k = int(input('Выберите столбец (1-3): '))
        if j and k == n and m:
            print('Клетка занята!')
            section != 'O'
            j = int(input('Выберите строку еще раз (1-3): '))
            k = int(input('Выберите столбец еще раз (1-3): '))
            section = 'O'
        else:
            section = 'O'
        
        dask[j-1][k-1] = section
        print(dask[0])
        print(dask[1])
        print(dask[2])

    for x in range(3):
        if dask[x][0] == dask[x][1] == dask[x][2] and dask[x][0] != '*':
            win_line = dask[x][0]
            stop = True
            break
        elif dask[0][x] == dask[1][x] == dask[2][x] and dask[0][x] != '*':
            win_line = dask[0][x]
            stop = True
            break
    if dask[0][0] == dask[1][1] == dask[2][2] and dask[0][0] != '*':
        win_line = dask[0][0]
        stop = True
    elif dask[0][2] == dask[1][1] == dask[2][0] and dask[0][x] != '*':
        win_line = dask[0][2]
        stop = True

if win_line == 'X':
    print('Победил игрок 1')
elif win_line == 'O':
    print('Победил игрок 2')
else:
    print('Ничья')

#__________________________________________________________________________
#       Вариант 1

""" section = ''
first_p = None
second_p = None
j = None
k = None
stop = False
for i in range(9):
    if stop == True:
        break
    if i % 2 == 0:
        print()
        print('Первый игрок делает ход')
        n = int(input('Выберите строку (1-3): '))
        m = int(input('Выберите столбец (1-3): '))
        if n == j and m == k:
            print('Секция занята!')
        if dask[n - 1][m - 1] == 'X':
            dask[n - 1][m - 1] == 'X'
        else:
            dask[n - 1][m - 1] == 'O'
        section = 'О'
        dask[n - 1][m - 1] = section
        first_p = dask[n - 1][m - 1]
        print(dask[0])
        print(dask[1])
        print(dask[2])
    else:
        print()
        print('Второй игрок делает ход')
        j = int(input('Выберите строку (1-3): '))
        k = int(input('Выберите столбец (1-3): '))
        if n == j and m == k:
            print('Секция занята!')
        if dask[n - 1][m - 1] == 'O':
            dask[n - 1][m - 1] == 'O'
        else:
            dask[n - 1][m - 1] == 'X'
        section = 'X'
        dask[j - 1][k - 1] = section
        second_p = dask[j - 1][k - 1]
        print(dask[0])
        print(dask[1])
        print(dask[2])
    
    for x in range(3):
        if dask[x][0] == dask[x][1] == dask[x][2] and dask[x][0] != '*':
            win_line = dask[x][0]
            stop = True
            break
        elif dask[0][x] == dask[1][x] == dask[2][x] and dask[0][x] != '*':
            win_line = dask[0][x]
            stop = True
            break
    if dask[0][0] == dask[1][1] == dask[2][2] and dask[0][0] != '*':
            win_line = dask[0][0]
            stop = True
    elif dask[0][2] == dask[1][1] == dask[2][0] and dask[0][x] != '*':
            win_line = dask[0][2]
            stop = True

if win_line == 'O':
    print('Победил игрок 1')
elif win_line == 'X':
    print('Победил игрок 2')
else:
    print('Ничья')
    
print(dask[0])
print(dask[1])
print(dask[2]) """



 
""" a = dask[0][0] = 1
b = dask[0][1] = 2
c = dask[0][2] = 3
d = dask[1][0] = 4
e = dask[1][1] = 5
f = dask[1][2] = 6
g = dask[2][0] = 7
h = dask[2][1] = 8
z = dask[2][2] = 9 """    