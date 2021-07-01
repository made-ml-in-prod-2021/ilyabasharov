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

    path_raw = os.path.join(DOCKER_PATH_DATA, 'raw/{{ ds }}/')

    wait_for_data = FileSensor(
        task_id = 'wait-for-data',
        poke_interval = 10,
        retries = 5,
        filepath = os.path.join(path_raw, 'data.csv'),
    )

    model_path = os.path.join(DOCKER_PATH_DATA, 'model/{{ ds }}/')

    wait_for_model = FileSensor(
        task_id = 'wait-for-model',
        poke_interval = 10,
        retries = 5,
        filepath = os.path.join(model_path, 'model.joblib'),
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

    prediction_path = os.path.join(DOCKER_PATH_DATA, 'prediction/{{ ds }}/')

    predict = DockerOperator(
        image = 'ilyabasharov/airflow-predict',
        command = f'--data_dir {path_raw} --prediction_dir {prediction_path} --model_dir {model_path}',
        network_mode = 'bridge',
        task_id = 'docker-airflow-predict',
        do_xcom_push = False,
        volumes = [f'{LOCAL_PATH_DATA}:{DOCKER_PATH_DATA}', ],
    )

    start >> [wait_for_data, wait_for_model] >> preprocess >> predict >> end
