# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
#


def dictionar(lista):
    dictionar = {}
    for numar in lista:
        de_cate_ori = {numar:lista.count(numar)}
        dictionar.update(de_cate_ori)
    return dictionar

print(dictionar([1,2,3,4,5]))



print(dictionar([1,2,3,4,5]))



print(dictionar([0,1,2,3,4,4,5,5,5,5]))



#print(dictionar([1,3,1,4,4,5,6,7,7,7,7,7]))
