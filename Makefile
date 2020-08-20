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

# Pre-commit things
pre-commit: blackcheck flake8 docformatter
style: black flake8 reorder-imports docformatter

docformattercheck:
	docformatter -r --make-summary-multi-line --pre-summary-newline webmaster_verification/ --check

docformatter:
	docformatter -r --make-summary-multi-line --pre-summary-newline webmaster_verification/ -i

.PHONY: flake8
flake8:
	flake8

.PHONY: pylint
pylint:
	pylint --exit-zero webmaster_verification > reports/pylint.json
	pylint-json2html -f jsonextended -o reports/pylint.html < reports/pylint.json

.PHONY: reorder-imports
reorder-imports:
	PYTHONPATH="" find webmaster_verification/ -type f -name "*.py" -exec reorder-python-imports --py36-plus --application-directories=.:webmaster_verification {} \;

.PHONY: black blackcheck
black:
	black --line-length 89 webmaster_verification/

blackcheck:
	black --check --line-length 89 webmaster_verification/
