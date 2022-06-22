#Concatenar cadenas de caracteres
#Supongamos que queremmos crear una cadena que diga:
#Aprende a programar con ___________.

#organizacion = "freeCodeCamp"

#print("Aprende a programar con " + organizacion)
#print("Aprende a programar con {}".format(organizacion))
#print(f"Aprende a programar con {organizacion}") #f-string

#Mad Libs (Historias locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo(plural): ")

madlib = f"¿Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas.¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"  #Alt + Z

print(madlib)