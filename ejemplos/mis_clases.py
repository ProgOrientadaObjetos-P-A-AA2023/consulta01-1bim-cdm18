"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Auto:
    def __init__(self, cilindraje, gama, precio, marca):
        self.cilindraje = cilindraje
        self.gama = gama
        self.precio = precio
        self.marca = marca
       
    def establecerCilindraje (self, cili):
        cilindraje = cili
    def establecerGama (self, gam):
        gama = gam

    def establecerPrecio (self,preci):
        precio = preci

    def establecerMarca (self, marc):
        marca = marc


    def obtenerCilindraje (self):
        return self.cilindraje
    
    def obtenerGama (self):
        return self.gama

    def obtenerPrecio (self):
        return self.precio

    def obtenerMarca (self):
        return self.marca

    def __str__(self):
        mensaje = (f"El auto de marca: {self.marca}\nCilindraje: {self.cilindraje} CC\nGama: {self.gama}\nPrecio: ${self.precio}")
        return mensaje


# clase 02
class Avion:
    def __init__(self, marca:str, aerolinea:str, tipo:str, precio:float):
        self.marca = marca
        self.aerolinea = aerolinea
        self.tipo_avion = tipo
        self.precio = precio
    
    def establecerMarca (self, marc):
        marca = marc
    def establecerAerolinea (self, aero):
        aerolinea = aero

    def establecerPrecio (self,preci):
        precio = preci

    def establecerTipo (self, tip):
        tipo_avion = tip


    def obtenerMarca (self):
        return self.marca
    
    def obtenerAerolinea (self):
        return self.aerolinea

    def obtenerTipo (self):
        return self.tipo_avion

    def obtenerPrecio (self):
        return self.precio 

    

    def __str__(self):
        mensaje = (f"Avion de marca: {self.marca}\nAerolinea: {self.aerolinea} \nTipo: {self.tipo_avion}\nPrecio: $ {self.precio}")
        return mensaje
