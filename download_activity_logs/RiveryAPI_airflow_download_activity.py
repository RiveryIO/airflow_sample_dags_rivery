# Rivery API Airflow DAG example - check_run

# Import libraries.
from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

"""Set default values for variables."""
with DAG(
    dag_id="airflow_rivery_check_run",
    schedule_interval='@once',
    start_date=datetime.now(),
    catchup=False,
    tags=["example"],
) as dag:

	def download_activity_logs_initial_request(**kwargs):
		"""Import libraries"""
		import requests
		import json
		
		"""Parse configuration variables."""
		run_id = kwargs['dag_run'].conf['run_id']
		access_token = kwargs['dag_run'].conf['access_token']
		
		"""Make HTTP request and log the response."""
		url = f"https://console.rivery.io/api/check_run?run_id={run_id}"
		 
		payload={}
		headers = {
		 'Authorization': f"Bearer {access_token}"
		}
		 
		response = requests.request("GET", url, headers=headers, data=payload)
 
		print(response.text)
		return response.json()['queryId']

	def download_activity_logs_second_request(**kwargs):
		"""Import libraries"""
		import requests
		import json
		
		"""Parse configuration variables."""
		run_id = kwargs['dag_run'].conf['run_id']
		access_token = kwargs['dag_run'].conf['access_token']
		
		"""Make HTTP request and log the response."""
		url = f"https://console.rivery.io/api/check_run?run_id={run_id}"
		 
		payload={}
		headers = {
		 'Authorization': f"Bearer {access_token}"
		}
		 
		response = requests.request("GET", url, headers=headers, data=payload)
 
		print(response.text)
		return response.text


	"""Create dummy operator for dag initiation."""
	start = DummyOperator(task_id="download_activity_log", dag=dag)

	initial_request = PythonOperator(
		task_id="first_request",
		python_callable=download_activity_logs,
	)

	second_request = PythonOperator(
		task_id="second_request",
		python_callable=download_activity_logs_second_request,
	)

	"""Execute DAG."""
	second_request.set_upstream(first_request)
	initial_request.set_upstream(start)