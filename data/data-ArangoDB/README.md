# Proyecto de Sistemas -Tarea 02-

El siguiente proyecto tiene como finalidad de poder estudiar y descubrir,
esto realizandolo de forma autodidacta, cómo implementar diferentes
tecnologías de almacenamiento de datos. Para este caso en particular, 
primeramente se habla de ArangoDB, y cómo este nos ayuda a realizar
confecciones bases de datos de mutiple opciones. Sin embargo, para este
punto nos centraremos en la base de datos orientada a **grafos**.

## Primeros pasos en ArangoDB

> Como práctica se estará utilizando una base de datos realizada con la 
> inteligencia artificial de ChatGPT.

### Creando collecciones:

> Primeramente estaremos trabajando con la creación de collecciones, las
> cuales pueden ser creadas con código o manula, para este caso serán 
> llevadas a cabo con código.

> .[!IMPORTANT]

Las consultas deben de ser una por una, no se pueden realizar con 
exepciones  de ';', dado que este no comprende esa parte.

Para llevar acabo las consultas se deben de realizar de tipo:

+ CREATE COLLECTION users

+ CREATE COLLECTION posts

+ CREATE EDGE COLLECTION friendships

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

Los cual va a ir generando la integración de cada uno en un ciclo. Terminada
con esta parte, se continua con la agregración posts, pero hay que eliminar
el **query** pasado,

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
    INSERT post_ INTO post

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
dentro de las colleciones,

```sql
// Lo que realiza esta acción es extraer todas la informació
FOR usuario IN users
    RETURN usuario

```