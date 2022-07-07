# stocheaza pe principiul cheie valoare

dictionar = {
    'brand': 'Volvo',
    'model': 'XC 60',
    'year' : '2011',
}

print(dictionar)

dictionar[2] = 'Pepsi'
print(dictionar)

capitale = {
    'Romania' : 'Bucuresti',
    'Bulgaria': 'Sofia',
    'Franta': 'Paris'
}

intrari_in_tara = {
    'Romania' : 1,
    'Bulgaria': 0,
    'fRanta': 0,
}

print(capitale['Romania'])  # printam o valoare

# functia update()

capitale.update(intrari_in_tara)
print(capitale)

fructe = {'mere':2, 'pere':234} # dict pe un singur rand
print(fructe)

#dict gol
dictionaaar = {}

print(type(dictionaaar))

