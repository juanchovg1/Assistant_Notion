Proyecto de Asistente de Voz para Notion
Este proyecto es un asistente de voz que interactúa con bases de datos de Notion para realizar operaciones como agregar, actualizar o eliminar registros. Utiliza reconocimiento de voz para interpretar los comandos del usuario y actuar en consecuencia en las bases de datos de Notion.

Requisitos
Python 3.x
Instala las dependencias necesarias utilizando el siguiente comando:
bash
Copy code
pip install -r requirements.txt
Configuración de Tokens de Notion
Antes de ejecutar el programa, asegúrate de configurar los tokens de integración para autenticarte con la API de Notion. Necesitarás obtener tu token de integración desde la configuración de Notion y reemplazar los placeholders YOUR_SECRET_TOKEN, YOUR_MOVIES_DATABASE_ID, YOUR_BOOK_DATABASE_ID y YOUR_PLACES_DATABASE_ID en el código con tus propios tokens y IDs de base de datos respectivamente.

Estructura de las Bases de Datos
Base de Datos de Películas (Movies): Ejemplo duplicable -> https://juanvillota.notion.site/e87c69a9049e428db9aad127166e24c3?v=bdc7985fba114c4481def8d6812ebbfd&pvs=4 
Título: Texto (Title)
Director: Texto (Director)
Año de Estreno: Texto (Release Year)
Género: Selección Múltiple (Genre)
Notas Adicionales: Texto (Additional Notes)
Base de Datos de Libros (Books): Ejemplo duplicable -> https://juanvillota.notion.site/f80d212e99184deaa3329c2d3bbf52f9?v=18cbdb91c2f349cfa1b93f32b1184883&pvs=4
Título: Texto (Title)
Autor: Texto (Author)
Fecha de Publicación: Texto (Publication Date)
Género: Selección Múltiple (Genre)
Notas Adicionales: Texto (Additional Notes)
Base de Datos de Lugares (Places): Ejemplo duplicable -> https://juanvillota.notion.site/56281989a2cc45fab6dc6b6bbf119a8a?v=b41ecff8f3f841729eb48f4ce72c7cb7&pvs=4
Nombre del Lugar: Texto (Place Name)
Tipo de Lugar: Selección Múltiple (Place Type)
Ejecución del Programa
Una vez que hayas configurado tus tokens de Notion y asegurado la estructura de las bases de datos, puedes ejecutar el programa assistant.py. El asistente capturará tu comando de voz, procesará la acción y la categoría correspondientes, y realizará la operación en la base de datos correspondiente de Notion.

¡Disfruta interactuando con tu asistente de voz para Notion!

