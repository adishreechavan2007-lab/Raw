# IoT Based Home Security System - ESP32

**Hardware:** ESP32 DevKit V1 + PIR Motion Sensor (HC-SR501) + Magnetic Door Sensor + Buzzer

### Features
- Detects motion via PIR
- Detects door open/close via Reed Switch
- Buzzer alert + Mobile notification via Blynk IoT
- Web Dashboard for monitoring

### Wiring
PIR OUT -> GPIO13, Door Sensor -> GPIO14, Buzzer -> GPIO25

### How to Run Demo on GitHub (Shows Output)
1. Go to `Web_Demo_For_GitHub/app.py`
2. Click `Code -> Codespaces -> Create Codespace`
3. Run: `pip install flask` then `python app.py`
4. Open the forwarded port link - You will see LIVE Dashboard

### Real Hardware
Upload `ESP32_Code/home_security_esp32.ino` via Arduino IDE

Made by Adishree Chavan
Tech Stack: C, Python, IoT, Blynk
