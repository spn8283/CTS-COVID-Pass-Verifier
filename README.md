# CTS-COVID-Pass-Verifier
CTS COVID vaccine pass verifier


**Honeywell Scanner Setup** 

  Scan below Barcode code from the Honeywell USB scanner to enable serial usb.
    ![image](https://user-images.githubusercontent.com/45216584/146834997-d85f0fb8-1a28-480a-a80d-5e2ddb5e11a1.png)
    image 1
    
**Raspberry pi GPIO PinOut for Relay** 

  ![image](https://user-images.githubusercontent.com/45216584/146830382-7400a04a-d538-48c2-bada-c808d45a6fa4.png
      image 2
  
  ![image](https://user-images.githubusercontent.com/45216584/146835034-e95bb36a-7bc1-44ee-ac49-26add9c0ae9e.png)
    image 3

  Configure two relay board.

    1. Connect 5V power pin(number 2 pin from the image 2) to power pin on relay board(VCC).

    2. Pass Verified - Connect GPIO 17 pin(number 11 pin from the image 2) to input pin on board (IN1).

    3. Pass Not Verified - Connect GPIO 18 pin(number 12 pin from the image 2) to input pin on board(IN2).

    4. Ground - connect ground pin (number 6 pin from the image 2) to ground pin the relay board(GND).
