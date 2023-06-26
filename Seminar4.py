# Напишите функцию, которая принимает строку текста. 
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого 
# длинного слова был один пробел между ним и номером строки.


def textPrinting(text, count, lenMaxWord):
    print(count, text.rjust(lenMaxWord, '-'))
def superFunc(text):
    text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
    myWords = sorted(text.split(' '))
    count = 1
    lenMaxWord = len(max(myWords, key=len))  # Длина макс. слова. Чтобы не поплыл текст при выводе
    for i in myWords:
        textPrinting(i, count, lenMaxWord)
        count += 1

text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
superFunc(text)


# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого 
# символа введённой строки отсортированный по убыванию.


def textUnicode(text):
    uniList = []
    text = list(text)
    text.sort(reverse = True)
    print(text)
    for i in text :
        uniList.append(ord(i))
    return uniList

text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
print(text)
text = "".join([i for i in text.lower() if i.isalpha() or i ==" "]).replace(' ','')
print(set(textUnicode(text)))


# Функция получает на вход строку из двух чисел через пробел. 
# Сформируйте словарь, где ключом будет 
# символ из Unicode, а значением —  целое число. 
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def dictUnicode(numIn):
    numIn = list(map(int, numIn.split(' ')))
    maxN = max(numIn)
    minN = min(numIn)
    for i in range(minN, maxN + 1):
        myDict[chr(i)] = i
    return myDict
numIn = input('вводим два числа через пробел')
myDict = {}

print(dictUnicode(numIn))


# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.


def create_list():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(числа), по окончанию ввода нажмите Enter')
    new_list = []
    while True:
        try:
            element = int(input('> '))
            int(element)
            new_list.append(element)
        except:
            break
    return new_list

def sort_bubble(sort_list):  # Сортируем по возрастанию
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list) - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list

def main():
    new_list = create_list()
    print(new_list)
    if len(new_list) == 0:
        print('Отсутствуют числовые элементы в списке')
        exit()
    sort_list = sort_bubble(new_list)
    print(sort_list)

main()



# ИЛИ

def superSort(myList):
    for i in range (len(myList)):
        for j in range(i, len(myList)):
            if i == j : continue
            elif myList[i] > myList[j] :
                myList[i], myList[j] = myList[j], myList[i]
    return myList
myList = [6, 3, 1, 2, 5, 7, 8, 2, 5, 2, 5, 7, 7, 9, 1, 0, 9, 1, 3, 4]
print(superSort(myList))


# Функция принимает на вход три списка одинаковой длины:
# имена str, 
# ставка int, 
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой 
# премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии.


premium = 0.1025

def create_list_rate():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(ставки), по окончанию ввода нажмите Enter')
    new_list_rate = []
    while True:
        try:
            element = float(input('> '))
            float(element)
            new_list_rate.append(element)
        except:
            break
    return new_list_rate

def create_list_name():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(имена), по окончанию ввода нажмите Enter')
    new_list_name = []
    while True:
        try:
            element = str(input('> '))
            if element == '' or element == ' ':
                break
            new_list_name.append(element)
        except:
            break
    return new_list_name

def create_list_dictionary_sum_premium(list_rate, list_name):
    list_premium = []
    for i in range(len(list_rate)):
        list_premium.append(float("{0:.2f}".format(list_rate[i] * premium)))

    list_dict_premium = dict(zip(list_name, list_premium))
    return list_dict_premium

def main():
    new_list_rate = create_list_rate()
    # print(new_list_rate)
    new_list_name = create_list_name()
    # print(new_list_name)
    if (len(new_list_rate)) == 0 or (len(new_list_rate) == 0) \
            or len(new_list_rate) != len(new_list_name):
        print('Отсутствуют элементы в списке или кого-то не хватает')
        exit()
    list_dict_premium = create_list_dictionary_sum_premium(new_list_rate, new_list_name)
    print(list_dict_premium)

main()


# ИЛИ


def salary(names, rate, bonus):
    workers ={}
    for i in range (len(names)):
        percent = float(bonus[i].replace('%',''))/100
        workers[names[i]] = percent*rate[i] + rate[i]
    return workers

names = ['Петров','Иванов','Денисов','Сидоров']
rate = [15000, 12500, 13700, 21000]
bonus = ['9.25%', '10.25%', '15%', '11.10%']
workerSalary = salary(names, rate, bonus)
print(workerSalary)


# Функция получает на вход список чисел и два индекса. 
# Вернуть сумму чисел между между переданными индексами. 
# Если индекс выходит за пределы списка, сумма считается 
# до конца и/или начала списка.


def create_list():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(ставки), по окончанию ввода нажмите Enter')
    new_list = []
    while True:
        try:
            element = int(input('> '))
            int(element)
            new_list.append(element)
        except:
            break
    return new_list

def sequence_sum(new_list, index_list):
    list_sum = []
    list_sum_min = []
    list_sum_max = []
    for item in new_list:
        if item >= index_list[0] and item <= index_list[1]:
            list_sum.append(item)
        elif item < index_list[0]:
            list_sum_min.append(item)
        elif item > index_list[1]:
            list_sum_max.append(item)
    if len(list_sum) != 0:
        return sum(list_sum)
    elif len(list_sum_min) != 0:
        return sum(list_sum_min)
    elif len(list_sum_max) != 0:
        return sum(list_sum_max)

def main():
    new_list = create_list()
    print(new_list)
    new_list.sort()
    print(new_list)
    index = str(input('Введите два индекса через пробел >>> '))
    index_list = index.split()
    index_list = [int(item) for item in index_list]
    index_list.sort()
    print(index_list)
    if (len(new_list)) == 0 or len(index_list) != 2:
        print('Отсутствуют элементы в списке или индексов не два')
        exit()
    print('Сумма = ', sequence_sum(new_list, index_list))

main()


# ИЛИ


def indRange(ind, limit):
    if ind < 0 : ind = 0
    if ind > limit : ind = limit - 1
    return ind
def sumNums(myList, ind, ind2):
    ind = indRange(ind, len(myList))
    ind2 = indRange(ind2, len(myList))
    sum = 0
    for i in  range(ind, ind2+1):   #сумма включая числа под заданными инксами
    #for i in range(ind+1, ind2):    # сумма без чисел под индексами
        sum = sum + myList[i]
    return sum
myList = [1, 3, 5, 2, 4, 6, 8]
ind = int(input('введите индекс №1 - >> '))
ind2 = int(input('введите индекс №2 - >> '))
print(sumNums(myList, ind, ind2))


# Функция получает на вход словарь с названием компании в качестве ключа 
# и списком с доходами и расходами (3-10 чисел) в качестве значения. 
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


list_company = ['New Company', 'Real Company', 'Company', 'CompBiz',
                'Mega brand', 'Mega King', 'Everything', 'Modest']

list_profit_and_loss = [(100, 200, 300, -100, -200), (200, 600, 400, -300, -400),
                        (200, 300, 300, -500, -100), (200, 200, 100, -100, -400),
                        (100, 100, 100, -100, -100), (100, 300, 100, -100, -100),
                        (300, 200, 100, -100, -200), (400, 600, 100, -100, -100)]

list_dictionary = dict(zip(list_company, list_profit_and_loss))
keys = list(list_dictionary.keys())

def check_company():
    for i in range(len(list_dictionary)):
        if sum(list_dictionary[keys[i]]) < 0:
            return False
    return True

print(check_company())


# ИЛИ


def positiveBalans(company):
    for comp, balans in company.items():
        if sum(balans) >= 0:
            x = True
        else:
            x = False
            break
    return True if x == True else False

company = {
    'CompanyOne': [1000, 123331, 1000, 2000],
    'CompanyTwo': [9999, -1000, 12000],
    'CompanyThree': [10000, -23322, 100000, -9999]
}
print(positiveBalans(company))


# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


names = "Ivan"
next = 6
tigers = "White"
dogs = "Rex"
mute = 7
ENDSWITH_STR = 's'

def changing_variable_names():
    glob = globals()
    print(glob)
    print()
    for key in tuple(glob.keys()):
        if key.endswith(ENDSWITH_STR):
            temp = glob[key]
            glob[key] = None
            glob[key[: -1]] = temp
    print(glob)


changing_variable_names()
print()
print("check")
print()
print(names, name)
print(tigers, tiger)
print(dogs, dog)


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
listKeys = list(myDict.keys())
listItems = list(myDict.values())
print(type(listItems))
maxWeight = 13
someList=[]
def func(someList, index, weight):
    print('Уже уложено:', someList)
    for i in range(index, len(listKeys)):
        print('Пробуем положить', listKeys[i])
        if listItems[i]+weight <= maxWeight :
            emptyList = someList.copy()
            emptyList.append(listKeys[i])
            print('Влазит')
            func(emptyList, i+1, weight+listItems[i])
        else: print('Не влазит')
    if len(someList) >= 3 : print(someList, weight)
func(someList, 0, 0)