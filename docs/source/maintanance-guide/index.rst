Maintanance Guide
=====================
Purpose
---------------------

The purpose of this document is to enable the maintainers of this project to develop changes for the solution.


The following should be installed to develop on OS2 Valghalla. It is assumed a Windows laptop is used.

Requirements on developer machine
---------------------
*	Visual studio 2022 or later
*	Node.js 18.13.0 or latest lts
*	Angular CLI 15.0.4 or later
*	PostgreSQL
*	.Net 7 or higher
*	.Net tools
*	RabbitMQ

Source Code
---------------------
Github is used to store the source code for the OS2Valghalla project. It uses the following repository:
<INSERT GITHUB REPO HERE>

Requirements
---------------------

*	NodeJS – download the latest version at https://nodejs.org/en/
*	PostgreSQL – download at https://www.postgresql.org/ (Include Pgadmin)
*	.Net Tools – Information at https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools 
*	Angular CLI - information at https://angular.io/cli 
*	RabbitMQ - download at https://www.rabbitmq.com/download.html 
*	Alternatively build the docker compose on the local dev machine and use RabbitMQ and PostgreSQL from docker. 

Setup development
---------------------

*	Get the solution from Github and clone the code. 
*	Navigate to web project from a terminal and run command “npm install”
*	Change the connection string in the OnConfigure method of the DataContext to the correct connectionstring. Then run "dotnet ef database update --project Valghalla.Database" to create/update the database. 

Migrations
---------------------

This project is using EntityFrameworkCore migrations when changes are applied to the database. More information can be found on https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/?tabs=dotnet-core-cli

Generate migrations
~~~~~~~~~~~~~~~~~~~~~
If you modify or add an entity (or more than one entity) and/or relationships, you then need to generate a migration. In the console you write: “dotnet ef migrations add <your name of the migration>”. Then a migration file will be created in the migration folder. If no changes have been made to the entity classes, no migrations are generated.

Apply migrations
~~~~~~~~~~~~~~~~~~~~~
Change the connection string in the OnConfigure method of the DataContext to the database that you want to update. Then in the console write: “dotnet ef database update –project .\Valghalla.Database”. The console will then build the solution and add the migrations that is not present in the database. 


