# % de benzina ramasa + daca scadem 15% afisam un warning



def procentaj(rezervor, benzina_consumata):
     benzina_ramasa = rezervor - benzina_consumata
     procent = benzina_ramasa * 100 / rezervor
     if procent <= 15:
         print(procent)
         print('Warning, mai putin de 15% benzina ramasa')

     else:
        print(procent)

     return procent


x = procentaj(100,99)

b = 'ana are mere'
print(b[4:9])






