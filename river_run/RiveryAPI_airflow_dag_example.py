# Rivery API Airflow DAG example.

# Import libraries.
from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

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

start = DummyOperator(
	task_id="airflow_rivery_api_test",
	dag=dag)

t1 = BashOperator(
	task_id= 'test_initiate_river',
	start_date= datetime.now(),
	bash_command= "curl -X POST “https://console.rivery.io/api/run\” "

					"-H \“accept: application/json\”"

					"-H \“Authorization: Bearer <your_api_token>\”"

					"-H \“Content-Type: application/json\”"

					"-d \"{ \\\“river_id\\\”: \\\"<your_river_id>\\\"}\")"
				)

start >> [t1]