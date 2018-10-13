Steps to Run Project,

1. Clone the Repositry using the Git url.
2. Change directory into the Repositry.
3. Create a Virtual Environment.
4. Activate the Virtual Environment.
5. Install the requirements using the requirements.txt "pip install -r requirements.txt".
6. Run the Migrations using the command "python manage.py migrate".
7. Create the Admin Super User using command "python manage.py createsuperuser".
6. Run the project using command "python manage.py runserver".
7. Access the Application from the url "localhost:8000"in the browser.

API Url's:

1. List all Todos : localhost:8000/todos
2. Display Single Todo : localhost:8000/todo/<todo-id>