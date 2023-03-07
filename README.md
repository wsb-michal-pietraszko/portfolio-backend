### Bootstrap ###
#### 1. Install pipenv ####
``` $ pip3 install pipenv ```

#### 2. Run pipenv shell ####
``` $ pipenv shell ```
> **_Note_:**
Automatically creates and enables venv

#### 3. Run server #### 
``` $ python3 manage.py runserver ```

### Project info ###
##### Available endpoints: 
* ```/``` - displays: ```Hello Michal```
* ```/hello/``` displays a form with name input then displays the the message: ```Hello <name>```

#### Testing #### 
``` $ python manage.py tests ```

> **_Note_:**
Runs tests from ```/playground/tests.py```