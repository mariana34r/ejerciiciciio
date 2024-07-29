import carga_guarda as gg

def reg_city():
    data = gg.cargar_city()
    datos = {}
    cd_postal = int(input("Digite el codigo postal de la ciudad que va a crear: "))
    if str(cd_postal) in data["ciudades"]:
        print("Ya existe una ciudad con este codigo postal")
    datos["Nombre"] = str(input("Digite el nombre de la ciudad: "))
    datos["Pais"] = str(input("Digite el pais donde se encuentra esta ciudad: "))
    datos["Poblacion"] = int(input("Digite la poblacion de la ciudad: "))
    datos["Codigo posatal"] = cd_postal
    data["ciudades"][cd_postal] = datos
    gg.guarda_city(data)
    
