import letreros

print("Binevenido :)")
print("Ingrese su Nombre Usuario")
Nombre=input("-")
print("Binevenido",Nombre)
while True:
    print("Que desea hacer ")
    print("\n.1 Crear cuidades\n2.Editar Cuidades\n3.Mostrar Cuidades\n4.Buscar Cuidades\n5.Salir")
    print("Escoga una Opcion")
    try:
        opc = input("-")
        if opc == '1':
            letreros.letrero1()
        elif opc == '2':
            letreros.letrero2()
        elif opc == '3':
            letreros.letrero3()
        elif opc == '4':
            letreros.letrero4()
        elif opc == '5':
            letreros.letrero5()
            break  
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
    
    except Exception as e:
        print(f"Se ha producido un error: {e}")
        print("HOLA MUNDO..")
        
        
        
