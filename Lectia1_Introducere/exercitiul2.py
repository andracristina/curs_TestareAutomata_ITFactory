# exercitiul 2 -  nu a iesit OK !!

# pt un string afisati nr de char mici, mari, cifre si speciale

nr_car_mici = 0
nr_car_mari = 0
nr_cifre = 0
nr_car_speciale = 0

input_string = 'Curs de Python la adresa: @120.20.1'

for i in range(len(input_string)):
    if input_string[i].isupper():
        nr_car_mari = nr_car_mari +1
    elif input_string[i].islower():
        nr_car_mici = nr_car_mari +1
    elif input_string[i].isdigit():
        nr_cifre = nr_cifre +1
    else:
        nr_car_speciale = nr_car_speciale +1


print(f'nr car mici = ', nr_car_mici)
print(f'nr car mari = ', nr_car_mari)
print(f'nr cifre = ', nr_cifre)
print(f'nr car speciale = ', nr_cifre)