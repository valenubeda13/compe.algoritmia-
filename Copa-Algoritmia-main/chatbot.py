
import difflib # Librería para encontrar coincidencias similares

def cargar_preguntas(nombre_archivo):
    preguntas_respuestas = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        pregunta_actual = ""
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Respuesta:"):
                respuesta = linea.replace("Respuesta:", "").strip()
                preguntas_respuestas[pregunta_actual] = respuesta
            elif linea != "" and linea[0].isdigit() and ")" in linea:
                pregunta_actual = linea.split(")", 1)[1].strip()
    return preguntas_respuestas

def encontrar_pregunta_similar(entrada, lista_preguntas): # Encontrar la pregunta más similar a la entrada del usuario
    coincidencias = difflib.get_close_matches(entrada, lista_preguntas, n=1, cutoff=0.6)
    return coincidencias[0] if coincidencias else None

def chatbot(): #  Cargar preguntas y respuestas desde el archivo
    archivo = "ASISTENTE DE VIAJES.txt"
    preguntas = cargar_preguntas(archivo)
    print("**********************************")
    print("🧳 Bienvenido al Asistente de Viajes. Escribí una pregunta o 'salir' para terminar.")
    print("**********************************")
    
    while True:  # Bucle principal del chatbot
        entrada = input("✈️ Tu pregunta: ").strip()
        if entrada.lower() == "salir":
            print("👋 ¡Gracias por usar el asistente de viajes! ¡Buen viaje!")
            break # Salir del bucle

        pregunta_similar = encontrar_pregunta_similar(entrada, preguntas.keys()) # Buscar pregunta similar
        if pregunta_similar:
            print("💬 Respuesta:", preguntas[pregunta_similar])
        else:
            print("🤔 No tengo esa pregunta. ¿Querés agregarla al archivo? (sí/no)")
            opcion = input("> ").strip().lower()
            if opcion == "sí": # Si el usuario quiere agregar la pregunta
                nueva_respuesta = input("✍️ Ingresá la respuesta: ").strip()
                agregar_pregunta(archivo, entrada, nueva_respuesta)
                preguntas[entrada] = nueva_respuesta
                print("✅ Pregunta agregada con éxito.")

def agregar_pregunta(nombre_archivo, pregunta, respuesta): # Agregar pregunta y respuesta al archivo
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        nuevo_numero = contar_preguntas(nombre_archivo) + 1
        archivo.write(f"\n{nuevo_numero}) {pregunta}\nRespuesta: {respuesta}\n")

def contar_preguntas(nombre_archivo): # Contar el número de preguntas en el archivo
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return sum(1 for linea in archivo if linea.strip().startswith(tuple("1234567890")))

if __name__ == "__main__": # Ejecutar el chatbot
    chatbot()
