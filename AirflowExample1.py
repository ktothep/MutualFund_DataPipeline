import json
import logging
from datetime import timedelta, datetime
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
log = logging.getLogger(__name__)

default_args = {
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag=DAG(
        "fetch_save_csv",
        default_args=default_args,
        start_date=datetime(2022, 4 ,11,17,00),
        schedule_interval='@daily',
        catchup=False,
        )

def first_function():
    req_date = datetime.date.today()
    x = req_date.day
    y = req_date.strftime("%b")
    z = req_date.year
    formatted_date = str(x - 1) + "-" + y + "-" + str(z)
    params = {'frmdt': formatted_date}
    resp = requests.get("https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx",params=params)
    response_text = resp.text
    filtered_response = "".join(c for c in response_text if ord(c) < 128)
    with open('sample' + formatted_date + '.txt', 'w') as json_file:
        for lines in filtered_response:
            json_file.writelines(str(lines))


task1=PythonOperator(
    task_id="first_task",
    python_callable=first_function,
    dag=dag,
)

task1