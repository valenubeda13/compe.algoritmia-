import unicodedata
import string


def normalizar (texto):
    texto = texto.lower() #Convierte el texto a minúsculas
    texto = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8") #Elimina los acentos y caracteres especiales
    texto = "".join (c for c in texto if c not in string.punctuation) 
    return texto

def cargar_preguntas_txt(archivo):
    preguntas_respuestas={} #Crea un diccionario vacío
    with open (archivo, mode='r', encoding='utf-8') as f:
        for linea in f:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1) #Separa la línea en pregunta y respuesta
                preguntas_respuestas[normalizar(pregunta)] = normalizar(respuesta)
    return preguntas_respuestas #Devuelve el diccionario con las preguntas y respuestas



def chatbot ():  #esta funcion va a manejar la conversacion 
    
    preguntas = cargar_preguntas_txt("preguntas.txt") #Carga las preguntas y respuestas desde el archivo
    print ("******************************************")
    print (" Chatbot: Hola, soy tu asistente virtual. ¿En que puedo ayudarte?") #Mensaje de bienvenida
    print (" (Escribe salir para terminar.)")
    print ("******************************************")

    while True:
        entrada = input ("Tu: ").strip().lower()
        if entrada == "salir":
            print("Chatbot: Hasta luego.")
            break
        entrada_normalizada = normalizar(entrada) #Normaliza la entrada del usuario
        respuesta = preguntas.get(entrada_normalizada, "Lo siento, no tengo una respuesta para eso.") #Busca la respuesta en el diccionario
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    chatbot() #Ejecuta la función chatbot
    
