
def eliminar_duplicados(lista):
    duplicados = []
    for i in range(len(lista)-1):
        for e in range(i+1, len(lista)):
            if lista[i] == lista[e] and e not in duplicados:
                duplicados.append(e)
    duplicados.sort(reverse=True)
    for e in duplicados:
        lista.pop(e)
    for i in range(len(lista)):
        tupla = lista[i].strip().split(",")
        tupla.insert(0, i)
        lista[i] = tupla


def separar_tablas(lista, cols, id):
    duplicados = []
    for i in range(len(lista)):
        lista[i] = lista[i].strip().split(",")
        for c in cols:
            lista[i].pop(c)
    for i in range(len(lista)-1):
        for e in range(i+1, len(lista)):
            if lista[i] == lista[e] and e not in duplicados:
                duplicados.append(e)
    duplicados.sort(reverse=True)
    for e in duplicados:
        lista.pop(e)
    if id:
        for i in range(len(lista)):
            lista[i].insert(0, i)


def cambiar_a_id(lista1, lista2, i1, i2):
    for i in range(len(lista1)):
        count = 0
        busqueda = f"{lista1[i][i1]}"
        for e in range(len(lista2)):
            if busqueda == lista2[e][i2]:
                count += 1
                #if count > 1:
                    #print(f"rep:{busqueda}-> {lista1[i][i1]}-{lista2[e][i2]}")
                lista1[i][i1] = lista2[e][0]


def cambiar_a_id_cond(lista1, lista2, i1, i2, i3, i4):
    for i in range(len(lista1)):
        count = 0
        busqueda = f"{lista1[i][i1]}"
        for e in range(len(lista2)):
            if busqueda == lista2[e][i2] and lista1[i][i3] == lista2[e][i4]:
                count += 1
                #if count > 1:
                    #print(f"rep:{busqueda}-> {lista1[i][i1]}-{lista2[e][i2]}")
                lista1[i][i1] = lista2[e][0]


def formato_fecha(fecha):
    f1 = fecha.strip().split("/")
    if len(f1) < 2:
        print(f1)
    fecha2 = f"{f1[2]}-{f1[1]}-{f1[0]}"
    return fecha2


# CARGAR DATOS


def cargar_productoras():
    with open("Datos Pares/Productoras.csv", encoding="utf-8") as f:
        productoras = f.readlines()[1:]
        eliminar_duplicados(productoras)
    return productoras


def cargar_eventos():
    with open("Datos Pares/Evento.csv", encoding="utf-8") as f:
        eventos = f.readlines()[1:]
        separar_tablas(eventos, [4], True)
    return eventos


def cargar_recintos():
    with open("Datos Pares/Recinto.csv", encoding="utf-8") as f:
        recintos = f.readlines()[1:]
        eliminar_duplicados(recintos)
    return recintos


def cargar_entradas():
    with open("Datos Pares/Entradas.csv", encoding="utf-8") as f:
        entradas = f.readlines()[1:]
        eliminar_duplicados(entradas)
    return entradas


def cargar_artistas():
    with open("Datos Pares/Artistas.csv", encoding="utf-8") as f:
        artistas = f.readlines()[1:]
        eliminar_duplicados(artistas)
    return artistas


def cargar_eventos_artistas():
    with open("Datos Pares/Evento.csv", encoding="utf-8") as f:
        eventos_artistas = f.readlines()[1:]
        separar_tablas(eventos_artistas, [5, 3, 1], False)
        for t in eventos_artistas:
            art = t[2]
            t[2] = t[1]
            t[1] = art
    return eventos_artistas


###################################################################

productoras = cargar_productoras()
eventos = cargar_eventos()
recintos = cargar_recintos()
entradas = cargar_entradas()
artistas = cargar_artistas()
artistas_eventos = cargar_eventos_artistas()


cambiar_a_id(eventos, recintos, 2, 1)
cambiar_a_id(eventos, productoras, 5, 1)
cambiar_a_id(entradas, eventos, 1, 1)
cambiar_a_id_cond(artistas_eventos, eventos, 0, 1, 2, 3)
cambiar_a_id(artistas_eventos, artistas, 1, 1)


with open("productora.csv", "w") as f:
    for t in productoras:
        t[3] = formato_fecha(t[3])
        print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]}", file=f)

with open("evento.csv", "w") as f:
    for t in eventos:
        t[3] = formato_fecha(t[3])
        t[4] = formato_fecha(t[4])
        print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]}", file=f)

with open("recinto.csv", "w") as f:
    for t in recintos:
        print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]}", file=f)

with open("entrada.csv", "w") as f:
    for t in entradas:
        print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]}", file=f)

with open("artista.csv", "w") as f:
    for t in artistas:
        print(f"{t[0]},{t[1]},{t[2]}", file=f)

with open("Artista_Evento.csv", "w") as f:
    for t in artistas_eventos:
        t[2] = formato_fecha(t[2])
        print(f"{t[0]},{t[1]},{t[2]}", file=f)
