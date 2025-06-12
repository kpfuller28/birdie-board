

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

shell:
	python3 manage.py shell

# Create a virtual environment in the folder 'venv'
venv:
	python3 -m venv venv

# Install requirements into the virtual environment
install:
	. venv/bin/activate && pip install -r requirements.txt

# Activate the venv and run the Django server
run:
	. venv/bin/activate && python manage.py runserver
