drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

# в drone по очереди попадает каждый дрон из списка drone_list
# for drone in drone_list:
# 	print(drone)

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
input_name = input("Введите производителя дронов: ")
name = input_name.split()[0].lower()
drone_count = 0
for dron in drone_list:
  if name == dron.split()[0].lower():
    drone_count += 1
    if name == 'dji':
      true_dron_name = 'DJI ' + " ".join(dron.split()[1:])
    elif name == 'autel':
      true_dron_name = 'Autel ' + " ".join(dron.split()[1:])
    else:
      true_dron_name = dron
    print(true_dron_name)
print(f'Количество дронов данного производителя: {drone_count}')
print('---------------')

#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
drone_names = dict()
for drone in drone_list:
  key = drone.split()[0].lower()
  drone_names[key] = drone_names.get(key, 0) + 1
for key, value in drone_names.items():
  if key == 'dji':
    new_key = key.upper()
  else:
    new_key = key.capitalize()
  print(f'{new_key}: {value} шт')
print('---------------')

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
drones_to_register = []
drones_not_to_register = []
for drone, weight in zip(drone_list,  drone_weight_list):
  if weight > 150:
    drones_to_register.append(drone)
  else:
    drones_not_to_register.append(drone)
print(f'Дроны, подлежащие регистрации: {drones_to_register}')
print(f'Дроны, не подлежащие регистрации: {drones_not_to_register}')
print('---------------')

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!
height = int(input("Введите максимальную высоту полёта: "))
if input('Полёт будет проходить над населённым пунктом? (y/n): ') == 'y':
  is_above_the_city = True
else:
  is_above_the_city = False
if input('Полёт будет проходить вне закрытых зон? (y/n): ') == 'y':
  is_above_closed_zone = False
else:
  is_above_closed_zone = True
if input('Полёт будет проходить в прямой видимости? (y/n): ') == 'y':
  is_in_visibility = True
else:
  is_in_visibility = False
for drone, weight in zip(drone_list,  drone_weight_list):
  if height > 150 or weight > 150 and is_above_the_city or is_above_closed_zone or not is_in_visibility:
    print(f'{drone}: необходимо согласовать полёт')
  else:
    print(f'{drone}: полёт согласовать не нужно')
print('---------------')

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine
input_name = input("Введите производителя дронов: ")
name = input_name.split()[0].lower()
drone_count = 0
for dron in drone_list:
  if name == dron.split()[0].lower():
    drone_count += 1
    model = " ".join(dron.split()[1:])
    print(model)
print('---------------')