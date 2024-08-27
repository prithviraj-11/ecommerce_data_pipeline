from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.data_extract import extract_data
from scripts.data_cleaning import clean_data
from scripts.data_transform import transform_data
from scripts.data_load import load_data
from scripts.generate_insights import generate_insights

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ecommerce_pipeline',
    default_args=default_args,
    description='ETL pipeline for e-commerce data',
    schedule_interval='0 */3 * * *', #None,
    catchup=False,
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

clean_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

insights_task = PythonOperator(
    task_id='insights_data',
    python_callable=generate_insights,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_task >> clean_task >> transform_task >> insights_task >> load_task
