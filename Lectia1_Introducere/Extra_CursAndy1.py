import math

a = 3.15844575

# sintaxa care limiteaza nr de zecimale
print('{:.2f}'.format(a))

#sintaxa care rotunjeste catre cel mai apropiat nr intreg
print(round(a))

#fortam rotunjire in jos
print(math.floor(a))

#fortam rotunjire in sus
print(math.ceil(a))


#f - vine de la format string, forteaza variabilele dintre {} se se comporte ca niste stringuri
nume = 'Andra'
age = 33
print(f'My name is {nume} and I am {age} years old')
