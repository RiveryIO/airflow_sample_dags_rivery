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

	def check_river(**kwargs):
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
		return response.json()['river_run_status']


	"""Create dummy operator for dag initiation."""
	start = DummyOperator(task_id="Initiate_Dag", dag=dag)

	run_this = PythonOperator(
		task_id="Check_run_status",
		python_callable=check_river,
	)

	"""Execute DAG."""
	run_this.set_upstream(start)