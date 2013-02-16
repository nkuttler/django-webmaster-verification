.PHONY: test
test: db.sqlite
	python manage.py test --failfast --settings=test_project.settings_multicode
	python manage.py test --failfast

db.sqlite:
	python manage.py syncdb --noinput

.coverage:
	coverage run --source=webmaster_verification manage.py test

htmlcov: .coverage
	coverage html
