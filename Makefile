install:
	python setup.py develop
	pip install -r requirements.txt

test:
	./runtests.py

travis: install test
