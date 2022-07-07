# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
#

import random
from random import randrange

nr_secret = randrange(30)
print(nr_secret)

nr_ghicit = int(input('Ghiciti un nr intreg: '))

while nr_ghicit != nr_secret:
    if nr_ghicit > nr_secret:
        print('Nr secret e mai mic')
        break
    elif nr_ghicit < nr_secret:
        print('Nr secret e mai mare')
        break
else:
    print('Felicitari! Ai ghicit!')

