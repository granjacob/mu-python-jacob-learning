
maximo_tablas = 666
maximo_operaciones = 999

contador_tablas = 0
contador_operaciones = 0




while contador_tablas < maximo_tablas:
    while contador_operaciones < maximo_operaciones:
        numero_tabla = contador_tablas + 1
        numero_operacion = contador_operaciones + 1
        print( numero_tabla, " X ", numero_operacion, " = ", numero_tabla * numero_operacion  )
        contador_operaciones += 1
    print()
    contador_tablas += 1
    contador_operaciones = 0


