def primo():

    n = int(input("Ingrese un número: "))

    es_primo = True

    if n < 2:
        es_primo = False

    for i in range(2, n):

        if n % i == 0:
            es_primo = False

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

primo()