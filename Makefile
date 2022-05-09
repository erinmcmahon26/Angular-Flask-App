# installs virtual environment
setup:
	python3 -m venv ~/.Flask-App

# installs source code from a requirements file
# also updates pip to the current version
install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

# test the libraries and notebooks
test:
	python -m pytest -vv test_hello.py
	#python -m pytest --nbval notebook.ipynb

format:
	black *.py

# disables false positives and keeps recommendation warnings but leaves errors
# linting library, command-line tool, and web application
lint:
	pylint --disable=R,C hello.py

# run "make all" to have all commands run
all: install lint test