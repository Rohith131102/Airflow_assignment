from airflow.providers.postgres.operators.postgres import PostgresOperator
import airflow
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(1),
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id= 'postgre_crud',
    default_args=default_args,
    description='DAG to connect to mysql server',
    schedule_interval='@daily'
)

createtask = PostgresOperator(
    sql= "sql/create_table.sql",
    task_id="createtable_task", 
    postgres_conn_id = "postgres_conn_id",
    dag=dag
)

inserttask = PostgresOperator(
    sql = "sql/insert_data.sql",
    task_id="insertValues_task",
    postgres_conn_id = "postgres_conn_id",
    dag=dag
)

selecttask = PostgresOperator(
    sql="sql/select_data.sql",
    task_id="selectdata_task" ,
    postgres_conn_id = "postgres_conn_id",
    dag=dag
)

createtask >> inserttask >> selecttask