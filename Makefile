install:
	python setup.py develop
	pip install -r requirements.txt

coverage:
	coverage run ./runtests.py

travis: install coverage
