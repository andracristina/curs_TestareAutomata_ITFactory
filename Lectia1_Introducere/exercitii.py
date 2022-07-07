# exercitiul 1
# palindrom - un cuv ce e la fel citit de la dreapta la stanga sau de la stanga la dreapta, de ex. lupul
# print(varibila[::-1])  # intoarce caracterele de la cap la coada

cuvantul = input('Cuvantul este: ')
cuv_invers = cuvantul[::-1]

if cuvantul == cuv_invers:
    print ('CUvantul este palindrom')

if cuvantul == cuvantul[::-1]:
    print('merge')



