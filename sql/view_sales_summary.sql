SET search_path TO ecom_olist_stores_db;
CREATE VIEW sales_summary AS
SELECT
    DATE_TRUNC('month', CAST(o.order_purchase_timestamp AS TIMESTAMP)) AS month,
    SUM(oi.price) AS total_sales,
    AVG(oi.price) AS average_order_value,
    p.product_id,
    p.product_category_id,
	pc.product_category_name_english
FROM
    orders o
JOIN
    order_items oi ON o.order_id = oi.order_id
JOIN
    products p ON oi.product_id = p.product_id
LEFT JOIN
	product_categories pc ON p.product_category_id = pc.product_category_id
GROUP BY
    DATE_TRUNC('month', CAST(o.order_purchase_timestamp AS TIMESTAMP)),
    p.product_id,
    p.product_category_id,
	pc.product_category_name_english;


