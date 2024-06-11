# Olist Ecommerce ETL Data Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) data pipeline for the Olist Ecommerce dataset. The pipeline extracts data from multiple CSV files, transforms it to meet specific requirements, and loads it into a PostgreSQL database. The project uses Pandas for data manipulation and SQLAlchemy for database operations.

## Dataset 

Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Prerequisites

- Python 3.x
- Pandas
- SQLAlchemy
- PostgreSQL

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Olist_Ecommerce_ETL_Data_Pipeline.git
    cd Olist_Ecommerce_ETL_Data_Pipeline
    ```

2. **Install required packages**:
    ```bash
    pip install pandas sqlalchemy psycopg2-binary
    ```

3. **Configure PostgreSQL**:
    Ensure you have a PostgreSQL database set up. Update the `config.py` file with your database credentials:
    ```python
    # config.py
    DB_USER = 'your_db_user'
    DB_PASSWORD = 'your_db_password'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'ecom_olist_stores_db'
    ```

## Running the Pipeline

1. **Extract, Transform, Load**:
    Run the `main.py` script to execute the entire ETL process:
    ```bash
    python main.py
    ```

## Data Modeling

The data from the Olist dataset is modeled into several tables in the PostgreSQL database. Below are the details:

### ER Diagram

The ER diagram for the data model:

![alt text](image.png)
