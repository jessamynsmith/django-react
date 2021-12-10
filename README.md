# Django React Example

This project integrates a React app (from Create React App) into a Django webapp.

## Getting started

git clone https://github.com/jessamynsmith/django-react.git
cd django-react

### Frontend

cd frontend
yarn build

### Backend

Create a virtualenvironment and activate it.

    pip install -r requirements.txt

    python manage.py migrate

    python manage.py runserver

In the browser, go to the application and sign up:

    http://127.0.0.1:8000/accounts/signup/

You can see the homepage at:

    http://127.0.0.1:8000