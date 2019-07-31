install:
	pip3 install -r requirements.txt --user
	python3 setup.py install

clean:
	python setup.py clean
	rm -rf MANIFEST build dist moon.egg-info

build:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

test:
	pytest tests

