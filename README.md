#  Homework 02
Assignment for "ML in production" course by Mail.ru group

## Project structure
```
├── docker <- Directory for docker
│	│
│	├── Dockerfile
│	├── build.sh
│	├── start_devel.sh
│	└── into.sh
│
├── online_inference <- Code for Homework2 (see additionals inside)
│
└── README.md <- this file which you are reading right now
```

## Installation

There are two ways of docker image build: locally (via dockerfile) and via dockerhub.

### Install the docker image via dockerfile

```bash
git clone --branch homework2 https://github.com/made-ml-in-prod-2021/ilyabasharov.git
cd ilyabasharov/
./docker/build.sh
```

### Install the docker image via dockerhub
```bash
git clone --branch homework2 https://github.com/made-ml-in-prod-2021/ilyabasharov.git
cd ilyabasharov/
docker pull ilyabasharov/made_mail.ru:latest
```

## Run the app

P.S. all runnings have `--help` argument.

```bash
./docker/start_devel.sh
python3 src/app.py \
	--host '0.0.0.0'
	--port 8000
```

If you want to check how it works on fake data, run in new terminal tab:

```bash
./docker/into.sh
python3 src/request.py \
	--n_samples 10
	--host '0.0.0.0'
	--port 8000
	--log_config 'configs/logs/request.yaml'
```

## Docker image size reduction

There was experiments with docker images:
1) python:3.8 - > 1 GB P.S. Huge
2) python:3.8-alpine - < 300 MB P.S. Installation takes a huge amount of time!
3) python:3.8-slim - ~ 600 MB P.S. Optimal

## Review

:heavy_plus_sign: 0) Ветку назовите homework2, положите код в папку online_inference(0 баллов)
:zero:

:heavy_plus_sign: 1) Оберните inference вашей модели в rest сервис(вы можете использовать как `FastAPI`, так и `flask`, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict (3 балла)
:three:

??? 2) Напишите тест для /predict (3 балла) ([пример fastapi](https://fastapi.tiangolo.com/tutorial/testing/), [пример flask](https://flask.palletsprojects.com/en/1.1.x/testing/))

Пояснение - request обернут в `pydantic` для избежания дальнейшнего проверки типов. Будет ли это зачтено лектором - не знаю.
:three:

:heavy_plus_sign: 3) ВНапишите скрипт, который будет делать запросы к вашему сервису (2 балла)
:five:

:heavy_plus_sign: 4) Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном, типы не те и пр, в рамках вашей фантазии)  (вы можете сохранить вместе с моделью доп информацию, о структуре входных данных, если это нужно)
[пример](https://fastapi.tiangolo.com/tutorial/handling-errors/) -- возращайте 400, в случае, если валидация не пройдена (3 балла)
:eight:

:heavy_plus_sign: 5) Напишите `dockerfile`, соберите на его основе образ и запустите локально контейнер(`docker build`, `docker run`), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4 балла)
:one::two:

:heavy_minus_sign::heavy_plus_sign: 6) Оптимизируйте размер docker image (опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться) -- [пример](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) (3 балла)
:one::three:

:heavy_plus_sign: 7) опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) (2 балла)
:one::five:

:heavy_plus_sign: 8) Hапишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1 балл)
:one::six:

:heavy_plus_sign: 9) проведите самооценку (1 балл)
:one::seven:

:heavy_plus_sign: 10) создайте пулл-реквест и поставьте label -- hw2 (0 баллов)
:one::seven: :penguin:

Итого :one::seven:
