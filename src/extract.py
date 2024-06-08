import pandas as pd

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path: The path to the CSV file.
    
    Returns:
    - A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def extract_data():
    # Define file paths
    file_paths = {
        'customers': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_customers_dataset.csv',
        'geolocation': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_geolocation_dataset.csv',
        'orders': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_orders_dataset.csv',
        'order_items': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_order_items_dataset.csv',
        'order_payments': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_order_payments_dataset.csv',
        'order_reviews': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_order_reviews_dataset.csv',
        'products': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_products_dataset.csv',
        'product_categories': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/product_category_name_translation.csv',
        'sellers': '/Users/krishnaapurva/Documents/GitHub/Olist_Ecommerce_ETL_Data_Pipeline/data/olist_sellers_dataset.csv'
    }
    
    # Load data
    data_frames = {key: load_data(path) for key, path in file_paths.items()}
    return data_frames

if __name__ == "__main__":
    data = extract_data()
    for key, df in data.items():
        print(f"{key}:\n{df.head()}\n")
