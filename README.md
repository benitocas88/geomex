# Normalize in a relational database the sepomex data from csv file

### To run project you will need install:

- Docker version 19.03.11
- docker-compose version 1.26.0



- Put on root project and type:

``
make up
``

- In browser go to:

``http://127.0.01``

- Compile the assets:

``make webpack``

- Run script to populate the database from a csv file:

`make geo`

- Just restore dump:

`make georestore`

Read more in 
``
src/geoscript/README.md
``

Please feel free to edit, pull request, comments, fixes etc. Welcome everything improve
