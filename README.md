# CTS-COVID-Pass-Verifier
CTS COVID vaccine pass verifier


**Honeywell Scanner Setup** 
  1. Scann below Barcode code from the Honywell USB scanner to enable Serail usb.
   ![image](https://user-images.githubusercontent.com/45216584/146660975-41be57b9-7d8a-48f4-a86b-e1d41588aafa.png)

**Config file setup**

  config file use for get MTTR api setting and email setting.
  
  [MTR] 

  client_id = Client id from MTTR api's

  client_secret = Client Secret for MTTR api's

  url = Tanent URL after register new tenent under MTTR account
  

  [TOKEN]
  bearer = bearer token used for verify covid pass. Program will get automaticaly bearer token from MTTR
  expires_in = Update automaticaly by program it self

  [EMAIL]
  enableemail = it is used for enable email for prgram for sending logs value (True=active, False=Deactivate)
  emailaccount = Email addreess from send email
  emailpassword = Email passsword for email
  senderemail = email address from send
  receiveremail = receiver email address
  receivername = receiver name
  smtphost = smtp.gmail.com smtp server 
  smtpport = 465 smtp port

