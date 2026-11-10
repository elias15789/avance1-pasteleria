# Segmentación de clientes · Pastelería Dulce Tentación

**Avance 1 – Inteligencia de Negocios (Zegel).** EDA, limpieza y modelado no supervisado (PCA + K-Means) sobre un año de ventas de una pastelería de Ica.

> Los datos son **simulados con fines académicos** (nov-2025 a oct-2026). El script `src/generar_datos.py` muestra cómo se generaron.

## Resultados principales

| | |
|---|---|
| Ventas analizadas | 16,983 (16,896 después de limpiar) |
| Clientes | 641 |
| PCA | 3 componentes explican el **83 %** de la varianza |
| K-Means | **k = 5**, silhouette **0.47** |
| Hallazgo clave | 22 clientes corporativos (3 %) generan el **44 %** de las ventas |

| Segmento | Clientes | Gasto anual prom. | Días con compra/año |
|---|---|---|---|
| Cafeteros diarios | 149 | S/ 1,055 | 41.6 |
| Familias de fin de semana | 186 | S/ 954 | 14.3 |
| Celebraciones (tortas) | 115 | S/ 571 | 6.1 |
| Ocasionales | 169 | S/ 55 | 3.7 |
| Corporativos | 22 | S/ 14,417 | 15.3 |

## Estructura

```
datasets/   Pasteleria_Ventas_Completo.csv  (una fila por venta, 33 columnas)
notebooks/  Avance1_Pasteleria.ipynb        (análisis completo, genera los 15 gráficos)
outputs/    img/ (gráficos), clientes_segmentados.csv, resultados.json
slides/     Avance1_Pasteleria.pptx         (presentación)
sql/        db_Pasteleria_v3.sql            (base DW_Pasteleria para SQL Server)
src/        generar_datos.py                (generador de los datos simulados)
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
jupyter notebook notebooks/Avance1_Pasteleria.ipynb   # luego "Run All"
```

El notebook lee `datasets/` y guarda los gráficos en `outputs/img/`. También funciona en Google Colab o VS Code (extensiones Python + Jupyter).

## Contenido del notebook (rúbrica)

1. **Problema y datos:** `shape`, `head`, `info`, `describe`.
2. **EDA:** histogramas, barras, dispersión y matriz de correlación.
3. **Limpieza:** nulos (umbral 20 %, recálculo, `ffill`), 87 duplicados, outliers por IQR, `log1p`, `StandardScaler`, retornos mensuales con `.pct_change()`.
4. **Modelo:** PCA (varianza y cargas), K-Means (codo + silhouette), perfil de segmentos e impacto en el negocio.

## Integrantes

José Luis Elías Díaz · Leonel Isais Vargas Huaroto · Thiago Bernardo Pacheco Fajardo · Rick Anderson Arirama del Aguila · Oscar Alejandro Franco Amasifuen · Gian Lucas Valdivia Tomasto · Fabricio Gamaniel Polanco Hernández
