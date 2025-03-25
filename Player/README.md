Documentación de la Aplicación de Reproducción de Música
1. Requisitos del Sistema
Para ejecutar correctamente la aplicación, asegúrese de contar con los siguientes requisitos:
1.1 Versión de Python
•	Python 3.1.0 o superior
1.2 Paquetes Necesarios
Antes de ejecutar la aplicación, instale las dependencias necesarias con:
pip install flask
2. Estructura del Proyecto
/musica_app/
│── app.py
│── /templates/
│   ├── index.html
│── /static/
│   ├── styles.css
│   ├── script.js
│── /songs/
•	app.py : Archivo principal que ejecuta la aplicación Flask.
•	/templates/index.html : Interfaz de usuario en HTML.
•	/static/styles.css : Archivo de estilos CSS.
•	/static/script.js : Lógica de interacción con el frontend.
•	/songs/ : Carpeta donde se almacenan los archivos de música en formato MP3.
3. Ejecución de la Aplicación
Para ejecutar la aplicación, use:
python app.py
La aplicación estará disponible en: http://127.0.0.1:5000
4. Endpoints de la API
4.1 Obtener todas las canciones
GET /songs Devuelve una lista de canciones disponibles.
4.2 Marcar/Desmarcar Favorito
POST /favorite
•	Parámetro JSON: {“title": "Nombre de la canción”}
•	Alterna el estado de favorito de una canción.
4.3 Obtener canciones favoritas
GET /favorites Devuelve la lista de canciones favoritas.
4.4 Obtener un archivo de música
GET /songs/<nombre_archivo> Devuelve el archivo MP3 correspondiente.
5. Funcionalidades Claves
•	Reproducción de canciones almacenadas en la carpeta songs/.
•	Administración de una lista de favoritos.
•	Control de reproducción: adelantar, retroceder, pausar y cambiar de canción.
•	Búsqueda de canciones.
•	Modo oscuro en la interfaz.
6. Notas Adicionales
•	La aplicación solo soporta archivos .mp3.
•	Se recomienda almacenar los archivos de música en songs/ antes de iniciar la aplicación esto si quiere agregar una canción y que se mantenga en la carpeta.
