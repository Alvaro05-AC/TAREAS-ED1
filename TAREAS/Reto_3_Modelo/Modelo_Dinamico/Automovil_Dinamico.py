class AutomovilDinamico:
    def __init__(self,marca,modelo,año): #Contructor de la clase
        #Diccionario para el modelo Dinamico
        #La clave son los nombres de los atributos
        self.datos={ 
            "marca":marca,
            "modelo":modelo,
            "año": año
        }
        
#Metodos GETTER(para obtener datos)-----------------------------------------------------------------------------
    def get_marca(self):  #DEvuelve la marca del automovil
        return self.datos["marca"]
    
    def get_modelo(self):  #DEvuelve el modelo del automovil
        return self.datos["modelo"]
    
    def get_año(self):  #DEvuelve el año del automovil
        return self.datos["año"]
    

#Metodos SETTER(para modificar datos)-----------------------------------------------------------------
    def set_marca(self, marca):  #Modifica la marca del automovil
        self.datos["marca"]= marca
        
    def set_modelo(self, modelo):  #Modifica el modelo del automovil
        self.datos["modelo"]= modelo
        
    def set_año(self, año):  #Modifica el modelo del automovil
        self.datos["año"]= año
        
        
        