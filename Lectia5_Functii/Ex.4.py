#3. Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

def nr_char(nume, prenume, nume_mijlociu):
    return len(nume) + len(prenume) + len(nume_mijlociu)


print(nr_char('Trifu', 'I', 'Cristina'))