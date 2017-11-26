# backand adatpter:
# -fetch data (get)
# -create object from fetched data(json->dict)
# create get_matches:
#   call endpoint address
# create get_custom_match(match_id):
#   call endpoint address
# http://192.168.1.9:6969/get

import requests
import json
from setting import *


def get_matches():
    print(BASE_URL)
    response = requests.get(BASE_URL)
    return response.json()

def get_match_ids():
	data = get_matches()
	ids = []
	for i in range (1000):
		ids.append(data["matches"][i]["id"]) 
	
	print(ids)
