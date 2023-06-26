# # Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.


def double_list(myList : list[int]) :
    res = set()
    for item in myList :
        counter = myList.count(item)
        if counter > 1 :
            res.add(item)
    return list(res)


print(double_list([2, 2, 3, 3, 4, 4, 5, 6, 8, 7, 1]))


# # В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# # За основу возьмите любую статью из википедии или из документации к языку.


def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = 'Хорошие статьи — статьи, которые отвечают определённым критериям качества и считаются одними из лучших в проекте.\
        Хорошие статьи написаны со знанием вопроса и раскрывают затронутую тему. По тем или иным причинам они (пока ещё) не соответствуют \
        критериям избранных статей, но все желающие могут принять участие в их доработке до уровня избранных. \
        Перед тем как появиться на этой страничке, хорошие статьи проходят процедуру избрания на странице Википедия:Кандидаты в хорошие статьи,\
        где их обсуждают на предмет точности, нейтральности, полноты и стиля изложения.'


print(most_frequent(text))




# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

# Скоммунизжено из 4 семинара



from itertools import combinations
#from itertools import permutations
myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
maxWeight = 15
bigBag = {}

print("Вес всех вещей")
print(round(sum(myDict.values()),2))

weight = maxWeight

itemName = [*myDict.keys()]
variants = []
for n in range(1, len(itemName) + 1):
    comby = combinations(itemName, n)
    for variant in comby:
        sumItems = 0
        tempVariant = set()
        for el in variant:
            if sumItems + myDict[el] > weight:  # если сумма с добавление вещи превысит лимит, то
                continue
            sumItems += myDict[el]
            tempVariant.add(el)
        if tempVariant not in variants:  # полученное до этого множество добавляем в список вариантов (если его там еще нет)
            variants.append(tempVariant)

# проверим являются ли варианты подмножествами других вариантов, если да, то удалим эти варианты
i = 0
while i < len(variants):
    for j in range(0, len(variants)):
        if i == j:
            continue
        if variants[i] < variants[j]:
            variants.pop(i)
            break
    else:
        i += 1

print(f"Количество полученных вариантов: {len(variants)}")
print()

for var in sorted(variants, key=lambda x: sum(myDict[s] for s in x), reverse=True):
    print(*sorted(list(var)))
    wght = sum(myDict[s] for s in var)
    print(f" вес предметов {wght}")
    print()


#     ------------------------------------------------------------------------------------------------------------------------------


    import random

list_item = ['Палатка', 'Спальник', 'Пенка', 'Посуда', 'Фляга', 'Фонарик',
             'Горелка', 'Газ', 'Котелок', 'Топор', 'Нож', 'Тент',
             'Бахилы', 'Носки', 'Куртка', 'Штаны', 'Пуховка', 'Кофта',
             'Термобельё', 'Тапочки', 'Мыло', 'Спички', 'Трусы', 'Вода']

list_weight = [2.2, 2.1, 0.5, 1.2, 0.5, 0.5,
               0.5, 0.2, 1.5, 2.5, 0.6, 0.2,
               0.2, 0.1, 0.8, 0.7, 0.9, 0.6,
               0.3, 0.4, 0.1, 0.1, 0.1, 1.1]

max_capacity = 9

list_dictionary = dict(zip(list_item, list_weight))

def random_Bags_Of_Items(i):
    list_dictionary_random = random.sample(list_dictionary.keys(), len(list_dictionary))
    print('Вариант - ', i + 1)
    sum_weight = 0
    for j in range(len(list_dictionary)):
        if sum_weight + list_dictionary[list_dictionary_random[j]] <= max_capacity:
            sum_weight = sum_weight + list_dictionary[list_dictionary_random[j]]
            sum_weight = float('{:.1f}'.format(sum_weight))
            print(list_dictionary_random[j])
    print('')

def Main():
    print('Введите количество вариантов сборки рюкзака, \n которое хотели бы увидеть')
    num = int(input('>>> '))
    for i in range(num):
        random_Bags_Of_Items(i)

Main()

