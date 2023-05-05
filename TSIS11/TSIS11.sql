-- Active: 1683269682388@@127.0.0.1@5432@pp2_1
DROP TABLE contacts;

create table contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR (50),
    phone VARCHAR (50)
);