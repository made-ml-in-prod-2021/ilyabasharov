##  Homework 01
Assignments for "ML in production" course by Mail.ru group

### Project structure
```
├── LICENSE		<- MIT Licence.
├── setup.py		<- Allows to install the project via `pip install -e .`
├── requirements.txt	<- Required libraries. Will be installed automatically (see below)
├── configs		<- Directory with config files.
│	│
│	├── run		<- Dir with main configs [with paths for <model, dataset, processors> configs]
│	├── datasets	<- ... for custom datasets
│	└── modules		<- ... for custom modules
│		│
│		├── models	<- ... module = models which will be trained
│		└── process	<- ... module = process raw data to model features
│
├── datasets		<- Data which will be used for training/evaluation
│	│
│	├── raw		<- Directiory with raw data
│	└── fake		<- Generated data
│
├── modules		<- Saved modules (models, preprocessors etc.)
│	│
│	├── models		<- Directiory with fitted models
│	└── process		<- Directiory with fitted data processors
│
├── src			<- Source project code
│	│
│	├── test.py		<- Test pipeline
│	├── train.py	<- Train pipeline
│	├── entities	<- Set of entities in the form of dataclass. All suggested params of
│	│	│
│	│	├── dataset.py	<- ... custom dataset
│	│	├── features.py <- ... features included categorical, numerical, target.
│	│	├── module.py	<- ... modules with non-fixed intrinsic params.
│	│	├── process.py	<- ... raw data processor to make features.
│	│	├── module.py	<- ... modules with non-fixed intrinsic params.
│	│	├── split.py	<- ... dataset splitting.
│	│	├── main.py	<- ... set of paths to <model, dataset, processor>.
│	│	└── loader.py	<- Basic loader for all type of structures
│	│
│	├── modules		<- Module constructors
│	│	│ 
│	│	├── models
│	│	│	│
│	│	│	├── base.py	<- Base form of Model class.
│	│	│	└── model.py
│	│	│		<- Model class example
│	│	│
│	│	└─── process
│	│		│   
│	│		├── base.py <- Base form of Process class.
│	│		│
│	│		├── preprocess.py
│	│		│		<- Preprocess class example
│	│		└── build_features.py
│	│				<- Example of transformer from raw to features
│	├── visualisation
│	│				<- Directiory for report
│	├── io.py	<- Save/load module via joblib
│	└── logs.py <- Utils for logging
└── tests			<- Tests (empty)

```

### Installation

```bash
pip install -e .
```

### Run the project
P.S. all runnings have `--help` argument.

#### Run training/evaluation

```bash
python3 src/train.py --config configs/run/train_logreg.yaml
```
Models and preprocessors will be saved based on `--config` argument.
Also you can change the the model and preprocessor pipeline inside `--config` argument path.

#### Run testing

```bash
python3 src/test.py --config configs/run/test.yaml
```
Predictions will be saved based on `--config` argument path.

#### Run fake data generation
```bash
python3 src/generate_data.py --n_samples 1000 --original_data_path datasets/raw/heart_disease.csv --save_path datasets/fake/fake.csv
```

#### Run report creation

```bash
python3 python3 src/visualisation/report.py --dataset_path datasets/raw/heart_disease.csv --save_path logs/report.html
```

### Review

:heavy_plus_sign: -2) Назовите ветку homework1 (1 балл)
:one:

:heavy_plus_sign: -1) положите код в папку ml_project
:one:

:heavy_plus_sign: 0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (2 балла)
:three:

:heavy_plus_sign: 1) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов)
Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)
Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл)
:six:

:heavy_plus_sign: 2) Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов)
:eight:

:heavy_plus_sign: 3) использованы логгеры (2 балла)
:one::zero:

:heavy_minus_sign: 4) написаны тесты на отдельные модули и на прогон всего пайплайна(3 баллов)
*Не сделано*
:one::zero:

:heavy_plus_sign: 5) Для тестов генерируются синтетические данные, приближенные к реальным (3 баллов)
- можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
- можно просто руками посоздавать данных, собственноручно написанными функциями
как альтернатива, можно закоммитить файл с подмножеством трейна(это не оценивается)
*Генератор данных написан в файле generate_data.py, см запуск выше*
:one::three:

:heavy_plus_sign: 6) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла)  
*sgd_classifier и logistic regression, лежат в папке `configs/run`*
:one::six:

:heavy_plus_sign: 7) Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) 
:one::nine:

&pm; 8) Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3 балла)
*Написан, но не протестирован, 2 балла?*
:two::one:

:heavy_plus_sign: 9) Обучите модель, запишите в readme как это предлагается (3 балла)
:two::four:

:heavy_plus_sign: 10) напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла)  
*Описано выше, реализован метод в классе Model*
:two::seven:

:heavy_minus_sign: 11) Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы)
:two::seven: :penguin:

:heavy_plus_sign: 12) Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome)
:two::seven: :penguin:

:heavy_plus_sign: 13) Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы)
:two::eight: :penguin:
