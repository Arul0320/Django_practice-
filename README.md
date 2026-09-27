# Django Student Portal — Day 2, 3 & 4
## Setup (Windows)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations portal
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ . Pages: `/register/`, `/contact/`, `/admin/`.
Email uses Django's console backend, so email content is printed in the terminal instead of being sent externally.
