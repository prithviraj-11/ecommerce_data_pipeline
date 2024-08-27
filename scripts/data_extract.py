import pandas as pd
import pymysql

def extract_data():
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='ecommerce_db', port=3306)

    customers = pd.read_sql("SELECT * FROM customers", connection)
    orders = pd.read_sql("SELECT * FROM orders WHERE order_date >= NOW() - INTERVAL 3 HOUR", connection)
    order_items = pd.read_sql("SELECT * FROM order_items", connection)
    products = pd.read_sql("SELECT * FROM products", connection)
    categories = pd.read_sql("SELECT * FROM categories", connection)
    reviews = pd.read_sql("SELECT * FROM reviews WHERE review_date >= NOW() - INTERVAL 3 HOUR", connection)
    # print(customers)

    customers.to_csv('tmp/customers.csv', index=False)
    orders.to_csv('tmp/orders.csv', index=False)
    order_items.to_csv('tmp/order_items.csv', index=False)
    products.to_csv('tmp/products.csv', index=False)
    categories.to_csv('tmp/categories.csv', index=False)
    reviews.to_csv('tmp/reviews.csv', index=False)
    connection.close()
