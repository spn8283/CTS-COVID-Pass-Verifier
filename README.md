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
  enable_email = it is used for enable email for program for sending logs value (True=active, False=Deactivate)

  email_account = Email addreess from send email

  email_password = Email password for email

  sender_email = email address from send

  receiver_email = receiver email address

  receiver_name = receiver name

  smtp_host = smtp.gmail.com smtp server

  smtp_port = 465 smtp port
  

