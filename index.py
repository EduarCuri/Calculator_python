#SOFTWARE DE PRUEBA
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

#PIDIENDO AL USUARIO LA INFORMACION DE LA OPERACION MATEMATICA
operation = input('Ingrese la inicial de la operacion que desea realizar: ')
#VALIDANDO LA OPCION INTRODUCIDA POR EL USUARIO
while operation != 's' and operation != 'r' and operation != 'm' and operation != 'd':
    print('ERROR, operacion no encontrada')
    operation = input('Ingrese la inicial del aoperacion que desea realizar nuevamente: ')
#DESARROLLO DE ACUERDO A PETICION
if operation == 's':
    addition()
elif operation == 'r':
    subtraction()
elif operation == 'm':
    multiplication()
else:
    division()


