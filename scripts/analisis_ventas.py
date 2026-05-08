import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================
# SCRIPT: analisis_ventas.py
# DESCRIPCIÓN: Analiza el dataset de ventas para calcular
# indicadores clave y generar gráficos de evolución.
# AUTOR: Célula de Desarrollo — Escenario B
# ============================================================

# --- Carga del dataset ---
# Se usa ruta relativa para garantizar reproducibilidad en cualquier entorno
df = pd.read_csv("datos/ventas.csv", parse_dates=["sales_date"])

# --- Calcular monto total por fila ---
# Se multiplica cantidad por precio para obtener el ingreso real por venta
df["total_venta"] = df["quantity"] * df["price"]

# --- Indicador 1: Ventas totales ---
ventas_totales = df["total_venta"].sum()
print(f"💰 Ventas totales del período: ${ventas_totales:,.2f}")

# --- Indicador 2: Producto más vendido ---
# Se agrupa por producto y se suma la cantidad total de unidades vendidas
producto_mas_vendido = df.groupby("product")["quantity"].sum().idxmax()
unidades = df.groupby("product")["quantity"].sum().max()
print(f"🏆 Producto más vendido: {producto_mas_vendido} ({unidades} unidades)")

# --- Indicador 3: Ventas por mes ---
# Se extrae el mes/año de la fecha para agrupar temporalmente
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total_venta"].sum()
print("\n📅 Ventas por mes:")
print(ventas_por_mes.to_string())

# --- Indicador 4: Gráfico de evolución de ventas ---
# Se genera un gráfico de línea para visualizar la tendencia mensual
os.makedirs("resultados", exist_ok=True)

plt.figure(figsize=(10, 5))
ventas_por_mes.plot(kind="line", marker="o", color="steelblue", linewidth=2)
plt.title("Evolución de Ventas Mensuales — 2024", fontsize=14)
plt.xlabel("Mes")
plt.ylabel("Total Vendido ($)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png", dpi=150)
plt.show()
print("\n✅ Gráfico guardado en resultados/grafico_ventas.png")

# ============================================================
# REVISIÓN QA — P3 (Luis)
# - Verificado: sin datos sensibles expuestos
# - Verificado: rutas relativas correctas
# - Verificado: código comentado y reproducible en Colab
# ============================================================
