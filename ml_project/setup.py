import os
import setuptools

REQUIREMENTS_PATH = "requirements.txt"

with open(REQUIREMENTS_PATH, 'r') as file:
    required_libraries = file.read().splitlines()

setuptools.setup(
	name             = 'Homework01',
	version          = '0.1.0',
	description      = 'Machine Learning in Production course: Homework 01',
	long_description = 'README.md',
	packages         = setuptools.find_packages(),
	author           = 'Basharov Ilya',
	install_requires = required_libraries,
	license          = 'MIT',
	license_files    = 'LICENSE',
)