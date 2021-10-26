# Rivery API Airflow DAG example.

# Import libraries.
 from datetime import timedelta

 import airflow
 from airflow.operators import DAG
 from airflow.operators.https_operator import SimpleHttpOperator
 from airflow.operators.bash_operator import BashOperator

 default_args = {
 	'owner': 'airflow',
 	'depends_on_past': 'False',
 	'start_date': airflow.utils.dates.days_ago(0),
 	'email_on_failure': True,
 	'email_on_retry': False,
 	'retries': 1,
 	'retry_delay': timedelta(minutes=1)
 }

dag = DAG('airflow_rivery_api_test',
    schedule_interval='@once',
    default_args=default_args)

t1 = BashOperator(
	bash_command)

t1 = SimpleHttpOperator(
    task_id='test_initiate_river',
    method='POST',
    http_conn_id='https://',
    endpoint='console.rivery.io/#/river/55bf7c4270fdca16cac18761/river/5f2d75c4f5682c764a8da7c1',
    headers={"accept": "application/json",
    		 "Authorization": "Bearer <your_api_token>",
    		 "Content-Type": "application/json"},
    dag=dag)

t1 = BashOperator(
	task_id= 'test_initiate_river',
	start_date= datetime.datetime.now(),
	bash_command= "curl -X POST “https://console.rivery.io/api/run\” "

					"-H \“accept: application/json\”"

					"-H \“Authorization: Bearer <your_api_token>\”"

					"-H \“Content-Type: application/json\”"

					"-d \"{ \\\“river_id\\\”: \\\"<your_river_id>\\\"}\"",")")

start >> [t1]