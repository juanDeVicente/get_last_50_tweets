# get_last_50_tweets
Repositorio para la práctica 3 de la asignatura de <b>verificación y desarrollo de programas</b>.
## Autores
<a href="https://github.com/juanDeVicente">Juan de Vicente</a><br>
<a href="https://github.com/JaimeEscribano">Jaime Escribano</a><br>
<a href="https://github.com/Ayato27">Raúl Matrinez</a><br>
<a href="https://github.com/PaulaPascual">Paula Pascual</a><br>
<a href="https://github.com/ClaudiaRodriguezM">Claudia Rodríguez</a>
## Instrucciones de instalación
1. Clonar el repositorio git.
2. Instalar las librerias listadas en <a href="https://github.com/juanDeVicente/get_last_50_tweets/blob/master/requirements.txt">requirements.txt</a>
3. Abrir la consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import nltk
    >>> nltk.download()
    ```
    En la ventana emergente seleccionar la pestaña CORPORA.
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-43.png)
    
    En la pestaña seleccionar el "identifier" stopwords y hacer click en el botón de "Download".
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-44.png)
4. Añadir tus creedenciales de <a href="https://developer.twitter.com/en/apply-for-access">desarrollador de twitter</a> a las variables de entorno de Python.<br>
    Abrir una consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import os
    >>> os.environ['ACCESS_TOKEN_KEY'] = 'ACCESS_TOKEN_KEY'
    >>> os.environ['ACCESS_TOKEN_SECRET'] = 'ACCESS_TOKEN_SECRET'
    >>> os.environ['CONSUMER_KEY'] = 'CONSUMER_KEY'
    >>> os.environ['CONSUMER_SECRET'] = 'CONSUMER_SECRET'
    ```
## Instrucciones para ejecutar los tests
1. Abrir la terminal
2. Ejecutar el siguiente comando para ejecutar todos los tests disponibles:
    ```
    <rutapython> <rutaproyecto> Python -m pytest tests/ -v
    ```
3. Ejecutar el siguiente comando para ejecutar los tests de "twitter_word_count.py":
    ```
    <rutapython> <rutaproyecto> -m pytest tests/twitter_word_count_test.py -v
    ```
## Instrucciones para ejecutar las pruebas
1. Abrir la terminal
2. Ejecutar el siguiente comando para ejecutar la prueba de "twitter_word_count_test.py":
    ```
    <rutapython> <rutaproyecto>/twitter_word_count.py
    ```
