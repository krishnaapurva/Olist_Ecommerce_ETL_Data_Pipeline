SET search_path TO ecom_olist_stores_db;
CREATE VIEW customer_orders AS
SELECT distinct
    c.customer_id,
	c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_purchase_timestamp,
    oi.product_id,
    p.product_category_id,
	pc.product_category_name_english,
    oi.price
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_items oi ON o.order_id = oi.order_id
JOIN
    products p ON oi.product_id = p.product_id
JOIN
	product_categories pc ON p.product_category_id = pc.product_category_id;
	
