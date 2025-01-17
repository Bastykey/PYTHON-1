def registrar_trabajador(documentos_trabajadores):
    nombres=input("Ingrese el Nombre  y el apellido:")
    cargo=input("Ingrese el cargo del trabajador:")
    sueldo_bruto=float(input("Ingrese el sueldo bruto del trabajador:"))
    descuento_salud=sueldo_bruto*0.07
    descuento_afp=sueldo_bruto*0.12
    liquido_pagar=sueldo_bruto - descuento_afp - descuento_salud
    trabajador={ 
        "nombre":nombres,
        "cargo":cargo,
        "sueldo_bruto":sueldo_bruto,
        "descuento_afp":descuento_afp,
        "descuento_salud": descuento_salud,
        "liquido_pagar": liquido_pagar
    }
    documentos_trabajadores.append(trabajador)
    print("Trabajador agregado con exito :)")
        
    
def lista_trabajadores(trabajadores):
    if not documentos_trabajadores:
        print("No hay trabajadores registrados")
    archivo_lista_trabajadores = "Planilla_lista_trabajadores.txt"
    with open(archivo_lista_trabajadores, "w") as archivo:
        for trabajador in trabajadores:
            archivo.write(f"{trabajador}\n")


def imprimir_planilla_sueldos(lista_trabajadores):
    if not documentos_trabajadores:
        print("No hay trabajadores registrados")
        return

    cargos=["CEO","DESARROLLADOR","ANALISTA DE DATOS"]
    print("Seleccione un cargo:")
    print("0. TODOS")
    print("1. CEO")
    print("2. DESAROLLADOR")
    print("3. ANALISTA DE DATOS")
    op=int(input("ingrese su opcion:"))
    if op==0:
       todos_cargos="todos"
    else:
        todos_cargos=cargos[op-1]
    archivos_nombres="Planilla_todos.txt" if todos_cargos=="todos" else f"planilla_{todos_cargos}" 
    archivo=open(archivos_nombres,"w")
    for trabajador in lista_trabajadores:
        if todos_cargos=="todos" or trabajador['cargo'] == todos_cargos:
            archivo.write(f"{trabajador['nombre']} - {trabajador['cargo']} -  {trabajador['sueldo_bruto']} - {trabajador['descuento_salud']} - {trabajador['descuento_afp']} - {trabajador['liquido_pagar']}\n")
    archivo.close()
    print(f"Planilla de sueldo guardadas en {archivos_nombres}")
documentos_trabajadores=[]
while True:
    print("**********************************")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    print("**********************************")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        registrar_trabajador(documentos_trabajadores)
    elif opcion == 2:
        lista_trabajadores(documentos_trabajadores)
    elif opcion == 3:
        imprimir_planilla_sueldos(documentos_trabajadores)
    elif opcion == 4:
        break
    else:
        print("Opción no válida. Intente de nuevo.")