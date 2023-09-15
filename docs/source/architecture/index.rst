Architecture
=====================
The architecture is built upon the clean architecture but with a specific approach to web applications. 
This means that the project is not using a domain layer to handle all the domain logic. 
This instead is handled in the application layer. 
An overall thought on the application can be viewed in figure 1 below.

.. image:: ../images/architecture.png
*Figure 1 ASP.NET Core Architecture (Microsoft, 2023)*

The application is also using a CQRS pattern (Command and query responsibility segregation) which means that the application has separate endpoints for handling data storage and queries. 
By doing this the application gets a segregation between business logic for example validation and logic needed for the data storage and simple queries which makes object mapping simpler and cleaner. 

Overview of the architecture layers
----------------------
The architectural design consists of three layers which is the API, Application, Infrastructure layer and the Web application. 
The API is responsible for all the startup procedures and the endpoints. 
As the application holds two different applications in the same solution the project is also having some shared projects such as the database project and the integration project. 

API
----------------------
The API is the receiving end of all the communication from the frontend application. 

Middleware’s
~~~~~~~~~~~~~~~~~~~~~
Valghalla is having four different middleware’s that is doing logic in a specific order before the actual application logic is being handled in the application. The four different middleware’s are described here.

*	UserContextHandlingMiddleware. Has the responsibility to set a UserContext based on the claims from the given token. As the claims in the token doesn’t hold information about the user from Valghalla the middleware adds this information to the user context. This context can later be used in the application to know which user is doing all the request. 

*	UserRequestHandlingMiddleware. This middleware is responsible to log all the request that comes to the application and from what user. 

*	TenantContextMiddleware. This middleware is responsible to determine which tenant the requests come from and selects the correct database based on the given address. 

*	GlobalExceptionHandlingMiddleware. This middleware handles all the exceptions in the application and masks all the information that is being returned to the UI. It is also logging the full exception to the correct log file. 

Application
-------------------
This is the business logic layer that should handle all the logic inside of the application. As the system is being module based each module have its own folder containing all the commands and queries in the system. Each command/query is its own file and has its own validation using the library fluent validation. 

Infrastructure
-------------------
This layer handles all the communications towards the database and its main purpose is to deliver the minimal data that is needed for each request. To help with the communication towards the database the application is using entity framework. 

Web
-------------------
Contains the Angular applications which is the frontend application. The application is using lazy loading to only load the specific modules that is needed at the time. The application was generated on version 14 of angular and later upgraded to version 15. The web is later hosted on wwwroot under the API. 
