from flask import Flask, render_template, request
import json
import requests



app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html');


@app.route("/searchhandler", methods=['GET', 'POST'])
def search():

	riotKey = 'RGAPI-33ddda68-2769-46cc-8a03-1c8c393551ad'

	if request.method == 'POST':
		searchName = request.get_data().decode("utf-8")
		
		summInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + searchName + '?api_key=' + riotKey)
		summInfo = json.loads(summInfoJson.text)
		summInfoId = summInfo[searchName]['id']
		print(summInfoId)
		summChampInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + summInfoId + '/ranked?season=SEASON2016&api_key=' + riotKey)


		'''
			Next Steps:
				Finish getting information
				sort out the information to top3 champions
				make some sort of js library to get the right picture depending on the champion id
				integrate vue.js to load the correct champions depending on who it is, and to crate the right statistics (maybe just show the champions plus name is
				good enough in some form of a lightbox)
		'''



		return str(summInfoId)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000, debug=True);


