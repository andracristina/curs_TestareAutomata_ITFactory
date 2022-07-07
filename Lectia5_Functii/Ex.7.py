# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

def cautam_char(text):
    if 'a' in text:
        return True
    else:
        return False


print(cautam_char('ion'))