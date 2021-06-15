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
    'predict_model',
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

    wait_for_data = FileSensor(
        task_id = 'wait-for-data',
        poke_interval = 10,
        retries = 5,
        filepath = 'data/raw/{{ ds }}/data.csv',
    )

    wait_for_model = FileSensor(
        task_id = 'wait-for-model',
        poke_interval = 10,
        retries = 5,
        filepath = 'data/model/{{ ds }}/model.pkl',
    )

    preprocess = DockerOperator(
        image = 'airflow-preprocess',
        command = '--data_dir /data/raw/{{ ds }} --output_dir /data/pure/{{ ds }}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-preprocess',
        do_xcom_push = False,
        volumes = f'{LOCAL_PATH_DATA}:/{DOCKER_PATH_DATA}',
    )

    predict = DockerOperator(
        image = 'airflow-predict',
        command = '--data_dir /data/raw/{{ ds }} --prediction_dir /data/prediction/{{ ds }} --model_dir data/model/{{ ds }}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-predict',
        do_xcom_push = False,
        volumes = f'{LOCAL_PATH_DATA}:/{DOCKER_PATH_DATA}',
    )

    start >> [wait_for_data, wait_for_model] >> preprocess >> predict >> end
