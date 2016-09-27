from flask import Flask, render_template, request
import json
import requests



app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html');

#fix routing so that ajax psases it properly
@app.route("/searchhandler", methods=['GET', 'POST'])
def search():

	riotKey = 'RGAPI-33ddda68-2769-46cc-8a03-1c8c393551ad'

	if request.method == 'POST':
		searchName = request.get_data().decode("utf-8")
		
		summInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + searchName + '?api_key=' + riotKey)
		summInfo = json.loads(summInfoJson.text)
		summInfoId = str(summInfo[searchName]['id'])

		print(summInfoId)
		summChampInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + summInfoId + '/ranked?season=SEASON2016&api_key=' + riotKey)
		summChampInfo = json.loads(summChampInfoJson.text)

		# Sort Information

		champInfo = summChampInfo['champions']

		sortedChampInfo = []

		for champion in champInfo:
			#put this shit into lists and then add em into champ objects

		#sort out the champions -> take top 3.
		



		print(summChampInfo['champions'][0]['stats']['totalSessionsPlayed'])

		return(searchName)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=3000, debug=True, threaded=True);


