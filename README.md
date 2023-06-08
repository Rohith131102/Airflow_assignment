# Airflow_assignment

## Questions
<img width="465" alt="Screenshot 2023-06-08 at 4 29 10 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/1a5fe7c0-617d-4d69-828b-083c86243898">



### solution-1
- created connection 'postgres_conn_id' with postgres using airflow ui 
- used postgresoperator ,The postgresOperator is a custom operator provided by the postgres-connector-python package, which allows Airflow to interact with postgres databases
- and then performed the 3 tasks - create table,insert in table,select in table

<img width="1440" alt="Screenshot 2023-05-25 at 11 37 48 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/8709bf8a-051c-4cdb-b50e-c6a7cb2fad34">

<img width="1434" alt="Screenshot 2023-05-25 at 11 37 05 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/dc5fec1d-924a-4e23-90c8-b10856aa1a6b">


### solution-2

- Created a dummy operator, which never fails and an email operator for sending mails upon completion of above task
- The EmailOperator is a built-in operator provided by Airflow, which sends emails using the SMTP (Simple Mail Transfer Protocol) server specified in the Airflow configuration.
- For sending mails we need to make some changes in docker-compose.yaml file which contains from mail address, port, host and many more.

<img width="513" alt="Screenshot 2023-06-08 at 4 30 46 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/d0b21928-11e3-48fe-8e1b-e327c57b08c2">

<img width="713" alt="Screenshot 2023-06-08 at 4 31 41 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/dfd4bbc8-b284-4c6c-b836-d34517daf157">



### solution-3
- Created a connection in airflow, for having communication with slack with some login details and connection
- This code creates a string variable SLACK_CONN_ID that contains the identifier for a connection to Slack in Airflow, and retrieves the password (i.e., Slack webhook token) for the Slack connection using BaseHook.get_connection(SLACK_CONN_ID).password. BaseHook is a class in Airflow that provides a uniform interface to interact with various external systems (such as databases, message queues, and APIs) through Airflow connections. Here, BaseHook.get_connection(SLACK_CONN_ID) returns the Airflow connection object associated with the SLACK_CONN_ID identifier, and .password returns the password (i.e., Slack webhook token) for the connection and it also retrieves the login field (i.e., channel) for the Slack connection using BaseHook.get_connection(SLACK_CONN_ID).login. This line assumes that the login field in the connection object contains the name of the Slack channel where the message should be sent.

```
SLACK_CONN_ID = "SLACK_CONN_ID"
webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
channel = BaseHook.get_connection(SLACK_CONN_ID).login
```
- Created a function which fails/passes sometimes when the randomly generated number is less than/greater than 0.5

<img width="626" alt="Screenshot 2023-06-08 at 4 32 25 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/6e8ffe66-b894-42e4-b091-4aae3744dec4">

<img width="621" alt="Screenshot 2023-06-08 at 4 32 33 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/dcdba262-c96b-4a5a-875a-2b404dab8003">

<img width="620" alt="Screenshot 2023-06-08 at 4 32 42 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/0b1a2296-b712-471e-b59f-3a1678f1ff89">

<img width="625" alt="Screenshot 2023-06-08 at 4 32 51 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/78ace0d8-3c70-46fe-9f42-a3f12d2bd987">



