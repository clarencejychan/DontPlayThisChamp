class Champion:
	championID = None
	numDeaths = None
	numKills = None
	totalSessions = None

	def __init__(self, championID, numDeaths, numKills, totalSessions):
		self.championID = championID
		self.nuMDeaths = numDeaths
		self.numKills = numKills
		self.totalSessions = totalSessions



	def getAverageKills(self):

