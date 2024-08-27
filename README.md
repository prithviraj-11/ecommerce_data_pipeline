# ecommerce_data_pipeline
This project involves designing and implementing a data pipeline to extract data from a SQL data base, transform it, and load it into a NoSQL database. The pipeline is orchestrated using  Airflow and is scheduled to run every 3 hours.


Setup Instructions
#SQL Database Setup
1. Install MySQL Community Server
 - Download and install MySQL Community Server from the official website.
 - Follow the installation instructions provided.

2. Create the Database and Tables
 - Use the provided SQL scripts to create the ecommerce_db database and the necessary tables.
 - Example:
	CREATE DATABASE ecommerce_db;

	USE ecommerce_db;

3. Insert Sample Data
 - Use the provided sample data insertion scripts to populate the tables with sample data.

#NoSQL Database Setup
1. Install MongoDB
 - Download and install MongoDB Community Server from the official website.
 - Follow the installation instructions provided.

2. Create MongoDB Database and Collections
 - Create the ecommerce_db database and collections (aggregated_data, insights_generated_data).


#Airflow Setup
1. Install Apache Airflow
 - Follow the official installation guide for Airflow installation.
 - Example command:
	pip install apache-airflow

2. Initialize the Airflow Database
 - Initialize the Airflow metadata database:
	airflow db init

3. Configure Airflow
 - Update airflow.cfg with necessary configurations for your environment.
 - Set up your DAG file as described below.

#Instructions to Run the Pipeline
1. Place the DAG File
 - Save the Airflow DAG script (data_pipeline.py) in the Airflow DAGs directory (airflow/dags).

2. Start Airflow Services
 - Start the Airflow web server:
      airflow webserver --port 8080
 - Start the Airflow scheduler:
      airflow scheduler

3. Trigger the DAG
 - Access the Airflow web interface at http://localhost:8080.
 - Trigger the data_pipeline DAG manually or wait for the automated schedule.

#Data Structures and Time Complexities
##SQL Tables
1. customers: Contains customer details.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

2. orders: Contains order details.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

3. order_items: Contains details of items in orders.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

4. products: Contains product details.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

5. categories: Contains product categories. 
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

6. reviews: Contains product reviews.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, SELECT) assuming indexed columns.

##NoSQL Collections
1. aggregated_data: Stores aggregated results from the data pipeline.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, FIND) assuming indexed fields.

2. insights_generated_data: Stores insights generated from the data.
 - Time Complexity: O(1) for basic operations (e.g., INSERT, FIND) assuming indexed fields.

##Data Structures Used in the Pipeline
#DataFrames (Pandas):
 - Time Complexity: Operations like filtering, joining, and aggregating are generally O(n) where n is the number of rows.
 - Memory Complexity: O(n), where n is the number of rows in the DataFrame.

#Challenges and Solutions
 - Incremental Data Extraction: Extracting only changed data efficiently. 
 - Solution: Add a last_updated timestamp column to tables and filtered data based on this 
   timestamp. (Implementation Pending)
 - Data Transformation Complexity: Handling complex joins and aggregations.
 - Handling Errors and Fault Tolerance: It is pending due to time concerns but it is important 
   to ensure pipeline robustness and recovery from failures.

#Orchestration Script
The orchestration script (data_pipeline.py) is provided in the airflow/dags directory. It includes:
    - Data extraction from SQL.
    - Data cleaning and transformation.
    - Insights generation.
    - Data loading into MongoDB.

#Sample Data
Sample data scripts are included to help you populate the SQL tables with sample records. The files are named insert_sample_data.sql.
