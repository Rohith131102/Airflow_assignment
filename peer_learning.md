# Peer learning document
## Aswat Bisht's Approach

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

  c. Python operator is an operator provided by the python provider in Airflow.It allows us to python functions and code

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
  
  c. Python operator is an operator provided by the python provider in Airflow.It allows us to python functions and code

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

  a. The first task named 'conditional_task' using the defined a funtion which randomly generates number between 1 and 10 and raises value error if generated number is less than 5
