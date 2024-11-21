my_dict =  {'Sergei': 1973, 'Egor': 1999, 'Masha': 2002}
print(f'{my_dict = }')
print('existing value:', my_dict['Sergei'])
print('not existing value:', my_dict.get('Michael', None))
my_dict['Michael'] = 1958
my_dict['Leo'] = 1942
print('deleted value:', my_dict.pop('Egor'))
print(f'{my_dict = }')

my_set = {1, 1, '1', '1', 1.0, 1.0}
print(f'{my_set = }')
my_set.add(2)
my_set.add(3)
my_set.remove(1)
print(f'{my_set = }')
