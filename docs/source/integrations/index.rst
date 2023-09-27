Integrations
================

CPR Service
-------------

The CPR integration will fetch information about participants in the social security register, to ensure it is as easy as possible to participate and that the administrators always has correct and up to date information.

The information is requested when a participant is created in the system.

Information
The administrators of the system require different types of information from the CPR integration, like:

* Validation information
    * Age
    * Citizenship
* Communication information
    * Digital post status
* Personal information
    * Address
    * Name

The list is not complete but just an example of the kind of information requested.
The integration is described here https://digitaliseringskataloget.dk/integration/sf1520

FK (Fælles kommunal / Common municipal) access control
-------------

The FK access control is used for the internal part of the solution, it is used by all municipals and facilitate SSO (Single Sign-On) between systems and ensure that municipal users can use their PC login to authentication to work with systems.

This is also called a context handler and a lot of the information available references the FK access control as the context handler.

Some registration, configuration and communication is needed.

Almost all the documentation regarding FK access control and MitID is in Danish.
Adgangsstyrning was selected as the identity provider for the internal application. 
Each municipality have their own certificate to be able to communicate with the identity provider. 
The certificate is stored is the municipality’s database. 

MitID
--------

The MitID authentication setup is used for the external part of the solution, it is used by all citizens who will act as volenteers in the system.

This is also called NemLog-In and roughly half of the information available references the MitID authentication as the NemLog-In.

Some registration, configuration and communication is needed.

Almost all the documentation regarding FK access control and MitID is in Danish.

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