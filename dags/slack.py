from airflow import DAG
from datetime import datetime, timedelta
#importing SlackWebhookHook used to for interacting with incoming webhooks
from airflow.providers.slack.hooks.slack_webhook import SlackWebhookHook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
#used for implementing hooks
from airflow.hooks.base_hook import BaseHook
from airflow.utils.dates import days_ago
import random

# defining parameters
SLACK_CONN_ID = "SLACK_CONN_ID"
webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
channel = BaseHook.get_connection(SLACK_CONN_ID).login

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}


#defining function that passes and fails sometimes
def random_pass_fail():
    if random.random() > 0.5:
        print("Task succeeded!")
    else:
        raise ValueError("Task failed!")

with DAG(
    dag_id="slack_sending",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:
    # Creating a task fails some time
    task1 = PythonOperator(
        task_id='random_result',
        python_callable=random_pass_fail,
        dag=dag
    )
    # Creating success message task in slack, which triggers on success of above task using trigger rule
    task2 = SlackWebhookOperator(
        task_id='slack_success',
        webhook_token=webhook_token,
        message='Task succeded',
        channel=channel,
        username='airflow',
        http_conn_id=SLACK_CONN_ID,
        trigger_rule=TriggerRule.ALL_SUCCESS
    )
    # Creating success message task in slack, which triggers on fail of above task using trigger rule
    task3 = SlackWebhookOperator(
        task_id='slack_fail',
        webhook_token=webhook_token,
        message='Task Failed',
        channel=channel,
        username='airflow',
        http_conn_id=SLACK_CONN_ID,
        trigger_rule=TriggerRule.ALL_FAILED
    )


    task1 >> [task2,task3]