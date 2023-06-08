# Airflow_assignment

## Questions
<img width="441" alt="Screenshot 2023-06-08 at 12 56 09 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/2181db6b-7389-40cc-a20e-05fe190e3503">


### solution-1
- created connection 'postgres_conn_id' with postgres using airflow ui 
- used postgresoperator ,The postgresOperator is a custom operator provided by the postgres-connector-python package, which allows Airflow to interact with postgres databases
- and then performed the 3 tasks - create table,insert in table,select in table

<img width="1440" alt="Screenshot 2023-05-25 at 11 37 48 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/e473a48e-28ba-4fe5-bc7b-aeb3d6069daf">

<img width="1434" alt="Screenshot 2023-05-25 at 11 37 05 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/00691478-7c25-44b7-9275-f1d0a84757a0">

### solution-2

- Created a dummy operator, which never fails and an email operator for sending mails upon completion of above task
- The EmailOperator is a built-in operator provided by Airflow, which sends emails using the SMTP (Simple Mail Transfer Protocol) server specified in the Airflow configuration.
- For sending mails we need to make some changes in docker-compose.yaml file which contains from mail address, port, host and many more.

<img width="588" alt="Screenshot 2023-06-08 at 1 26 57 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/02505e83-9d3c-4492-b4f7-3d69f9fcb9ab">

<img width="724" alt="Screenshot 2023-06-08 at 1 28 21 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/ee6a9e84-519d-40e5-8572-c5456603d999">

### solution-3
- Created a connection in airflow, for having communication with slack with some login details and connection
- This code creates a string variable SLACK_CONN_ID that contains the identifier for a connection to Slack in Airflow, and retrieves the password (i.e., Slack webhook token) for the Slack connection using BaseHook.get_connection(SLACK_CONN_ID).password. BaseHook is a class in Airflow that provides a uniform interface to interact with various external systems (such as databases, message queues, and APIs) through Airflow connections. Here, BaseHook.get_connection(SLACK_CONN_ID) returns the Airflow connection object associated with the SLACK_CONN_ID identifier, and .password returns the password (i.e., Slack webhook token) for the connection and it also retrieves the login field (i.e., channel) for the Slack connection using BaseHook.get_connection(SLACK_CONN_ID).login. This line assumes that the login field in the connection object contains the name of the Slack channel where the message should be sent.
```
SLACK_CONN_ID = "SLACK_CONN_ID"
webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
channel = BaseHook.get_connection(SLACK_CONN_ID).login
```
- Created a function which fails/passes sometimes when the randomly generated number is less than/greater than 0.5

<img width="618" alt="Screenshot 2023-06-08 at 1 38 19 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/68aa2bca-dc6b-4372-9f98-65be1760e75c">

<img width="618" alt="Screenshot 2023-06-08 at 1 38 39 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/aa89667b-6c4d-404e-abf5-ca3929e55fa9">


<img width="617" alt="Screenshot 2023-06-08 at 1 36 14 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/4d69c445-21c4-4782-a311-18fdca51f2e9">


<img width="625" alt="Screenshot 2023-06-08 at 1 37 29 PM" src="https://github.com/Rohith131102/Airflow_assignment/assets/123619674/6e4e1196-aeb8-4a29-b0fd-55f76ee73c96">


