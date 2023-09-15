Docker container
=============

OS2 Valghalla is being packed as one docker container containing seven images. 
Four of these are specific developed as the system OS2 Valghalla and the rest is prepared images for PostgreSQL, RabbitMQ and Nginx. 

In the solution each project has its own Docker-file that creates the image and then in the solution there is also a Docker compose file that creates the container based on all the images that are being used.
The container contains one network that all images are using, this is for them all to be able to communicate with each other. 
For the file storage PostgreSQL and RabbitMQ have a local storage for its files. 
This is so that the data is not being overwritten on a new deploy. 
The rest of the application also have their own file storage that should not be overwritten on deploy. 
The files stored here is the logging and the secrets. 

Nginx is used as a reverse proxy inside of the container. 
All the network traffic is going through this and the based on the incoming address sent to the correct image. 
For changing addresses based on the production environment nginx have a configuration file that sets the incoming addresses and where to route them to. 
