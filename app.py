from flask import Flask, render_template, url_for, redirect, request
from iwlist import scan, parse



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "GET":
		return render_template('index.html',wifiscan=parse(scan()))
	else:
		ssid = request.form['ssid']
		pw = request.form['pw']
		conf = open('/home/pi/conf.conf','a')
		print(ssid,pw)
		conf.write('network={ssid=\"'+ssid+'\"psk=\"'+pw+'\"}')
		conf.close()
		return render_template('saved.html')
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=80)
