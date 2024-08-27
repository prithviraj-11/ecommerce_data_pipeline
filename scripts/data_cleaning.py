import pandas as pd

def clean_data():
    customers = pd.read_csv('tmp/customers.csv')
    orders = pd.read_csv('tmp/orders.csv')
    order_items = pd.read_csv('tmp/order_items.csv')
    products = pd.read_csv('tmp/products.csv')
    categories = pd.read_csv('tmp/categories.csv')
    reviews = pd.read_csv('tmp/reviews.csv')

    
    customers.drop_duplicates(inplace=True)
    orders.drop_duplicates(inplace=True)
    order_items.drop_duplicates(inplace=True)
    products.drop_duplicates(inplace=True)
    categories.drop_duplicates(inplace=True)
    reviews.drop_duplicates(inplace=True)

    
    customers.fillna('Unknown', inplace=True)
    orders.fillna(0, inplace=True)
    order_items.fillna(0, inplace=True)
    products.fillna('Unknown', inplace=True)
    categories.fillna('Unknown', inplace=True)
    reviews.fillna(0, inplace=True)
    # print(customers)
    
    customers.to_csv('tmp/cleaned_customers.csv', index=False)
    orders.to_csv('tmp/cleaned_orders.csv', index=False)
    order_items.to_csv('tmp/cleaned_order_items.csv', index=False)
    products.to_csv('tmp/cleaned_products.csv', index=False)
    categories.to_csv('tmp/cleaned_categories.csv', index=False)
    reviews.to_csv('tmp/cleaned_reviews.csv', index=False)
