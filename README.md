# Entrega1-Tofalo
- Ejecutar el código en la terminar con runserver e ingresar a http://127.0.0.1:8000/comercio/.
Los modelos creados son productos (productos disponibiles de la empresa), mayoristas (empresas interesadas para que se registren para recibir información) y sorteo (mensualmente se realiza, el usuario debe registrarse para acceder a la base de datos)

Incio - http://127.0.0.1:8000/comercio/inicio/:
Alli se ve el template de inicio heredado de template base. Se ve la totalidad de productos que tenemos en la base de datos cuya información cargada es el nombre, el material y el precio.
Tambien se puede interactuar con los botones de redes sociales.

Producto - http://127.0.0.1:8000/comercio/producto/:
Esta vista se utiliza para cargar productos en nuestra base de datos. Al cargar los valores, pueden observarse directamente en nuestra base de datos. Tambien hereda el formato del template base. 

Mayoristas - http://127.0.0.1:8000/comercio/mayoristas/
Esta vista sirve para que los interesados en recibir la información sobre precios mayoristas se anoten en el formulario. Los datos se encuentran en la base de datos (nombre, empresa y correo). Tambien hereda el formato del template base.

Sorteo - http://127.0.0.1:8000/comercio/sorteo/
Esta vista refleja las novedades mensuales. Los clientes que quieren participar se pueden registrar ingresando nombre, mail y localidad (se registra en la base de datos). Tambien hereda el formato del template base.

En la base de datos db.sqlite se encontraran los valores cargados para cada modelo, en los que pueden cargarse nuevos valores tal como se menciono previamente.
