# Rivery API Airflow DAG example vua python

# Import libraries.
from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

"""Set default values for variables."""
with DAG(
    dag_id="airflow_rivery_python_test",
    schedule_interval='@once',
    start_date=datetime.now(),
    catchup=False,
    tags=["example"],
) as dag:

	def run_river(**kwargs):
		"""Import libraries"""
		import requests
		import json
		
		"""Parse configuration variables."""
		river_id = kwargs['dag_run'].conf['river_id']
		access_token = kwargs['dag_run'].conf['access_token']
		
		"""Make HTTP request and log the response."""
		url = "https://console.rivery.io/api/run"  
		payload = json.dumps({
			"river_id": f"{river_id}"
		})
		headers = {
			'Content-Type': 'application/json',
			'Authorization': f"Bearer {access_token}"
		}
		 
		response = requests.request("POST", url, headers=headers, data=payload)

		print(response.text)
		return response.json()['run_id']

	"""Create dummy operator for dag initiation."""
	start = DummyOperator(task_id="Initiate_Dag", dag=dag)

	run_this = PythonOperator(
		task_id="Execute_River",
		python_callable=run_river,
	)

	"""Execute DAG."""
	run_this.set_upstream(start)