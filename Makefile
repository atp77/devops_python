install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app

test:
	pytest --cov=app

format:
	black *.py