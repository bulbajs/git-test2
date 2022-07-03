# alphabet = ['a', 'b', 'c', 'd']
# alphabet.append('e')
# print(alphabet)
# print(alphabet[len(alphabet)-1])
# print(alphabet[-1])
# print(alphabet[2])
# #alphabet.pop(0)
# print(alphabet[-2:-4:-1])

#alphabet = str(alphabet)
#print(str(alphabet))
#alphabet = alphabet.split(',')
#alphabet = '\n'.join(alphabet)
#print(alphabet)

#L = ["а", "б", "в", 1, 2, 3, 4]
#print (L[-4:-8:-1])
# [4, 3, 2]

# L = [3.3, 4.4, 5.5, 6.6]
# print(list(map(round, L)))
#
# L = ['3.3', '4.4', '5.5', '6.6']
# print (list(map(float, L)))

# L = [3, 4, 5, 6, 7, 8]
# print(sum(L[::2]))
#
# string = input('Введите числа')
# list_of_string = string.split()
# list_of_string = list(map(int,list_of_string))
# print(sum(list_of_string[::3]))


# n = input('Введите числа')
# n = list(n)
# n[0],n[-1] = n[-1], n[0]
# print(n)
# n = list(map(int,n))
# print(sum(n[::1]))
# n.append(sum(n[::1]))
# print(n)

# n = list(map(int, input('Введите числа').split()))
# n[0],n[-1] = n[-1],n[0]
# n.append(sum(n))
# print(n)

# person = {'name': 'Adelya'}
# person['phone'] = '+7(999)-675-40-30'
#
# print(person.keys())
# print(person.values())
# person.pop('phone')
# print(person)
#
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print(d)
#
# print("||".join(d.keys()))

# s = ("'Книга':'Разумный инвестор', 'Автор':'Бенджамин Грэм', 'Дата': 2016")
title = input('Введите название книги')
author = input('Введите имя автора')
date = input('Введите дату написания книги')
book = {'Книга': title, 'Автор': author, 'Дата': date}
print(book)