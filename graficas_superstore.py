import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

base = os.path.expanduser("~/superstore_spark")
carpeta = os.path.join(base, "graficas")
os.makedirs(carpeta, exist_ok=True)

categorias = ["Technology", "Furniture", "Office Supplies"]
ventas_categoria = [835900.07, 733046.86, 703502.93]

plt.figure(figsize=(9, 5))
barras = plt.bar(categorias, ventas_categoria)

plt.title("Ventas totales por categoria")
plt.xlabel("Categoria")
plt.ylabel("Ventas")
plt.bar_label(barras, fmt="%.2f", padding=3)
plt.tight_layout()

plt.savefig(os.path.join(carpeta, "ventas_categoria.png"), dpi=150)
plt.close()

regiones = ["West", "East", "Central", "South"]
ventas_region = [713471.34, 672194.05, 497800.87, 388983.59]

plt.figure(figsize=(9, 5))
barras = plt.bar(regiones, ventas_region)

plt.title("Ventas totales por region")
plt.xlabel("Region")
plt.ylabel("Ventas")
plt.bar_label(barras, fmt="%.f2", padding=3)
plt.tight_layout()

plt.savefig(os.path.join(carpeta, "ventas_region.png"), dpi=150)
plt.close()

print("GRAFICAS GUARDADAS CORRECTAMENTE")
print("Ubicacion", carpeta)
print("Archivo 1: ventas_categoria.png")
print("Archivo 2: ventas_region.png")
