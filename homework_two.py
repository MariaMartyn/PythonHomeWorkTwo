#Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def FindFactorial():
    N = int(input('Введите число N: '))
    new_list = []
    f=1
    for i in range(1, N+1): 
        f*=i
        new_list.append(f)
    print(f'Список факториалов для чисел от 1 до {N} - {new_list}')

#FindFactorial()

#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def TruthTable():
    print('x|y|z| ¬ (X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                res = not (x and y) or z
                print(f'{x}|{y}|{z}|{int(res)}')
TruthTable()

#Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

def FindCount():
    string_1=input('Input the first string: ')
    string_2=input('Input the second string: ')
    count = []
    for i in range(len(string_1)):
        count.append(string_2.count(string_1[i]))
        print(f'{string_1[i]} - {count[i]}', end = ', ')
#FindCount()

#Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.

def CreateArray():
    N = int(input('Введите число N: '))
    list = []
    for i in range(-N, N+1):
        list.append(i)
    print(list)
    return(list)

def MoveArray():
    list = CreateArray()
    step = int(input('Введите число, на сколько позиций сдвигается список: '))
    for i in range(step):
        list.insert(0, list.pop())
    return(list)

#print(MoveArray())