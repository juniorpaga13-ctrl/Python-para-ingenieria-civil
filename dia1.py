# EJERCICIO 1 : Calculadora simple con input + if (suma, resta, multiplicación).

A = float(input("Ingrese 1er número: "))
B = float(input("Ingrese 2do número: "))
    
suma = A + B
multiplicacion = A * B
    
if A>B:
    resta = A - B
elif A == B:
    resta = A - B
else:
    resta = B - A

print(f"Suma de números: {suma}")
print(f"Resta de números: {resta}")
print(f"Multiplicación de números: {multiplicacion}")


# EJERCICIO 2 : Lista de 5 materiales, agrega uno más con append, imprime la lista.
lista_materiales = []

for i in range(1,6):
    materiales = input(f"Ingrese material {i} de construcción: ")
    material_limpio = materiales.strip()
    material_mayuscula = material_limpio.upper()
    lista_materiales.append(material_mayuscula)
    
print(lista_materiales)


# EJERCICIO 3 : Diccionario con 4 materiales y precios, imprime el más caro (usa max con key).

apu_concreto = {
    "Cemento por bolsa": 30,
    "Arena gruesa por m3":70,
    "Varilla de acero #3":26,
    "Varilla de acero #4":34}

material_caro = max(apu_concreto.keys())
mas_caro = apu_concreto[material_caro]

print(f"El material mas caro de esta partida: {material_caro}, con un precio de: s/{mas_caro} por unidad")


# EJERCICIO 4 : While: pide precios de materiales hasta que el usuario escriba 0, calcula promedio.

precios_materiales = []

while True:
    entrada = float(input("Ingresar precio del material (para finalizar ponga '0') s/: "))
    if entrada == 0:
        break
    
    try:
        if entrada <= 0:
            print("El area debe ser mayor que '0' ")
            continue
        
        precios_materiales.append(entrada)
    
    except ValueError:
        print("Entrada invalida, ingrese un número")

if len(precios_materiales) > 0:
    area_total = sum(precios_materiales)
    promedio = area_total/len(precios_materiales)
    
    print(f"Promedio de los materiales ingresados: s/ {promedio:.2f}")
    

# EJERCICIO 5 : 
    # If anidado: según tipo de material (input: "cemento", "fierro", etc.) 
    # indica si necesita "almacenamiento seco" o "protegido de humedad".

tipo_material = input("Ingrese su material: ").strip.lower

print("INGRESE QUE QUE TIPO DE ALMACENAMIENTO REQUIERE EL EQUIPO")
print("Almacenamiento seco: (1)")
print("protegido de humedad: (2)")
tipo_almacenamiento = input("Coloque (1) o (2): ")

if tipo_almacenamiento == 1:
    print(f"El material: {tipo_material}, requiere un 'Almacenamiento seco'")
else:
    print(f"El material: {tipo_material}, requiere un almacenamiento 'protegido de humedad'")