# airflow_sample_dags_rivery
Repository to hold sample code for creating DAG's in apache airflow using the rivery api.

## Folders:

### 1. river_run.
Contains DAG code to remotely execute a river. Must trigger dag with config file in the format:

{"river_id": "<your_river_id>",
"access_token": "<your_access_token>"}


### 2. check_run.
Contains DAG code to check the status of a river provided the run_id. Must trigger dag with config file in the format:

{"run_id": "<your_run_id>",
"access_token": "<your_access_token>"}

### 3. rivery_download_activity_log.
Contains DAG code to download the csv file holding the logs of a run.
