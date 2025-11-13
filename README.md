# Task List (GER: Aufgabenliste)

A lightweight TODO list web application developed with Django, designed to demonstrate the framework’s core features.

## Prerequisites

- Install [Python](https://www.python.org/downloads/) (version 3.10 or higher recommended).
- Make sure `pip` is available (it comes bundled with Python).

## Installation

1. **Clone the repository**
   ```
   git clone https://github.com/RafaelFloimayr/Aufgabenliste.git     
   cd Aufgabenliste

2. Create a virtual environment (recommended)
   
   ```
   python -m venv venv  
   source venv/bin/activate   # Linux/Mac     
   venv\Scripts\activate      # Windows

3. Install Django
   
   ```
   pip install django

5. Apply migrations - This will set up the database tables:
   
   ```
   python manage.py migrate

5. Start the webserver
    
   ```
   python manage.py runserver

7. Access the website
Open http://localhost:8000/ in your web browser.

Additional notes
    Run `python manage.py createsuperuser` to create an admin account and access the Django Admin interface.  
    Use `python manage.py makemigrations` to prepare new database changes.  
    After making model changes, run `python manage.py migrate` again to apply them.
