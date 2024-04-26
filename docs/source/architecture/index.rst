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
The application is following a module based pattern where each main pages is one module. 

Schema
---------------

The schema is split up in three different views to make it easier to understand the logic. 
All applications in the Valghalla projects is charing the same queue and the internal and the external is sharing each tenants database.

Internal application
~~~~~~~~~~~~~~

The internal application flow looks like this. The internal application is sending out notifications using both email, sms and digital post. 
The way the application is doing this is by putting a message to the queue so that worker is handling that. 
Thats why those integrations are not in this schema. 

.. image:: ../images/internal.png

External application
~~~~~~~~~~~~~~

The external application flow looks like this. 
As mentioned earlier the tenant database is the same as for the internal application even though theses view are separated.

.. image:: ../images/external.png

Integrations
~~~~~~~~~~~~~~

The worker and message receiver is handling all the notifications that are being sent out from the system. 
The internal and external application puts messages in the queue and the worker is then doing jobs based on those messages. 

.. image:: ../images/integrations.png

Authentication
------------------
Intially, Valghalla used built-in functionalities from ITfoxtec (https://www.itfoxtec.com/identitysaml2) to integrate with Kombit & MitID providers for authentication. While in development we saw no issue, the production hosting had many issues related cookies due to many factors (many kind of different browsers blocking 3rd party cookies from end users computer, load balancer from production blocking cookies...) so the authentication layer has big refactor to overcome the challenge.

Intial auth implementation
~~~~~~~~~~~~~~

.. image:: ../images/initial_auth.png

The first integration with Kombit & MitID we used cookies lifetime directly from the providers so whenever the cookies expired, the client side code will open hidden iframe with same url from main frame. In best scenario, the iframe would not open login page required user input again so the cookies will automatically refreshed, it then callbacks to main frame to trigger any requests failed due to expired cookies again. If iframe took a long time to respond then it's likely that the page in iframe required user to input credential then main frame would reload the page to force user input credential again.
For most of the time in development and testing, we didn't see any issues but things changed when we launched in production. All the requests in iframe blocked so most of the time, the main frame needed to reload. This was bad user experience.

New auth implementation
~~~~~~~~~~~~~~

With all the issues we had in initial implementation, we looked into where the root cause is and found that if we somehow can refresh the cooikes from backend only without relying on providers then the issue will be solved. We implemented a custom token key binding to out 1st party cookie, this token key created after user has successfult authenticated from providers. We store encrypted tokens to our database and compare them with all the requests come in to our systems to verify if users are authorized or not.

.. image:: ../images/internal_auth.png

For Kombit provider used in internal app, the tokens also keeps changing every 30 minutes to make sure the keys are not the same for a long time for security measure. If users not doing anything for 1 hour then the token expire, they will then need to authenticate again directly from providers.

.. image:: ../images/external_auth.png

For MitId provider used in external app, the tokens last only 1 hour without generating new one. This is due to nature that external app has anonymous mode require no login.

.. image:: ../images/database_auth.png

The token (Id + Code hased to base64) included in cookie that send to browser contains NO PII data. The PII data (Value) is encrypted before writing to database to make sure NO one can read it even database administrator.
The encryption we use is based on Microsoft state of the art data protection. A background job will run every 4 hours to remove expired tokens in database to ensure the size will not grow too big overtime.


3rd party dependencies
-------------------

OS2Valghalla uses the following 3rd party dependencies:

.. table:: 
================= ===================================================================================================  ========================================================================= ============================== ==============
Component         Use                                                                                                  Reference                                                                 License                        Version
================= ===================================================================================================  ========================================================================= ============================== ==============
RabbitMQ          Queue                                                                                                https://www.rabbitmq.com/                                                 Mozilla Public License 2.0     3.12.5
PostgreSQL        Persistent data storage                                                                              https://www.postgresql.org/                                               PostgreSQL License             15
Docker            Virtualization software                                                                              https://www.docker.com/                                                   Apache License 2.0             24.0.6
EF Core           Object Relatrional Mapper to the database                                                            https://learn.microsoft.com/en-us/ef/core/                                MIT                            7.09
MediatR           Mediates communication                                                                               https://github.com/jbogard/MediatR                                        Apache-2.0                     12.0.1
ITfoxtec          SAML 2.0 integration                                                                                 https://www.itfoxtec.com/IdentitySaml2                                    BSD-3-Clause                   4.8.6
Fluent validation Validates commands and queries                                                                       https://fluentvalidation.net/                                             Apache-2.0                     11.0
Automapper        Maps objects                                                                                         https://automapper.org/                                                   MIT                            12.0.1
Serilog           Logging helper                                                                                       https://github.com/serilog/serilog/aspnetcore/                            Apache-2.0                     7.0.0
MailKit           SMTP client                                                                                          http://www.mimekit.net/                                                   MIT                            4.2.0
MassTransit       Abstraction layer to easier code against RabbitMQ.                                                   https://masstransit.io/                                                   Apache-2.0                     8.0.16
Angular           Frontend framework                                                                                   https://angular.io/                                                       MIT                            15.0.5
Angular Material  Angular design system                                                                                https://material.angular.io/                                              MIT                            15.0.3
SubSink           Handle subscription                                                                                  https://github.com/wardbell/subsink                                       MIT                            1.0.2                                                                                
Transloco         Internationalization                                                                                 https://github.com/ngneat/transloco                                       MIT                            4.2.1
designsystem.dk   Danish design system                                                                                 https://designsystem.dk/                                                  Various                        9.0.0
NetArchTest       Architecture tests                                                                                   https://github.com/BenMorris/NetArchTest                                  MIT                            1.3.2 
HealthChecks      Help library for health HealthChecks                                                                 https://github.com/Xabaril/AspNetCore.Diagnostics.HealthChecks            Apache-2.0                     7.0.2
Dynamic Linq      Helps with LINQ                                                                                      https://dynamic-linq.net/                                                 Apache-2.0                     1.3.2
ngx-editor        Rich text editor                                                                                     https://github.com/sibiraj-s/ngx-editor                                   MIT                            15.3.0                                                                              
ngx-file-drop     File drop component                                                                                  https://github.com/georgipeltekov/ngx-file-drop                           MIT                            15.0.0
mat-timepicker    Time picker                                                                                          https://github.com/tonysamperi/ngx-mat-timepicker                         MIT                            15.1.4                                                                              
skeleton-loader   Skeleton loader                                                                                      https://github.com/willmendesneto/ngx-skeleton-loader                     MIT                            7.0.0
xng-breadcrumb    Breadcrumb component                                                                                 https://github.com/udayvunnam/xng-breadcrumb                              MIT                            9.0.0
exceljs           Xlsx file helper                                                                                     https://github.com/exceljs/exceljs                                        MIT                            4.4.0
================= ===================================================================================================  ========================================================================= ============================== ==============

