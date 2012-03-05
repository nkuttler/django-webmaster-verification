db.sqlite:
	python manage.py syncdb --noinput

.PHONY: test
test: db.sqlite
	python manage.py test --settings=test_project.settings_multicode
	python manage.py test
