from flask import Flask, render_template, url_for, redirect, request
from iwlist import scan, parse
win = 1


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "GET":
		if win:
			ret = open("C:\\Users\\61301765\\Documents\\shsb-pi\\wifiscan_result.txt").read()
		else :
			ret = scan()
		return render_template('index.html',wifiscan=parse(ret))
	else:
		ssid = request.form['ssid']
		pw = request.form['pw']
		if  not win:
			conf = open('/home/pi/conf.conf','a')
		else :
			conf = open("C:\\Users\\61301765\\Documents\\shsb-captive-portal\\wpa-conf.txt",'a')
		print(ssid,pw)
		conf.write('network={ssid=\"'+ssid+'\"psk=\"'+pw+'\"}')
		conf.close()
		return render_template('saved.html')
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=80)
