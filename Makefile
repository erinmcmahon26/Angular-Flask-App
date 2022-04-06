# installs virtual environment
setup:
	python3 -m venv ~/.Flask-App

# installs source code from a requirements file
# also updates pip to the current version
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# test the libraries and notebooks
test:
	python -m pytest -vv --cov=Flask-Applib tests/*.py
	python -m pytest --nbval notebook.ipynb

# disables false positives and keeps recommendation warnings but leaves errors
# linting library, command-line tool, and web application
lint:
	pylint --disable=R,C Flask-Applib cli web

# will run all of them together
# run "make all"
all: install lint test