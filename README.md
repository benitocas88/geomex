# Normalize all postal codes from Mexico. States, municipalities and neighborhoods

### To run the project you will need install the next:

- Docker version 19.03.11
- docker-compose version 1.26.0

Ensure the ```.env``` file exists into `src` folder and contains the next line:

``
SQLALCHEMY_DATABASE_URI=mysql+mysqldb://develop:secret@mariadb:3306/geomex
``

After that only execute the next command

``
docker-compose up -d --build
``

Then you could connect into container ``docker exec -it CONTAINERID bash`` and go to path ``src/`` and type:
``flask geo`` 

Read more in 
``
src/geoscript/README.md
``

Please feel free to edit, pull request, comments, fixes etc. Welcome everything improve
