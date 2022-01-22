web: gunicorn PlanningWebApp.wsgi --log-file -
release: python manage.py migrate
release: python manage.py makemigration