test:
	make -C test_project test

.coverage:
	coverage run --source=webmaster_verification manage.py test

htmlcov: .coverage
	coverage html
