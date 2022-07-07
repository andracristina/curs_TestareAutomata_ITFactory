multime = {'lola', 'bolaa'}

print(type(multime))

dict = {'lola':200, 'bola':300}

print(type(dict))

lista = ['lola', 'bolaa']

print(type(lista))

tuuple = ('lola', 'bolaa')

print(type(tuuple))


for j in range(10):
    for i in range(999):
        print(i)
        if i == 4:
            break    # j merge pana la 10, break aici opreste doar i
        print(f'j = {j}')


for i in range(5):
    if i == 3:
        continue #skips a step
    print(i)
