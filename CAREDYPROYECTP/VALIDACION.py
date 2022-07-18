class ValidacionCAREDY:
    def __init__(self):
        pass
    def menuCAREDY (self, opciones,titulo):
        print("*"*20,titulo,"*"*20) #Ayuda a la aparicion de los titulos a lo largo del identificacion
        for opcion in opciones:
            print(opcion)
        opc= input ("elija opcion 1...{}: " .format(len(opciones)))
        return opc
    
def validar_CAREDY(validar):
    if len(validar)>20:
        print("Ingrese una cantidad menor a 20 rlsacteres")
    elif len(validar) <1:
        print("Ingrese una cantidad mayor a 1 rlsacter")
    else: 
        print("Datos ingresados correctamente")
        return True
    
def validar_CAREDY2(validar):
    if len(validar)>20:
        print("Ingrese una cantidad menor a 20 rlsacteres")
    elif len(validar) <5:
        print("Ingrese una cantidad mayor a 5 rlsacter")
    else: 
        print("Datos ingresados correctamente")
        return True

def validar_CAREDYempleado(empl):
    while (len(empl) < 3 or len(empl) > 20):
        print(" Incorrecto, Nuevamente ingrese ")
        empl = input("   NOMBRE: ")
    return empl
def validar_CAREDYcedula(cedula):
    while len(cedula) != 10 or not cedula.isdigit():
        print("Incorrecto, Ingrese cédula de 10 dígitos")
        cedula = input("   CEDULA: ")
    return cedula


