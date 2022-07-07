# modulo  - the % symbol in Python is called the Modulo Operator.
# It returns the remainder of dividing the left hand operand by right hand operand.

print (5%3)


#Flow Control - if, if else, if... elif... else


#exercitiu1
#scrieti un program care sa printeze toate nr de la 0 la 6, mai putin 3 si 6

s = '' #string gol
for x in range(0,6):
    if not (x == 3 or x == 6):
        print(x)
        s += str(x) + ' '     #transformam x in string pt a le printa pe aceeasi linie; practic, la s-ul gol adaugam toate x urile printate mai sus
print(s)

#exercitiu2

""" write a Python program to construct the following pattern:
1
22
333
4444
55555
666666
7777777
88888888
999999999

"""
s = ''
for i in range(1,10):
    s = ''   # resetam variabila, altfel stocheaza toate valorile
    for j in range(0, i+1):
        s = s + str(i)
    print(s)



"""
exercitiul 3

*
**
***
****
*****
****
***
**
*

"""

s = ''
for i in range(1,6):
    s = ''
    for j in range(1,i):
        s += '*'
    print(s)
for i in range(6, 1, -1):
    s = ''
    for j in range (1, i):
        s += '*'
    print(s)


"""
exercitiul 4
se dau laturile unui triunghi: x, y, z
sa se determine daca triunghiul este
oarecare
isoscel
echilateral

"""
x = int(input('Prima latura: '))
y = int(input('A doua latura: '))
z = int(input('A treia latura: '))

if x == y == z:
    print('Echilateral')
elif x == y or x == z or y == z:
    print('Isoscel')
else:
    print('oarecare')


# tabla inmultirii pt un input

a = int(input('Introdu un nr: '))

for i in range (1,11):
    print(a, '', 'x', '', 'i', '', '=', a*i)

 """

 Fibbonaci

 """

nr_fib = int(input('Introduceti cate nr fib sa afisam: '))

  a = 0
b = 1
s = 0

    for i in range(0, nr_fib):
        print(a + b)
        a_vechi = a
        a = b
        b = a_vechi + b

