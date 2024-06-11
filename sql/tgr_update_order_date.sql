SET search_path TO ecom_olist_stores_db;

CREATE OR REPLACE FUNCTION update_order_dates() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.order_status = 'approved' THEN
        NEW.order_approved_at = CURRENT_TIMESTAMP;
    ELSIF NEW.order_status = 'delivered_carrier' THEN
        NEW.order_delivered_carrier_date = CURRENT_TIMESTAMP;
    ELSIF NEW.order_status = 'delivered_customer' THEN
        NEW.order_delivered_customer_date = CURRENT_TIMESTAMP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_order_dates
BEFORE UPDATE ON orders
FOR EACH ROW
EXECUTE FUNCTION update_order_dates();
