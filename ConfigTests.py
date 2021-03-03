import json
import urllib.request
import requests
from collections import defaultdict


def TestTags(api_req, api_target, context, tags):  # TestTags(api_req,api_target,TEMPLATE)

    print("success! the source api taglist is: ")
    print(tags)

    source = urllib.request.urlopen(api_target + context).read()
    data = json.loads(source)
    for i in range(len(tags)):
        print("testing tag " + tags[i] + "...", end="")
        if tags[i] not in data:
            raise ValueError(tags[i] + " is not in the resulting data!")
        print("OK")
    print("all tags from api source match in data from target api. compability OK")


def TestParams(api_req, api_target):
    apisource = urllib.request.urlopen(api_req).read()
    apidata = json.loads(apisource)

    params = apidata['paths']['/']['get']['parameters']  # can use this for more test cases later
    print(params)
    if (params == 'string'):
        print('expected input is string, testing api_target')
        source = urllib.request.urlopen(api_target + context).read()
        data = json.loads(source)
        print(data)

def TestConnection():
    urllist = ["http://127.0.0.1:5000", "http://127.0.0.1:5050", "http://127.0.0.1:8080"]
    for x in urllist:
        try:
            if requests.get(x):
                #print(x + " Works!")
                source = urllib.request.urlopen(x).read()
                try:
                    data = json.loads(source)
                    #print("It is Json")
                except:
                    print("Not Json!")
                    break

        except:
            print("Server " + x + " is down")
            break


def Testall():
	# read file
    #TestConnection()
 with open('api_template.json', 'r') as myfile:
  data=myfile.read()
 obj = json.loads(data)
 TestTags(obj['apis']['2']['from'], obj['apis']['1']['url'], '?city=Oslo', obj['apis']['2']['req_tags'])
    # loop to get all subtags


# example test: take expected tags from interface / in api1 and see if api3 results match
#api1_doc = 'http://api.swaggerhub.com/apis/SoS_Temperature/API3/0.0.1'
#api3_url = 'http://127.0.0.1:8080/'
#SoS_template = file.json


Testall()
#TestTags(api1_doc, api3_url, '?city=Oslo')
#TestTags(api1_doc,api3_url,TEMPLATE)
#TestParams(api1_doc,api3_url)
