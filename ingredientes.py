from cola import Cola

obj=Cola()
class Nodo:
    def __init__(self,ingrediente,tiempo,cantidad):
        self.ingrediente=ingrediente
        self.tiempo=tiempo
        self.cantidad=cantidad
        self.siguiente=None
    
class Ingrediente:
    def __init__(self):
        self.primero=None
    
    def agregar(self,ingrediente,tiempo,cantidad):
        if self.primero is None:
            self.primero=Nodo(ingrediente,tiempo,cantidad)
            return
        actual=self.primero
        while actual.siguiente!= None:
            actual=actual.siguiente
        actual.siguiente=Nodo(ingrediente,tiempo,cantidad)

    def tiempo(self):
        actual=self.primero
        a=0
        while actual!=None:
            a+=actual.tiempo*actual.cantidad
            actual=actual.siguiente
        return a
    
    def cantid(self):
        b=0
        actual=self.primero
        while actual!=None:
            b+=actual.cantidad
            actual=actual.siguiente
        return b

    def eliminiar(self):
        self.primero=None

    def anniadir(self):
        ingrediente1=None
        ingrediente2=None
        ingrediente3=None
        ingrediente4=None
        ingrediente5=None
        actual=self.primero
        b=self.tiempo()
        c=self.cantid()
        
        while actual!=None:
            if actual.ingrediente=="Salchicha":
                ingrediente1="Salchicha"
            elif actual.ingrediente=="Chorizo":
                ingrediente2="Chorizo"
            elif actual.ingrediente=="Salami":
                ingrediente3="Salami"
            elif actual.ingrediente=="Longaniza":
                ingrediente4="Longaniza"
            elif actual.ingrediente=="Costilla":
                ingrediente5="Costilla"
            actual=actual.siguiente
        
        obj.encolar(c,b,ingrediente1,ingrediente2,ingrediente3,ingrediente4,ingrediente5)
        obj.generarimg()

    def desencolar(self):
        obj.desencolar()
        obj.generarimg()
