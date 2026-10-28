from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc, when, round as spark_round

spark = SparkSession.builder.appName("AnalisisVentasSuperstore").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

ruta = "/home/vboxuser/superstore_spark/Sample - Superstore.csv"
ventas = spark.read.csv(ruta, header=True, inferSchema=True)

print("\nPRIMERAS CINCO FILAS")
ventas.show(5, truncate=False)

print("\nCOLUMNAS")
print(ventas.columns)

print("\nESQUEMA DE LOS DATOS")
ventas.printSchema()

print("\nTOTAL DE REGISTROS")
print(ventas.count())

print("\nLIMPIEZA DE DATOS")
ventas_limpias = ventas.withColumn("Sales", col("Sales").cast("double"))
ventas_limpias = ventas_limpias.withColumn("Profit", col("profit").cast("double"))
ventas_limpias = ventas_limpias.withColumn("Quantity", col("Quantity").cast("integer"))
ventas_limpias = ventas_limpias.withColumn("Discount", col("Discount").cast("double"))
ventas_limpias = ventas_limpias.dropna(subset=["Sales", "Profit", "Category", "Region"])

print("REGISTROS DESPUES DE LA LIMPIEZA")
print(ventas_limpias.count())

print("\nESTADISTICAS DESCRIPTIVAS")
ventas_limpias.select("Sales", "Quantity", "Discount", "Profit").describe().show()

print("\nVENTAS POR CATEGORIA")
por_categoria = ventas_limpias.groupBy("Category").agg(spark_round(sum("Sales"), 2).alias("Ventas_Totales"), spark_round(sum("Profit"), 2).alias("Ganancia_Total"))
por_categoria.orderBy(desc("Ventas_Totales")).show()

print("\nVENTAS POR REGION")
por_region = ventas_limpias.groupBy("Region").agg(spark_round(sum("Sales"), 2).alias("Ventas_Totales"), spark_round(sum("Profit"), 2).alias("Ganancia_Total"))
por_region.orderBy(desc("Ventas_Totales")).show()

print("\nANALISIS CON RDD")
rdd_ventas = ventas_limpias.select("Category", "Sales").rdd
rdd_totales = rdd_ventas.map(lambda fila: (fila["Category"], fila["Sales"]))
rdd_totales = rdd_totales.reduceByKey(lambda a, b: (a or 0) + (b or 0))
for categoria, total in rdd_totales.collect():
    print(categoria, round(float(total), 2))

print("\nGUARDANDO RESULTADOS PARA GRAFICAS")
por_categoria.coalesce(1).write.mode("overwrite").option("header", True).csv("/home/vboxuser/superstore_spark/resultados_categoria")
por_region.coalesce(1).write.mode("overwrite").option("header", True).csv("/home/vboxuser/superstore_spark/resultados_region")

print("RESULTADOS GUARDADOS CORRECTAMENTE")

spark.stop()


