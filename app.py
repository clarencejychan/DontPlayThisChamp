from flask import *
from champion import *
import json
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def index():
	if (request.args.get('nouser') == 'error'):
		return ('no-user')
	return render_template('index.html');

#fix routing so that ajax psases it properly
@app.route("/searchhandler", methods=['GET', 'POST'])
def search():

	riotKey = 'RGAPI-33ddda68-2769-46cc-8a03-1c8c393551ad'

	if request.method == 'POST':
		searchName = request.get_data().decode("utf-8")
		
		# Get the summoner name by whatever was in the searchbar
		summInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + searchName + '?api_key=' + riotKey)
		print(summInfoJson)
		# The user does not exist in the Riot DB
		if summInfoJson.status_code == 404:
			nouser = 'error'
			return redirect(url_for('index', nouser=nouser))


		summInfoId = str(summInfoJson.json()[searchName]['id'])

		# Get champion info
		summChampInfoJson = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + summInfoId + '/ranked?season=SEASON2017&api_key=' + riotKey)
		summChampInfo = summChampInfoJson.json()

		if summChampInfoJson == 404:
			nouser = 'error'
			return redirect(url_for('index', nouser=nouser))

		# Sort Information
		champInfo = summChampInfo['champions']

		champArray = []

		# Create new champion objects for easier organization of data required.
		for champion in champInfo:
			if champion['id'] == 0:
				break
			temp = Champion(champion['id'], champion['stats']['totalDeathsPerSession'], champion['stats']['totalChampionKills'], champion['stats']['totalAssists'], champion['stats']['totalSessionsPlayed'])
			champArray.append(temp)

		# sorted by KDA
		sortedChampInfo = sorted(champArray, key=lambda x: x.getKDA())
			
		#sort out the champions -> take top 3 worst KDA.

		top3 = sortedChampInfo[:3]
		finalList = []

		for champion in top3:
			temp = [champion.championName, champion.championImageURL, champion.numDeaths, champion.numKills, champion.totalSessions]
			finalList.append(temp)

		session[searchName] = json.dumps(finalList)
		return redirect(url_for('summoner', searchName=searchName))


# Champion Name, Image, Deaths, Kills, Total Games
@app.route("/summoner/<searchName>")
def summoner(searchName):
	champions = session[searchName]
	print(champions)

	'''
	for champion in champions:
		print(str(champion.getKDA()) + ' ' + champion.championName)
	'''
	return 'ay lmao'


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=3000, debug=True, threaded=True);


