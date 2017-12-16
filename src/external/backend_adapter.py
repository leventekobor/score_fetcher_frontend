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
import sys
from setting import *
from src.external.logger import log
from src.external.local_adapter import handle_single_match, finalize_fetch


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
    match_ids = get_match_ids()
    all_match = str(len(match_ids))
    fetched_counter = 0
    log("all avaible match: " + all_match)
    for match_id in match_ids:
        log("fetch match data  " + str(match_id) + " " + str(fetched_counter) + "/" + all_match)
        try:
            resp = requests.get(BASE_URL + "/" + str(match_id))
            final_data.append(filter_manage_data(resp))
            handle_single_match(filter_manage_data(resp))
            fetched_counter += 1
        except KeyboardInterrupt:
            sys.exit(2)    
        except:
            log("fetch failed, id: " + str(match_id) , "WARN")
            match_ids.append(match_id)    
    finalize_fetch(final_data)


def filter_manage_data(resp):
    match_data = {}
    match_data["away"] = resp.json()["away_last_matches"][0:9:]
    match_data["home"] = resp.json()["home_last_matches"][0:9:]
    match_data["mutual"] = resp.json()["mutual_last_matches"][0:9:]
    return match_data
