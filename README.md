# Button Press Web

A web project using Django

## Setup

make sure python and git installed and clone the repository into a directory

    git clone https://github.com/mbdaryanto/button_press_web.git

make virtualenv inside the directory

    cd button_press_web
    python3 -m venv venv
    source venv/bin/activate

install all the python requirements

    pip install -r requirements

change the settings in `djsite/settings.py` if you want to store
using another database or leave it if you want to use sqlite.
Run the database migration

    python manage.py migrate

and finally run the server

    python manage.py runserver
