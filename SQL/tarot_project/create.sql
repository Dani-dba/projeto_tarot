--create database tarot_db
--use tarot_db

/*cria tabela de cartas
-- Tabela principal de cartas
create table cartas_tarot (
id_carta int primary key identity (1,1),
nome_carta varchar (100) not null ,
significado text not null,
arcano varchar(10) check(arcano in ('maior','menor')),
url_imagem varchar (255))
*/

/* cria tabela atributos
-- Tabela de tipos de atributos (ex.: Elemento, Planeta, Arcano)
create table atributos (
id_atributo int primary key identity(1,1),
nome_atributo varchar(50) not null unique -- Ex: "Elemento", "Planeta", "Arcano"
)

*/
/*
-- Tabela que relaciona cartas aos seus atributos
create table cartas_atributos(
id_carta_atributo int primary key identity(1,1),
id_carta int not null,
id_atributo int not null, 
valor varchar(100) not null, -- Ex: "Ar", "Urano", "Metraton"
foreign key (id_carta) references cartas_tarot(id_carta),
foreign key (id_atributo) references atributos(id_atributo)
)
*/

/*
select * from cartas_tarot
*/

