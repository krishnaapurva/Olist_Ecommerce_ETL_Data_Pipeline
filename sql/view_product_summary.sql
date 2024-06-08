SET search_path TO ecom_olist_stores_db;

CREATE VIEW product_summary AS
SELECT
    p.product_id,
    p.product_category_id,
	pc.product_category_name_english,
    COUNT(oi.order_item_id) AS total_sales,
    AVG(oi.price) AS average_price
FROM
    products p
INNER JOIN
    order_items oi ON p.product_id = oi.product_id
LEFT JOIN
	product_categories pc ON p.product_category_id = pc.product_category_id
GROUP BY
    p.product_id, p.product_category_id, pc.product_category_name_english;
