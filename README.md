![Visits Badge](https://badges.pufler.dev/visits/saeedhosseini21/AuthService)
[![GitHub license](https://img.shields.io/github/license/saeedhosseini21/AuthService)](https://github.com/saeedhosseini21/AuthService/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/saeedhosseini21/AuthService)](https://github.com/saeedhosseini21/AuthService/stargazers)

# Authentication Micro-service
Simple authentication micro-service using Python Flask, Pytest and a cloud-native methodology

## The Aim of this project
The aim of this project is demonstrating how a cloud-native microservice has been developed using the 12-factor methodology.

## 12-Factor Methodology
The 12-Factor methodology is an influential pattern to designing scalable application architectures.
The twelve-factor methodology can be applied to apps written in any programming language, and which
use any combination of backing services (database, queue, memory cache, etc).
For details about the 12-facor methodology, refer to [12-Factor methodology](https://12factor.net/) .

<img src="images/12-factor.png" alt="drawing" width="520"  height="400" />

&nbsp;


The table below describes some factors of the 12-factor which are implemented in this project:

|Number|Factor|Codebase|Implemented |
|:-:|:--|:--|:-:|
| 1 |Codebase|This application contains only one repository and is tracked int Git.|:white_check_mark:|
| 2 |Dependencies|Required packages are clearly stated in the requirements.txt file.|:white_check_mark:|
| 3 |Config| All the service configs are read from the enviroment variables.|:white_check_mark:|
| 4 |Backing Services|The service is attached to it's database by a URL.|:white_check_mark:|
| 5 |Build, Release, Run|Build, release and run stages of the service are seperate|:white_check_mark:|
| 6 |Processes|The serivce is stateless and stores nothing in the service memory or disk|:white_check_mark:|
| 7 |Port binding|The service is self-contained and bound to a specific http port|:white_check_mark:|
| 8 |Concurrency|The service can be run by multiple workers and scale horizontally|:white_check_mark:|
| 9 |Disposability|The service does not support graceful shutdown|:x:|
|10 |Dev/Prod Parity|The service is deployed in containers so Dev/prod parity is achieved|:white_check_mark:|
|11 |Logs| Logs are written to stdout of the process|:white_check_mark:|
|12 |Admin Processes|Migration scripts are run in such a way|:white_check_mark:|


## Frameworks
Python Flask and Pytest are used for web-service and test-case development respectively.
#### Flask Framework
Flask in a popular, extensible web micro-framework for building web applications with Python.
The example below shows how easy one can create an API by Flask with only a few lines of code.

    from flask import Flask
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
    return 'Hello, World!'

    if __name__ == '__main__':
    app.run()

#### Pytest
[Pytest](https://docs.pytest.org/en/7.1.x/) is a popular Python testing framework which can scale to support complex functional testing for applications and libraries.
By integrating Pytest and another library named [Coverage](https://coverage.readthedocs.io/en/6.3.2/), code coverage of the apllication can be measured.

## Design Pattern
The design pattern which this service is based on is Model-View-Controller (MVC).
MVC is an architectural design pattern which divides an application into three main logical
components:

[<img src="https://www.tutorialsteacher.com/Content/images/mvc/mvc-architecture.png" width="400"  height="400" >](https://www.tutorialsteacher.com)


#### Model
It is the application's dynamic data structure, independent of the user interface. It directly manages the data, logic and rules of the application.

#### View
The View component is used for all the UI logic of the application and defines what the user can see on te UI.

#### Controller
The controller acts as the link between the view and model to process all the business logic and incoming requests, manipulate data and interact with the View.

## How to install:

#### Get started:
First, pull the repository and install required packages in a Virtualenv.

    git pull https://github.com/saeedhosseini21/AuthService.git

    python -m venv venv

    source venv/bin/activate

    pip install -U pip & pip install -r requirements.txt

The service default database is MYSQL. Pull a MySQL docker image from Docker-hub and run it:

    docker pull mysql:8

    docker run --rm -it --name mysql -e MYSQL_ROOT_PASSWORD=my_password -e MYSQL_DATABASE=my_database -p 3306:3306  mysql:8

Set proper password and database name in the docker run command enviroment variables.

Set this enviroment variable based on the password and database name set before:

    export TECHLAND_AUTHZ_DATABASE_URI=mysql+pymysql://root:my_pasword@localhost:3306/test

Migrate the database and then run the service:

    flask db upgrade

    flask run

#### Test the service:
Run this command and you should get a http code of 200.

    curl -H 'Content-Type: application/json' localhost:5000/api/v1/users

## How to use:
The authentication currently supports GET, POST, DELETE, UPDATE methods for user reource and GET, POST for JWT token.

#### User APIs

###### Create a new user:

    curl -H 'Content-Type: application/json' localhost:5000/api/v1/users -d '{"username":"saeed", "password":"123456"}'

###### Retrieve list of all users:

    curl -H 'Content-Type: application/json' localhost:5000/api/v1/users

###### Retrieve a specific user by it's id:

    curl -H 'Content-Type: application/json' localhost:5000/api/v1/user/<user_id>

###### Update a specific user:

    curl -X PATCH -H 'Content-Type: application/json' localhost:5000/api/v1/user/<user_id> -d '{"password":"test", "oldpassword":"123456"}'

###### Delete a specified user:

    curl -X DELETE -H 'Content-Type: application/json' localhost:5000/api/v1/user/<user_id>

#### Token APIs

###### Create a new JWT toke

    curl -v -H 'Content-Type: application/json' localhost:5000/api/v1/auth -d  '{"username":"saeed", "password":"123456"}'

###### Validate a JWT token:

    curl -H 'Content-Type: application/json' -H 'X-Subject-Token:<token-talue>' localhost:5000/api/v1/auth

#### Install using docker
For running the service as a container, First the docker image must be created:

    make build

Run the container:

    docker run --rm -it --name authz -p 8080:8080 -e TECHLAND_AUTHZ_DATABASE_URI=mysql+pymysql://root:123456@<docker-IP>:3306/test authz:latest

Test if the service is running properly:

    curl -H 'Content-Type: application/json' localhost:8080/api/v1/users

## Tests and code-coverage

#### Running unit-tests
To run the unit-tests, first run the service:

    docker run --rm -it --name mysql -e MYSQL_ROOT_PASSWORD=my_password -e MYSQL_DATABASE=my_database -p 3306:3306  mysql:8

    export TECHLAND_AUTHZ_DATABASE_URI=mysql+pymysql://root:my_pasword@localhost:3306/test

    flask db upgrade

    flask run

Run the unit-tests:

    coverage run -m pytest

If no test fails, the test result will be like this:

<img src="images/tests.png" alt="drawing" width="700"  height="400" />

#### Code-coverage

To see the code-coverage of the service, got to /authz/htmlcov and open the index.html file.
As you can see in the image below, the current code-coverage of this service is 80%.

<img src="images/coverage.png" alt="drawing" width="700"  height="400" />

## How to contribute:
You can fork this project and develop new features.

Copyright 2022 Saeed Hosseini saeedhosseini21@gmail.com
