# Importing the required libraries
from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago


# Declaring time and message for content in mail.
time_now = datetime.now() 
message = (f"<h3> Hello </h3>, Message from airflow -> Given scheduled Task is completed at {time_now} .")

# Declaring default arguments for the dag
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(1),
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    dag_id= 'email_alert',
    default_args=default_args,
    description='DAG to send email alert',
    schedule_interval='@daily'
)

# dummy task which always passes
dummy_pass_task=EmptyOperator(
    task_id="Dummy",
    dag=dag
)

# Task2 - for sending success message of the task to below mail with above message
send_email_task=EmailOperator(
    task_id="Sending_Email",
    to="rohith.reddy@sigmoidanalytics.com",
    subject="Success Message",
    html_content=message,
    dag=dag
)

dummy_pass_task >> send_email_task