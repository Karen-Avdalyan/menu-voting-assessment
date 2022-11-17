# Installation process

this is project about restaurant menu voting api...

#### how to configure and get run the project
1. you need to clone this project to your computer
2. you will need some tools like docker and python

## how to run with docker
1. open the terminal
2. go to project root directory (if you didn't know how you can use command cd <relative path/absalute path to project>)
3. copy the .env.example file and rename to .env 
4. you will need to build dockerized project.For this<br/>
type:
    ```
    docker compose build
    ```
*if you get the error you can try with docker-compose (use this if you get error like docker command not found, or something like that)... <br/>
<br/>
5.  then just run:
    ```
    docker compose up
    ```

## how to run without docker
###### (not recomended, becouse you will need to run local db  and so on , but in docker version you can just run the application with dockerized db)
if you want to run without docker files (locally) you can continue with this steps.<br/>
1. open terminal 
2. go to root dir of project
3. activate conda or venv environment (here will be example with conda, but if you want to run with venv you can try to search it's sample proces like this)
    ```
    conda activate
    ```
4. after activating you need to download all modules that need for correct working
    ```cmd
    pip install -r requirements.txt
    ```
5. you need to have mysql db with conditionals witch are mentioned in .env.example (or you can put your conditionals on .env file)
6. then just run migrations for this type this commands
    ```cmd
    python manage.py makemigrations
    ```
    ```cmd
    python manage.py migrate
    ```
7. just run the application.
    ```cmd
    python manage.py runserver
    ```
   
## how to run tests

1. To run tests you will need a sample database.
2. Create test db, run migrations via `manage.py makemigrations` then `manage.py migrate`.
3. Change environment variables to work with test db.
4. View `test_db.py` for info on what should the db have.
5. Run tests via `manage.py test`
