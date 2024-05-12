import speech_recognition as sr
import requests
from notion.client import NotionClient
from notion_client import Client
from notion.collection import NotionDate

def capture_voice():
    # Crear un objeto Recognizer para reconocimiento de voz
    recognizer = sr.Recognizer()

    # Establecer el umbral de energía
    recognizer.energy_threshold = 4000  # Este valor puede necesitar ajustes dependiendo de tu entorno

    try:
        # Usar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("Di tu comando:")
            # Escuchar al usuario
            audio = recognizer.listen(source, timeout=5)  # Tiempo de espera de 5 segundos

        # Reconocer el comando de voz y convertirlo en texto utilizando Google Speech Recognition
        command = recognizer.recognize_google(audio, language="es-ES")
        print("Comando recibido:", command)
        
        return command

    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error al recuperar resultados; {0}".format(e))
        return ""

def determine_action(command):
    # Convertir el comando a minúsculas para facilitar el procesamiento
    command = command.lower()

    # Definir palabras clave para cada tipo de acción
    create_keywords = ['agrega', 'añade', 'crea', 'inserta']
    update_keywords = ['actualiza', 'modifica', 'edita']
    delete_keywords = ['elimina', 'borra', 'quita']

    # Verificar si alguna de las palabras clave de creación está presente en el comando
    for keyword in create_keywords:
        if keyword in command:
            return 'Crear'

    # Verificar si alguna de las palabras clave de actualización está presente en el comando
    for keyword in update_keywords:
        if keyword in command:
            return 'Actualizar'

    # Verificar si alguna de las palabras clave de eliminación está presente en el comando
    for keyword in delete_keywords:
        if keyword in command:
            return 'Eliminar'

    # Si no se encuentra ninguna palabra clave, devolver None
    return None

def process_command(command):
    # Convertir el comando a minúsculas para facilitar el procesamiento
    command = command.lower()

    # Inicializar variables para almacenar la acción, la categoría y el nombre de la entidad
    action = None
    category = None
    entity_name = None

    # Dividir el comando en palabras
    words = command.split()

    # Buscar la acción (verbo) en el comando
    for word in words:
        if word in ['agrega', 'añade', 'incluye', 'actualiza', 'modifica', 'edita']:
            action = word
            break

    # Buscar la categoría (sustantivo) en el comando
    for word in words:
        if word in ['peliculas', 'movies', 'películas', 'films', 'libros', 'books', 'lugares', 'places']:
            category = word
            break

    # Si se encontraron la acción y la categoría, extraer el nombre de la entidad
    if action and category:
        start_index = words.index(action) + 1
        end_index = words.index(category)
        entity_name = ' '.join(words[start_index:end_index])

        # Verificar si la última palabra es un artículo y eliminarlo si es necesario
        last_word = words[end_index - 1]
        articles = ['a', 'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'en', 'de']
        if last_word in articles:
            entity_name = ' '.join(words[start_index:end_index - 1])

    return action, category, entity_name

def determine_database(category):
    if any(word in category for word in ['peliculas', 'pelicula', 'películas', 'película', 'film', 'films', 'pelis', 'pelís', 'movie', 'movies']):
        return 'Movies'
    elif any(word in category for word in ['libros', 'libro', 'books', 'book']):
        return 'Books'
    elif any(word in category for word in ['lugares', 'lugar', 'places', 'place']):
        return 'Places'
    else:
        return None

def create_record_in_notion_movies(entity_name):
    # Autenticación con el token de integración
    notion = Client(auth="secret_JDEWk68oFM34pBIWch6dKwoqE3x3XEmHFesQByd3hv8")

    # ID de la base de datos
    database_id = "e87c69a9049e428db9aad127166e24c3"

    # Crear una nueva entrada en la base de datos
    new_page = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": entity_name
                        }
                    }
                ]
            },
            "Director": {
                "rich_text": []
            },
            "Release Year": {
                "rich_text": []
            },
            "Genre": {
                "multi_select": []
            },
            # No incluir Status si va a estar vacío
            "Additional Notes": {
                "rich_text": []
            }
        }
    )
    print(f"Registro creado con éxito: {new_page['id']}")

def create_record_in_notion_books(entity_name):
    # Autenticación con el token de integración
    notion = Client(auth="secret_JDEWk68oFM34pBIWch6dKwoqE3x3XEmHFesQByd3hv8")

    # ID de la base de datos
    database_id = "f80d212e99184deaa3329c2d3bbf52f9"

    # Crear una nueva entrada en la base de datos
    new_page = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": entity_name
                        }
                    }
                ]
            },
            "Autor": {
                "rich_text": []
            },
            "Publication Date": {
                "rich_text": []
            },
            "Genre": {
                "multi_select": []
            },
            # No incluir Status si va a estar vacío
            "Additional Notes": {
                "rich_text": []
            }
        }
    )
    print(f"Registro creado con éxito: {new_page['id']}")

def create_record_in_notion_places(entity_name):
    # Autenticación con el token de integración
    notion = Client(auth="secret_JDEWk68oFM34pBIWch6dKwoqE3x3XEmHFesQByd3hv8")

    # ID de la base de datos
    database_id = "56281989a2cc45fab6dc6b6bbf119a8a"

    # Crear una nueva entrada en la base de datos
    new_page = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Place Name": {
                "title": [
                    {
                        "text": {
                            "content": entity_name
                        }
                    }
                ]
            },
            "Place Type": {
                "multi_select": []
            },
        }
    )
    print(f"Registro creado con éxito: {new_page['id']}")

def respond_to_user(response):
    # Función para generar una respuesta al usuario
    pass

def main():
    # Lógica principal del programa
    voice_command = capture_voice()
    print("Comando capturado:", voice_command)
    
    # Procesar el comando capturado
    action, category, entity_name = process_command(voice_command)
    print("Acción:", action)
    print("Categoría:", category)
    print("Nombre de la entidad:", entity_name)
    
    # Determinar el tipo de acción utilizando determine_action
    action_2 = determine_action(voice_command)
    if action_2:
        print("Tipo de acción:", action_2)
    else:
        print("Tipo de acción: No se pudo determinar")
    
    # Determinar la base de datos
    database = determine_database(category)
    
    # Condicionar el llamado a Notion
    if action_2 == 'Crear':
        if database == 'Movies':
            create_record_in_notion_movies(entity_name.title())
        elif database == 'Books':
            create_record_in_notion_books(entity_name.title())
        elif database == 'Places':
            create_record_in_notion_places(entity_name.title())
        else:
            print("No se pudo determinar la base de datos para crear el registro.")
    else:
        print("La acción no es 'Crear', no se realizará ninguna operación.")

if __name__ == "__main__":
    main()
