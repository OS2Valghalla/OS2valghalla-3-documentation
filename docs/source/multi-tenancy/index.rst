Multi tenancy
=================

OS2 Valghalla is built to handle all request from all different tenancies in one single instance of the application. 
The first thing that is being done every time the API is handling a request is that it goes through the TenantContextHandlingMiddleware. 
The purpose of that middleware is to determine where the request is coming from. 
Based on the address that the request is coming from the middleware then goes to the secrets find a JSON string containing all the tenant basic addresses and connection strings to the database. 
With that information contained the application then creates a new instance of the correct database context to query the correct database. 

Each municipality is having its own database on the database server, all the data for the municipality should be stored in their own database with the exception for the queue. 
