SET search_path TO ecom_olist_stores_db;

CREATE VIEW order_history AS
SELECT
    o.order_id,
    o.customer_id,
    o.order_purchase_timestamp AS order_date,
    o.order_status
FROM
    orders o;
