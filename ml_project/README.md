##  Homework 01
Assignments for "ML in production" course by Mail.ru group

### Project structure
```
├── LICENSE		<- MIT Licence.
├── setup.py		<- Allows to install the project via `pip install -e .`
├── requirements.txt	<- Required libraries. Will be installed automatically (see below)
├── configs		<- Directory with config files.
│   │
│   ├── main.yaml	<- config with paths for <model, dataset, processors> configs
│   ├── datasets	<- ... for custom datasets
│   └── modules		<- ... for custom modules
│	│
│   	├── models	<- ... module = models which will be trained
│   	└── process	<- ... module = process raw data to model features
│
├── datasets		<- Data which will be used for training/evaluation
│   │
│   ├── raw		<- Directiory with raw data
│   └── fake		<- Generated data
│
├── modules		<- Saved modules (models, preprocessors etc.)
│   │
│   ├── models		<- Directiory with fitted models
│   └── process		<- Directiory with fitted data processors
│
├── src			<- Source project code
│   │
│   ├── main.py		<- Main file for run
│   ├── entities	<- Set of entities in the form of dataclass. All suggested params of
│   │   │
│   │   ├── dataset.py	<- ... custom dataset
│   │   ├── features.py <- ... features included categorical, numerical, target.
│   │   ├── module.py	<- ... modules with non-fixed intrinsic params.
│   │   ├── process.py	<- ... raw data processor to make features.
│   │	├── module.py	<- ... modules with non-fixed intrinsic params.
│   │   ├── split.py	<- ... dataset splitting.
│   │	├── main.py	<- ... set of paths to <model, dataset, processor>.
│   │	└── loader.py	<- Basic loader for all type of structures
│   │
│   └── modules		<- Module constructors
│	│
│       ├── models
│	│   │
│       │   ├── base.py	<- Base form of Model class.
│	│   └── model.py
│	│		<- Model class example
│	│
│	├── process
│	│   │   
│	│   ├── base.py <- Base form of Process class.
│	│   │
│	│   ├── preprocess.py
│	│   │		<- Preprocess class example
│	│   └── build_features.py
│	│		<- Example of transformer from raw to features
│	└── io.py	<- Save/load module as joblib
│
└── tests             	<- Tests

```

### Installation

```bash
	pip install -e .
```