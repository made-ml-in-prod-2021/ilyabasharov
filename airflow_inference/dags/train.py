from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
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

    wait_for_data = FileSensor(
        task_id = 'wait-for-data',
        poke_interval = 10,
        retries = 5,
        filepath = 'data/raw/{{ ds }}/data.csv',
    )

    wait_for_target = FileSensor(
        task_id = 'wait-for-target',
        poke_interval = 10,
        retries = 5,
        filepath = 'data/raw/{{ ds }}/target.csv',
    )

    preprocess = DockerOperator(
        image = 'airflow-preprocess',
        command = ' \
            --data_dir /data/raw/{{ ds }} \
            --output_dir /data/pure/{{ ds }} \
        ',
        network_mode = 'bridge',
        task_id = 'docker-airflow-preprocess',
        do_xcom_push = False,
        volumes = f'{LOCAL_PATH_DATA}:/{DOCKER_PATH_DATA}',
    )

    train = DockerOperator(
        image = 'airflow-train',
        command = ' \
        --data_dir /data/processed/{{ ds }} \
        --model_dir /data/models/{{ ds }} \
        ', 
        network_mode = 'bridge',
        task_id = 'docker-airflow-train',
        do_xcom_push = False,
        volumes = f'{LOCAL_PATH_DATA}:/{DOCKER_PATH_DATA}',
    )

    start >> [wait_for_data, wait_for_target] >> preprocess >> train >> end