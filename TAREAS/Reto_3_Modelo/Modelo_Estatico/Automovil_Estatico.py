class AutomovilEstatico:
    def __init__(self, marca, modelo, año): #Metodo constructor, lo realizamos al crear un objeto de esta clase
        self.datos=[None] * 3 #Creamos una lista de 3 elementos
        self.datos[0]=marca   #Guardamos la marca en la posicion 0
        self.datos[1]=modelo  #Guardamos el modelo en la posicion 1
        self.datos[2]=año     #Guardamos el año en la posicion 2
        
#Metodo GETTER(para obtener Datos)--------------------------------------------------------------
    def get_marca(self):     #Devuelve la marca del automovil
         return self.datos[0]
    
    def get_modelo(self):    #Devuelve el modelo del autonmovil
        return self.datos[1]
    
    def get_año(self):    #Devuelve el año del autonmovil
        return self.datos[2]
    
#Metodos SETTER(para modificar Datos)-----------------------------------------------------------
    def set_marca(self, marca):     #Cambia la marca del automovil
        self.datos[0]= marca
    
    def set_modelo(self, modelo):     #Cambia el modelo del automovil
        self.datos[1]= modelo
        
    def set_año(self, año):        #Cambia el año del automovil
        self.datos[2]= año