'''
Write a Python program to move all zero digits to end of a given list of numbers. Go to the editor
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

lista1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
lista_fara_zero = []
lista_zero = []

for i in range(0, len(lista1)):
    if lista1[i] == 0:
        lista_zero.append(lista1[i])
    else:
        lista_fara_zero.append(lista1[i])

print(lista_zero)
print(lista_fara_zero)
print(lista_fara_zero, lista_zero) # adauga ca un singur element


lista_fara_zero.extend(lista_zero) # extinde lista cu toate elementele
print(lista_fara_zero)

#
# 71. Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

lista_de_dictioare = [{}, {}, {}]
lista2 = [{1,2},{},{}]
lista_este_goala = True

for i in range(0,len(lista2)):
    if len(lista2[i]) != 0:
        lista_este_goala = False
print(lista_este_goala)

