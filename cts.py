import requests
from configparser import ConfigParser
from datetime import datetime, timedelta
import time
import RPi.GPIO as GPIO
import logging
import _thread
import serial
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class CTSRelay:
    # Initialized variables on object creation of CTMRelay
    #   Set currunt date time for the token verification
    #   Read config file for all the details
    #   Check token expiring time 
    #      Update token bearer and expiry time for the new token
    def __init__(self):
       
        self.now=datetime.now()
        self.config_object = ConfigParser()
        self.config_object.read("config.ini")    
        self.authinfo = self.config_object["MTR"]
        self.tokeninfo = self.config_object["TOKEN"]
        self.emailInfo = self.config_object["EMAIL"]
        
        if not  self.tokeninfo['expires_in'] or not  self.tokeninfo['bearer']:
            self.updateToken() 
        elif  self.tokeninfo['expires_in'] and  self.tokeninfo['bearer']:
            if datetime.strptime(self.tokeninfo['expires_in'], '%Y-%m-%d %H:%M:%S.%f') < self.now:
                self.updateToken()
        
    def readQRCode(self):
        ser = serial.Serial('/dev/ttyACM0', 19200, timeout = 0)
        while True:
            line = ser.readline().decode()
            if len(line) > 0:
                if self.verifyPass(line):
                    self.VerifiedRelay()
                else:
                    self.NotVerifiedRelay()
            time.sleep(0.1)

    # def checkTokenValidity(self):
    #     if self.now.strptime(self.tokeninfo['expires_in'], '%Y-%m-%d %H:%M:%S.%f') < self.now():
    #         print("valid")
    #     else:
    #         print("expired")

    #   Check token expiring time 
    #      Update token bearer and expiry time for the new token to the config file
    def updateToken(self):
        
        url = "https://auth.mattr.global/oauth/token"

        payload = {
        "client_id": self.authinfo['client_id'],
        "client_secret": self.authinfo['client_secret'],
        "audience": "https://vii.mattr.global",
        "grant_type": "client_credentials"
        }

        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                seconds=data['expires_in']-60
                self.tokeninfo['expires_in'] = str(self.now+timedelta(seconds=seconds))
                self.tokeninfo['bearer'] = str(data['access_token'])
                with open('config.ini', 'w') as conf:
                    self.config_object.write(conf)
        except requests.exceptions.HTTPError as e:
            # logging.exception("Error: " + str(e))
            self.logError(str(e))
        
   
 
    def verifyPass(self,data):
        if data:
            url = self.authinfo['url']

            payload = {
              "payload": data.strip()
            }

            
            headers = {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + self.tokeninfo['bearer']
            }
            #print(headers)
            try:
                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    verifyData = response.json()
                    print(verifyData)
                    return verifyData['verified']
                else:
                    return False
            except requests.exceptions.HTTPError as e:
                # logging.exception("Error: " + str(e))
                self.logError(str(e))
                return False

    def NotVerifiedRelay(self):
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(18, GPIO.OUT)
         GPIO.output(18, GPIO.LOW)
         time.sleep(0.25)

         GPIO.output(18, GPIO.HIGH)
         GPIO.cleanup()

    def VerifiedRelay(self):
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(17, GPIO.OUT)
         GPIO.output(17, GPIO.LOW)

         time.sleep(0.25)

         GPIO.output(17, GPIO.HIGH)
         GPIO.cleanup()

    def sendEmail(self,subject,message,filename):
        try:
            
            if self.emailInfo['enableEmail']:
                subject = subject
                html = """\
                <html>
                <body>
                    $(message)
                </body>
                </html>
                """
                html = html.replace("$(message)", message)
                part2 = MIMEText(html, "html")

                sender_email = self.emailInfo['emailAccount']
                password = self.emailInfo['emailPassword']
                receiver_email = self.emailInfo['receiverEmail']

                # Create a multipart message and set headers
                message = MIMEMultipart()

                message.attach(part2)
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                #message["Bcc"] = receiver_email  # Recommended for mass emails  
                if filename:
                    # Open PDF file in binary mode
                    with open(filename, "rb") as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email    
                    encoders.encode_base64(part)

                    # Add header as key/value pair to attachment part
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                    )

                    # Add attachment to message and convert message to string
                    message.attach(part)
                    
                    # Log in to server using secure context and send email
                text = message.as_string()
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(self.emailInfo['smtpHost'], self.emailInfo['smtpPort'], context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
        except Exception as error:
            self.logError(error)

    def logError(self,error):
        f = open('log.txt', 'w')
        f.write('self.now  - %s' % error)
        f.close()            




cts= CTSRelay()
try:
    _thread.start_new_thread( cts.readQRCode(), ("QR-1" ))
except Exception as error:
    print (error)
    #cts.NotVerifiedRelay()
    #cts.logError(error)
while 1:
    pass
