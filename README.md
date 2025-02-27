# Descripición del proyecto 

Puedes consultar el motor de recomendaciones en el siguiente enlace:
https://motor-recomendaciones-851807229496.us-south1.run.app/

## Identificación de los archivos del repositorio
* **Resultados:** Carpeta que contiene los modelos entrenados previamente para obtener la predicción de recomendaciones basadas en modelos híbridos.
* **templates:** Contiene el sistema de archivos para el despliege de la aplicación web con Vanilla js.
* **App.py:** Código donde se ejecuta el motor de recomendación implementado.
* **Dockerfile:** Archivo con la estructura para el desarrollo de la imagen que contiene el proyecto.
* **Entrenamiento.ipynb:** Cuaderno de jupyter donde se realizó el análisis exploratorio de datos y entrenamiento de los algoritmos utilizados en el motor de recomendaciones.
* **environment.yml:** Archivo que contiene la información necesaria para replicar el entorno virtual con el que se ejecuta la aplicación a partir de su creación con _conda_.

## Implementación y despliegue 
El archivo Dockerfile provee las instrucciones para la construcción de la imagen que permite el despliegue de la aplicación en servicios de la nube como GCP. En términos de la infraestructura que se utilizó, cabe resaltar que se desarrolló una aplicación a través de APIS con Flask, frameworks de python para recomendación como _surprise_, el front-end implicó el desarrolló de una página web estática y sencilla a partir de Vanilla JS, y finalmente el despliegue de la aplicación se realizó a través Cloud Run, la plataforma de GCP para contenedores en la infraestructura de Google, sin servidores.

## Funcionalidad de la aplicación
Para realizar consultas en el motor de recomendaciones diríjase a: https://motor-recomendaciones-851807229496.us-south1.run.app/. Allí encontrará un espacio donde podrá digitar el número de identificación de un cliente, luego de oprimir el botón predecir, se desplegarán en pantalla los productos y servicios que el motor le recomienda a cada usuario en específico.
