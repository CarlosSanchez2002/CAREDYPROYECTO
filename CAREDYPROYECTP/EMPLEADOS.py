class EmpleadosCAREDY:
    secuencia =3
    Empleados = [{"identificacion":1,"nombre":"Carlos", "cedula":"0926015850", "rol":1,"operacion":1,"sueldo":11003.50},
                 {"identificacion":2,"nombre":"Edinson","cedula":"0914592522","rol":2,"operacion":2,"sueldo":5648.40},
                {"identificacion":3,"nombre":"Allison","cedula":"0914592522","rol":3,"operacion":3,"sueldo":3210.10}]

    def __init__(self, nombre, cedula, codRol, codOperacion, sueldo):
        EmpleadosCAREDY.secuencia +=1
        self.identificacion = EmpleadosCAREDY.secuencia 
        self.nombre = nombre
        self.cedula = cedula
        self.rol = codRol
        self.operacion = codOperacion
        self.sueldo = sueldo

    def registro(self):
        return {"identificacion":self.identificacion, "nombre": self.nombre,"cedula":self.cedula, "rol":self.rol, "operacion":self.operacion, "sueldo":self.sueldo}