# Sobre 
Este documento é para colocar as anotações sobre estudo de banco de dados.

#SQLTools:
Como mencionado anteriormente, o SQLTools é uma extensão versátil que também suporta SQLite. Ele oferece uma interface unificada para trabalhar com vários SGBDs, incluindo SQLite, o que pode ser útil se você trabalhar com diferentes tipos de bancos de dados.

#SQLite Viewer:
Essa extensão permite que você visualize seus bancos de dados sqlite diretamente no vscode, facilitando a analise dos dados

#Comandos Básicos SQL
##DDL - Estruturação
Create database
Create Table
Alter Table
Drop Table

##DQL - Consulta 
Select

##DML - Manipulação de Dados
Insert
Update
Delete

Em #src/db/connection.py# 
Adicionamos PRIMARY KEY AUTOINCREMENT para garantir que id seja único.
✔ Adicionamos NOT NULL para evitar campos vazios.
✔ Adicionamos DEFAULT CURRENT_TIMESTAMP em entrada, para registrar automaticamente o horário de entrada.
✔ Adicionamos FOREIGN KEY (aluno_id) REFERENCES aluno(id) para garantir que aluno_id pertence a um aluno existente.

