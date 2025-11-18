# Task List (GER: Aufgabenliste)

A lightweight TODO list web application developed with Django, designed to demonstrate the framework’s core features.
<img width="987" height="247" alt="Task1_Task2" src="https://github.com/user-attachments/assets/e3483f25-bb97-4538-ba10-61e2000146d5" />


## Prerequisites

- Install [Python](https://www.python.org/downloads/) (version 3.10 or higher recommended).
- Make sure `pip` is available (it comes bundled with Python).

## Installation

1. **Clone the repository**
   ```
   git clone https://github.com/RafaelFloimayr/Aufgabenliste.git     
   cd Aufgabenliste
2. **Create a virtual environment (recommended)**
   
   ```
   python -m venv venv  
   source venv/bin/activate   # Linux/Mac     
   venv\Scripts\activate      # Windows
3. **Install Django**
   
   ```
   pip install django
4. **Apply migrations - This will set up the database tables:**
   
   ```
   python manage.py migrate
5. **Start the webserver**
    
   ```
   python manage.py runserver
6. **Access the website**
   
Open http://localhost:8000/ in your web browser and manage your tasks.

7. **Django REST framework**
   
Open http://localhost:8000/tasks/ in your web browser to view your tasks. Using the browsable REST API interface, you can perform GET and POST requests directly.
<img width="1178" height="780" alt="DjangoRestFramework" src="https://github.com/user-attachments/assets/678a9d85-77fc-4b98-a4c6-cfe2ab351456" />
To perform DELETE and PUT requests, append the task number to the URL, e.g. http://localhost:8000/tasks/1.

## Additional notes
Run `python manage.py createsuperuser` to create an admin account and access the Django Admin interface.  
Use `python manage.py makemigrations` to prepare new database changes.  
After making model changes, run `python manage.py migrate` again to apply them.
