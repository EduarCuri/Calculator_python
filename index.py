#CREACION DE UN ACALCULADORA SIMPLE CON FUNCIONES

#DEFINIENDO FUNCIONES
def addition():
    number_1 = float(input('Ingrese un numero: ')) #PETICIION DE NUMEROS
    number_2 = float(input('Ingrese el siguiente numero: '))
    addition = number_1 + number_2
    print(addition)

def subtraction():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    subtraction = number_1 - number_2
    print(subtraction)

def multiplication():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    multiplication = number_1 * number_2
    print(multiplication)

def division():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    division = number_1 / number_2
    print(division)

print(':::::BIENVENIDO A LA CALCULADORA:::::')
print('\n> ADICION ("A")') #MEUN DE OPCIONES PARA EL USUARIO
print('> SUSTRACCION ("S")')
print('> MULTIPLICACION ("M")')
print('> DIVISION ("D")')
#PIDIENDO AL USUARIO LA INFORMACION DE LA OPERACION MATEMATICA
operation = input('\nINGRESE LA OPCIÓN QUE DESEA REALIZAR: ').upper()
#VALIDANDO LA OPCION INTRODUCIDA POR EL USUARIO
while operation != 'A' and operation != 'S' and operation != 'M' and operation != 'D':
    print('ERROR, operacion no encontrada')
    operation = input('Ingrese la inicial del aoperacion que desea realizar nuevamente: ').upper()
#DESARROLLO DE ACUERDO A PETICION
if operation == 'A':
    addition()
elif operation == 'S':
    subtraction()
elif operation == 'M':
    multiplication()
else:
    division()


