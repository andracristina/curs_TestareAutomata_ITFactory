# Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def cate_caractere(text):
    d = {'uppercase':0, 'lowercase':0}
    for c in text:
        if c.islower():
            d['lowercase']+=1
        elif c.isupper():
            d['uppercase']+=1
    print('no of lowercase char:', d['lowercase'])
    print('no of uppercase char:', d['uppercase'])


cate_caractere('the WoLF iS cHeeky')


