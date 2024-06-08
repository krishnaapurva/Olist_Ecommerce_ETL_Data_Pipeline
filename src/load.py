import pandas as pd
from sqlalchemy import create_engine
import config

def load_data_to_postgres():
    engine = create_engine(f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')

    # Load transformed data
    customers_df = pd.read_csv("transformed_data/customers.csv")
    geolocation_df = pd.read_csv("transformed_data/geolocation.csv")
    orders_df = pd.read_csv("transformed_data/orders.csv")
    order_items_df = pd.read_csv("transformed_data/order_items.csv")
    order_payments_df = pd.read_csv("transformed_data/order_payments.csv")
    order_reviews_df = pd.read_csv("transformed_data/order_reviews.csv")
    products_df = pd.read_csv("transformed_data/products.csv")
    product_categories_df = pd.read_csv("transformed_data/product_categories.csv")
    sellers_df = pd.read_csv("transformed_data/sellers.csv")
    payment_types_df = pd.read_csv("transformed_data/payment_types.csv")

    # Load data into PostgreSQL
    customers_df.to_sql('customers', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    geolocation_df.to_sql('geolocation', engine,schema='ecom_olist_stores_db', if_exists='replace', index=False)
    orders_df.to_sql('orders', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    order_items_df.to_sql('order_items', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    order_payments_df.to_sql('order_payments', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    order_reviews_df.to_sql('order_reviews', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    products_df.to_sql('products', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    product_categories_df.to_sql('product_categories', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    sellers_df.to_sql('sellers', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)
    payment_types_df.to_sql('payment_types', engine, schema='ecom_olist_stores_db', if_exists='replace', index=False)

if __name__ == "__main__":
    load_data_to_postgres()
