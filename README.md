# Housing Society Management System — Django Edition

This version migrates the original JSP page layouts to Django templates while retaining the original CSS files, page colors, image assets and main HTML structure. The Java/JSP scriptlets have been removed; data-driven legacy tables may need their Django model/query implementation completed.

## Run in Visual Studio Code (Windows)
1. Extract this ZIP and open the `Housing_Society_Django` folder in VS Code.
2. Open Terminal and run:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python manage.py makemigrations society
   python manage.py migrate
   python manage.py runserver
   ```
3. Visit http://127.0.0.1:8000/ .
4. Admin: `python manage.py createsuperuser`, then open http://127.0.0.1:8000/admin/ .

Database: SQLite (created automatically). CSS assets are copied from the original project without redesigning their colors.


## Admin login flow
1. Run `python manage.py createsuperuser` and create an account.
2. Use that username and password on `/admin_login/`. The account must be staff (the superuser created by this command is staff).
3. Successful login redirects to `/admin_dashboard/`. POST forms include Django CSRF tokens.
"# Housing-Society-Management-System" 
