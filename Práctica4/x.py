

ocurrencias = []
with open("/Users/frana/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","r") as lineas:
    for linea in lineas:
        if linea[0] != "P":
            ocurrencias.append(linea)

print(len(ocurrencias))