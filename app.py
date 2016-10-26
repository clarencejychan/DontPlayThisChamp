from flask import Flask, render_template, request
from 	champion import Champion
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
		
		# Get the summoner name by whatever was in the searchbar
		summInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + searchName + '?api_key=' + riotKey)
		summInfo = json.loads(summInfoJson.text)
		summInfoId = str(summInfo[searchName]['id'])

		#print(summInfoId)

		# Get champion info
		summChampInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + summInfoId + '/ranked?season=SEASON2016&api_key=' + riotKey)
		summChampInfo = json.loads(summChampInfoJson.text)

		# Sort Information
		champInfo = summChampInfo['champions']

		champArray = []

		# Create new champion objects for easier organization of data required.
		for champion in champInfo:
			temp = Champion(champion['id'], champion['stats']['totalDeathsPerSession'], champion['stats']['totalChampionKills'], champion['stats']['totalSessionsPlayed'])
			champArray.append(temp)

		
		sortedChampInfo = []

		#for champObject in sortedChampInfo:
			
		#sort out the champions -> take top 3.

		print(summChampInfo['champions'][0]['stats']['totalSessionsPlayed'])

		return(searchName + '2')

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=3000, debug=True, threaded=True);


