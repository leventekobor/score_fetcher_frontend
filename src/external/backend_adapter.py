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
from src.external.logger import log


def get_matches():
    response = requests.get(BASE_URL)
    return response.json()


def get_match_ids():
    log("all match fetch start")
    data = get_matches()
    log("all match fetch end")
    ids = []
    log("parse id's start")
    for match in data["matches"]:
        ids.append(match["id"])
    log("parse id's end")    
    return ids

def receive_match_data():
    final_data = []
    for match_id in get_match_ids():
        log("fetch match data  " + str(match_id))
        resp = requests.get(BASE_URL + "/" + str(match_id))
        final_data.append(filter_manage_data(resp))
    print(final_data)


def filter_manage_data(resp):
    match_data = {}
    match_data["away"] = resp.json()["away_last_matches"][0:9:]
    match_data["home"] = resp.json()["home_last_matches"][0:9:]
    match_data["mutual"] = resp.json()["mutual_last_matches"][0:9:]
    return match_data
