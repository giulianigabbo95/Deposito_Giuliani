use classicmodels;

/*
# Scrivere una query SQL che restituisca solo i record dalla tabella "products" con un prezzo superiore a 50.
SELECT *
FROM products
WHERE buyPrice > 50
ORDER BY buyPrice DESC;
*/

# Scrivere una query SQL che elimini tutti gli ordini nella tabella "orders" con lo stato "Cancelled".
DELETE
FROM orderdetails
WHERE orderNumber
IN (
	SELECT orderNumber
    FROM orders
    WHERE status = 'Cancelled'
);