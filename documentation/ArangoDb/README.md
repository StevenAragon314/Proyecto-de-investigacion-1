# Proyecto de Sistemas -Tarea 02-

Nuestro proyecto tiene como finalidad estudiar y descubrir, de forma autodidacta, cómo implementar 
diferentes tecnologías de almacenamiento de datos. En este archivo nos vamos a enfocar primeramente
en la base de datos multimodelo ArangoDB, y cómo este nos brinda multiples opciones para realizar 
confecciones de bases de datos.En nuestro caso nos centraremos en la base de datos orientada a **grafos**.

## Primeros pasos en ArangoDB

> Como práctica se estará utilizando una base de datos generada por medio de la 
> inteligencia artificial ChatGPT.

### Creando colecciones:

> El primer paso es trabajando con la creación de colecciones, las
> cuales pueden ser creadas con código o manualmuente. En nuestro caso serán 
> llevadas a cabo con código.

> .[!AVISO IMPORTANTE!]

Las consultas deben de ser una por una, no se pueden realizar con seguidas 
por medio del ';'. El codigo no lo registra como una consulta aparte.

Para llevar acabo las creacion de las colecciones con codigo se debe de hacer por medio del command prompt o shell.
```console
  docker exec -it <NOMBRE CONTENEDOR> arangosh
```
Luego el lenguaje de la consola se transofmra a javascript, por lo tanto los comandos restantes se codifican en este lenguaje.
```javascript
db._useDatabase('<NOMBRE BASE DE DATOS>');
```
+ CREATE COLLECTION users
```javascript
db._create('users');
```
+ CREATE COLLECTION posts
```javascript
db._create('posts');
```
+ CREATE EDGE COLLECTION friendships
```javascript
db._createEdgeCollection('friendships');
```
### Alimentando las bases de datos

> Se debe de declarar una variable con todas las inserciones nuevas que se 
plaean realizar, por tanto la declaración de la variable va a tomar una
conoctacción especial:

```sql

LET user = [
  {
    "_key": "user1",
    "nombre": "Ana López",
    "email": "ana.lopez@ejemplo.com",
    "edad": 28,
    "ciudad": "Madrid"
  },
  {
    "_key": "user2",
    "nombre": "Luis García",
    "email": "luis.garcia@ejemplo.com",
    "edad": 34,
    "ciudad": "Barcelona"
  },
  {
    "_key": "user3",
    "nombre": "María Fernández",
    "email": "maria.fernandez@ejemplo.com",
    "edad": 22,
    "ciudad": "Valencia"
  },
  {
    "_key": "user4",
    "nombre": "Carlos Martínez",
    "email": "carlos.martinez@ejemplo.com",
    "edad": 45,
    "ciudad": "Sevilla"
  },
  {
    "_key": "user5",
    "nombre": "Laura Sánchez",
    "email": "laura.sanchez@ejemplo.com",
    "edad": 31,
    "ciudad": "Bilbao"
  }
]

FOR user_ IN user
    INSERT user_ INTO users

```

> Los cuales van a ir generando la integración de cada uno en un ciclo. 
> Finalizada la primer insercion, se continua con la agregración de los "posts",
>  pero hay que borrar el codigo del **query** anterior,

```sql
LET post = [
  {
    "_key": "post1",
    "autor": "user1",
    "contenido": "¡Hola a todos! Estoy empezando a aprender ArangoDB.",
    "fecha": "2024-04-01T10:00:00Z"
  },
  {
    "_key": "post2",
    "autor": "user2",
    "contenido": "¿Alguien tiene recomendaciones de libros de base de datos?",
    "fecha": "2024-04-02T12:30:00Z"
  },
  {
    "_key": "post3",
    "autor": "user3",
    "contenido": "Acabo de asistir a un taller de AQL. ¡Muy interesante!",
    "fecha": "2024-04-03T09:15:00Z"
  },
  {
    "_key": "post4",
    "autor": "user4",
    "contenido": "Planeando un viaje a la montaña este fin de semana.",
    "fecha": "2024-04-04T14:45:00Z"
  },
  {
    "_key": "post5",
    "autor": "user5",
    "contenido": "¿Quién quiere unirse a mi club de lectura?",
    "fecha": "2024-04-05T18:20:00Z"
  }
]

FOR post_ IN post
    INSERT post_ INTO posts

```
Por último, se va ir agregando las relaciones que se tienen, en este caso 
las **frinedships**, para lo cual se declara el siguiente código.

```sql
LET friendship = [
  {
    "_from": "users/user1",
    "_to": "users/user2",
    "fecha": "2023-06-15T08:00:00Z"
  },
  {
    "_from": "users/user1",
    "_to": "users/user3",
    "fecha": "2023-07-20T09:30:00Z"
  },
  {
    "_from": "users/user2",
    "_to": "users/user4",
    "fecha": "2023-08-05T11:45:00Z"
  },
  {
    "_from": "users/user3",
    "_to": "users/user5",
    "fecha": "2023-09-10T14:10:00Z"
  },
  {
    "_from": "users/user4",
    "_to": "users/user5",
    "fecha": "2023-10-12T16:25:00Z"
  }
]

FOR friendship_ IN friendship
    INSERT friendship_ INTO friendships

```

### Creando consultas

Para poder observar cómo funciona las consultas de extraer información
dentro de las colecciones,

```sql
// Lo que realiza esta acción es extraer todas la informació
FOR usuario IN users
    RETURN usuario

```
### Usuarios Especificos

```sql

FOR usuario IN users
  FILTER usuario.nombre == "Ana López"
  RETURN usuario

```

### Buscar Todas las Publicaciones de un Usuario

```sql

FOR post IN posts
  FILTER post.autor == "user1"
  RETURN post

```

### Encontrando todas las amistades un usuario

```sql

FOR friend IN 1..1 OUTBOUND "users/user1" friendships
  RETURN friend

```

### Encontrando Amigos de Amigos

```sql

FOR friend IN 2 OUTBOUND "users/user1" friendships
  FILTER friend._key != "user1" AND !(
    FOR directFriend IN 1 OUTBOUND "users/user1" friendships
      FILTER directFriend._key == friend._key
      RETURN 1
  )
  RETURN friend

```

### Contar el Número de Amigos por Usuario

```sql
FOR usuario IN users
  LET numeroAmigos = LENGTH(
    FOR friend IN 1 OUTBOUND usuario._id friendships
      RETURN 1
  )
  RETURN { nombre: usuario.nombre, numeroAmigos }

```
