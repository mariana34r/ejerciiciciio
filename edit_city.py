import carga_guarda as gg
def menu():
    menu = ["1. Para editar Nombre", "2. Para editar pais", "3. Para editar Poblacion",]
    for n in menu:
        print(n)
menu()
    
def edit_city():
    data = gg.cargar_city()
    cd_post = int(input())