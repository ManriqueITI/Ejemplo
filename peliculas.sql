create database peliculas;
use peliculas;
create table peliculaRen(
id_pelicula int not null auto_increment primary key,
cliente varchar(50) collate latin1_spanish_ci not null,
pelicula varchar(10) collate latin1_spanish_ci not null,
tiempo varchar(50) collate latin1_spanish_ci not null,
total int(10) collate latin1_spanish_ci not null
);