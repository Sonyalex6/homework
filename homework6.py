my_dict = {'Саша': 1999, 'Лиза': 2000, 'Кирилл': 2001, 'Максим': 2002, 'Леша': 2003}
print('Словарь:', my_dict)
print('Год рождения Лизы:', my_dict['Лиза'])
print('Год рождения Елены:', my_dict.get('Лена', 'нет такого ключа'))
my_dict.update({'Женя': 1995, 'Света': 2005})
removed_year = my_dict.pop('Света')
print('Значение удалённого элемента \'Светы \':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)