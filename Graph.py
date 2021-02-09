class Graph:
	def __init__(self,timeSeriesLength=100):
		self.nodes=[]
		self.BIG_BANG=0
		self.TIME_SERIES_LENGTH=timeSeriesLength

	def addNode(self,time):
		print("GRAPH: adding node")
		self.nodes.append(Person())
		return len(self.nodes)-1


	def getNode(self,idx):
		return self.nodes[idx]

	def saveToFile(self,fileName="graph.txt"):
		data={}
		data["N"]=len(self.nodes)
		data["nodes"]=[]
		for n in self.nodes:
			data["nodes"].append(n.getParamsDict)
		with open(fileName, 'w') as outfile:
			json.dump(data, outfile)
		print("Finished writing all nodes to {}".format(fileName))

	def loadFromFile(self, fileName="graph.txt"):
		with open(fileName) as json_file:
			data = json.load(json_file)
		N=data["N"]
		for n in range(N):
			p=Person()
			p.setParamsFromDict(data["nodes"][n])
			self.nodes.append(p)

		print("Finished reading {} modes from {}".format(len(self.nodes),fileName))
	