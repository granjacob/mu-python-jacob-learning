# Juego pou

from rich.status import Status

porcentaje_comida = 30
porcentaje_salud = 100
porcentaje_diversion = 80
porcentaje_energia = 90
monedas = 200

compras = {

}

alimentos = {
    'bacon' : { 'cantidad' : 1, 'energia' : 10, 'precio' : 3, 'categoria' : 'comida' },
    'egg' : {  'cantidad' : 1,'energia' : 10, 'precio': 3, 'categoria' : 'comida' },
    'sausages' : {  'cantidad' : 1,'energia': 23, 'precio' : 6, 'categoria' : 'comida' },
    'strawberry_ham' : {  'cantidad' : 1,'energia': 23, 'precio' : 8, 'categoria' : 'comida' },
    'peach_jam' : {  'cantidad' : 1,'energia' : 23, 'precio':8, 'categoria' : 'comida' }
}

ind_exit = False
selected = ""
while not ind_exit:
    print( "1. Status" )
    print( "2. Tienda" )
    print( "3. Comprar")
    print( "4. Alimentarse")
    print( "5. Nevera")
    print( "6. Exit" )
    selected = input("Escoga una opcion: ")

    if selected == "1":
        print( "Status >>" )
        print( "Comida ", porcentaje_comida, "%" )
        print( "Salud ", porcentaje_salud, "%" )
        print( "Diversion ", porcentaje_diversion, "%" )
        print( "Energia ", porcentaje_energia, "%" )


    if selected == "2":
        print( "Tienda >>" )
        for nombre, propiedades in alimentos.items():

            print(f"{nombre}:")
            for propiedad, valor in propiedades.items():
                print(f"  {propiedad}: {valor}")

    if selected == "3":
        print( "Comprar >>" )
        for nombre  in alimentos.items():
            print( f"- {nombre}")
        producto = input( "Escriba el nombre del producto a comprar")
        for nombre, propiedades in alimentos.items():
            if nombre == producto:
                compra = compras.get(nombre)
                if compra is None:
                    compras.__setitem__(nombre, propiedades)
                else:
                    compra['cantidad'] += 1
                    compras.__setitem__( nombre, compra  )
                break

    if selected == "4":
        for nombre in compras.items():
            print( f"   -{nombre}" )

        producto = input("Que quieres comer?")
        for nombre, propiedades in compras.items():
            print( "Comparando ", nombre, " con ", producto )
            if nombre == producto:
                compra = compras.get( nombre )
                if 'energia' in compra:
                    porcentaje_energia += compra['energia']
                if 'comida' in compra:
                    porcentaje_comida += compra['comida']
                if 'salud' in compra:
                    porcentaje_salud += compra['salud']
                if 'diversion' in compra:
                    porcentaje_diversion += compra['diversion']

                compras.__setitem__( nombre, compra )
                break

    if selected == "5":
        print("Nevera >>")
        for nombre, propiedades in compras.items():
            print(f"{nombre} x{propiedades['cantidad']}:")
            for propiedad, valor in propiedades.items():
                print(f"  {propiedad}: {valor}")

    if selected == "6":
        ind_exit = True

