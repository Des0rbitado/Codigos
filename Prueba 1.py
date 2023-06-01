sw = 1
# Variables Contador y Acumulador
Cont_Entradas = 0  # Contador para el número total de entradas vendidas
Acum_Total = 0  # Acumulador para el monto total recaudado

Total_Ganancia = 0

Cont_Ni = 0  # Contador para el número de entradas de la categoría "Niño"
Cont_Joven = 0  # Contador para el número de entradas de la categoría "Joven"
Cont_Adulto = 0  # Contador para el número de entradas de la categoría "Adulto"

# Mientras sw no cambie a 0, se mostrará el menú y se seguirá ejecutando el algoritmo
while sw == 1:
    print("===============================")
    print("Bienvenido al Cine Moro")
    print("1. Comprar entrada")
    print("2. Ver total del día")
    print("3. Ver porcentaje del día")
    print("4. Salir")
    print("===============================")

    try:
        opcion = int(input("Seleccione una opción: "))

        # Opción 1: Comprar entrada
        if opcion == 1:
            cantidad = int(input("Ingrese la cantidad de entradas: "))

            print("===============================")
            print("CATEGORÍAS:")
            print("1. Niño [$5500]")
            print("2. Joven [$7000]")
            print("3. Adulto [$9000]")
            categoria = int(input("Seleccione una categoría: "))

            # Comprar entrada de la categoría "Niño"
            if categoria == 1:
                subtotal = cantidad * 5500
                Cont_Ni += cantidad

            # Comprar entrada de la categoría "Joven"
            elif categoria == 2:
                subtotal = cantidad * 7000
                Cont_Joven += cantidad

            # Comprar entrada de la categoría "Adulto"
            elif categoria == 3:
                subtotal = cantidad * 9000
                Cont_Adulto += cantidad

            Cont_Entradas += cantidad
            Acum_Total += subtotal

        # Opción 2: Ver total del día
        elif opcion == 2:
            print("===============================")
            print("Total del día")
            print("********************************")
            print("Cantidad de entradas vendidas:", Cont_Entradas)
            print("Monto total recaudado: $", Acum_Total)

        # Opción 3: Ver porcentaje del día
        elif opcion == 3:
            print("===============================")
            print("Porcentaje del día")
            print("********************************")
            print("Porcentaje de entradas por categoría:")
            total_entradas = Cont_Ni + Cont_Joven + Cont_Adulto
            if total_entradas > 0:
                porcentaje_ni = (Cont_Ni / total_entradas) * 100
                porcentaje_joven = (Cont_Joven / total_entradas) * 100
                porcentaje_adulto = (Cont_Adulto / total_entradas) * 100
                print("Niño:", porcentaje_ni, "%")
                print("Joven:", porcentaje_joven, "%")
                print("Adulto:", porcentaje_adulto, "%")
            else:
                print("No se han vendido entradas aún.")

        # Opción 4: Salir
        elif opcion == 4:
            sw = 0  # Cambia el valor de "sw" a 0 para salir del bucle y terminar el programa

        else:
            print("Opción inválida")

    except ValueError:
        print("Opción inválida")

print("Terminado...")
