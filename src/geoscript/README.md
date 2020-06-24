# Migrating from sepomex file in a relational database

The proposal for this project is pass from a simple file downloaded 
from [sepomex](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx) 
service and normalize the data and save into database.

The project contains a file previously downloaded from sepomex in folder path geomex/src/geoscript
but if you prefer re-download the file please do the next:

Download from [sepomex](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx)
and choose the format txt file. You could save the file in any place, but when you uncompress the file 
you should change the name file and format extension by sepomex.csv or if you prefer, feel free to edit
the ```__init__.py``` file into geoscript but is very important mantain the extension format as .csv

Ensure the ```filename.csv``` exists and matching
 
``
path_doc = os.path.join(os.path.abspath('..'), "src", "geoscript", "filename.csv")
``
 
 If everything is ok, so are you ready to start. Let's go! 
