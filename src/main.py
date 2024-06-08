import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from extract import extract_data
from transform import transform_data
from load import load_data_to_postgres

def main():

    # Extract data
    data_frames = extract_data()
    
    # Transform data
    transform_data(data_frames)
    
    # Load data to PostgreSQL
    load_data_to_postgres()

if __name__ == "__main__":
    main()
