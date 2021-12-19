# CTS-COVID-Pass-Verifier
CTS COVID vaccine pass verifier


**Honeywell Scanner Setup** 
  1. Scan below Barcode code from the Honeywell USB scanner to enable serial usb.
   ![image](https://user-images.githubusercontent.com/45216584/146660975-41be57b9-7d8a-48f4-a86b-e1d41588aafa.png)

**Config file setup**

  config file use for get MATTR api setting and email setting.
  
  [MTR] 

  client_id = Client id from MATTR api's

  client_secret = Client Secret for MATTR api's

  url = Tenet URL after register new tenet under MATTR account

  

  [TOKEN]

  bearer = bearer token used for verify covid pass. Program will get automatically bearer token from MATTR

  expires_in = Update automatically by program it self


  [EMAIL]
  enableemail = it is used for enable email for program for sending logs value (True=active, False=Deactivate)

  emailaccount = Email addreess from send email

  emailpassword = Email password for email

  senderemail = email address from send

  receiveremail = receiver email address

  receivername = receiver name

  smtphost = smtp.gmail.com smtp server

  smtpport = 465 smtp port
  

