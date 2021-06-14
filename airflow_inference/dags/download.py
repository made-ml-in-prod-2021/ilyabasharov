from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'airflow',
    'email': ['ilya.basharov.98@mail.ru', ],
    'retries': 1,
    "retry_delay": timedelta(minutes=5),
}

LOCAL_PATH_DATA = Variable.get('LOCAL_PATH_DATA')
DOCKER_PATH_DATA =  Variable.get('DOCKER_PATH_DATA')

with DAG(
    'download_dag',
    default_args = default_args,
    schedule_interval = '@daily',
    start_date = days_ago(1),
) as dag:

    start = DummyOperator(
        task_id = 'start',
    )

    end = DummyOperator(
        task_id = 'end',
    )

    download = DockerOperator(
        image = 'airflow/airflow-download',
        command = '--output_dir /data/raw/{{ ds }}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-download',
        do_xcom_push = False,
        volumes = f'{LOCAL_PATH_DATA}:/{DOCKER_PATH_DATA}',
    )

    start >> download >> end