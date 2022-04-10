# Project description 
This is a simple project for a sample Charging Station Management System (CSMS)

# Quick Start 

To start the project follow the below steps (Linux, Mac):

- ```sudo docker-compose build  ```
- ```sudo docker-compose up -d ```
- ```sudo docker-compose exec web python manage.py migrate ```
- * ***if the migrate process failed try again, sometimes this happens, docker depends on problem***

open project at http://127.0.0.1:8000, the index page is a swagger documentation which can be used interactively to test the charging end-point. The example input from pdf is located in exampe.json file in the project root directory. 
## Run test cases 

There is only one test case for charging view that can be run using the following command:

- ``` sudo docker-compose exec web python manage.py test charging ```

## Docker description

There are three docker services as follow:

- Postgres: Postgresql is used for database
- Pgadmin: Pgadmin for managing postgresql more easily
- Web: The custom docker file that build the image based on requirements for the Django backend

# Technical description
The price calculation section is located under the views.py in the charging app, api sub-directory that is located in apps folder. the view name is ChargeHandlingView. this view takes all the inputs as post parameters. There is a serializer for validation of inputs. Validation can be more comprehensive.

## Design pattern 

Price calculation has different components, enery, time and transaction. So, the composite design pattern is used to make system maintenance more easier. Also the architecture allows adding more component in the future more easily. The price calculation is based on 3 decimal places, but the representation in API result is 2 decimal precision which is truncated.
