
from VALIDACION import ValidacionCAREDY, validar_CAREDY2, validar_CAREDY,validar_CAREDYcedula,validar_CAREDYempleado #Invoca la clase que pertenece a otro modulo
from ROL import RolesCAREDY
from OPERACION import OperacionCAREDY
from EMPLEADOS import EmpleadosCAREDY
from VALIDACION import validar_CAREDY
import os

def cons_datos(cod,indi):
    esp = ""
    if indi == 1:
        for pos in range(0,len(RolesCAREDY.roles)):
            valrls = RolesCAREDY.roles[pos]
            if valrls["identificacion"] == cod:
                esp = valrls["rol"]
    elif indi == 2:
        for pos in range(0,len(OperacionCAREDY.operacions)):
            valope = OperacionCAREDY.operacions[pos]
            if valope["identificacion"] == cod:
                esp = valope["operacion"]
    return esp
def busca_rol(codC):
    c = 0
    for posc in range(0,len(RolesCAREDY.roles)):
        c = RolesCAREDY.roles[posc]
        if c["identificacion"] == codC:
            c = c["rol"]
            break
    return c
def busca_operacion(codD):
    d = 0
    for posd in range(0,len(OperacionCAREDY.operacions)):
        d = OperacionCAREDY.operacions[posd]
        if d["identificacion"] == codD:
            d = d["operacion"]
            break
    return d
def sea_de(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
################################################################################################################################################################################################
                                                #MENU ROL
help = ValidacionCAREDY()
lista = ["1) ROLES","2) OPERACIONES","3) EMPLEADOS","4) SALIR"] #para cambiar por el DEBER
opcion = ""
while opcion !="4":                                                     #la opcion 4 es porque es la opcion SALIR
    opcion = help.menuCAREDY(lista, "MODULO DE SEGURIDAD")            #Funciona con VALIDACION ya que es un titulo
    os.system("cls")                                                    #Sirve para borrar y presentar limpio el identificacion en pantalla
    if opcion == "1":                                                   #Estos son los Menus-Padre, dentro de estos van a estar minimenus
        opc1 =""
        while opc1 !="3":
            os.system("cls") 
            opc1= help.menuCAREDY(["1) CREAR ROL","2) CONSULTAR ROL","3) SALIR"],"MODULO DE ROLES")
            os.system("cls")   
            if opc1 == "1":
                print("*"*20, "INGRESO DE ROLES","*"*20)
                intentos=0
                while True:
                    nombre = input("INGRESO ROL: ")
                    intentos +=1
                    if validar_CAREDY (nombre):
                        print("El rol introducido fue: {}, correcto?".format(nombre))
                        nombrerol= RolesCAREDY(nombre)
                        rol=nombrerol.registro()
                        RolesCAREDY.roles.append(rol)
                        input("Datos ingresados correctamente.")
                        break
                    elif intentos >5:
                        nombre=None
                        print("No cumple los parametros")
                        break
                    
            elif opc1 == "2":
                print("*"*20, "LISTADO DE ROLES","*"*20) 
                print("Identificacion", " "*5, "Descripcion")  
                for nombrerol in RolesCAREDY.roles:
                    cod = nombrerol["identificacion"]
                    des = nombrerol["rol"]
                    print(" " * 2, cod, " " * 15,des)
                input("Presione una tecla para continuar...")
################################################################################################################################################################################################  
                                          #MENU OPERACIONES
    elif opcion == "2":
        opc1 =""
        while opc1 !="3":
            os.system("cls") 
            opc1= help.menuCAREDY(["1) CREAR OPERACION","2) CONSULTAR OPERACION","3) SALIR"],"MANTENIMIENTO DE OPERACIONES")
            os.system("cls")   
            if opc1 == "1":
                print("*"*20, "INGRESO DE OPERACION","*"*20)
                intentos=0
                while True:
                    nombre = input("Ingrese operación: ")
                    intentos +=1
                    if validar_CAREDY2 (nombre):
                        print("La operación introducido fue: {}, correcto?".format(nombre))
                        nombreoperacion= OperacionCAREDY(nombre)
                        operacion=nombreoperacion.registro()
                        OperacionCAREDY.operacions.append(operacion)
                        input("Datos ingresados correctamente.")
                        break
                    elif intentos >5:
                        nombre=None
                        print("No cumple parametros")
                        break
                    
            elif opc1 == "2":
                print("*"*20, "LISTADO DE OPERACIONES","*"*20) 
                print("Identificacion", " "*5, "Descripcion")  
                for nombreoperacion in OperacionCAREDY.operacions:
                    cod = nombreoperacion["identificacion"]
                    des = nombreoperacion["operacion"]
                    print(" " * 2, cod, " " * 15,des)
                input("Presione una tecla para continuar...")

################################################################################################################################################################################################
                                                  #MENU EMPLEADOS

    elif opcion == "3":
        if opcion == "3":
            opc1 = ""
            while opc1 != "3":
                os.system("cls")
                opc1 = help.menuCAREDY(["1) CREAR EMPLEADO", "2) CONSULTAR EMPLEADOS", "3) SALIR"], "MANTENIMIENTO DE EMPLEADOS")
                os.system("cls")
                if opc1 == "1":
                    print("*" * 10, "Ingreso de Empleados", "*" * 10)
                    nombree = input("Ingrese el nombre del Empleado (3-20 Caracteres): ")
                    if validar_CAREDYempleado(nombree):
                        print("El nombre introducido ha sido {}, correcto?".format(nombree))
                    cedul = input("Ingrese número de cédula (inserte solo 10 digitos): ")
                    if validar_CAREDYcedula(cedul):
                        print("Número de cédula registrado correctamente.")
                    rls = int(input("Ingrese código del rol: "))
                    rol3 = busca_rol(rls)
                    while rol3 == 0:
                        print(" El código del rol es inexistente, ingrese identificacion valido.")
                        rls = int(input("Ingrese código del Rol: "))
                        rol3 = busca_operacion(rls)
                    oper = int(input("Ingrese código del Operacion: "))
                    operacion3 = busca_operacion(oper)
                    while operacion3 == 0:
                        print("El código del operacion es inexistente, ingrese identificacion valido.")
                        oper = int(input("Ingrese código del Operacion: "))
                        operacion3 = busca_rol(oper)
                    sueld = input("Ingrese monto de sueldo: $ ")
                    while sea_de (sueld) is False:
                        print("El monto es incorrecto")
                        sueld = input("Ingrese monto de sueldo: $ ")
                    sueld = round(float(sueld), 2)

                    emp = EmpleadosCAREDY(nombree,cedul,rls,oper,sueld)
                    empleado= emp.registro()
                    EmpleadosCAREDY.Empleados.append(empleado)
                    input("Datos ingresados satisfactoriamente, presione una tecla para continuar...")
                elif opc1 == "2":
                    print("*" * 20, "LISTADO DE EMPLEADOS", "*" * 20)
                    print("Identificacion", " " * 3, "Nombre", " "*20, "Cedula", " "*15, "Rol", " "*17, "Operacion", " "*25, "Sueldo")
                    for emp in EmpleadosCAREDY.Empleados:
                        cod = emp["identificacion"]
                        des = emp["nombre"]
                        ced= emp["cedula"]
                        rls= emp["rol"]
                        rls1= cons_datos(rls,1)
                        ope= emp["operacion"]
                        ope1= cons_datos(ope,2)
                        suel= emp["sueldo"]
                        print(" " * 4, cod, " " *(13-len(str(cod))), des, " " * (25-len(str(des))), ced, " " *(21-len(ced)) , rls1," " * (20 -len(str(rls1))),ope1, " "*(35-len(ope1)), suel)
                    input("Presione una tecla para continuar...")

    elif opcion == "4":
            print("Saliendo del programa...\n")
    print("Hasta luego :) ....")