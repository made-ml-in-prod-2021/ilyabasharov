#  Homework 03
Assignment for "ML in production" course by Mail.ru group

## Project structure
```
├── airflow_inference <- Code for Homework3 (see additionals inside)
│
└── README.md <- this file you are reading right now
```

## Installation

There are two ways of docker image build: locally (via dockerfile) and via dockerhub.

### Change the paths on .env file

### Install the docker image via dockerfile

```bash
git clone --branch homework3 https://github.com/made-ml-in-prod-2021/ilyabasharov.git
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
cd ilyabasharov/airflow_inference/
docker-compose build
```

## Run the app

P.S. all runnings have `--help` argument.

```bash
cd ilyabasharov/airflow_inference/
docker-compose up
```

## Review

:heavy_plus_sign: 0) Поднимите airflow локально, используя docker compose (можно использовать из примера) (0 баллов)
:zero:

:heavy_plus_sign: 1) Реализуйте dag, который генерирует данные для обучения модели (генерируйте данные, можете использовать как генератор синтетики из первой дз, так и что-то из датасетов sklearn), вам важно проэмулировать ситуации постоянно поступающих данных (5 балла)
:five:

:heavy_minus_sign::heavy_plus_sign: 2) Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. В вашем пайплайне должно быть как минимум 4 стадии, но дайте волю своей фантазии=)

Пояснение: Реализовано 2/4 - preprocess/train

:one::zero:

:heavy_plus_sign: 3) Реализуйте dag, который использует модель ежедневно (5 баллов)
:one::five:

:heavy_plus_sign: 4) вы можете выбрать 2 пути для выполнения ДЗ. все даги реализованы только с помощью DockerOperator (10 баллов)
:two::five:

:heavy_minus_sign: 5) Протестируйте ваши даги (5 баллов) https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
:two::five:

:heavy_minus_sign: 6) В docker compose так же настройте поднятие mlflow и запишите туда параметры обучения, метрики и артефакт(модель) (5 доп баллов)
:two::five:

:heavy_minus_sign: 7) Вместо пути в airflow variables используйте апи Mlflow Model Registry (5 доп баллов)
:two::five:

:heavy_minus_sign: 8) Настройте alert в случае падения дага (3 доп. балла)
:two::five:

:heavy_plus_sign: 9) традиционно, самооценка (1 балл)
:two::six:

:heavy_plus_sign: 10) создайте пулл-реквест и поставьте label -- hw3 (0 баллов)
:two::six: :penguin:

Итого :two::six:

PS. Было очень тяжело дебажить - в логах полно непонятной информации, в интернетах пишут всякое разное ...
