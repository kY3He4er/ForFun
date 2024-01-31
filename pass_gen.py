import random
import string

def genpas(paslen):
    ltr_upper = string.ascii_uppercase
    ltr_lower = string.ascii_lowercase
    dig = string.digits
    spec = string.punctuation

    #minimo 4 sibolos con caracter de cada tipo
    password = [
        random.choice(ltr_upper),
        random.choice(ltr_lower),
        random.choice(dig),
        random.choice(spec)
    ]

    #completa la longitud restante con caracteres aleatorios
    achar = ltr_upper + ltr_lower + dig + spec
    password += [random.choice(achar) for _ in range(paslen - 4)]

    random.shuffle(password) #mezcla el cacao
    return ''.join(password) #convertir lista en linea

paslen = int(input("Longitud de la contraseña: "))
if paslen < 4:
    print(f"Para una contraseña de {paslen} caracteres no me necesitas. Toma unas de 4!")
    paslen = 4
else:
    print(f"Aqui tienes 5 contraseñas con {paslen} simbolos")
#5 variantes de contraseña para elegir
for i in range(5):
    passd = genpas(paslen)
    print(passd)