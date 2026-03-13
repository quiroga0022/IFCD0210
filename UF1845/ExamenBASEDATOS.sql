-- Ejercicios SQL sobre la base de datos jardineria
-- 1. Obtener el nombre y precio de venta de todos los productos.

select p.nombre, p.precio_venta  from producto p

-- 2. Mostrar los clientes que pertenecen a España.

select c.nombre_cliente , c.pais from cliente c 
where c.pais = 'Spain'

-- 3. Mostrar los productos ordenados por precio de venta de mayor a menor.

select p.precio_venta, p.nombre   from producto p
order by p.precio_venta desc

-- 4. Mostrar el nombre del cliente y el código de los pedidos que ha realizado.

select c.nombre_cliente , p.codigo_pedido from cliente c
join pedido p 
on c.codigo_cliente = p.codigo_cliente 

-- 5. Mostrar el nombre del cliente, el código del pedido y el nombre del producto comprado.

select c.nombre_cliente, pe.codigo_pedido, pr.nombre
from cliente c
join pedido pe on c.codigo_cliente = pe.codigo_cliente
join detalle_pedido dp on pe.codigo_pedido = dp.codigo_pedido
join producto pr on dp.codigo_producto = pr.codigo_producto;

-- 6. Contar cuántos clientes hay registrados en la base de datos.

SELECT COUNT(*) AS total_clientes
FROM cliente;

-- 7. Calcular el precio medio de venta de los productos.

SELECT AVG(precio_venta) AS precio_medio
FROM producto;

-- 8. Mostrar cuántos productos hay en cada gama de productos.

SELECT gama, COUNT(*) AS total_productos
FROM producto
GROUP BY gama;

-- 9. Actualizar el teléfono del cliente con código 10 a '600123456'.

UPDATE cliente
SET telefono = '600123456'
WHERE codigo_cliente = 10;

-- 10. Eliminar los pagos realizados antes del 1 de enero de 2005.

DELETE FROM pago
WHERE fecha_pago < '2005-01-01';
