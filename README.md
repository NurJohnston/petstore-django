This project was a proof-of-concept to show I understand how to build something in Django. It covers 
setting up models, handling requests, database operations, and basic CRUD functionality. For the API 
integration piece, I built endpoints to handle GET, POST, PUT, PATCH, and DELETE, then tested all of 
them with Postman to make sure everything was hitting correctly.

To run it:
git clone https://github.com/NurJohnston/petstore-django.git
cd petstore-django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
