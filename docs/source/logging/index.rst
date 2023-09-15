Logging
====================

The applications are having different loggings, one is the audit log and the other is the application logs. 

Audit logs
--------------------
OS2 Valghalla have audit logging implemented so that history is being saved on what user have changed some records. 
This information is being stored in the municipality’s own database and can be connected to entities in the system such as persons. 
The audit logging has also been modified from the generic to add logging for each CPR lookup that has been made in the system, this for the purpose of tracking who did a lookup towards the CPR and on who the lookup was made on.

Application logs
-------------------
The application logs are being written to a file on hosting server. For each day the application is writing logs it also creates a new file with the date. 
The applications have some different scenarios implemented, the error scenario and the request scenario.
Every time an error occurs in the application it logs to the file.
Every time a request is being sent the application logs what user made the request, the name of the request and the status of the request. 

Each municipality have their own log file, so when the application has determined where the request has been sent from and what tenant should be used all the logging will be logged to that specific file. 
If an error occur before the system has determined where the request comes from the logging will be to a general log file for the application.

The internal, external and the worker have different log files. 
