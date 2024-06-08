CREATE VIEW high_value_customers AS
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    SUM(oi.price) AS total_spent
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_items oi ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_city,
    c.customer_state
HAVING
    SUM(oi.price) > 1000;
