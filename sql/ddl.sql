/* =====================================================================
   DW_Pasteleria v3 - Pastelería "Dulce Tentación" (Ica)
   DATOS SIMULADOS con fines académicos (nov-2025 a oct-2026)
   Incluye: estacionalidad, alza de precios (mar-2026), nulos y outliers
   ===================================================================== */
USE master;
GO
IF DB_ID('DW_Pasteleria') IS NOT NULL
BEGIN
    ALTER DATABASE DW_Pasteleria SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE DW_Pasteleria;
END
GO
CREATE DATABASE DW_Pasteleria;
GO

USE DW_Pasteleria;
GO

CREATE TABLE Tiempo (
    TiempoKey INT PRIMARY KEY,
    Fecha DATE NOT NULL,
    Año INT NOT NULL,
    Trimestre INT NOT NULL,
    Mes INT NOT NULL,
    NombreMes VARCHAR(20) NOT NULL,
    Semana INT NOT NULL,
    Dia INT NOT NULL,
    DiaSemana VARCHAR(20) NOT NULL,
    EsFinDeSemana BIT NOT NULL
);

CREATE TABLE Cliente (
    ClienteKey INT IDENTITY(1,1) PRIMARY KEY,
    CodigoCliente VARCHAR(20) NOT NULL,
    NombreCliente VARCHAR(100) NOT NULL,
    TipoCliente VARCHAR(50) NULL,
    Distrito VARCHAR(50) NULL,
    Telefono VARCHAR(20) NULL,
    Email VARCHAR(100) NULL,
    FechaRegistro DATE NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE Producto (
    ProductoKey INT IDENTITY(1,1) PRIMARY KEY,
    CodigoProducto VARCHAR(20) NOT NULL,
    NombreProducto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NULL,
    SubCategoria VARCHAR(50) NULL,
    PrecioVenta DECIMAL(10,2) NOT NULL,
    Costo DECIMAL(10,2) NOT NULL,
    UnidadMedida VARCHAR(20) NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE Sucursal (
    SucursalKey INT IDENTITY(1,1) PRIMARY KEY,
    CodigoSucursal VARCHAR(20) NOT NULL,
    NombreSucursal VARCHAR(100) NOT NULL,
    Distrito VARCHAR(50) NULL,
    Direccion VARCHAR(150) NULL,
    TipoLocal VARCHAR(50) NULL,
    Telefono VARCHAR(20) NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE Vendedor (
    VendedorKey INT IDENTITY(1,1) PRIMARY KEY,
    CodigoVendedor VARCHAR(20) NOT NULL,
    NombreVendedor VARCHAR(100) NOT NULL,
    SucursalKey INT NULL,
    Cargo VARCHAR(50) NULL,
    FechaIngreso DATE NULL,
    Activo BIT DEFAULT 1,
    FOREIGN KEY (SucursalKey) REFERENCES Sucursal(SucursalKey)
);

CREATE TABLE Ventas (
    VentaID BIGINT IDENTITY(1,1) PRIMARY KEY,
    TiempoKey INT NOT NULL,
    ClienteKey INT NOT NULL,
    ProductoKey INT NOT NULL,
    SucursalKey INT NOT NULL,
    VendedorKey INT NOT NULL,
    Cantidad INT NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL,
    MontoTotal DECIMAL(10,2) NOT NULL,
    Descuento DECIMAL(10,2) DEFAULT 0.00,
    CostoTotal DECIMAL(10,2) NOT NULL,
    CanalVenta VARCHAR(50) NULL,
    FOREIGN KEY (TiempoKey) REFERENCES Tiempo(TiempoKey),
    FOREIGN KEY (ClienteKey) REFERENCES Cliente(ClienteKey),
    FOREIGN KEY (ProductoKey) REFERENCES Producto(ProductoKey),
    FOREIGN KEY (SucursalKey) REFERENCES Sucursal(SucursalKey),
    FOREIGN KEY (VendedorKey) REFERENCES Vendedor(VendedorKey)
);

CREATE TABLE Compras (
    CompraID BIGINT IDENTITY(1,1) PRIMARY KEY,
    TiempoKey INT NOT NULL,
    ProductoKey INT NOT NULL,
    SucursalKey INT NOT NULL,
    CantidadComprada INT NOT NULL,
    CostoUnitario DECIMAL(10,2) NOT NULL,
    TotalCompra DECIMAL(10,2) NOT NULL,
    Proveedor VARCHAR(100) NULL,
    FOREIGN KEY (TiempoKey) REFERENCES Tiempo(TiempoKey),
    FOREIGN KEY (ProductoKey) REFERENCES Producto(ProductoKey),
    FOREIGN KEY (SucursalKey) REFERENCES Sucursal(SucursalKey)
);

CREATE TABLE Atencion (
    AtencionID BIGINT IDENTITY(1,1) PRIMARY KEY,
    TiempoKey INT NOT NULL,
    ClienteKey INT NOT NULL,
    SucursalKey INT NOT NULL,
    VendedorKey INT NOT NULL,
    TiempoAtencionMinutos INT NOT NULL,
    Calificacion INT NULL,
    NroReclamos INT DEFAULT 0,
    TipoAtencion VARCHAR(50) NULL,
    FOREIGN KEY (TiempoKey) REFERENCES Tiempo(TiempoKey),
    FOREIGN KEY (ClienteKey) REFERENCES Cliente(ClienteKey),
    FOREIGN KEY (SucursalKey) REFERENCES Sucursal(SucursalKey),
    FOREIGN KEY (VendedorKey) REFERENCES Vendedor(VendedorKey)
);
GO
