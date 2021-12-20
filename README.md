# CTS-COVID-Pass-Verifier
CTS COVID vaccine pass verifier


**Honeywell Scanner Setup** 
  Scan below Barcode code from the Honeywell USB scanner to enable serial usb.
   ![image](https://user-images.githubusercontent.com/45216584/146660975-41be57b9-7d8a-48f4-a86b-e1d41588aafa.png)

**Raspberry pi GPIO PinOut for Relay** 
  ![image](https://user-images.githubusercontent.com/45216584/146830382-7400a04a-d538-48c2-bada-c808d45a6fa4.png)

  Configure two relay board.
    1. Connect 5V power pin(number 2 pin from the image) to VCC on relay board 
    2. Pass Verified - Connect GPIO 17 pin(number 11 pin from the image) to input pin on board
    3. Pass Not Verified - Connect GPIO 18 pin(number 12 pin from the image) to input pin on board
    4. Ground - connect ground pin (number 6 pin from the image) to the relay board ground pin.