from rdflib import Graph
import requests
import json

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

lr = "https://raw.githubusercontent.com/OpenSensingCity/DatasetsLiftingRules/master/grenoble/parking/grenoble_parking_static.rqg"
query = requests.get(lr)
query = query.text

headers = {'content-type': 'application/x-www-form-urlencoded'}

params = {"query":query}

url = "127.0.0.1:80/sparql-generate/api/transform"
response = requests.post(url, params=params, headers=headers)
data = json.loads(response.text)
graphdata = data["output"]
print graphdata.encode("utf-8")
