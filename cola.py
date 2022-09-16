import os 
class Nodo:
    def __init__(self,cantidad,tiempo,ingrediente1,ingrediente2,ingrediente3,ingrediente4,ingrediente5) -> None:
        self.cantidad=cantidad
        self.tiempo=tiempo
        self.ingrediente1=ingrediente1
        self.ingrediente2=ingrediente2
        self.ingrediente3=ingrediente3
        self.ingrediente4=ingrediente4
        self.ingrediente5=ingrediente5
        self.siguiente=None
        
    
class Cola:
    def __init__(self) -> None:
        self.primero=None
    
    def encolar(self,cantidad,tiempo,ingrediente1=None,ingrediente2=None,ingrediente3=None,ingrediente4=None,ingrediente5=None):
        if self.primero is None:
            self.primero=Nodo(cantidad,tiempo,ingrediente1,ingrediente2,ingrediente3,ingrediente4,ingrediente5)
            return
        actual=self.primero
        while actual.siguiente!= None:
            actual=actual.siguiente
        actual.siguiente=Nodo(cantidad,tiempo,ingrediente1,ingrediente2,ingrediente3,ingrediente4,ingrediente5) 
    
    def desencolar(self):
        actual=self.primero
        if actual is None:
            return 
        self.primero=actual.siguiente
        actual.siguiente=None
    
    def canti(self):
        a=0
        actual=self.primero
        while actual!=None:
            a+=1
            actual=actual.siguiente
        print(a)

    def generarimg(self):
        actual=self.primero
        if actual:
            var='bgcolor="lightgreen"'
            paso=False
            cadena='digraph { '
            cadena+='label="Cola" \n'
            cadena+='node [shape=none]\n'
            cadena+="n1 [label =\n"
            cadena+='<<TABLE cellspacing="3" cellpadding="10" bgcolor="white">\n'

            
            cadena+="<TR>\n"
            
            while actual!=None:
                if not paso:
                    cadena+=f'<TD {var}>\n'
                    paso=True
                else:
                    cadena+='<TD>\n'
                cadena+=f"Cantidad: {actual.cantidad}\n"
                cadena+=f"<BR/>Tiempo: {actual.tiempo} m\n"
                cadena+="<BR/>Pedidos: \n"
                if actual.ingrediente1!=None:
                    cadena+=f"<BR/>{actual.ingrediente1}\n"
                if actual.ingrediente2!=None:
                    cadena+=f"<BR/>{actual.ingrediente2}\n"
                if actual.ingrediente3!=None:
                    cadena+=f"<BR/>{actual.ingrediente3}\n"
                if actual.ingrediente4!=None:
                    cadena+=f"<BR/>{actual.ingrediente4}\n"
                if actual.ingrediente5!= None:
                    cadena+=f"<BR/>{actual.ingrediente5}\n"
                cadena+="</TD>\n"
                
                actual=actual.siguiente
            
            cadena+="</TR>\n"
            cadena+="</TABLE>>]"
        
            cadena+='}'
            file=open("./nodo.dot","w+") #Escribo un archivo dot
            file.write(cadena) 
            file.close()
            os.system("dot -Tpng ./nodo.dot -o ./Ordenes.png")
        
        else:
            print("La cola está vacía")
            cadena='digraph { '
            cadena+='label="Cola" \n'
            cadena+='node [shape=none]\n'
            cadena+="n1 [label =\n"
            cadena+='<<TABLE cellspacing="3" cellpadding="10" bgcolor="white">\n'
            cadena+="<TR>"
            cadena+="<TD>"
            cadena+="Cola <BR/>de<BR/>ordenes"
            cadena+="</TD>"
            cadena+="</TR>"
            cadena+="</TABLE>>]"
            cadena+='}'
            file=open("./nodo.dot","w+") #Escribo un archivo dot
            file.write(cadena) 
            file.close()
            os.system("dot -Tpng ./nodo.dot -o ./Ordenes.png")