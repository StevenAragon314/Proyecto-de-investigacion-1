# Vertex
## Estructura inicial
name_server: Estudiantes_Profesionales
user: root
password: 1234

## Nodo Profesionales
Carrera (String)
Trayectoria (String)
Nombre (String)
Apellidos (String)

## Nodo Publicaciones
Titulo (String)
Fecha_publicacion (Date)
DOI (String)
Palabras_clave (String)
Tipo_publicación (String)
Contacto_correo (String)


## Nodo Estudiantes
Area_interes (String)
Universidad (String)
Carrera (String)
Nombre (String)
Apellidos (String)
Edad_cumplida (Inter)

# Edges
## Autor_de
porcentaje_contribucion (Integer)  :: Relacion 1 a N 

## Colabora_profesional
fecha_inicio (Date)
fecha_fin (Date)
tipo_contribucion (String) 
comentarios (String) 
nombre_proyecto (String) :: Relacion N a N

## Colabora_estudiante
fecha_inicio (Date)
fecha_fin (Date)
tipo_contribucion (String) 
comentarios (String) 
nombre_proyecto (String) :: Relacion N a N

## Consulta
tipo_consulta (string)
fecha_consulta (Date)