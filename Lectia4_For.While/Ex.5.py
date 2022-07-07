# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masini_vechi =[]

for i in range(len(masini)):
    masina = masini[i]
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini[i] = 'Tesla'

print(masini)
print(masini_vechi)

