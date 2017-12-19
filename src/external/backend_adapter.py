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


GLOBAL_CAP = 15

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
        if match["score"] == "-:-":
            ids.append((match["id"], match["home_name"], match["away_name"]))
    log("parse id's end")    
    return ids

def receive_match_data():
    final_data = []
    match_ids_with_names = get_match_ids()
    all_match = str(len(match_ids_with_names))
    fetched_counter = 0
    log("all avaible match: " + all_match)
    for index, match_id_with_names in enumerate(match_ids_with_names):
        match_id = match_id_with_names[0]
        home = match_id_with_names[1]
        away = match_id_with_names[2]
        log("fetch match data  " + str(match_id) + " " + str(fetched_counter) + "/" + all_match)
        try:
            resp = requests.get(BASE_URL + "/" + str(match_id))
            final_data.append(filter_manage_data(resp))
            handle_single_match(filter_manage_data(resp), home, away, index)
            fetched_counter += 1
            if fetched_counter == GLOBAL_CAP:
                log("cap reached, fetch end", "TEST")
                break

        except KeyboardInterrupt:
            sys.exit(2)    
        except ValueError:
            log("fetch failed, id: " + str(match_id) , "WARN")
            match_ids_with_names.append(match_id_with_names)    
    finalize_fetch(final_data)


def filter_manage_data(resp):
    match_data = {}
    match_data["away"] = resp.json()["away_last_matches"][0:9:]
    match_data["home"] = resp.json()["home_last_matches"][0:9:]
    match_data["mutual"] = resp.json()["mutual_last_matches"][0:9:]
    return match_data
