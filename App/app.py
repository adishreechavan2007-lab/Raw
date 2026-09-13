from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<body style="font-family:Arial; text-align:center; padding-top:50px;">
<h1>IoT Home Security - ESP32</h1>
<h2 style="color:{{'red' if status=='ALERT!' else 'green'}}">{{status}}</h2>
<p>PIR Sensor: {{pir}}</p>
<p>Door Sensor: {{door}}</p>
<p>Buzzer: {{buzzer}}</p>
<a href="/"><button>Refresh</button></a>
</body>
"""

@app.route('/')
def home():
    pir = random.choice(["No Motion", "Motion Detected!"])
    door = random.choice(["Door Closed", "Door Opened!"])
    alert = "Detected" in pir or "Opened" in door
    return render_template_string(HTML, pir=pir, door=door, 
                                  status="ALERT!" if alert else "SAFE",
                                  buzzer="ON" if alert else "OFF")

app.run(host='0.0.0.0', port=8080)
