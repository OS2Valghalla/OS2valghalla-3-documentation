Integrations
================

CPR Service
-------------

The CPR integrations is sending question towards the Danish CPR system go retrieve information about all the participants in the system. This is to get the latest and correct information about all the participants that are working during the election. 
OS2 Valghalla uses a certificate to authenticate towards the CPR service and that is an agreement that needs to be setup for the application. 


Adgangsstyrning
-------------

Adgangsstyrning was selected as the identity provider for the internal application. 
Each municipality have their own certificate to be able to communicate with the identity provider. 
The certificate is stored is the municipality’s database. 

MitID
--------

MitID was selected as the identity provider for the external authentication. 
Each municipality have their own certificate to be able to communicate towards the MitID. The certificate is stored is the municipality’s database.

Computic (SMS-Gateway)
---------

To be able to send out SMS from Valghalla the application is sending API requests to a system called Computopic which is a Danish SMS provider. 
Settings for this can be changed from the administrative website https://www.SMS-admin.dk. 

Email
-------

As no specific email vendor was selected in the projected this integration has a basic smtp integration implemented. 
The email integration has been built to send a request to a smtp server to send email. The settings for the smtp server can be set in the appsettings.json. 

Digital Post
--------