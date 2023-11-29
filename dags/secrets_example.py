from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.secret import Secret
import os

ods_secrets = Secret(deploy_target="env", deploy_type = "env", secret = "ods-database")
dict_secrets = ods_secrets.__dict__ 
ods_secrets.to_env_secret()

def print_secrets():
    print("secret object:", ods_secrets)
    print("env var database name:", os.getenv('ODS_DATABASE'))
    print("dictionary secret:", dict_secrets)

dag = DAG(
    dag_id='secrets_example',
    schedule=None,
    start_date=datetime(2023, 11, 23),
    catchup=False,
)

print_task = PythonOperator(
    task_id='secrets_example',
    python_callable=print_secrets,
    # provide_context=True,  
    # op_args=[ods_secrets],  
    # env_vars={'ODS_DATABASE': '{{ var.value.ODS_DATABASE }}'},
    dag=dag
)