Microblog
===================

[![CI](https://github.com/andreasarne/microblog-stud2/actions/workflows/ci.yml/badge.svg)](https://github.com/andreasarne/microblog-stud2/actions/workflows/ci.yml)

[![Join the chat at https://gitter.im/dbwebb-se/devops](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dbwebb-se/devops?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Course material for a devops course, aimed at a Swedish course in computer science on University level new to devops. The students are to further develop this application and integreate it with new tools.

Released as part of a University course: https://dbwebb.se/kurser/devops

The application used in this course is based on [The flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).




Dev environment
------------------

The development environment is a dev container: a container with the tools of the course, at fixed versions. More tools are added to it as the course goes on. Here is how you setup the development environment and start the application.



### Dev container

1. Install Docker (Docker Desktop must be running), Git and Visual Studio Code with the extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). On Windows, use WSL and clone the repo inside WSL, not on the C: drive.
2. Open the folder in VS Code and choose "Reopen in Container".

The first start takes a few minutes. It creates a virtual environment in `venv/` and installs the packages for testing. Use the terminal in VS Code, it runs in the container.

The application and the containers you start run on your computer, not inside the dev container. Reach them with your browser on `localhost:<port>`. `curl localhost:<port>` in the terminal inside the dev container does not reach them.



### Packages

The dev container installs the packages for you. Without the dev container, use Python 3.11, create a virtual environment and install the packages:
```
python3 -m venv venv
source venv/bin/activate
make install-test
```

Later in the course `make install-dev` installs the packages for Ansible too.


### Database

Setup SQLite database if `migrations` folder already exist:
```
flask db upgrade
```

If you have upgraded the code for any SQLAlchemy models:
```
flask db migrate -m '<message>'
flask db upgrade
```

You probably won't need to do this. But if you need to recreate `app.db` and migrations folder:
```
flask db init
flask db migrate -m '<message>'
flask db upgrade
```

If you have the wrong migrations version in the database when you want to upgrade it you can change it with:
```
flask db stamp head
flask db upgrade
```



### Test application

There are several make commands for testing the application. Use `make help` to see which. To run all tests and validation use:
```
make test
```



### Run application

Start the app with the following command and go to `localhost:5000` in your browser.
```
flask run
```

To run in debug mode, where the app reloads when you change the code:
```
FLASK_DEBUG=1 flask run
```



Production environment
------------------

Follow the scripts in `scripts/` or [Driftsätta en flask app](https://dbwebb.se/kunskap/driftsatta-en-flask-app).



License
-------------------

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.



Acknowledgement
-------------------

This is a co-effort of several people using freely available documentation and tools from the open source community.

For contributors, see commit history and issues.

Feel free to help building up the repository with more content suited for training and education.
