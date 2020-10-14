#CREACION DE UN ACALCULADORA SIMPLE CON FUNCIONES

#DEFINIENDO FUNCIONES

def operations(): #MENU DE OPERACIONES
    print('\n> ADICION ("A")') 
    print('> SUSTRACCION ("S")')
    print('> MULTIPLICACION ("M")')
    print('> DIVISION ("D")')

def addition():
    number_1 = float(input('Ingrese un numero: ')) #PETICIION DE NUMEROS A OPERAR
    number_2 = float(input('Ingrese el siguiente numero: '))
    addition = number_1 + number_2
    print(f'La adicion de {number_1} y {number_2} es: {addition}')

def subtraction():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    subtraction = number_1 - number_2
    print(f'La sustraccion de {number_1} y {number_2} es: {subtraction}')

def multiplication():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    multiplication = number_1 * number_2
    print(f'La multiplication de {number_1} y {number_2} es: {multiplication}')

def division():
    number_1 = float(input('Ingrese un numero: '))
    number_2 = float(input('Ingrese el siguiente numero: '))
    division = number_1 / number_2
    print(f'La division de {number_1} y {number_2} es: {division}')

print(':::::BIENVENIDO A LA CALCULADORA:::::')

control = True

while control == True:
    operations()
    #PIDIENDO AL USUARIO LA INFORMACION DE LA OPERACION MATEMATICA
    operation = input('\nINGRESE LA OPERACIÓN QUE DESEA REALIZAR: ').upper()
    #VALIDANDO LA OPCION INTRODUCIDA POR EL USUARIO
    while operation != 'A' and operation != 'S' and operation != 'M' and operation != 'D':
        print('¡¡ERROR, operación incorrecta!!')
        operation = input('INGRESE LA OPERACIÓN QUE DESEA REALIZAR:  ').upper()

    if operation == 'A': #DESARROLLO DE ACUERDO A LA PETICION DEL USUARIO
        addition()
    elif operation == 'S':
        subtraction()
    elif operation == 'M':
        multiplication()
    else:
        division()

    print('""OPERACIÓN RELAIZADA CON EXITO""') #MENSAJE DE OPERACIÓN EXITOSA

    print('\n> SI ("S")')
    print('> NO ("N")')
    decision = input('\n¿DESEA REALIZAR OTRA OPERACIÓN?: ').upper() #PETICION AL USUARIO PARA CONTINUAR
    
    while decision != 'S' and decision != 'N': #VALIDANDO LA DECISION DEL USUARIO
        print('¡¡ERROR, operación incorrecta!!')
        decision = input('¿DESEA REALIZAR OTRA OPERACIÓN?').upper()

    if decision == 'S':
        control = True #LA VARIABLE control TOMA UN VALOR PARA VOLVER A INGRESAR AL LOOP
    else:
        control = False #LA VARIABLE control TOMA UN VALOR PARA DEJAR DE INGRESAR AL LOOP
    print('HASTA PRONTO')



