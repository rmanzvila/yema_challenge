# Yema challenge

#### Technologies

  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](http://www.django-rest-framework.org/)
  * [VUE](https://www.google.com/search?client=safari&rls=en&q=vue&ie=UTF-8&oe=UTF-8)
  

## Make Up project

For run the project, complete the next steps to make up, all the commands and compact in a makefile with a list. 
You need to have installed `git`, `docker`, `ssh` and and a use a `terminal`.

Before continue, create a folder with the name `.envs` on root, after that, download the zip with envs vars (which contains 3 folder `dev, prod, test`) and paste inside the recent created folder `.envs`
 
After that, run in the next order to generate a correct enviroment:

#### Basic commands
  * `make create_network` Create a network for process.
  * `make build` build the images for development.
  * `make migrations` run django make migrations command
  * `make migrate` run django migrate command 
  * `make superuser` make a superuser for develoment.
  * `make up` up the server using unicorn and nginx.
 
### Running server
  * After `make up` command, the server is running: http://localhost:8000/admin for access to the admin.
  * The minimum webapp is running on http://localhost:8000/ but is necessary create doctors since admin.  
  
### For other components  
  * `make test` running the command to check the tests.
  * `make coverage` generate a report about coverage in a folder `htmlcov`, where can check index.html file to get a resumen.

