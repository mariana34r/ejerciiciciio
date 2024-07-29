import carga_guarda as gg
def menu():
    menu = ["1. Para editar Nombre", "2. Para editar pais", "3. Para editar Poblacion","4. Para salir"]
    for n in menu:
        print(n)

    
def edit_city():
    while True:
        data = gg.cargar_city()
        cd_post = int(input("Digite el codigo postal de la ciudad que quieres editar: "))
        if str(cd_post) in data["ciudades"]:
            menu()
            op = int(input("Seleccione una opcion: "))
            
            if op ==1:
                nuevo = str(input("Digite el nuevo nombre de la ciudad: "))
                data["ciudades"][str(cd_post)]["Nombre"] = nuevo
                gg.guarda_city(data)
                break
            elif op ==2:
                nuevo = str(input("Digite el nuevo nombre del pais: "))
                data["ciudades"][str(cd_post)]["Pais"] = nuevo
                gg.guarda_city(data)
                break
            elif op ==3:
                nuevo = int(input("Digite la nueva poblacion: "))
                data["ciudades"][str(cd_post)]["Poblacion"] = nuevo
                gg.guarda_city(data)
                break            
            gg.guarda_city(data)
        else:
            print("No hay ninguna ciudad con este codigo postal")

