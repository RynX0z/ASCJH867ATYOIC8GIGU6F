from flask import Flask,request
from sistem import Bot
import Bot
import get,post
import json
import os

api = f"https://api.telegram.org/bot{token_bot}/"
update_id = 0

print("BOT ACTIVED")
print("PRESS CTRL + C TO EXIT ")
while True:
	try:
		req = get(f"https://api.telegram.org/bot{token_bot}/getupdates",params={"offset":update_id}).json()
		if len(req['result']) == 0:
			continue
		try:
			update = req["result"][0]
			Bot(update)
			update_id = update['update_id'] + 1
			print("-"*40)
		except KeyError:
			continue
	except KeyboardInterrupt:
		exit()
	except requests.exceptions.ConnectionError:
		continue
	
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
	if request.method == 'POST':
		update = request.get_json()
		Bot(update)
		return "oke - 200"
	else:
		return "INDEX"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=int(os.environ.get('PORT','5000')))
