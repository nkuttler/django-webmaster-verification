test:
	python quicktest.py webmaster_verification
	python quicktest.py webmaster_verification --multicode

install:
	python setup.py install

build:
	python setup.py build

sdist:
	python setup.py sdist

upload:
	python setup.py sdist upload

clean:
	rm -rf dist build *.egg-info django-webmaster-verification-*
	rm -rf .coverage coverage

.PHONY: .coverage
.coverage:
	coverage run --source=webmaster_verification quicktest.py webmaster_verification
	coverage run --source=webmaster_verification quicktest.py webmaster_verification --multicode

coverage: .coverage
	coverage html -d coverage
