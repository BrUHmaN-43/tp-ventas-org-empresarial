# 📊 Análisis de Ventas — Célula de Desarrollo Ágil

> **Trabajo Práctico:** Gestión Colaborativa, Control de Versiones y Organización Empresarial  
> **Cátedra:** Organización Empresarial  
> **Institución:** Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación (TUP) — Modalidad a Distancia  
> **Año Lectivo:** 2026

---

## 👥 Integrantes del Equipo

| Rol | Personaje | Nombre |
|-----|-----------|--------|
| P1 — Líder y Organizador | Hugo | JULIÁN SALCEDO SCARDINO |
| P2 — Desarrollador Técnico | Paco | JULIÁN SALCEDO SCARDINO |
| P3 — Revisor y QA | Luis | JULIÁN SALCEDO SCARDINO |

---

## 📁 Escenario Elegido

**Escenario B — Análisis de Ventas de una Pequeña Empresa**

El proyecto analiza un conjunto de datos simulados de ventas comerciales con el objetivo de generar indicadores clave que permitan interpretar el desempeño de la empresa a lo largo del tiempo.

---

## 🗂️ Estructura del Repositorio

```
tp-ventas-org-empresarial/
│
├── datos/
│   └── ventas.csv               # Dataset de ventas utilizado en el análisis
│
├── scripts/
│   └── analisis_ventas.py       # Script principal de análisis en Python
│
├── resultados/
│   └── grafico_ventas.png       # Gráfico de evolución de ventas generado
│
├── README.md                    # Documentación del proyecto
└── .gitignore                   # Exclusión de archivos innecesarios
```

## 📦 Dataset Utilizado

- **Nombre:** Dataset simulado de ventas comerciales  
- **Formato:** CSV  
- **Fuente:** [gist.github.com/khanusama20](https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6)  
- **Columnas principales:**

| Campo | Descripción |
|-------|-------------|
| `id` | Identificador único del registro |
| `sales_date` | Fecha de la venta |
| `sales_amount` | Monto total de la venta |
| `product` | Nombre del producto vendido |
| `quantity` | Cantidad de unidades vendidas |

---

## 📊 Indicadores Calculados

El script genera los siguientes indicadores:

- ✅ **Ventas totales** del período analizado
- ✅ **Producto más vendido** por cantidad de unidades
- ✅ **Ventas por mes** (agrupación temporal)
- ✅ **Gráfico de evolución** de ventas a lo largo del tiempo

---

## ▶️ Instrucciones para Ejecutar

### Opción 1 — Google Colab (recomendado)

1. Abrir [Google Colab](https://colab.research.google.com)
2. Clonar el repositorio:
```bash
!git clone https://github.com/BrUHmaN-43/tp-ventas-org-empresarial.git
```
3. Navegar a la carpeta del proyecto:
```bash
%cd tp-ventas-org-empresarial
```
4. Ejecutar el script:
```bash
!python scripts/analisis_ventas.py
```
5. Los resultados se guardan automáticamente en la carpeta `/resultados`

### Opción 2 — Entorno local

```bash
git clone https://github.com/BrUHmaN-43/tp-ventas-org-empresarial.git
cd tp-ventas-org-empresarial
pip install pandas matplotlib
python scripts/analisis_ventas.py
```

---

## 🔧 Tecnologías Utilizadas

| Herramienta | Uso |
|-------------|-----|
| Python 3 | Lenguaje de programación principal |
| Pandas | Procesamiento y análisis de datos |
| Matplotlib | Generación de gráficos |
| Git & GitHub | Control de versiones y colaboración |
| Jira | Gestión de tareas y trazabilidad |
| Google Colab | Entorno de ejecución en la nube |

---

## 🔗 Trazabilidad con Jira

Todos los commits de este repositorio siguen el formato de **Conventional Commits** vinculados al tablero de Jira:

PROY-1: Inicializar estructura de carpetas y README
PROY-2: Agregar dataset de ventas en /datos
PROY-3: Desarrollar script de análisis en /scripts
PROY-4: Generar gráfico y exportar resultados

---

## 🔒 Seguridad

- El token de autenticación (PAT) **nunca** se expone en el código ni en el repositorio.
- El archivo `.gitignore` excluye archivos temporales, checkpoints y datos sensibles.

---

## 📋 Gestión del Proyecto

| Herramienta | Enlace |
|-------------|--------|
| Repositorio GitHub | [tp-ventas-org-empresarial](https://github.com/BrUHmaN-43/tp-ventas-org-empresarial) |
| Tablero Jira | https://salcedoscardino456.atlassian.net/jira/software/projects/PROY/boards/36 |
