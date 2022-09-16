from ingredientes import Ingrediente
obj=Ingrediente()
def preparar():
    op=""
    while op!="6":
        print("1.Salchicha")
        print("2.Chorizo")
        print("3.Salami")
        print("4.Longaniza")
        print("5.Costilla")
        print("6.Ordenar")
        print("7.Regresar")
        op=input("Ingrese opción:\n")
        if op=="1":
            opcion=int(input("Ingrese cantidad:\n"))
            obj.agregar("Salchicha",2,opcion)
        elif op=="2":
            opcion=int(input("Ingrese cantidad:\n"))
            obj.agregar("Chorizo",3,opcion)
        elif op=="3":
            opcion=int(input("Ingrese cantidad:\n"))
            obj.agregar("Salami",1.5,opcion)
        elif op=="4":
            opcion=int(input("Ingrese cantidad:\n"))
            obj.agregar("Longaniza",4,opcion)
        elif op=="5":
            opcion=int(input("Ingrese cantidad:\n"))
            obj.agregar("Costilla",6,opcion)
        elif op=="6":
            obj.anniadir()
            obj.eliminiar()
            menu()
        elif op=="7":
            menu()
            

def menu():
    print("****Menu****")
    print("1.Prepara tu shuco")
    print("2.Despachar")
    print("3.Información")
    print("4.Salir")
    opc=input("Elija una opcion: \n")

    if opc=="1":
        preparar()

    if opc=="2":
        obj.desencolar()
        menu()
    if opc=="3":
        print("Nombre: Raúl Josue Castillo Barco")
        print("Carnet: 202001932")
        menu()
    if opc=="4":
        exit()
menu()


