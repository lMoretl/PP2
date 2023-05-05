-- Active: 1683003901034@@127.0.0.1@5432@pp2
DROP TABLE contacts;
create table contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR (50),
    surname VARCHAR (50),
    phone_number VARCHAR (50)   
);

create table users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR (50),
    level INT
)