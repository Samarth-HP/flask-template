# Flask boilerplate template
## includes boilerplate template for setting up a flask-project with:
- nginx, 
- celery, 
- rabbit mq (broker), 
- postgres-db, 
- logging, 
- logstash

## Folder Structure
```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── logs
│   └── logs.md
├── requirements.txt
├── scripts
│   ├── default.conf ==> (conf file for nginx)
│   └── init.sql     ==> (sql script to create tables and entries on docker build)
├── src
│   └── app.py
├── templates
│   └── template.md
├── static
│   └── static.md
├── tests
│   └── test.md
```

## Glossary:  
- *logs* => This folder stores logs generated by flask app
- *scripts* => use this folder to add pre-build scripts for any container running via docker
- *src* => project source folder
- *static* => use this folder to store static project files
- *templates* => use this folder to store project template files
- *tests* => use this folder to store test files for the project
- *.env* => environment file to store environment variables used in the project
- *.gitignore* => gitignore file to add the files you want to ignore during staging
- *requirements.txt* => use this file to store all the dependencies and libraries used in the project development
- *Dockerfile* => Dockerfile to build the project image
- *docker-compose.yml* => docker-compose file to run container image and other services
- *README.md* => README file for git

## How to use:
- click on **Use Template** to clone this template in your project
- comment the services you are not using from docker-compose file
- then you can directly run docker-compose command:  
```console
docker-compose up -d
```

- by default all the unicorn requests are sent to nginx and you can check these requests being served at *localhost* (by default)  
  `you can update nginx configurations by updating default.conf file`
