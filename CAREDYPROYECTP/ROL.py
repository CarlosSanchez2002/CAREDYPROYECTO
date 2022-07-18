class RolesCAREDY:
    secuencia = 3                                                   #Es un atributo de clase ya que funciona para todas las instancias
    roles = [{"identificacion":1,"rol":"Jefe Seguridad"}, {"identificacion":2,"rol":"Supervisor Seguridad"},{"identificacion":3,"rol":"Guardia"}]
    def __init__(self,descrip):
        RolesCAREDY.secuencia +=1
        self.identificacion= RolesCAREDY.secuencia                         #Atributo de instancia solo pertenecen a la instancia en la que fueron creadas
        self.rol= descrip
        
    def registro(self):
        return {"identificacion":self.identificacion , "rol":self.rol}
        
                
        
    