--==== Creating Schema ====--
-- DROP SCHEMA IF EXISTS ecom_olist_stores_db CASCADE;
CREATE SCHEMA IF NOT EXISTS ecom_olist_stores_db;

--==== set the path to schema ====--

SET search_path TO ecom_olist_stores_db;

--=== DROP Views ===--
DROP VIEW IF EXISTS high_value_customers Cascade;
DROP VIEW IF EXISTS order_history Cascade;
DROP VIEW IF EXISTS product_summary Cascade;
DROP VIEW IF EXISTS sales_summary Cascade;
DROP VIEW IF EXISTS customer_orders Cascade;

--==== DROP Tables ====--

DROP TABLE IF EXISTS customers Cascade;
DROP TABLE IF EXISTS order_items Cascade;
DROP TABLE IF EXISTS orders Cascade;
DROP TABLE IF EXISTS sellers Cascade;
DROP TABLE IF EXISTS order_payments Cascade;
DROP TABLE IF EXISTS order_reviews Cascade;
DROP TABLE IF EXISTS products Cascade;
DROP TABLE IF EXISTS product_categories Cascade;
DROP TABLE IF EXISTS geolocation Cascade;
DROP TABLE IF EXISTS payment_type Cascade;

--==== create tables ===--

--=== Customers table ===--

CREATE TABLE customers (
    customer_id SERIAL NOT NULL,
    unique_customer_id VARCHAR(255) UNIQUE NOT NULL,
    customer_zipcode VARCHAR(10) NOT NULL,
    customer_city VARCHAR(255),
    customer_state VARCHAR(255),
	
	CONSTRAINT pk_customer PRIMARY KEY (customer_id)
);

--=== geolocation table ===--

CREATE TABLE geolocation (
    zipcode VARCHAR(10),                    
    longitude DECIMAL(10, 8) NOT NULL,                  
    latitude DECIMAL(10, 8) NOT NULL,                   
    city VARCHAR(255) NOT NULL,                         
    state VARCHAR(255) NOT NULL, 
	
    CONSTRAINT pk_geolocation PRIMARY KEY (zipcode)  
);

--=== sellers table ===--

CREATE TABLE sellers (
	seller_id INT,
	seller_zipcode VARCHAR(10),
    seller_city VARCHAR(255),
    seller_state VARCHAR(255),
	
	CONSTRAINT pk_sellers PRIMARY KEY (seller_id)
);

--=== orders table ===--

CREATE TABLE orders (
    order_id INT,                                       
    customer_id INT NOT NULL,                           
    order_status VARCHAR(50) NOT NULL,                  
    order_purchase_timestamp TIMESTAMP NOT NULL,        
    order_approved_at TIMESTAMP,                        
    order_delivered_carrier_date TIMESTAMP,             
    order_delivered_customer_date TIMESTAMP,            
    order_estimate_delivery_date TIMESTAMP,             
    
	CONSTRAINT pk_orders PRIMARY KEY (order_id),   
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) 
);

--=== product_categories Table ===--

CREATE TABLE product_categories (
	product_category_id INT,
	product_category_name VARCHAR(255),                
    product_category_name_english VARCHAR(255),           
    
	CONSTRAINT pk_product_categories PRIMARY KEY (product_category_id)
);

--=== products table ===--

CREATE TABLE products (
    product_id INT,                                   
    product_category_id INT,                
    product_name_length INT,                           
    product_description_length INT,                    
    product_photo_quantity INT,                        
    product_weight_gm INT,                       
    product_length_cm INT,                          
    product_height_cm INT,                          
    product_width_cm INT,                           
    
	CONSTRAINT pk_product PRIMARY KEY (product_id),
	FOREIGN KEY (product_category_id) REFERENCES product_categories
);

--=== order_item table ===--

CREATE TABLE order_items (
    order_id INT,                                       
    order_item_id INT,                                  
    product_id INT NOT NULL,                            
    seller_id INT NOT NULL,                             
    shipping_limit_date TIMESTAMP NOT NULL,             
    price DECIMAL(10, 2) NOT NULL,                      
    freight_value DECIMAL(10, 2) NOT NULL,
	total_price DECIMAL(10,2) NOT NULL,
	
    CONSTRAINT pk_order_item PRIMARY KEY (order_id, order_item_id),  
    FOREIGN KEY (order_id) REFERENCES orders(order_id),  
    FOREIGN KEY (product_id) REFERENCES products(product_id), 
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)     
);



--=== payment_type ===--

CREATE TABLE payment_type (
	payment_type_id INT,
	payment_type_name VARCHAR(255) NOT NULL,
	
	CONSTRAINT pk_payment_type PRIMARY KEY (payment_type_id)
);


--=== order_payments ===--

CREATE TABLE order_payments (
    order_id INT,                                       
    payment_sequential INT,                             
    payment_type_id INT NOT NULL,                  
    payment_installments INT NOT NULL,                  
    payment_value DECIMAL(10, 2) NOT NULL,              
    
	CONSTRAINT pk_order_payment PRIMARY KEY (order_id, payment_sequential), 
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (payment_type_id) REFERENCES payment_type(payment_type_id)
);

--=== order_review table ===--

CREATE TABLE order_reviews (
    review_id INT,                                     
    order_id INT NOT NULL,                              
    review_score INT CHECK (review_score >= 1 AND review_score <= 5), 
    review_comment_title TEXT,                          
    review_comment_msg TEXT,                            
    review_creation_date TIMESTAMP NOT NULL,            
    review_answer_timestamp TIMESTAMP,                  
    
	CONSTRAINT pk_order_reviews PRIMARY KEY (review_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) 
);




