# Herramienta para la detección rápida de neumonía
Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato DICOM con el fin de clasificarlas en 3 categorías diferentes:

* Neumonía Bacteriana
* Neumonía Viral
* Sin Neumonía

Aplicación de una técnica de explicación llamada Grad-CAM para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

## Uso de la herramienta:
A continuación le explicaremos cómo empezar a utilizarla.

### Requerimientos necesarios para el funcionamiento:

* Instale Docker Desktop del siguiente link: https://www.docker.com/products/docker-desktop/
* En caso de ejecutar la aplicación desde un computador con sistema Windows, intalar Xming: https://sourceforge.net/projects/xming/
* Agregar al repositorio el modelo  preentrenado (conv_MLP_84.h5) el cual se encuentra en: https://drive.google.com/file/d/1AnsMxjT5zk4cqOWDnfJcxMdWiuMcmKjU/view?usp=sharing

### Paso para ejecutar la aplicación desde un contenedor docker

Abra una terminal y ejecute las siguientes instrucciones:

* docker build -t proyecto .
* docker run -it -e DISPLAY=host.docker.Internal:0.0 proyecto **(este comando solo es necesario si se esta bajo el sistema Windows)**

Una vez finalice la creación del contenedor abra Docker Desktop y en la módulo de "contenedores" o "containers" busca la terminal que se encuentra ubicada en la pestaña "Exec", allí ejecutar:
* python detector_neumonia.py

Cuando se ejecute la interfaz gráfica realicé lo siguiente:

* Ingrese la cédula del paciente en la caja de texto
* Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del contenedor
* Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
* Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
* Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
* Presión el botón 'Borrar' si desea cargar una nueva imagen

Para realizar las pruebas unitarias cierre la aplicación e ingrese en la terminal de la pestaña "Exec", allí ejecute el siguiente comando

* pytest -v

## Arquitectura de archivos propuesta.
### detector_neumonia.py
#### Módulo: load_model.py
Descripción: Este módulo se encarga de cargar el modelo preentrenado de la red neuronal convolucional.

Funciones
model_fun(): Carga el modelo CNN desde una ruta especificada y lo retorna.

#### Módulo: preprocess_img.py
Descripción: Este módulo preprocesa las imágenes para que puedan ser ingresadas al modelo.
Funciones
preprocess(array): Redimensiona la imagen a 512x512, la convierte a escala de grises, aplica CLAHE, normaliza la imagen y la convierte a formato batch.

#### Módulo: read_img.py
Descripción: Este módulo lee imágenes en formato DICOM o JPG y las convierte a arreglos para su preprocesamiento.

Funciones
read_dicom_file(path): Lee una imagen DICOM, la convierte a un arreglo y la prepara para su visualización.
read_jpg_file(path): Lee una imagen JPG, la convierte a un arreglo y la prepara para su visualización.

#### Módulo: grad_cam.py
Descripción: Este módulo genera un mapa de calor Grad-CAM para visualizar las regiones importantes de la imagen para la predicción.

Funciones
grad_cam(array): Preprocesa la imagen, obtiene la predicción del modelo y genera el mapa de calor.


#### Módulo: integrador.py
Descripción: Este módulo integra las funcionalidades de los otros módulos para predecir la clase de neumonía y generar el mapa de calor.

Funciones
predict(array): Preprocesa la imagen, carga el modelo, hace la predicción y genera el mapa de calor.


#### Módulo: detector_neumonia.py
Descripción: Este módulo proporciona la interfaz gráfica para la aplicación de detección de neumonía.

Clases y Métodos
App: Clase principal que define la GUI.
__init__(): Inicializa la GUI.
load_img_file(): Carga una imagen desde el sistema de archivos.
run_model(): Ejecuta el modelo de predicción.
save_results_csv(): Guarda los resultados en un archivo CSV.
create_pdf(): Genera un informe en PDF.
delete(): Borra los datos mostrados en la GUI.

### Acerca del Modelo
La red neuronal convolucional implementada (CNN) es basada en el modelo implementado por F. Pasa, V.Golkov, F. Pfeifer, D. Cremers & D. Pfeifer en su artículo Efcient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization.

Está compuesta por 5 bloques convolucionales, cada uno contiene 3 convoluciones; dos secuenciales y una conexión 'skip' que evita el desvanecimiento del gradiente a medida que se avanza en profundidad. Con 16, 32, 48, 64 y 80 filtros de 3x3 para cada bloque respectivamente.

Después de cada bloque convolucional se encuentra una capa de max pooling y después de la última una capa de Average Pooling seguida por tres capas fully-connected (Dense) de 1024, 1024 y 3 neuronas respectivamente.

Para regularizar el modelo utilizamos 3 capas de Dropout al 20%; dos en los bloques 4 y 5 conv y otra después de la 1ra capa Dense.

# Proyecto tomado de: 
https://github.com/dalquinones/UAO-Neumonia

# Proyecto original realizado por:
Isabella Torres Revelo - https://github.com/isa-tr Nicolas Diaz Salazar - https://github.com/nicolasdiazsalazar
