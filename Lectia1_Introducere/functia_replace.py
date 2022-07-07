# exercitiul 1
propozitie1 = 'Ana are mere'

propozitie2 = propozitie1.replace('Ana ', 'Ion ')    # inlocuim Ana cu Ion

print(propozitie2)

# exercitiul 2
de_trimis = 'Contul bancar este: XXXXXXX'
print(de_trimis.replace('XXXXXXX', 'RO01BTRL0123562'))

# exercitiul 3
input_string = 'Ana merge la Piata'
output_string = ''

# programul - schimbam capitabilazarea literelor - opus

for i  in range(0, len(input_string)):
    if input_string[i].isupper():
       output_string = output_string + input_string[i].lower()
    else:
       output_string = output_string + input_string[i].upper()



expected_output_string = 'aNA MERGE LA pIATA'   # am facut manual modificare literelor
assert expected_output_string == output_string