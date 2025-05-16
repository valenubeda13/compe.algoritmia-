
def cargar_preguntas(nombre_archivo):
    preguntas_respuestas = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        pregunta_actual = ""
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Respuesta:"):
                respuesta = linea.replace("Respuesta:", "").strip()
                preguntas_respuestas.append((pregunta_actual, respuesta))
            elif linea != "" and ")" in linea and linea[0].isdigit():
                pregunta_actual = linea.split(")", 1)[1].strip()
    return preguntas_respuestas

def buscar_pregunta_por_palabras_clave(entrada_usuario, preguntas_respuestas):
    entrada_usuario = entrada_usuario.lower()
    mejor_match = None
    max_coincidencias = 0

    for pregunta, respuesta in preguntas_respuestas:
        palabras_clave = [palabra for palabra in pregunta.lower().split() if len(palabra) > 3]
        coincidencias = sum(1 for palabra in palabras_clave if palabra in entrada_usuario)
        
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_match = (pregunta, respuesta)
    
    if max_coincidencias >= 2:  # mínimo 2 palabras clave en común
        return mejor_match
    else:
        return None

def chatbot():
    archivo = "ASISTENTE DE VIAJES.txt"
    preguntas_respuestas = cargar_preguntas(archivo)
    
    print("**********************************")
    print("🧳 Bienvenido al Asistente de Viajes. Escribí una pregunta o 'salir' para terminar.")
    print("**********************************")

    entrada = ""
    while entrada != "salir":
        entrada = input("✈️ Tu pregunta: ").strip().lower()
        
        if entrada == "salir":
            print("👋 ¡Gracias por usar el asistente de viajes! ¡Buen viaje!")
        else:
            resultado = buscar_pregunta_por_palabras_clave(entrada, preguntas_respuestas)
            if resultado:
                print("💬 Respuesta:", resultado[1])
            else:
                print("🤔 No encontré una respuesta. ¿Querés agregarla al archivo? (si/no)")
                opcion = input("> ").strip().lower()
                if opcion == "si":
                    nueva_respuesta = input("✍️ Ingresá la respuesta: ").strip()
                    agregar_pregunta(archivo, entrada, nueva_respuesta)
                    preguntas_respuestas.append((entrada, nueva_respuesta))
                    print("✅ Pregunta agregada con éxito.")

def agregar_pregunta(nombre_archivo, pregunta, respuesta):
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        numero = contar_preguntas(nombre_archivo) + 1
        archivo.write(f"\n{numero}) {pregunta.capitalize()}\nRespuesta: {respuesta}\n")

def contar_preguntas(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return sum(1 for linea in archivo if linea.strip().startswith(tuple("1234567890")))

if __name__ == "__main__":
    chatbot()


