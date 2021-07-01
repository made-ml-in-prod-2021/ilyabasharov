import os
import setuptools

REQUIREMENTS_PATH = 'requirements.txt'
README_PATH       = 'README.md'

with open(REQUIREMENTS_PATH, 'r') as file:
    required_libraries = file.read().splitlines()

with open(README_PATH, 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name             = 'Homework02',
    version          = '0.1.0',
    description      = 'Machine Learning in Production course: Homework 02',
    long_description = long_description,
    long_description_content_type = \
                       'text/markdown',
    packages         = setuptools.find_packages(),
    author           = 'Basharov Ilya',
    author_email     = 'ilya.basharov.98@mail.ru',
    install_requires = required_libraries,
    license          = 'MIT',
    license_files    = 'LICENSE',
    python_requires  = '>=3.8',
    classifiers      = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    url              = 'https://github.com/made-ml-in-prod-2021/ilyabasharov/tree/homework2',
)
