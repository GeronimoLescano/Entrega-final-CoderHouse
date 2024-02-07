# Entrega-final-CoderHouse

## Nombre

Link en GitHub: https://github.com/GeronimoLescano/Pre-entrega-n-3.git
Nombre y apellido: Geronímo Lescano
Link de LinkeIn: www.linkedin.com/in/geronimo-lescano-049809196

## Resumen del proyecto
 
 En el presente proyecto se creo una bibloteca virtual, donde los usuarios pueden ingresar y visualizar los siguientes tipos de datos:
 -Registrar nuevos libros con sus respectivos autores y descargarlos.
 -Contiene un Login y un Logout para la usarios administradores para que puedan agregar, editar y eliminar Libros.
 -Los usuarios pueden registrarse en la parte inferior colocando su email para recibir las ultimas novedades de la pagina y antes de footer se encuentran los datos de contacto de la editorial. Ademas cuenta con informacion acerca del emprendimiento.

 ## Metodología de creacion
 
 Se inicio creando un repositorio en GitHub, luego se clono el mismo en el servidor local y se prosiguio a abrirlo a travez de visual studio code.
 
 ### Desarrollo
    
    Una vez realizado esto se continuo con:
        -Instalacion de espacio virtual y su activacion.
        -Creacion de carpeta de proyectos con la instalacion de Django
        -Creacion de archivo de tipo requirements.txt.
        -Creacion de Apps dentro de la carpeta Project y dentro de la misma se creo las aplicaciones "core", "producto".
        -Se creo models(Libro, Suscriptor).
        -Creacion y luego una posterior migracion de Models.
        -Creacion de visualizaciones de tipo form y list (en una primera instancia luego fueron cambiados a formato table) con importaciones de render, redirect, forms y models. Para la clase Libro se realizo un CRUD.
        -Creacion de urls para cada visualizacion.
        -Creacion de templates para cada visaulizacion con un tronco principal "base" y una ramificacion centralizada en "Index" como menu principal, luego los templates siguientes heredan de base.

### Tecnologías utilizadas:
    
    -IntegrityError: Es una excepción en Django que ocurre cuando se produce una violación de integridad en la base de datos al intentar realizar una operación como guardar un objeto o realizar una consulta. Por ejemplo, puede ocurrir cuando se intenta guardar un objeto que viola una restricción única o de clave externa en la base de datos.
    -get_object_or_404: Esta función es una utilidad de Django que se utiliza comúnmente en las vistas para recuperar un objeto de un modelo específico de la base de datos. Si el objeto no existe, devuelve una página de error 404 (página no encontrada). Es útil para simplificar el manejo de solicitudes de objetos que pueden no existir en la base de datos.
    -FileResponse: Es una clase en Django que se utiliza para enviar archivos como respuestas HTTP. Puedes utilizar esta clase para devolver archivos estáticos, archivos generados dinámicamente o archivos subidos por los usuarios como parte de una respuesta HTTP. Se puede utilizar en vistas para enviar archivos al navegador del cliente.
    -LoginRequiredMixin: Es una clase de mixin en Django que se utiliza para restringir el acceso a determinadas vistas a usuarios que hayan iniciado sesión. Si un usuario intenta acceder a una vista que utiliza este mixin y no ha iniciado sesión, se le redirigirá a la página de inicio de sesión. Es útil para proteger las vistas que requieren autenticación.
    -render: Es una función en Django que se utiliza para renderizar plantillas HTML con contexto y devolver la respuesta al cliente. Toma la solicitud HTTP, el nombre de la plantilla y un diccionario de contexto como argumentos y devuelve una respuesta HTTP con la plantilla renderizada. Es comúnmente utilizado en las vistas para generar y devolver páginas HTML dinámicas.
    -reverse_lazy: Es una versión diferida de la función reverse en Django. Se utiliza para resolver URLs inversas de manera diferida, lo que significa que la resolución de la URL no se produce hasta que se solicita explícitamente. Es útil en situaciones donde necesitas referenciar URLs en módulos que se cargan en el momento de la importación.

### Concluciones: 
    
    Fue un trabajo arduo su desarrolo, hubiron muchos errores que incluso llevaron dias en resolver, quedo satisfecho por el camino recorrido y el aprendisaje en cada parte del curso. La idea es continuar mejorando la pagina en un futuro, incluyendo clases de tipo HMLX.


#### Ejecucion de web en servidor:
    
    Nos colocamos en nuestra terminal de Visual Studio Code y procedemos a poner el siguiente codigo "python manage.py runserver". Recordar siempre estar situados dentro de la carpeta Project, ya que contiene nuestro archivo manage.py

## Admin

    Username: geronimo
    password: 1234
