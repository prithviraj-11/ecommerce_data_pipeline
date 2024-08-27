import pandas as pd

def generate_insights():
    transformed_data = pd.read_csv('tmp/aggregated_data.csv')

    top_customers = transformed_data.nlargest(5, 'total_amount_spent')[['customer_id', 'name', 'total_amount_spent']]

    order_items = pd.read_csv('tmp/order_items.csv')
    products = pd.read_csv('tmp/products.csv')
    top_products = order_items.groupby('product_id').size().nlargest(5).reset_index(name='order_count')
    top_products = top_products.merge(products[['product_id', 'product_name']], on='product_id', how='left')

    
    reviews = pd.read_csv('tmp/reviews.csv')
    categories = pd.read_csv('tmp/categories.csv') 
    product_reviews = reviews.merge(products[['product_id', 'category_id']], on='product_id', how='left')
    product_reviews = product_reviews.merge(categories[['category_id', 'category_name']], on='category_id', how='left')
    
    avg_rating_by_category = product_reviews.groupby('category_name')['rating'].mean().reset_index()


    orders = pd.read_csv('tmp/orders.csv')
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    monthly_sales = orders.resample('M', on='order_date')['total_amount'].sum().reset_index()
    monthly_sales['order_date'] = monthly_sales['order_date'].dt.strftime('%Y-%m')


    top_customers.to_csv('tmp/top_customers.csv', index=False)
    top_products.to_csv('tmp/top_products.csv', index=False)
    avg_rating_by_category.to_csv('tmp/avg_rating_by_category.csv', index=False)
    monthly_sales.to_csv('tmp/monthly_sales.csv', index=False)

