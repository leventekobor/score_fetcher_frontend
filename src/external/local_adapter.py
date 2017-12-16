from src.external.logger import log
# import csv

# f = csv.writer(open("data.csv", "wb+"))

LAST_MATCHES_CAP = 5


def finalize_fetch(fetched_data):
    log("handle " + str(len(fetched_data)) + " data particle")
    for data in fetched_data:
        pass


def handle_single_match(match_data, home, away):
    league = match_data["mutual"][0]["league"]
    match_name = home + " - " + away
    home_last_matches_win = get_egal_count(match_data["home"], home)
    away_last_matches_win = get_egal_count(match_data["away"], away)
    print(league, match_name, home_last_matches_win, away_last_matches_win)


def get_egal_count(data, name):
    counter = 0
    for i in range(LAST_MATCHES_CAP):
        counter += 1 if is_egal(data[i], name) else 0
    return counter


def is_egal(match, name):
    points = match["score"].split("(")[0].split(" : ")
    return int(points[0]) == int(points[1])
