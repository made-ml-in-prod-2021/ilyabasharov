##  Homework 02
Assignment for "ML in production" course by Mail.ru group

### Project structure
```
└─── online_inference <- Homework2 code
	│
	├── configs <- Directory with configs
	│	│
	│	├── entities <- Directory for entities configs
	│	└── logs <- Directory for logs configs
	│
	├── setup.py <- Allows to install the project via `pip install -e .`
	├── requirements.txt <- Required libraries. Will be installed automatically (see below)
	│
	├── modules <- Saved modules (models, preprocessors etc.)
	│	│
	│	├── models <- Directiory with fitted models
	│	└── process <- Directiory with fitted data processors
	│
	├── logs <- Directory with saved logs
	├── src	<- Source project code
	│	│
	│	├── test.py <- Test pipeline
	│	├── train.py <- Train pipeline
	│	├── entities <- Set of entities in the form of dataclass. All suggested params of
	│	│	│
	│	│	├── features.py <- ... features included categorical, numerical, target.
	│	│	├── response.py	<- ... basic response
	│	│	├── process.py <- ... raw data processor to make features.
	│	│	├── module.py <- ... modules with non-fixed intrinsic params.
	│	│	├── request.py <- ... basic request
	│	│	├── main.py <- ... set of paths to <model, dataset, processor>.
	│	│	└── loader.py <- Basic loader for all type of structures
	│	│
	│	├── modules <- Module constructors
	│	│	│ 
	│	│	├── models
	│	│	│	│
	│	│	│	├── base.py <- Base form of Model class.
	│	│	│	└── model.py <- Model class example
	│	│	├── io.py <- Save/load module via joblib
	│	│	│
	│	│	└── process
	│	│		│   
	│	│		├── base.py <- Base form of Process class.
	│	│		│
	│	│		├── preprocess.py <- Preprocess class example
	│	│		└── build_features.py <- Example of transformer from raw to features
	│	│
	│	├── logs.py <- Utils for logging
	│	├── app.py <- Main executable file for create web application
	│	└── request.py <- Main executable file for create requests for the app
	│	
	└── tests <- Tests (empty)

```

## Installation

```bash
git clone --branch homework2 https://github.com/made-ml-in-prod-2021/ilyabasharov.git
pip install -e .
```

## Run the app
P.S. all runnings have `--help` argument.

### Run web application

```bash
python3 src/app.py \
	--host '0.0.0.0' \
	--port 8000
```

If you want to check how it works on fake data, run in new terminal tab:

```bash
python3 src/request.py \
	--n_samples 10 \
	--host '0.0.0.0' \
	--port 8000 \
	--log_config 'configs/logs/request.yaml'
```
