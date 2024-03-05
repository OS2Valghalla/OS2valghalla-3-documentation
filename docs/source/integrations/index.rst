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
To be able to send Digital Post in Valghalla a few things has to be in place before Valghalla is allowed to send Digital Post on behalf of municipalities and recieve receipts from the "Beskedfordeler".

* **Serviceagreements**
  For every municipality there need to be created a Serviceagreement that include the following services:
    * KombiPostAfsend
      This service allowing Valghalla to send Digital Post on behalf of the municipality. When adding the service to the serviceagreement additional Data delimitation needs to be specified:

      - Dataafgrænsning: This needs to be "dummy".

      Documentation for this service kan be found here: `Digital Post integration service <https://digitaliseringskataloget.dk/integration/sf1601>`_ .
    
    * **BeskedModtag**
      This service allowing Valghalla to get receipts from the "Beskedfordeler". The receipts is created when a digital post is send out. In the receipt we can see a status of the digital post message that was send out.
      When adding the service to the serviceagreement additional Data delimitation needs to be specified:

      - Afsendende myndighed: This is the CVR number af the municipality.
      - Beskedtype: This needs to be "PKO_PostStatus" ID: d2bed63c-4853-4008-b6e0-a74c15b15fbf
      - Foelsomhed: This needs to be "Ikke fortrolige data" ID: 1d81c472-0808-44cc-963d-f5ef0170ae1d
      - Kommunalt forvaltningsomraade: This needs to be: "*".

      Documentation for this service kan be found here: `Getting receipts from beskedfordeler  <https://docs.kombit.dk/integration/sf1461>`_ .

* **Anvendersystem**
    The IT system craeted and useed in "Fælleskommunalt Administrationsmodul" needs to have specified an "Anvendersystem". In the Anvendersystem two things needs to be configured:
    * systemcertificate
      To use the anvendersystem a systemcertificate (PEM information) has to be uplaoded to the Anvendersystem.

    * Callback Endpoint
      The Beskedfordeler needs an endpoint URL to call for delevering receipts with status of messages sendt by Digital Post. The Callback endpoint configuration also need to have upladed an SSL certificate that the endpoint uses. 


**Certificates**
To be able to send Digital post the server running the application need to trust the following certificates:

 - ADG_PROD_Adgangsstyring_1
 - The system certificate that is uploaded to the "Anvenedersystem" for the IT system.

It is nesseray that the server trust the hole cerfificate chain. Kombit have ZIP packages with certificates for their test and production environments that can be downloaded here: https://digitaliseringskataloget.dk/teknik/certifikater.  


**Beskedfordeler**
The Beskedfordeler is a system that kan recieve receipts when digital post messages is send out. The receiptions holds status information regarding the messages that is send out. There are two ways to get the receiptions from the Beskedfordeler. 
 - Get the receiptions from the Beskedfordeler by pull request.
 - Get the receiptions where the Beskedfordeler sends receiptions to an endpoint that can recieve theese receiptions.

Valghalla is using the last option where the Beskedfordeler send the receiptions to an endpoint. The Beskedfordeler need to be configured with an SSL certificate and need to know what endpoint to send to. This is descriped under "Anvendersystem" in this dokumentation.

For the Beskedfordeler to be able to sendt receiptions to the endpoint some configuration needs to be done before sending receiptions is possible.
There is an environment for test and one for production. The configuration will be the same for both environments. Here are the links for the environments:

- Beskedfordeler Test: https://beskedfordeler-ui.eksterntest-stoettesystemerne.dk/ui/sts-bf-ui/#/beskedkatalog
- Beskedfordeler Production: https://beskedfordeler-ui.stoettesystemerne.dk/ui/sts-bf-ui/#/beskedkatalog

The documentation for setting up the Beskedfordeler to hold receiptions and send them the an endpoint can be found here: `Beskedfordeler documentation <https://docs.kombit.dk/integration/sf1461>`_ . A 'get started guide' can be found here: `Get started guide <https://digitaliseringskataloget.dk/files/integration-files/171020221203/Kom%20godt%20i%20gang%20-%20beskedfordeler.pdf>`_ .
The configuration will include the following:
 - Create subscription and 'Dueslag'
 - Create filter

The filter can filter the messages that will get to the subscription if there is different systems sending post. A filter can look like this where the system sending post is 'DigitalPost':

Beskedkuvert.Filtreringsdata.BeskedAnsvarligAktoer.UUIDIdentifikator = '96514e13-afdd-44d6-95a8-adc2ca19b127'

The server that hosts the endpoint that the beskedfordeler send receiptions to need to trust the following certificates:
- BFO_PROD_Beskedfordeler_1
- the SSL certificate that is attached to the endpoint

It is nesseray that the server trust the hole cerfificate chain. Kombit have ZIP packages with certificates for their test and production environments that can be downloaded here: `Certificates <https://digitaliseringskataloget.dk/teknik/certifikater>`_ . 
