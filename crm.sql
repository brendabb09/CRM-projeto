create  database crm_db;

use crm_db;

create table cliente(
id_cliente int auto_increment not null primary key,
nome varchar (90) not null,
telefone decimal (12,4) not null,
email varchar  (100) not null);



create table usuario(
id_usuario int auto_increment not null primary key,
nome varchar (90) not null,
telefone decimal (12,4) not null,
email varchar (100) not null,
senha decimal (12,4) not null);




select* from usuario