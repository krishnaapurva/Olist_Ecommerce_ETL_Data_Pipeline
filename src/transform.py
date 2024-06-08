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

    # Transform order items data
    order_items_df = data_frames['order_items']
    order_items_df['total_price'] = order_items_df['freight_value'] + order_items_df['price']

    # Transform order payments data
    order_payments_df = data_frames['order_payments']
    unique_payment_types = order_payments_df['payment_type'].unique()
    payment_type_id = range(1, len(unique_payment_types) + 1)
    payment_type_dict = dict(zip(payment_type_id, unique_payment_types))
    payment_type_df = pd.DataFrame(list(payment_type_dict.items()), columns=['payment_type_id', 'payment_type'])
    payment_map_dict = dict(zip(unique_payment_types, payment_type_id))
    order_payments_df['payment_type_id'] = order_payments_df['payment_type'].map(payment_map_dict)
    order_payments_df = order_payments_df.drop(columns=['payment_type'])

    # Transform product data
    products_df = data_frames['products']
    products_df = products_df.rename(columns={
        'product_name_lenght': 'product_name_length',
        'product_description_lenght': 'product_description_length'
    })

    # Transform product category data
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

    # Save transformed dataframes to csv
    customers_df.to_csv("transformed_data/customers.csv", index=False)
    data_frames['geolocation'].to_csv("transformed_data/geolocation.csv", index=False)
    data_frames['orders'].to_csv("transformed_data/orders.csv", index=False)
    order_items_df.to_csv("transformed_data/order_items.csv", index=False)
    order_payments_df.to_csv("transformed_data/order_payments.csv", index=False)
    data_frames['order_reviews'].to_csv("transformed_data/order_reviews.csv", index=False)
    products_df.to_csv("transformed_data/products.csv", index=False)
    product_categories_df.to_csv("transformed_data/product_categories.csv", index=False)
    data_frames['sellers'].to_csv("transformed_data/sellers.csv", index=False)
    payment_type_df.to_csv("transformed_data/payment_types.csv", index=False)

if __name__ == "__main__":
    from extract import extract_data
    data_frames = extract_data()
    transform_data(data_frames)
