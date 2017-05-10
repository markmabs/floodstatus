from flask import Flask, render_template, request, jsonify
import Pins

import urllib2
import json


app = Flask(__name__)

def sendNotification(token, channel, message):
	data = {
		"body" : message,
		"message_type" : "text/plain"
	}

	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(token))

	response = urllib2.urlopen(req, json.dumps(data))
	
# return index page when IP address of RPi is typed in the browser
@app.route("/")
def Index():
    return render_template("index.html", uptime=GetUptime())

# ajax GET call this function periodically to read button state
# the state is sent back as json data
@app.route("/_button")
def _button():
    if Pins.ReadButton():
        state = "Passable: Light & Heavy Vehicles"
        sendNotification("3be72d7b24b3a4b6dff00657bc58013488fdfb99", "Flood Monitoring", "Flood Alert = LEVEL1!")
    else:
        state = "----------------------------"
    return jsonify(buttonState=state)

@app.route("/_button1")
def _button1():
    if Pins.ReadButton1():
        state1 = "Not Passable: Light ; Passable: Heavy Vehicles"
        sendNotification("3be72d7b24b3a4b6dff00657bc58013488fdfb99", "Flood Monitoring", "Flood Alert = LEVEL2!")
    else:
        state1 = "---------------------------"
    return jsonify(buttonState1=state1)

@app.route("/_button11")
def _button11():
    if Pins.ReadButton11():
        state11 = "Not Passable: Light & Heavy Vehicles"
        sendNotification("3be72d7b24b3a4b6dff00657bc58013488fdfb99", "Flood Monitoring", "Flood Alert = LEVEL3!")
    else:
        state11 = "----------------------------"
    return jsonify(buttonState11=state11)


def GetUptime():
    # get uptime from the linux terminal command
    from subprocess import check_output
    output = check_output(["uptime"])
    # return only uptime info
    uptime = output[output.find("up"):output.find("user")-5]
    return uptime
    
# run the webserver on standard port 80, requires sudo
if __name__ == "__main__":
    Pins.Init()
    app.run(host='0.0.0.0', port=80, debug=True)
