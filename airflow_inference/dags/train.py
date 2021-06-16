import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
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
    'train_model',
    default_args = default_args,
    schedule_interval = '@weekly',
    start_date = days_ago(1),
) as dag:

    start = DummyOperator(
        task_id = 'start',
    )

    end = DummyOperator(
        task_id = 'end',
    )

    path_raw = os.path.join(DOCKER_PATH_DATA, 'raw/{{ ds }}/')

    wait_for_data = FileSensor(
        task_id = 'wait-for-data',
        poke_interval = 10,
        retries = 5,
        filepath = os.path.join(path_raw, 'data.csv'),
    )

    wait_for_target = FileSensor(
        task_id = 'wait-for-target',
        poke_interval = 10,
        retries = 5,
        filepath = os.path.join(path_raw, 'target.csv'),
    )

    preprocessed_path = os.path.join(DOCKER_PATH_DATA, 'pure/{{ ds }}/')

    preprocess = DockerOperator(
        image = 'ilyabasharov/airflow-preprocess',
        command = f'--data_dir {path_raw} --output_dir {preprocessed_path}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-preprocess',
        do_xcom_push = False,
        volumes = [f'{LOCAL_PATH_DATA}:{DOCKER_PATH_DATA}', ],
    )

    model_path = os.path.join(DOCKER_PATH_DATA, 'model/{{ ds }}/')

    train = DockerOperator(
        image = 'ilyabasharov/airflow-train',
        command = f'--data_dir {preprocessed_path} --model_dir {model_path}', 
        network_mode = 'bridge',
        task_id = 'docker-airflow-train',
        do_xcom_push = False,
        volumes = [f'{LOCAL_PATH_DATA}:{DOCKER_PATH_DATA}', ],
    )

    start >> [wait_for_data, wait_for_target] >> preprocess >> train >> end
    