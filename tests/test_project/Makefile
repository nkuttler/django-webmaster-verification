db.sqlite:
	python manage.py syncdb --noinput
	
.PHONY: test
test: db.sqlite
	PYTHONPATH=.. python manage.py test test_app
