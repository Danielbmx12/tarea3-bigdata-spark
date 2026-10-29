Tarea 3: Procesamiento de Datos con Apache Spark

1. Descripción del proyecto

Este proyecto se desarrolla como parte de la Tarea 3 del curso de Big Data y tiene como propósito aplicar herramientas para el procesamiento y análisis de datos mediante Apache Spark. Se implementan dos enfoques: procesamiento por lotes (Batch) y procesamiento de datos en tiempo real mediante la integración de Apache Kafka y Spark Streaming.

Para el procesamiento Batch se utiliza el conjunto de datos Sample - Superstore.csv, que contiene información comercial sobre ventas. Se realizan actividades de carga, limpieza, transformación y análisis para obtener resultados de ventas por categoría y región.

Adicionalmente, se implementa un flujo de procesamiento en tiempo real mediante datos simulados de sensores, que se envían a Kafka y posteriormente son recibidos y procesados por Spark Streaming.

2. Objetivo general

Implementar procesos de procesamiento y análisis de datos mediante Apache Spark, utilizando el procesamiento Batch para analizar información comercial y la integración de Apache Kafka con Spark Streaming para procesar datos en tiempo real.

3. Tecnologías utilizadas

Python: lenguaje utilizado para desarrollar los programas de procesamiento.

Apache Spark 3.5.3: motor de procesamiento distribuido de datos.

Apache Kafka 3.9.2: plataforma utilizada para transmitir los datos entre el productor y el consumidor.

PySpark: interfaz de Python para trabajar con Apache Spark.

Pandas y herramientas de visualización: utilizadas según las necesidades de los scripts de análisis y generación de gráficas.

Git y GitHub: herramientas para el control de versiones y la publicación del código fuente.

Ubuntu: entorno utilizado para ejecutar los procesos.

4. Estructura del proyecto

Los principales archivos y carpetas del repositorio son:

Archivo o carpeta

Descripción

superstore_batch.py

Ejecuta el procesamiento Batch del conjunto de datos Superstore.

graficas_superstore.py

Contiene el código relacionado con la generación de gráficas del análisis.

kafka_producer.py

Genera datos simulados de sensores y los envía al tema de Kafka.

spark_streaming_consumer.py

Lee y procesa los datos recibidos desde Kafka mediante Spark Streaming.

Sample - Superstore.csv

Conjunto de datos utilizado para el análisis comercial.

graficas/

Contiene las visualizaciones generadas durante el análisis.

resultados_categoria/

Carpeta de resultados del análisis por categoría.

resultados_region/

Carpeta de resultados del análisis por región.

5. Procesamiento Batch

El procesamiento Batch permite analizar un conjunto de datos almacenado. En este proyecto se utiliza el archivo Superstore para desarrollar las siguientes actividades:

Cargar los datos desde el archivo CSV.

Revisar y limpiar los registros.

Transformar la información para facilitar su análisis.

Agrupar las ventas por categoría y región.

Obtener resultados que permitan comparar el comportamiento comercial.

Generar visualizaciones para facilitar la interpretación de los resultados.

Ejecución

Desde la terminal de Ubuntu, ingresar a la carpeta del proyecto:

cd ~/superstore_spark

Ejecutar el procesamiento:

python3 superstore_batch.py

Para ejecutar el script de gráficas:

python3 graficas_superstore.py

Los resultados y las gráficas se almacenan en las carpetas correspondientes del proyecto.

6. Procesamiento en tiempo real con Kafka y Spark Streaming

Esta parte del proyecto implementa un flujo de datos que simula la transmisión continua de información de sensores.

Productor de Kafka

El archivo kafka_producer.py genera datos simulados que incluyen:

Identificador del sensor.

Temperatura.

Humedad.

Marca de tiempo.

Los datos generados se envían al tema sensor_data de Kafka.

Consumidor de Spark Streaming

El archivo spark_streaming_consumer.py crea una sesión de Spark, se conecta al servidor de Kafka y lee los mensajes del tema sensor_data. Posteriormente, interpreta la información recibida y presenta los datos procesados en la consola.

Ejecución

Los servicios de Kafka y el tema sensor_data deben estar configurados y activos antes de ejecutar los programas.

Iniciar el productor:

python3 ~/superstore_spark/kafka_producer.py

En otra terminal, ejecutar el consumidor desde la carpeta del proyecto:

cd ~/superstore_spark

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py

La ejecución del consumidor permite observar los datos recibidos y procesados mediante Spark Streaming.

7. Resultados obtenidos

En el procesamiento Batch se realizó la limpieza del conjunto de datos y se analizaron las ventas por categoría. En la ejecución realizada se obtuvieron los siguientes resultados:

Categoría

Ventas totales

Technology

835.900,07

Furniture

733.046,86

Office Supplies

703.502,93

Los resultados muestran que la categoría Technology presentó el mayor total de ventas entre las tres categorías analizadas.

En el procesamiento en tiempo real se generaron y transmitieron datos simulados de sensores mediante Kafka. Spark Streaming recibió los mensajes y presentó información correspondiente al identificador del sensor, la temperatura, la humedad y la marca de tiempo.

8. Visualización y seguimiento

Las gráficas del procesamiento Batch permiten observar las diferencias entre categorías y regiones. Además, la interfaz web de Spark facilita la consulta de información relacionada con la ejecución de las aplicaciones, los trabajos, las etapas y los recursos utilizados.

9. Conclusión

El desarrollo del proyecto permitió aplicar Apache Spark al análisis de datos comerciales mediante procesamiento Batch y explorar el procesamiento continuo de información mediante Kafka y Spark Streaming. La integración de estas herramientas permite comprender diferentes alternativas para transformar, analizar y presentar datos según las necesidades del problema.
