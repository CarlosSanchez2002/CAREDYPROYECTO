class OperacionCAREDY:
    secuencia = 3  #Es un atributo de clase ya que funciona para todas las instancias
    operacions = [{"identificacion":1,"operacion":"Acceso Videovigilancia y Alarma"}, {"identificacion":2,"operacion":"Vigilar Cámara"},{"identificacion":3,"operacion":"N/A"}]
    def __init__(self,descrip):
        OperacionCAREDY.secuencia +=1
        self.identificacion= OperacionCAREDY.secuencia  #Atributo de instancia solo pertenecen a la instancia en la que fueron creadas
        self.operacion= descrip

    def registro(self):
        return {"identificacion":self.identificacion, "operacion":self.operacion}