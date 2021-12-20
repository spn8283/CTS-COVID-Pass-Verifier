# CTS-COVID-Pass-Verifier
CTS COVID vaccine pass verifier


**Honeywell Scanner Setup** 

  Scan below Barcode code from the Honeywell USB scanner to enable serial usb.
  ![image](https://user-images.githubusercontent.com/45216584/146834671-06b2a8e5-fc46-41a0-bc8e-ebea6b5a0fbe.png)


**Raspberry pi GPIO PinOut for Relay** 
  ![image](https://user-images.githubusercontent.com/45216584/146830382-7400a04a-d538-48c2-bada-c808d45a6fa4.png)
  ![image](https://user-images.githubusercontent.com/45216584/146834359-67cb81c0-aedc-4c05-9514-ef401b1c891b.png)
  
  Configure two relay board.

    1. Connect 5V power pin(number 2 pin from the image) to power pin on relay board(VCC).

    2. Pass Verified - Connect GPIO 17 pin(number 11 pin from the image) to input pin on board (IN1).

    3. Pass Not Verified - Connect GPIO 18 pin(number 12 pin from the image) to input pin on board(IN2).

    4. Ground - connect ground pin (number 6 pin from the image) to ground pin the relay board(GND).
