menu_base.py
def datos_cristian():
    print("mi nombre es Crsitian Espinoza & tengo 29 años. ")
    
def datos_alvaro():
print("Mi nombre es Alvaro y tengo 26 años.")

def datos_ignacio():
print("Mi nombre es Ignacio Montecinos y tengo 23 años.")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
       datos_ignacio()
    elif op == "2":
        datos_alvaro()
    elif op == "3":
        datos_cristian()
        pass # Aquí se llamará a la función del integrante 3
    else:
        print(" Opción inválida.")
