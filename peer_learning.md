
# Peer learning document
## Aswat Bisht's Approach

Link - https://github.com/bisht-ash/Airflow_assignment/

#### Question - 1
- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.

  b. datetime is used to specify the start date for the DAG.

  c. PostgresOperator is an operator provided by the postgres provider in Airflow. It allows executing SQL queries on a PostgreSQL database.
  
- He initialized a DAG object named 'sql_dag'. The start_date parameter specifies the date and time from which the DAG should start running. The schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily.

- He then defined 3 tasks, which are as explained below 
 
    a. Task - 1: A task named 'createATable' using the PostgresOperator. It specifies a
PostgreSQL connection named 'postgres' using the postgres_conn_id parameter.
The sql parameter contains the SQL statements to be executed, which in this
case drops the table if it already exists and creates a new table called 'Products'
with the specified columns.

  b. Task - 2: A task named 'insertInto' using the PostgresOperator. It uses the
same PostgreSQL connection as before. The sql parameter contains an INSERT
statement to insert data into the 'Products' table. Two rows of data are inserted,
each with the specified values for the columns.

  c. Task - 3: A task, named 'selectFrom', is defined using the PostgresOperator. It
uses the same PostgreSQL connection as the previous tasks. The sql parameter
contains a SELECT statement that retrieves all rows and columns from the
'products' table

#### Question - 2

- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.

  b. datetime is used to specify the start date for the DAG.

  c. PythonOperator in Apache Airflow is a task that executes a Python callable as part of an Airflow workflow, allowing for custom Python code to be run as a task within a DAG.

  d. EmailOperator is an operator provided by Airflow that sends email notifications.

- He initialized a DAG object named 'email_dag'. The start_date parameter
specifies the date and time from which the DAG should start running. The
schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily. 

- He then defined 2 tasks, which are as explained below -
 
  a. The first task is named dummy task,he had written python function to print "Task Started" which always passes .
 
  b. A task named 'send_email' using the EmailOperator. It specifies the
email address to which the email will be sent (to parameter), the subject of the
email (subject parameter), and the content of the email, which includes the
execution date ({{ ds }} represents the execution date in Airflow's template
language)


#### Question - 3

- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.

  b. DateTime is used to specify the start date for the DAG.
  
  c. PythonOperator in Apache Airflow is a task that executes a Python callable as part of an Airflow workflow, allowing for custom Python code to be run as a task within a DAG.

  d. random is used to generate a random number.

  e. SlackWebhookOperator is an operator provided by Airflow that sends messages
to Slack.

  f. BaseHook is used to retrieve connection details from Airflow's Connection
feature.

  g. TriggerRule is used to define task execution rules based on task statuses.
  
- He retrieved the Slack connection details from Airflow's Connection feature. The
SLACK_CONN_ID variable is set to the connection identifier configured in Airflow, and
slack_webhook_token and channel are obtained from the connection.

- He initialized a DAG object named 'slack_dag'. The start_date parameter
specifies the date and time from which the DAG should start running. The
schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily. 

- He then defined 3 tasks, which are as explained below 

  a. The first task named 'conditionalTask' .It is a Python
function that generates a random number between 1 and 10. If the number is
less than or equal to 5, it raises a ValueError to simulate a task failure.

  b.Task - 2: He defined a task using the SlackWebhookOperator. It is responsible
for sending Slack notifications. The channel and slack_webhook_token
parameters are used to authenticate and connect to the Slack workspace. The
message parameter contains the text of the notification, and the username
parameter sets the username that appears as the sender in the Slack message.
The trigger_rule parameter defines the execution rule for the tasks. In this case,
slack_fail is triggered only when all preceding tasks have failed.

  c.Task-3 : He defined a task using the SlackWebhookOperator. It is responsible
for sending Slack notifications. The  channel and slack_webhook_token
parameters are used to authenticate and connect to the Slack workspace. The
message parameter contains the text of the notification, and the username
parameter sets the username that appears as the sender in the Slack message.
The trigger_rule parameter defines the execution rule for the tasks. In this case,
slack_pass is triggered only when all preceding tasks have succeeded

## Arin's Approach

Link - https://github.com/aroraarin/AirflowAssignment/

#### Question - 1
- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.

  b. datetime is used to specify the start date for the DAG and timedelta.

  c. PostgresOperator is an operator provided by the postgres provider in Airflow. It allows executing SQL queries on a PostgreSQL database.
  
  d.Postgres hook in Apache Airflow allows for seamless integration and interaction with PostgreSQL databases within Airflow tasks.
  
  e. PythonOperator in Apache Airflow is a task that executes a Python callable as part of an Airflow workflow, allowing for custom Python code to be run as a task within a DAG.
  
  
  - He initialized a DAG object named 'postgres_task_dag'. The start_date parameter specifies the date and time from which the DAG should start running. The schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily and The catchup parameter is set to False to prevent any
past runs from being executed.

- He then defined 3 tasks, which are as explained below 
 
    a. Task - 1: A task named 'create_table' using the PostgresOperator. It specifies a
PostgreSQL connection named 'postgres' using the postgres_conn_id parameter.
The sql parameter contains the SQL statements to be executed, which in this
case drops the table if it already exists and creates a new table called 'users'
with the specified columns.

  b. Task - 2: A task named 'insert_into_table' using the PostgresOperator. It uses the
same PostgreSQL connection as before. The sql parameter contains an INSERT
statement to insert data into the 'users' table. Four rows of data are inserted,
each with the specified values for the columns.

  c. Task - 3: A task, named 'select_table', is defined using the PostgresOperator. It
uses the same PostgreSQL connection as the previous tasks. The sql parameter
contains a SELECT statement that retrieves all rows and columns from the
'users' table 

#### Question-2

- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.
  
  b. DummyOperator is an operator provided by Airflow that represents a task with no
functionality.
  
  c. EmailOperator is an operator provided by Airflow for sending email notifications.

  d. datetime is used to specify dates and times.
  
- He initialized a DAG object named 'task_email_alert'. The start_date parameter
specifies the date and time from which the DAG should start running. The
schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily and The catchup parameter is set to False to prevent any
past runs from being executed.

- He then defined 2 tasks, which are explained below -
  a. Task - 1: A dummy task created using the DummyOperator. It represents a task
with no functionality and is used as a placeholder in the DAG.
  b. Task - 2: An EmailOperator task responsible for sending an email notification. It
specifies the to email address, the email subject, and the HTML content of the
email.

#### Question - 3

- He imported the required modules and each module is as defined below:

  a. DAG is used to define the DAG object.

  b. DateTime is used to specify the start date for the DAG.
  
  c. PythonOperator in Apache Airflow is a task that executes a Python callable as part of an Airflow workflow, allowing for custom Python code to be run as a task within a DAG.
  
  d. randint is used to generate random integer
  
  e. SlackWebhookOperator is an operator provided by Airflow that sends messages
to Slack.

 
- He initialized a DAG object named 'slack_dag'. The start_date parameter
specifies the date and time from which the DAG should start running. The
schedule_interval parameter determines the frequency at which the DAG should be
executed, in this case, once daily. 

- He then defined 3 tasks, which are as explained below 

   a. The first task named 'conditionalTask' .It is a Python
function that generates a random number between 1 and 2. If the number is
1, it raises a Exception to simulate a task failure.

   b.Task - 2: He defined a task using the SlackWebhookOperator. It is responsible
for sending Slack notifications. The http_conn_id slack will send the message.The trigger_rule parameter defines the execution rule for the tasks. In this case,
slack_fail is triggered only when all preceding tasks have failed.

   c.Task-3 : He defined a task using the SlackWebhookOperator. It is responsible
for sending Slack notifications. The http_conn_id slack will send the message.The trigger_rule parameter defines the execution rule for the tasks. In this case,slack_pass is triggered only when all preceding tasks have succeeded

  
