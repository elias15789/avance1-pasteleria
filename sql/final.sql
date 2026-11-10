SELECT 'Tiempo' AS Tabla, COUNT(*) AS Registros FROM Tiempo
UNION ALL
SELECT 'Cliente', COUNT(*) FROM Cliente
UNION ALL
SELECT 'Producto', COUNT(*) FROM Producto
UNION ALL
SELECT 'Sucursal', COUNT(*) FROM Sucursal
UNION ALL
SELECT 'Vendedor', COUNT(*) FROM Vendedor
UNION ALL
SELECT 'Ventas', COUNT(*) FROM Ventas
UNION ALL
SELECT 'Compras', COUNT(*) FROM Compras
UNION ALL
SELECT 'Atencion', COUNT(*) FROM Atencion;
GO
