# Clean Architecture

* Clean Architecture es un nombre popularizado por Robert Cecil Martin, conocido como “Uncle Bob”
con la base de estructura el código en capas o “layers” que solo se comunican con sus capas contiguas atravez de una "interface" o interfaz.

* La arquitectura limpia se basa en el mismo principio de diseño de software: La separación de responsabilidades.
Se establece una arquitectura por capas, cada una de ellas con una responsabilidad específica.

## Gracias a esta separación se consiguen sistemas:

* Independientes de librerías de terceros
* Testables
* Independientes de la vista
* Independientes de la tecnología de base de datos
* Independientes de agentes exteriores

## ¿ Que es una capa ?

* Una capa es un conjunto de clases, paquetes o ficheros que tienen unas responsabilidades relacionadas dentro del sistema.
Estas capas están organizadas de forma jerárquica unas encima de otras y las dependencias siempre van hacia abajo.
Es decir, que una capa dependerá solamente de las capas inferiores, pero nunca de las superiores.

## ¿Que es una interfaz ?

* Los adaptadores se van a encargar de transformar la información como se entiende y es representada en los detalles
de implementación o frameworks, drivers a como la entiende el dominio.