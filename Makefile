install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black scripts/*.py
	black cancerrisknet/

lint:
	pylint --disable=R,C scripts/*.py
	pyliny cancerrisknet/

deploy:
	# deploy here to AWS EC2

all: install format lint test deploy