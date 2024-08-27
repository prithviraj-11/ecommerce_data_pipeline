CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  country VARCHAR(50) NOT NULL
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_amount DECIMAL(10, 2) NOT NULL,
  status VARCHAR(20) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  item_id INT PRIMARY KEY,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table: categories
CREATE TABLE categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(100) NOT NULL
);

-- Table: products
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  category_id INT NOT NULL,
  FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Table: reviews
CREATE TABLE reviews (
  review_id INT PRIMARY KEY,
  product_id INT NOT NULL,
  customer_id INT NOT NULL,
  rating INT CHECK (rating BETWEEN 1 AND 5),
  review_date DATE NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (customer_id, name, email, country) VALUES
(1, 'Jay Shinde', 'jay@gmail.com', 'USA'),
(2, 'Rohit Kumar', 'rohit.kumar@gmail.com', 'Canada'),
(3, 'Akash More', 'akash.more@gmail.com', 'UK'),
(4, 'Dinesh More', 'dinesh.more@gmail.com', 'Australia'),
(5, 'Ram Desai', 'ram.desai@gmail.com', 'India');

INSERT INTO orders (order_id, customer_id, order_date, total_amount, status) VALUES
(101, 1, '2024-07-01', 150.50, 'Completed'),
(102, 2, '2024-07-02', 200.00, 'Completed'),
(103, 1, '2024-07-03', 300.75, 'Completed'),
(104, 3, '2024-07-04', 120.25, 'Pending'),
(105, 4, '2024-07-05', 250.10, 'Completed'),
(106, 5, '2024-07-06', 166.25, 'Completed'),
(107, 5, '2024-07-07', 377.68, 'Pending');

INSERT INTO categories (category_id, category_name) VALUES
(1, 'Electronics'),
(2, 'Accessories');

INSERT INTO products (product_id, product_name, category_id) VALUES
(1, 'Laptop', 1),
(2, 'Smartphone', 1),
(3, 'Headphones', 2),
(4, 'Monitor', 1),
(5, 'Keyboard', 2);

INSERT INTO order_items (item_id, order_id, product_id, quantity, price) VALUES
(1, 101, 1, 2, 50.00),
(2, 101, 2, 1, 50.50),
(3, 102, 1, 1, 100.00),
(4, 103, 3, 3, 75.25),
(5, 104, 4, 1, 120.25),
(6, 105, 5, 2, 125.05);

INSERT INTO reviews (review_id, product_id, customer_id, rating, review_date) VALUES
(1, 1, 1, 4, '2024-07-02'),
(2, 2, 2, 5, '2024-07-03'),
(3, 3, 1, 3, '2024-07-04'),
(4, 4, 3, 4, '2024-07-05'),
(5, 5, 4, 2, '2024-07-06');

select * from customers;
select * from orders;
select * from order_items;
select * from products;
select * from categories;
select * from reviews;

