
/* tiket promedio */
/*ya funciona*/
SELECT 
  ROUND(
    SUM(cant_producto)/COUNT(DISTINCT orden_compra), 2) AS avg_cant_producto_por_orden
FROM HechoVentas HV 
LEFT JOIN DimFecha DF 
  ON HV.id_fecha = DF.id_fecha
WHERE DF.fecha_completa BETWEEN '2022-01-01' AND '2022-12-31';

/* Tasa de Conversión de Ventas */
/*ya funciona*/
SELECT 
  ROUND(
  (cast(COUNT(DISTINCT HV.orden_compra) as float) / SUM(T.visitantes)) * 100, 2) AS tasa_conversion_ventas
FROM 
  HechoVentas HV
JOIN Tienda T 
  ON HV.id_tienda = T.id_tienda
WHERE 
  T.fecha_del_día BETWEEN '2024-07-01' AND '2025-12-31';

  select * from Tienda

  select * from HechoVentas

  /*Ventas netas */
  /*ya funciona*/
  
  SELECT 
  SUM(HV.ventas_brutas) - (SUM(HD.monto_devolucion) + SUM(DP.descuento)) AS ventas_netas
FROM 
  HechoVentas HV
LEFT JOIN 
  HechoDevoluciones HD 
  ON HV.id_venta = HD.id_venta
LEFT JOIN 
  Promociones DP 
  ON HV.id_promocion = DP.id_promocion
WHERE 
  HD.fecha_devolucion BETWEEN '2023-07-01' AND '2025-12-31';



  select * from HechoDevoluciones


  /* Tasa de Rotación del Inventario */
  /*ya funciona*/

	SELECT 
    (SUM(HI.costo_productos_vendidos) / SUM((HI.inventario_inicial + HI.inventario_final) / 2)) AS tasa_rotacion_inventario
FROM 
    HechoInventario HI
LEFT JOIN 
    DimFecha DF 
    ON HI.id_fecha = DF.id_fecha 
WHERE 
    DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31';



 select * from HechoInventario;

 UPDATE HechoInventario
SET costo_productos_vendidos = 20
WHERE id_producto = 10;


/*Retorno de la inversión en margen bruto (GMROI)*/
/*Ya funciona*/
SELECT 
    (SUM(HV.ventas_brutas - COALESCE(HD.monto_devolucion, 0) - COALESCE(HI.costo_productos_vendidos, 0)) /
    (SUM((HI.inventario_inicial + HI.inventario_final) / 2))) AS GMROI
FROM HechoVentas HV
LEFT JOIN HechoDevoluciones HD 
    ON HV.id_venta = HD.id_venta
LEFT JOIN HechoInventario HI 
    ON HV.id_producto = HI.id_producto 
    AND HV.id_tienda = HI.id_tienda
LEFT JOIN DimFecha DF 
    ON HV.id_fecha = DF.id_fecha
WHERE 
    DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31';



select * from DimFecha;

/*Contracción del inventario*/
/*ya funciona*/
SELECT 
  ROUND(
    ((cast(SUM(COALESCE(HI.inventario_esperado, 0)) as float) - SUM(COALESCE(HI.inventario_final, 0))) / SUM(COALESCE(HI.inventario_esperado, 0))) * 100, 2) AS contraccion_inventario
FROM 
  HechoInventario HI
LEFT JOIN DimFecha DF 
  ON HI.id_fecha = DF.id_fecha
WHERE 
    DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31';

select * from HechoInventario;

select * from DimFecha where id_fecha = 42;

/*Tasa de Satisfacción del Cliente*/
/*ya funciona*/
WITH ClientesConSatisfaccionMayorA5 AS (
    SELECT DISTINCT HV.id_cliente
    FROM HechoVentas HV
    LEFT JOIN DimFecha DF ON HV.id_fecha = DF.id_fecha
    WHERE DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31'
      AND HV.puntaje_satisfaccion > 5
      AND HV.puntaje_satisfaccion IS NOT NULL
),
TotalClientesEncuestados AS (
    SELECT DISTINCT HV.id_cliente
    FROM HechoVentas HV
    LEFT JOIN DimFecha DF ON HV.id_fecha = DF.id_fecha
    WHERE DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31'
      AND HV.puntaje_satisfaccion IS NOT NULL
)
SELECT 
    ROUND(
        (CAST((SELECT COUNT(*) FROM ClientesConSatisfaccionMayorA5) AS FLOAT) /
         CAST((SELECT COUNT(*) FROM TotalClientesEncuestados) AS FLOAT)) * 100, 2
    ) AS tasa_satisfaccion_cliente;


	select * from HechoVentas;

/*WHERE id_venta between 1 and 10*/


    

  select * from HechoVentas;

  /*Tasa de devoluciones*/
  /*Agregar cantidad de producto a devoluciones*/
  /*Ya funciona*/
  SELECT 
  (cast(SUM(ISNULL(HD.cant_producto, 0)) as float) / SUM(HV.cant_producto)*100) AS tasa_devoluciones
FROM HechoVentas HV
LEFT JOIN DimFecha DF
    ON HV.id_fecha = DF.id_fecha
LEFT JOIN HechoDevoluciones HD 
    ON HV.id_venta = HD.id_venta
WHERE 
    DF.fecha_completa BETWEEN '2022-01-01' AND '2025-12-31'
  AND HV.cant_producto IS NOT NULL;

select * from HechoVentas;

select * from HechoDevoluciones;

ALTER TABLE HechoDevoluciones
ADD cant_producto INT;

DELETE FROM HechoDevoluciones
WHERE id_devolucion = 10;


-- Actualiza la columna cant_producto con valores aleatorios entre 1 y 7
UPDATE HechoDevoluciones
SET cant_producto = ROUND(RAND() * 6 + 1, 0)  -- Valores aleatorios entre 1 y 7
WHERE id_devolucion BETWEEN 1 AND 10;

/*Desercion de clientes(Churn rate)*/
SELECT 
    ROUND(
      (COUNT(1) - 
      (SELECT COUNT(1) 
        FROM Cliente
        WHERE fecha_ultima_compra BETWEEN '2024-04-01' AND '2024-04-30'
        AND fecha_de_registro < '2022-01-01')) * 100 / 
      COUNT(1), 2) AS Churn_rate
  FROM Cliente
  WHERE fecha_ultima_compra BETWEEN '2024-05-01' AND '2024-05-30'



  /*clientes nuevos*/

SELECT 
    COUNT(id_cliente) AS total_clientes_nuevos
FROM 
    Cliente
WHERE 
    fecha_de_registro BETWEEN '2024-07-01' AND '2024-07-31';
	/**/

ALTER TABLE cliente
ADD 
    nombre_cliente NVARCHAR(100),  -- Puedes ajustar el tamaño según tus necesidades
    apellido_cliente NVARCHAR(100); -- Puedes ajustar el tamaño según tus necesidades


  select * from Cliente;