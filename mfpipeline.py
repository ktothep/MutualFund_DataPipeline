import json
import logging
from datetime import timedelta, datetime, date
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


from downloader.api import first_function
from parser.csvparser import csvParser
from utils.utils import getFileNamePart

log = logging.getLogger(__name__)

default_args = {
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag=DAG(
        "mf_parser",
        default_args=default_args,
        start_date=datetime(2022, 4 ,11,5,00),
        schedule_interval='@daily',
        catchup=False,
        )


task1=PythonOperator(
    task_id="first_task",
    python_callable=first_function,
    dag=dag,
)
task2=PythonOperator(
    task_id="csvParser",
    python_callable=csvParser,
    dag=dag,

)

task1 >> task2