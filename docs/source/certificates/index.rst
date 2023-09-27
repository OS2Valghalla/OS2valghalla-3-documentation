Certificates
=============

Valghalla is using a few different certificates to be able to use all the integratiosn, this section describes those certificates.

Solution certificates
---------------

The solution requires certificates for the following integrations

* FK Access control authentication
* MitID authentication
* CPR, the danish social security register
* Digital Post, the public electionic post system for all citizen in Denmark
* Some integrations can share certificates across municipals and some require unique certificate for each municipal.

Public/Private
~~~~~~~~~~~~~~

Certificates have a private and a public version.

Private is password protected and acts as a validation of identity and encryption. A private certificate can usually be installed and the public version can be exported from it.
File format is ex. pfx or p12.

Public is also for encryption and acts as a key to decrypt information recieved from a source with a correspondent private version.
File format is ex. cer or pem.

Use either windows certificate store or OpenSSL to work with certificates.

Get certificates
~~~~~~~~~~~~~~

The MitID erhverv portal can be used to order new certificates. The guide for the development/pre-prod portal Testportalen (https://www.nemlog-in.dk/vejledningertiltestmiljo) is a good place to start reading information.

Development and test certificates are ordered seperate from production certificates

Unique certificates
~~~~~~~~~~~~~~

The FK Access control and MitID integrations will require a unique certificate for each municipal

Aquire a new certificate with a private key for each integration for each municipal, two certificates in total per. municipal.

See FK Access control and/or MitID for details around registration and configuration.

Shared certificates
~~~~~~~~~~~~~~

CPR and Digital Post can share one certificate and it can be shared across municipals.

Aquire one certificate in total.

See CPR and Digital Post for details around registration and configuration.

CPR
---------

The integration requires a certificate to secure the information requests, the certificate is to be registered in the same portal as FK Access Control.

Before registration
~~~~~~~~~~~~~~

It is a shared certificate so it should only be necessary to obtain a certificate when setting up the first client, how to get a certificate is described here

Obtain the public part of the certificate.

Registration
~~~~~~~~~~~~~~~

Do the following to register the CPR integration binding:

* Login to the registration portal used to register FK Access Control
* Enable Anvender system for the relevant registration in the Stamdata tab.
* Upload/drag the public part of the certificate in the certificate area.
* Save

Service agreement
~~~~~~~~~~~~~~~~

Last step before the CPR integration will work is to request a service agreement in the registration portal.

* In the Type tab
    * Navigate to Serviceaftale
    * Click Anmod om serviceaftale
    * Set Serviceaftaletype to Uden videregivelse af data
    * Give it a Name
    * Choose an expiration date Gyldig til or leave it blank for a service agreement that will be active until further notice.
    * Give a description in Begrundelse
* In the System tab
    * Choose the system(s) from the list
* In the Myndigheder tab
    * Choose the responsible municipal
* In Services tab
    * Choose the service, search for Person stamdata, udvidet (lokal), the system is developed to support V 5.0
* In the Parametre tab
    * Add a role Tilføj rolle and choose the relevant from the list.
* In the Godkend tab
    * Review and read the Acceper vilkår og betingelser link
    * Send request send anmodning and follow-up with the municipal responsible.

FK (Fælles kommunal / Common municipal) access control
--------------------------

Registration steps
~~~~~~~~~~~~~~~~
Use the relevant administration portal

* Test
* Production
If your organization is not enrolled in the public infrastructure, the organization will need to enroll. See paragraph in a the Before registration section

List of relevant steps to perform when registering a new system:

* Create a new system
* Mark it as a Brugervendt system.
* Choose SP in Logisk IT-system
* Add relevant municipals.
* The configuration requires the system connection xml created either by hand or using the GitHub - digst/OIOSAML.Net solution.
* In the Brugervendt system section upload the system connection xml.
    * When configuring the settings please notice that it is necessary to enable and configure Understøtter Context Handler and Understøtter Context Handler NSIS sections.
    * Upload the same system connection xml file in both sections.
* Configure Krævet NIST assurance level which should be set to Niveau 3 - Høj tillid til påstået identitet
* Set Attributprofil to Fælles kommunal profil.
* Set OIOSAML Profil to OIOSAML3
* Set Krævet NSIS assurance level to Betydelig
* Create a user system role called Municipal administrator the only role nessesary for the internal part of the system.

Test and production
~~~~~~~~~~~~~~~~

Follow the guide on how to do test with a municipal and how to transition to production.

System configuration
~~~~~~~~~~~~~~~~

The way the system is built, it is required to do a new system registration for each municipal and do the test procedures in the FK access control registration portal.

Use the Valghalla tools to register the private certificate for the authentication in the internal application. it will be stored in the municipals database.

MitID
-------------

To get started use the guides Oprettelse og administration af tjenester. In this page it is important to choose the correct environment in the left hand side navigation in the Log-In section and OCES3 certifikater section.

Find the SAML for the MitID Platform end and SAML example / template for your system. They can be found after choosing the relevant environment in the left hand side navigation in the Log-In section.

The diagram below is a rough representation of the process and where the different parts of the registration process take place.

NemLog-In

The system to Idp binding (green) requires only the predefined SAML connection file for the MitID platform.

Registration steps
~~~~~~~~~~~~~~~~

To get started use the help section on the right hand side on the Oprettelse og administration af tjenester page or go strait to the help page with a link to the user manual. The user manual has information around the process for testing the MitID authentication process for both the test and production environment. It describes the steps required to get the integration approved.

List of relevant steps to perform when registering a new system:

* Login to registration portal.
* Add a new IT system in the IT systems provider section.
* Fill all relevant information and save/add
* Add an system user administrator
* Find the new system in the IT System section
* Select the new system registration and choose Upload metadata file in the Solve tasks section
* Upload the system connection xml created either by hand or using the GitHub - digst/OIOSAML.Net solution
* Choose Validate in the Solve tasks
* Now its ready for test

Use the Valghalla tools to register the private certificate for the authentication in the external application. it will be stored in the municipals database.