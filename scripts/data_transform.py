import pandas as pd

def transform_data():
    customers = pd.read_csv('tmp/cleaned_customers.csv')
    orders = pd.read_csv('tmp/cleaned_orders.csv')
    order_items = pd.read_csv('tmp/cleaned_order_items.csv')
    products = pd.read_csv('tmp/cleaned_products.csv')
    categories = pd.read_csv('tmp/cleaned_categories.csv')
    reviews = pd.read_csv('tmp/cleaned_reviews.csv')

    
    df = customers.merge(orders, on='customer_id').merge(order_items, on='order_id') \
                  .merge(products, on='product_id') \
                  .merge(categories, on='category_id') \
                  .merge(reviews, on=['customer_id', 'product_id'])

    aggregated_data = df.groupby(['customer_id', 'name', 'email', 'country']).agg(
        total_amount_spent=('total_amount', 'sum'),
        total_orders=('order_id', 'count'),
        average_order_value=('total_amount', 'mean'),
        total_products_ordered=('quantity', 'sum'),
        average_rating=('rating', 'mean')
    ).reset_index()

    aggregated_data.to_csv('tmp/aggregated_data.csv', index=False)
