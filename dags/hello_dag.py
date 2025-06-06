from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print(" Hello from composer!")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 5, 25),
    schedule_interval="@daily",  # Runs daily
    catchup=True,
    tags=["example"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello
    )

