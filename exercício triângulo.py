real = 0
tipo = 0
def triang_real (a, b, c):
    if a < b + c and b < a + c and c < a + b:
        real = 1
        return (real)
    else:
        return None

def tipo_triang (a, b, c):
    if a == b and a == c:
        tipo = 1
        return (tipo)
    elif a == b or a == c or b == c:
        tipo = 2
        return (tipo)
    else:
        tipo = 3
        return (tipo)

a = float(input('Informe o comprimento do lado A: '))
b = float(input('Informe o comprimento do lado B: '))
c = float(input('Informe o comprimento do lado C: '))

real = triang_real(a, b, c)
if real == 1:
    print(f'Os lados {a, b, c} formam um triângulo...')
    tipo = tipo_triang(a, b, c)
    if tipo == 1:
        print('EQUILÁTERO!')
    elif tipo == 2:
        print ('ISÓSCELES!')
    else:
        print ('ESCALENO!')



