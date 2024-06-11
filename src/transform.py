import os
import pandas as pd

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def transform_data(data_frames):
    # Create the transformed directory if it doesn't exist
    create_directory('transformed_data')

    # Transform customer data
    customers_df = data_frames['customers']
    customers_df = customers_df.rename(columns={'customer_zip_code_prefix': 'customer_zipcode'})

    # Data validation for customers data
    if customers_df.isnull().values.any():
        raise ValueError("Customers data contains missing values.")

    # Transform order items data
    order_items_df = data_frames['order_items']
    order_items_df['total_price'] = order_items_df['freight_value'] + order_items_df['price']
    # Data validation for order items data
    if order_items_df.isnull().values.any():
        raise ValueError("Order items data contains missing values.")
    if order_items_df['price'].min() < 0:
        raise ValueError("Order items data contains negative prices.")

    # Transform orders data
    orders_df = data_frames['orders']
    # Data validation for orders data
    if len(orders_df) != len(orders_df['order_id'].unique()):
        raise ValueError("Duplicate order_id found in orders data.")
    if set(orders_df['order_status'].unique()) != {'delivered', 'shipped', 'canceled', 'unavailable', 'processing', 'invoiced', 'created', 'approved'}:
        raise ValueError("Invalid order status found in orders data.")

    # Transform product and product categories data
    products_df = data_frames['products']
    products_df = products_df.rename(columns={
        'product_name_lenght': 'product_name_length',
        'product_description_lenght': 'product_description_length'
    })
    product_categories_df = data_frames['product_categories']
    product_categories_df = data_frames['product_categories']
    product_categories_df['product_category_id'] = range(1, len(product_categories_df['product_category_name'].unique()) + 1)
    additional_data = pd.DataFrame([
        {'product_category_name': None, 'product_category_name_english': None, 'product_category_id': 72},
        {'product_category_name': 'pc_gamer', 'product_category_name_english': 'pc_gamer', 'product_category_id': 73},
        {'product_category_name': 'portateis_cozinha_e_preparadores_de_alimentos', 'product_category_name_english': 'portable_kitchen_and_food_preparers', 'product_category_id': 74}
    ])
    product_categories_df = pd.concat([product_categories_df, additional_data], ignore_index=True)
    products_df = products_df.merge(product_categories_df, on='product_category_name', how='left')
    products_df = products_df.drop(columns=['product_category_name', 'product_category_name_english'])

    # Data validation for product categories data
    if len(product_categories_df) != len(product_categories_df['product_category_id'].unique()):
        raise ValueError("Duplicate product_category_id found in product categories data.")



    # Data validation for products data
    if len(products_df) != len(products_df['product_id'].unique()):
        raise ValueError("Duplicate product_id found in products data.")
    if products_df['product_name_length'].min() < 0 or products_df['product_description_length'].min() < 0:
        raise ValueError("Products data contains negative lengths.")

    # Transform sellers data
    sellers_df = data_frames['sellers']
    # Data validation for sellers data
    if sellers_df.isnull().values.any():
        raise ValueError("Sellers data contains missing values.")
    if len(sellers_df) != len(sellers_df['seller_id'].unique()):
        raise ValueError("Duplicate seller_id found in sellers data.")

    # Transform order payments data
    order_payments_df = data_frames['order_payments']
    order_payments_df = data_frames['order_payments']
    unique_payment_types = order_payments_df['payment_type'].unique()
    payment_type_id = range(1, len(unique_payment_types) + 1)
    payment_type_dict = dict(zip(payment_type_id, unique_payment_types))
    payment_type_df = pd.DataFrame(list(payment_type_dict.items()), columns=['payment_type_id', 'payment_type'])
    payment_map_dict = dict(zip(unique_payment_types, payment_type_id))
    order_payments_df['payment_type_id'] = order_payments_df['payment_type'].map(payment_map_dict)
    order_payments_df = order_payments_df.drop(columns=['payment_type'])

    # Data validation for order payments data
    if order_payments_df.isnull().values.any():
        raise ValueError("Order payments data contains missing values.")
    if order_payments_df['payment_value'].min() < 0:
        raise ValueError("Order payments data contains negative payment values.")

    # Transform order reviews data
    order_reviews_df = data_frames['order_reviews']
    # Data validation for order reviews data
    if order_reviews_df['review_score'].min() < 1 or order_reviews_df['review_score'].max() > 5:
        raise ValueError("Invalid review score found in order reviews data.")

    # Save transformed dataframes to csv
    customers_df.to_csv("transformed_data/customers.csv", index=False)
    data_frames['geolocation'].to_csv("transformed_data/geolocation.csv", index=False)
    orders_df.to_csv("transformed_data/orders.csv", index=False)
    order_items_df.to_csv("transformed_data/order_items.csv", index=False)
    order_payments_df.to_csv("transformed_data/order_payments.csv", index=False)
    order_reviews_df.to_csv("transformed_data/order_reviews.csv", index=False)
    products_df.to_csv("transformed_data/products.csv", index=False)
    product_categories_df.to_csv("transformed_data/product_categories.csv", index=False)
    data_frames['sellers'].to_csv("transformed_data/sellers.csv", index=False)
    payment_type_df.to_csv("transformed_data/payment_types.csv", index=False)
    sellers_df.to_csv("transformed_data/sellers.csv", index=False)

if __name__ == "__main__":
    from extract import extract_data
    data_frames = extract_data()
    transform_data(data_frames)
