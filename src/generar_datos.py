"""Genera DW_Pasteleria ampliado (datos simulados) -> script SQL Server + CSVs."""
import numpy as np
import pandas as pd
from datetime import date, timedelta
import os, zipfile

rng = np.random.default_rng(2026)
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = str(ROOT / "datasets" / "tablas")
os.makedirs(OUT, exist_ok=True)

INICIO, FIN = date(2025, 11, 1), date(2026, 10, 31)
FECHAS = [INICIO + timedelta(d) for d in range((FIN - INICIO).days + 1)]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# ---------------- Tiempo ----------------
tiempo = pd.DataFrame({
    "TiempoKey": [int(f.strftime("%Y%m%d")) for f in FECHAS],
    "Fecha": FECHAS,
    "Año": [f.year for f in FECHAS],
    "Trimestre": [(f.month - 1) // 3 + 1 for f in FECHAS],
    "Mes": [f.month for f in FECHAS],
    "NombreMes": [MESES[f.month - 1] for f in FECHAS],
    "Semana": [f.isocalendar()[1] for f in FECHAS],
    "Dia": [f.day for f in FECHAS],
    "DiaSemana": [DIAS[f.weekday()] for f in FECHAS],
    "EsFinDeSemana": [1 if f.weekday() >= 5 else 0 for f in FECHAS],
})

# ---------------- Sucursal ----------------
sucursal = pd.DataFrame([
    (1, "S001", "Dulce Tentacion Centro", "Ica", "Av. Municipalidad 150", "Principal", "956123456", 1),
    (2, "S002", "Dulce Tentacion San Isidro", "Ica", "Av. San Martin 250", "Secundaria", "956654321", 1),
    (3, "S003", "Dulce Tentacion Parcona", "Parcona", "Jr. Los Angeles 410", "Secundaria", "956777888", 1),
    (4, "S004", "Dulce Tentacion La Tinguiña", "La Tinguiña", "Av. Principal 89", "Express", None, 1),
], columns=["SucursalKey", "CodigoSucursal", "NombreSucursal", "Distrito", "Direccion",
            "TipoLocal", "Telefono", "Activo"])

# ---------------- Vendedor ----------------
vend_nombres = ["Andrea Garcia", "Miguel Sanchez", "Rosa Quispe", "Camila Herrera", "Daniel Flores",
                "Jhon Huaman", "Patricia Cueva", "Kevin Ore", "Milagros Yupanqui", "Renzo Tasayco",
                "Fiorella Uchuya", "Bruno Hernandez"]
vend_suc = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 1]
vend_cargo = ["Vendedora", "Cajero", "Vendedora", "Vendedora", "Cajero", "Vendedor",
              "Vendedora", "Cajero", "Vendedora", "Vendedor", "Vendedora", "Supervisor"]
vendedor = pd.DataFrame({
    "VendedorKey": range(1, 13),
    "CodigoVendedor": [f"V{i:03d}" for i in range(1, 13)],
    "NombreVendedor": vend_nombres,
    "SucursalKey": vend_suc,
    "Cargo": vend_cargo,
    "FechaIngreso": [date(2024, 1, 10) + timedelta(int(x)) for x in rng.integers(0, 600, 12)],
    "Activo": 1,
})

# ---------------- Producto ----------------
prods = [
    ("Torta de chocolate", "Tortas", "Tortas grandes", 85, 45),
    ("Torta tres leches", "Tortas", "Tortas grandes", 75, 38),
    ("Cheesecake", "Tortas", "Tortas especiales", 90, 48),
    ("Torta de fresa", "Tortas", "Tortas grandes", 80, 42),
    ("Torta selva negra", "Tortas", "Tortas grandes", 88, 46),
    ("Torta de zanahoria", "Tortas", "Tortas especiales", 70, 35),
    ("Torta personalizada", "Tortas", "Tortas especiales", 150, 80),
    ("Brownie", "Postres", "Porciones", 8, 3),
    ("Alfajor", "Postres", "Galletas", 5, 2),
    ("Cupcake de vainilla", "Postres", "Porciones", 7, 2.5),
    ("Galletas artesanales", "Postres", "Galletas", 4, 1.5),
    ("Pie de manzana", "Postres", "Pies", 9, 4),
    ("Milhojas", "Postres", "Porciones", 8, 3.5),
    ("Pie de limon", "Postres", "Pies", 9, 4),
    ("Tajada de torta", "Postres", "Porciones", 10, 4.5),
    ("Empanada de pollo", "Salados", "Empanadas", 6, 3),
    ("Empanada de carne", "Salados", "Empanadas", 6.5, 3.2),
    ("Sandwich de pollo", "Salados", "Sandwiches", 9, 4.5),
    ("Triple", "Salados", "Sandwiches", 8, 3.8),
    ("Croissant", "Panaderia", "Masas", 7, 3),
    ("Pan de yema", "Panaderia", "Panes", 1.5, 0.6),
    ("Chancay", "Panaderia", "Panes", 2, 0.8),
    ("Panetón artesanal", "Panaderia", "Temporada", 45, 22),
    ("Cafe americano", "Bebidas", "Calientes", 6, 2),
    ("Capuccino", "Bebidas", "Calientes", 9, 3.5),
    ("Chocolate caliente", "Bebidas", "Calientes", 8, 3),
    ("Jugo de naranja", "Bebidas", "Naturales", 8, 3),
    ("Limonada", "Bebidas", "Naturales", 7, 2.5),
    ("Frappé de fresa", "Bebidas", "Frías", 12, 4.5),
    ("Agua mineral", "Bebidas", "Frías", 3, 1.2),
]
producto = pd.DataFrame(prods, columns=["NombreProducto", "Categoria", "SubCategoria", "PrecioBase", "CostoBase"])
producto.insert(0, "ProductoKey", range(1, len(prods) + 1))
producto.insert(1, "CodigoProducto", [f"P{i:03d}" for i in producto.ProductoKey])
# Alza de precios desde marzo 2026 (~6% en tortas y bebidas calientes)
alza = producto.Categoria.isin(["Tortas"]) | (producto.SubCategoria == "Calientes")
producto["FactorAlza"] = np.where(alza, 1.06, 1.03)
producto["PrecioVenta"] = (producto.PrecioBase * producto.FactorAlza).round(1)
producto["Costo"] = (producto.CostoBase * producto.FactorAlza).round(2)
producto["UnidadMedida"] = "Unidad"
producto.loc[producto.SubCategoria.isin(["Tortas grandes", "Tortas especiales"]), "UnidadMedida"] = "Unidad"
producto.loc[producto.Categoria == "Bebidas", "UnidadMedida"] = "Vaso"
producto["Activo"] = 1
producto.loc[producto.NombreProducto == "Panetón artesanal", "Activo"] = 0  # producto de temporada

cat_idx = {c: producto.index[producto.Categoria == c].to_numpy() for c in producto.Categoria.unique()}

# ---------------- Clientes con perfiles ocultos ----------------
# perfil: (n_clientes, compras/año, preferencias por categoría, rango cantidad, canales)
perfiles = {
    "Cafetero diario":   (150, 48, {"Bebidas": .50, "Panaderia": .25, "Salados": .17, "Postres": .08, "Tortas": 0}, (1, 3), {"Presencial": .85, "Delivery": .05, "WhatsApp": .10}),
    "Familia fin de semana": (190, 16, {"Postres": .45, "Bebidas": .20, "Panaderia": .15, "Salados": .12, "Tortas": .08}, (2, 6), {"Presencial": .55, "Delivery": .25, "WhatsApp": .20}),
    "Celebraciones":     (120, 7, {"Tortas": .75, "Postres": .20, "Bebidas": .05, "Panaderia": 0, "Salados": 0}, (1, 2), {"Presencial": .25, "Delivery": .30, "WhatsApp": .45}),
    "Ocasional":         (170, 4, {"Postres": .35, "Bebidas": .30, "Salados": .20, "Panaderia": .10, "Tortas": .05}, (1, 2), {"Presencial": .70, "Delivery": .20, "WhatsApp": .10}),
    "Corporativo":       (20, 18, {"Salados": .35, "Postres": .30, "Bebidas": .20, "Tortas": .15, "Panaderia": 0}, (15, 45), {"Presencial": .05, "Delivery": .35, "WhatsApp": .60}),
}
nombres = ["Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Lucia", "Jorge", "Valeria", "Diego",
           "Rosa", "Juan", "Carmen", "Jose", "Elena", "Miguel", "Gabriela", "Ricardo", "Daniela", "Fernando",
           "Paola", "Hector", "Claudia", "Oscar", "Andrea", "Raul", "Veronica", "Victor", "Patricia", "Cesar"]
apellidos = ["Lopez", "Perez", "Torres", "Ramirez", "Mendoza", "Castillo", "Flores", "Diaz", "Rojas", "Vargas",
             "Quispe", "Huaman", "Tasayco", "Uchuya", "Hernandez", "Cabrera", "Munayco", "Aparcana", "Ore", "Yupanqui",
             "Garcia", "Salazar", "Chacaliaza", "Pecho", "Bendezu", "Ramos", "Gutierrez", "Saravia", "Lévano", "Chavez"]
empresas = ["Clinica San Juan", "Colegio San Luis Gonzaga", "Agroexportadora Ica SAC", "Banco Regional Ica",
            "Municipalidad de Parcona", "Hotel Las Dunas", "Vitivinicola Tacama", "Estudio Juridico Ica",
            "Constructora El Sur", "Universidad Privada Ica", "Notaria Ruiz", "Ferreteria Central",
            "Grifo Los Angeles", "Distribuidora Andina", "Inmobiliaria Huacachina", "Laboratorio Biomed",
            "Transportes Soyuz Ica", "Seguros del Sur", "Corporacion Agricola Ica", "Clinica Santa Maria"]
distritos = ["Ica", "Parcona", "La Tinguiña", "Subtanjalla", "Los Aquijes", "Salas", "Pueblo Nuevo"]
dist_p = [.45, .18, .12, .10, .06, .05, .04]
suc_por_dist = {"Ica": [1, 2], "Parcona": [3], "La Tinguiña": [4], "Subtanjalla": [1, 2],
                "Los Aquijes": [4], "Salas": [1], "Pueblo Nuevo": [2]}

clientes, ck = [], 0
for perfil, (n, freq, *_rest) in perfiles.items():
    for i in range(n):
        ck += 1
        if perfil == "Corporativo":
            nombre = empresas[i]
            tipo = "Corporativo"
        else:
            nombre = f"{rng.choice(nombres)} {rng.choice(apellidos)} {rng.choice(apellidos)}"
            tipo = None
        d = rng.choice(distritos, p=dist_p)
        # cliente "nuevo": se registra a mitad de año
        nuevo = perfil != "Corporativo" and rng.random() < 0.15
        if nuevo:
            reg = date(2026, 4, 1) + timedelta(int(rng.integers(0, 180)))
        else:
            reg = date(2023, 1, 1) + timedelta(int(rng.integers(0, 1030)))
        clientes.append(dict(ClienteKey=ck, Perfil=perfil, NombreCliente=nombre, Distrito=d, FechaRegistro=reg,
                             Nuevo=nuevo, TipoCliente=tipo))
cli = pd.DataFrame(clientes)
cli["CodigoCliente"] = [f"C{k:04d}" for k in cli.ClienteKey]
cli["Telefono"] = ["9" + "".join(map(str, rng.integers(0, 10, 8))) for _ in range(len(cli))]
cli["Email"] = [n.split()[0].lower() + n.split()[1].lower().replace("é", "e") + str(rng.integers(1, 99)) + "@gmail.com"
                if p != "Corporativo" else "compras@" + n.split()[0].lower() + n.split()[-1].lower() + ".com.pe"
                for n, p in zip(cli.NombreCliente, cli.Perfil)]
cli["Activo"] = (rng.random(len(cli)) > 0.04).astype(int)

# ---------------- Ventas ----------------
fechas_arr = np.array(FECHAS)
mes_arr = np.array([f.month for f in FECHAS]); dow = np.array([f.weekday() for f in FECHAS])
day_arr = np.array([f.day for f in FECHAS])
# estacionalidad: Navidad, San Valentin, Dia de la Madre, Fiestas Patrias, Vendimia (marzo, Ica)
season = np.ones(len(FECHAS))
season[mes_arr == 12] *= 1.6
season[(mes_arr == 2) & (day_arr >= 10) & (day_arr <= 14)] *= 2.2
season[(mes_arr == 5) & (day_arr >= 5) & (day_arr <= 11)] *= 2.0
season[(mes_arr == 7) & (day_arr >= 25)] *= 1.5
season[mes_arr == 3] *= 1.25
season[mes_arr.astype(int) == 1] *= 0.85  # cuesta de enero
season[mes_arr == 8] *= 0.9

def dist_fechas(perfil, desde):
    w = season.copy()
    if perfil == "Cafetero diario":
        w *= np.where(dow < 5, 1.3, 0.5)
    elif perfil == "Familia fin de semana":
        w *= np.where(dow >= 5, 3.0, 0.6)
    elif perfil == "Corporativo":
        w *= np.where(dow < 5, 1.4, 0.1)
        w[mes_arr == 12] *= 1.8
    elif perfil == "Celebraciones":
        w *= np.where(dow >= 4, 1.6, 0.9)
    w = np.where(fechas_arr >= desde, w, 0)
    return w / w.sum()

rows = []
for c in cli.itertuples():
    n_cli, freq, prefs, qrange, canales = perfiles[c.Perfil]
    desde = max(c.FechaRegistro, INICIO)
    frac = (FIN - desde).days / 365
    n = rng.poisson(freq * frac * rng.uniform(0.6, 1.4))
    if n == 0:
        continue
    p = dist_fechas(c.Perfil, desde)
    idx_f = rng.choice(len(FECHAS), size=n, p=p)
    sucs = suc_por_dist[c.Distrito]
    cats = list(prefs.keys()); cp = np.array(list(prefs.values())); cp = cp / cp.sum()
    for fi in idx_f:
        f = FECHAS[fi]
        # un ticket puede tener 1-3 líneas de producto
        n_lineas = 1 if c.Perfil in ("Celebraciones", "Ocasional") else rng.choice([1, 2, 3], p=[.55, .3, .15])
        s = int(rng.choice(sucs)) if rng.random() < 0.85 else int(rng.integers(1, 5))
        vends = vendedor.VendedorKey[vendedor.SucursalKey == s].to_numpy()
        v = int(rng.choice(vends))
        canal = rng.choice(list(canales.keys()), p=list(canales.values()))
        for _ in range(n_lineas):
            cat = rng.choice(cats, p=cp)
            pi = rng.choice(cat_idx[cat])
            pr = producto.loc[pi]
            # panetón solo nov-dic
            if pr.NombreProducto == "Panetón artesanal" and f.month not in (11, 12):
                pi = rng.choice(cat_idx["Postres"]); pr = producto.loc[pi]
            if pr.Categoria == "Tortas" and c.Perfil != "Corporativo":
                qty = int(rng.choice([1, 1, 1, 2]))
            else:
                qty = int(rng.integers(qrange[0], qrange[1] + 1))
            factor = pr.FactorAlza if f >= date(2026, 3, 1) else 1.0
            precio = round(pr.PrecioBase * factor, 1)
            costo_u = round(pr.CostoBase * factor, 2)
            bruto = qty * precio
            r = rng.random()
            if c.Perfil == "Corporativo" and bruto > 300:
                desc = round(bruto * 0.10, 2)
            elif r < 0.12:
                desc = round(bruto * 0.05, 2)
            else:
                desc = 0.0
            rows.append([int(f.strftime("%Y%m%d")), c.ClienteKey, int(pr.ProductoKey), s, v, qty, precio,
                         round(bruto - desc, 2), desc, round(qty * costo_u, 2), canal])

ventas = pd.DataFrame(rows, columns=["TiempoKey", "ClienteKey", "ProductoKey", "SucursalKey", "VendedorKey",
                                     "Cantidad", "PrecioUnitario", "MontoTotal", "Descuento", "CostoTotal", "CanalVenta"])
ventas = ventas.sort_values("TiempoKey", kind="stable").reset_index(drop=True)

# Outliers: pedidos grandes para eventos (matrimonios, promociones) -> cantidades extremas
out_idx = rng.choice(ventas.index[ventas.ProductoKey.isin(cat_idx["Postres"] + 1)], 25, replace=False)
for i in out_idx:
    q = int(rng.integers(80, 250))
    ventas.loc[i, "Cantidad"] = q
    bruto = q * ventas.loc[i, "PrecioUnitario"]
    ventas.loc[i, "Descuento"] = round(bruto * 0.15, 2)
    ventas.loc[i, "MontoTotal"] = round(bruto * 0.85, 2)
    cu = ventas.loc[i, "CostoTotal"] / max(1, ventas.loc[i, "Cantidad"])
    pk = ventas.loc[i, "ProductoKey"]; f = ventas.loc[i, "TiempoKey"]
    pr = producto.loc[pk - 1]
    ventas.loc[i, "CostoTotal"] = round(q * pr.CostoBase * (pr.FactorAlza if f >= 20260301 else 1), 2)

# Nulos (registro incompleto en caja)
ventas["Descuento"] = ventas["Descuento"].astype(object)
ventas.loc[rng.random(len(ventas)) < 0.03, "Descuento"] = None
ventas.loc[rng.random(len(ventas)) < 0.05, "CanalVenta"] = None
ventas.insert(0, "VentaID", range(1, len(ventas) + 1))

# Nulos en Cliente
cli.loc[(cli.TipoCliente.isna()), "TipoCliente"] = None
compras_cli = ventas.groupby("ClienteKey").size()
def tipo(c):
    if c.Perfil == "Corporativo": return "Corporativo"
    if c.Nuevo: return "Nuevo"
    n = compras_cli.get(c.ClienteKey, 0)
    return "Frecuente" if n >= 25 else "Regular"
cli["TipoCliente"] = [tipo(c) for c in cli.itertuples()]
cli.loc[rng.random(len(cli)) < 0.06, "TipoCliente"] = None
cli.loc[rng.random(len(cli)) < 0.12, "Telefono"] = None
cli.loc[rng.random(len(cli)) < 0.20, "Email"] = None
cli.loc[rng.random(len(cli)) < 0.04, "Distrito"] = None
cli.loc[rng.random(len(cli)) < 0.03, "FechaRegistro"] = None
cliente = cli[["ClienteKey", "CodigoCliente", "NombreCliente", "TipoCliente", "Distrito", "Telefono", "Email",
               "FechaRegistro", "Activo"]]

# ---------------- Compras (reposición semanal) ----------------
proveedores = {"Tortas": ["Distribuidora Dulce Sabor", "Insumos del Sur"],
               "Postres": ["Mayorista San Juan", "Distribuidora Dulce Sabor"],
               "Salados": ["Proveedor Alimentario Ica"], "Panaderia": ["Molinos Ica", "Proveedor Alimentario Ica"],
               "Bebidas": ["Cafe Peru", "Frutas Selectas Ica"]}
vent_sem = ventas.assign(F=pd.to_datetime(ventas.TiempoKey.astype(str)))
vent_sem["Lunes"] = vent_sem.F - pd.to_timedelta(vent_sem.F.dt.weekday, unit="D")
agg = vent_sem.groupby(["Lunes", "ProductoKey", "SucursalKey"]).Cantidad.sum().reset_index()
crows = []
for r in agg.itertuples():
    pr = producto.loc[r.ProductoKey - 1]
    f = (r.Lunes - pd.Timedelta(days=int(rng.integers(1, 4)))).date()
    if f < INICIO: f = INICIO
    q = int(np.ceil(r.Cantidad * rng.uniform(1.0, 1.3)))
    cu = round(pr.CostoBase * (pr.FactorAlza if f >= date(2026, 3, 1) else 1) * rng.uniform(0.95, 1.05), 2)
    crows.append([int(f.strftime("%Y%m%d")), int(r.ProductoKey), int(r.SucursalKey), q, cu, round(q * cu, 2),
                  rng.choice(proveedores[pr.Categoria])])
compras = pd.DataFrame(crows, columns=["TiempoKey", "ProductoKey", "SucursalKey", "CantidadComprada",
                                       "CostoUnitario", "TotalCompra", "Proveedor"])
compras = compras.sort_values("TiempoKey", kind="stable").reset_index(drop=True)
compras["Proveedor"] = compras.Proveedor.astype(object)
compras.loc[rng.random(len(compras)) < 0.04, "Proveedor"] = None
compras.insert(0, "CompraID", range(1, len(compras) + 1))

# ---------------- Atención ----------------
samp = ventas.sample(3500, random_state=7)
arows = []
for r in samp.itertuples():
    tipo_a = rng.choice(["Consulta", "Pedido", "Reclamo", "Seguimiento"], p=[.30, .55, .07, .08])
    base = {"Consulta": 5, "Pedido": 8, "Reclamo": 15, "Seguimiento": 6}[tipo_a]
    carga = 1.4 if r.SucursalKey == 1 else 1.0  # sucursal principal más congestionada
    mins = max(1, int(rng.gamma(4, base * carga / 4)))
    if rng.random() < 0.01: mins = int(rng.integers(60, 120))  # outliers
    recl = int(rng.poisson(1.2)) + 1 if tipo_a == "Reclamo" else int(rng.random() < 0.02)
    cal = 5 - (mins > 12) - (mins > 20) - min(recl, 2) + int(rng.choice([-1, 0, 0, 0, 1]))
    cal = int(np.clip(cal, 1, 5))
    arows.append([r.TiempoKey, r.ClienteKey, r.SucursalKey, r.VendedorKey, mins,
                  cal if rng.random() > 0.10 else None, recl, tipo_a])
atencion = pd.DataFrame(arows, columns=["TiempoKey", "ClienteKey", "SucursalKey", "VendedorKey",
                                        "TiempoAtencionMinutos", "Calificacion", "NroReclamos", "TipoAtencion"])
atencion["Calificacion"] = atencion.Calificacion.astype("Int64")
atencion = atencion.sort_values("TiempoKey", kind="stable").reset_index(drop=True)
atencion.insert(0, "AtencionID", range(1, len(atencion) + 1))

producto_out = producto[["ProductoKey", "CodigoProducto", "NombreProducto", "Categoria", "SubCategoria",
                         "PrecioVenta", "Costo", "UnidadMedida", "Activo"]]

tablas = {"Tiempo": tiempo, "Sucursal": sucursal, "Cliente": cliente, "Producto": producto_out,
          "Vendedor": vendedor, "Ventas": ventas, "Compras": compras, "Atencion": atencion}
for k, v in tablas.items():
    print(f"{k:10s} {len(v):>7,d}")
print("TOTAL", sum(len(v) for v in tablas.values()))

# ---------------- Export CSV ----------------
for k, v in tablas.items():
    v.to_csv(f"{OUT}/{k}.csv", index=False, encoding="utf-8-sig")
with zipfile.ZipFile(f"{OUT}/DW_Pasteleria_CSV.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for k in tablas:
        z.write(f"{OUT}/{k}.csv", f"{k}.csv")

# ---------------- Export SQL ----------------
def lit(x):
    if x is None or (isinstance(x, float) and np.isnan(x)) or x is pd.NA:
        return "NULL"
    if isinstance(x, (date, pd.Timestamp)):
        return f"'{x.strftime('%Y-%m-%d')}'"
    if isinstance(x, str):
        return "N'" + x.replace("'", "''") + "'"
    if isinstance(x, (float, np.floating)):
        return f"{x:.2f}".rstrip("0").rstrip(".") if x != int(x) else str(int(x))
    return str(int(x))

def inserts(nombre, df, identity, cols=None):
    cols = cols or list(df.columns)
    out = []
    if identity: out.append(f"SET IDENTITY_INSERT {nombre} ON;")
    vals = df[cols].astype(object).where(df[cols].notna(), None).values.tolist()
    for i in range(0, len(vals), 1000):
        out.append(f"INSERT INTO {nombre} ({', '.join(cols)}) VALUES")
        out.append(",\n".join("(" + ",".join(lit(x) for x in row) + ")" for row in vals[i:i + 1000]) + ";")
        if i % 5000 == 4000: out.append("GO")
    if identity: out.append(f"SET IDENTITY_INSERT {nombre} OFF;")
    out.append("GO\n")
    return "\n".join(out)

ddl = open(ROOT / "sql" / "ddl.sql", encoding="utf-8").read()
sql = [ddl]
sql.append("SET LANGUAGE Spanish;\nSET DATEFIRST 1;\nGO\n")
sql.append(inserts("Tiempo", tiempo, False))
for k in ["Sucursal", "Cliente", "Producto", "Vendedor", "Ventas", "Compras", "Atencion"]:
    sql.append(inserts(k, tablas[k], True))
sql.append(open(ROOT / "sql" / "final.sql", encoding="utf-8").read())
with open(f"{OUT}/db_Pasteleria_v3.sql", "w", encoding="utf-8-sig") as fh:
    fh.write("\n".join(sql))
