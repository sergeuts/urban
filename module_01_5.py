immutable_var = (True, 1, 1.0, '1')
print(f'{immutable_var = }')

print('immutable_var[0] = 1')
print("TypeError: 'tuple' object does not support item assignment")
print('Так как кортеж относится к неизменяемым типам данным (immutable), \nто при попытке изменить элементы кортежа возникает ошибка TypeError.')

mutable_list = [True, 1, 1.0, '1']
mutable_list[0] = 1
print(f'{mutable_list = }')
