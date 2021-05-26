#!/bin/bash

echo "Start train logistic regression model"
python3 src/train.py --config configs/run/train_logreg.yaml
echo "Done training logistic regression model"

echo "Start train Classifier model"
python3 src/train.py --config configs/run/train_sgd.yaml
echo "Done training SGD Classifier model"

echo "Start generating data for testing"
python3 src/generate_data.py \
	--n_samples 1000 \
	--original_data_path datasets/raw/heart_disease.csv \
	--save_path datasets/fake/fake.csv
echo "Done generating data for testing"

echo "Start testing a model"
python3 src/test.py --config configs/run/test.yaml
echo "Done testing a model"

echo "Start creating a report based on the dataset"
python3 src/visualisation/report.py \
	--dataset_path datasets/raw/heart_disease.csv \
	--save_path logs/report.html
echo "Done creating a report based on the dataset"

echo "Finished!"
