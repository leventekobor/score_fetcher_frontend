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
    print("request recived")
    return response.json()


def get_match_ids():
    data = get_matches()
    ids = []
    for match in data["matches"]:
        ids.append(match["id"])
    return ids

def receive_match_data():
    final_data = []
    for ids in get_match_ids():
        print("collecting data from: " + ids)
        resp = requests.get(BASE_URL + "/" + str(ids))
        final_data.append(filter_manage_data(resp))
    print(final_data)


def filter_manage_data(resp):
    match_data = {}
    match_data["away"] = resp.json()["away_last_matches"][0:9:]
    match_data["home"] = resp.json()["home_last_matches"][0:9:]
    match_data["mutual"] = resp.json()["mutual_last_matches"][0:9:]
    return match_data