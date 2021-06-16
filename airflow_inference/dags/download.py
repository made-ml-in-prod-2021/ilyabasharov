import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'airflow',
    'email': ['airflow@example.com', ],
    'retries': 1,
    "retry_delay": timedelta(minutes=5),
}

LOCAL_PATH_DATA = Variable.get('LOCAL_PATH_DATA')
DOCKER_PATH_DATA = Variable.get('DOCKER_PATH_DATA')

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

    path_raw = os.path.join(DOCKER_PATH_DATA, 'raw/{{ ds }}/')

    download = DockerOperator(
        image = 'ilyabasharov/airflow-download',
        command = f'--output_dir {path_raw}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-download',
        do_xcom_push = False,
        volumes = [f'{LOCAL_PATH_DATA}:{DOCKER_PATH_DATA}', ],
    )

    start >> download >> end