# **WELCOME TO DJANGO**
To use django in your system without any interruption create a virtual environ ment using 'pipenv'.

    ```
    pip install pipenv
    ```

After the installation of the 'pipenv' library, use it to install django.

    ```
    pipenv install django
    ```

This will create a new virtual environment with django in it.

Django offers following functionalities which can be used executed with either **django-admin** or **manage.py**.
These are all command-line tool in a Django project.

| **Functions** | **Functionalities** |
|---------------|---------------------|
| **check** | Checks the project for various problems, including syntax errors in Python files and potential issues with the project configuration.|
| **compilemessages** | Compiles all of the message files created with makemessages into binary message files that can be used by the gettext library. |
| **createcachetable** | Creates the database table used by the cache framework. |
| **dbshell** | Opens a database shell for the project's database, allowing the user to run SQL commands directly. |
| **diffsettings** | Displays the differences between the current project settings and the default settings. |
| **dumpdata** | Dumps the contents of the database as a JSON or YAML file. |
| **flush** | Deletes all data from the project's database. |
| **inspectdb** | Introspects the database tables and generates Django models based on them. |
| **loaddata** | Loads data from a JSON or YAML file into the project's database. |
| **makemessages** | Creates message files for translation using the gettext library. |
| **makemigrations** | Generates new database migration files based on changes to the project's models. |
| **migrate** | Runs the database migrations to update the schema to match the current models.|
| **optimizemigration** | Optimizes the migration files by removing redundant operations. |
| **runserver** | Starts the development server for the project.|
| **sendtestemail** | Sends a test email to the email address specified in the project settings. |
| **shell** | Opens a Python shell with the project's environment loaded. |
| **showmigrations** | Lists all of the project's migrations and their current status. |
| **sqlflush** | Prints the SQL statements that would be executed to delete all data from the project's database. |
| **sqlmigrate** | Prints the SQL statements that would be executed for a specific migration. |
| **sqlsequencereset** | Prints the SQL statements that would be executed to reset database sequences for a specific app. |
| **squashmigrations** | Combines multiple migration files into a single file. |
| **startapp** | Creates a new Django app within the project.|
| **startproject** | Creates a new Django project. |
| **test** | Runs the project's tests. |
| **testserver** | Runs a development server with the project's test database. |

# **Creating new project: P001**
For new project we created a new folder inside it that is 'P001'.

```
django-admin startproject studybud .
```
**Note: Here we have changed the directory to P001**

To check if the created application is working fine:

```
python manage.py runserver

In the created project we following file:

| Files in studybud project in P001 | Functionalities |
|-----------------------------------|-----------------|
| P001/studybud/__init__.py | The __init__.py file is a special Python file that is executed when a package is imported. It is used to define the package's behavior when it is imported and to execute any initialization code that the package requires.
Here are some common functions of the __init__.py file:
-  Package Initialization: The __init__.py file is used to define the behavior of a package when it is imported. It can define what modules should be loaded, what variables and functions should be exposed to the package namespace, and what subpackages should be imported.

-  Namespace Packages: In Python 3.3 and later versions, the __init__.py file is not required for namespace packages. Instead, a namespace package is defined as a directory containing a __init__.py file or a set of directories containing packages or other namespace packages.

-  Initialization Code: The __init__.py file can also contain initialization code that the package requires to function properly. This can include setting up environment variables, initializing database connections, or any other code that needs to be run before the package can be used.

-  Import Statements: The __init__.py file can also contain import statements that load modules or subpackages that the package depends on. This allows the package to be self-contained and self-sufficient, without requiring the user to manually import dependencies.

In summary, the __init__.py file is used to define a package's behavior when it is imported and to execute any initialization code that the package requires. It is an essential component of any Python package and allows for efficient and organized package management. |
| P001/studybud/asgi.py |  |
| P001/studybud/settings.py |  |
| P001/studybud/urls.py |  |
| P001/studybud/wsgi.py | This stands for web server gateway interface |
| P001/db.sqlite3 |  |
| P001/manage.py |  |