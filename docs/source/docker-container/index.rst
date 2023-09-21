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

When going to production postgresql should be set to not allow empty password, instead it should be set to demand admin account.

Volumes
------------

As mentioned earlier the docker container have a few volumes included to keep data when new deploys are made. 
These volumes are the following:

* postgresql_data
* rabbitmq_data
* message_logging
* worker_logging
* internal_logging
* external_logging
* certs
* environment
* nginx

The volumes ending with _data is keeping data for the applications so that no data will be lost on new deployments.
The volumes ending with _logging is keeping logfiles so that no logfiles will go missing.
Cert volumes is a folder to store and share certificates between the images, these certificates can be used for the CPR service and the digital post. 
Environment is holding the secrets.json to share the same file between images.
Nginx volume is holding the configuration for nginx as the reverse proxy. 

