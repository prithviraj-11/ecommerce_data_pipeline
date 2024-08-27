import pandas as pd
from pymongo import MongoClient

def load_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ecommerce_db']
    collection = db['aggregated_data']

    aggregated_data = pd.read_csv('tmp/aggregated_data.csv')
    collection.insert_many(aggregated_data.to_dict('records'))

    insights_collection = db['insights_generated_data']

    top_customers = pd.read_csv('tmp/top_customers.csv')
    top_products = pd.read_csv('tmp/top_products.csv')
    avg_rating_by_category = pd.read_csv('tmp/avg_rating_by_category.csv')
    monthly_sales = pd.read_csv('tmp/monthly_sales.csv')

    insights_collection.insert_many([
        {"insight": "Top 5 Customers by Total Amount Spent", "data": top_customers.to_dict('records')},
        {"insight": "Top 5 Products by Number of Orders", "data": top_products.to_dict('records')},
        {"insight": "Average Rating of Products by Category", "data": avg_rating_by_category.to_dict('records')},
        {"insight": "Monthly Sales Trend", "data": monthly_sales.to_dict('records')}
    ])