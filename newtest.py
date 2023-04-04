count = int(input('Введите количество посетителей: '))
total_price = 0

for x in range(count):
    age = int(input('Сколько лет посетителю? '))
    if age >= 18 and age < 25:
        total_price = total_price + 990
    elif age >= 25:
        total_price = total_price + 1390

if count > 3:
    total_price = total_price * 0.9

print(total_price)












