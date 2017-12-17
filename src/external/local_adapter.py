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
    home_last_matches_egal = get_egal_count(match_data["home"])
    away_last_matches_egal = get_egal_count(match_data["away"])
    mutual_last_matches_egal = get_egal_count(match_data["mutual"])
    print(league, match_name, home_last_matches_egal, LAST_MATCHES_CAP -
          home_last_matches_egal, away_last_matches_egal, LAST_MATCHES_CAP - away_last_matches_egal, mutual_last_matches_egal)


def get_egal_count(data):
    counter = 0
    for i in range(LAST_MATCHES_CAP):
        try:
            counter += 1 if is_egal(data[i]) else 0
        except:
            pass
    return counter


def is_egal(match):
    points = match["score"].split("(")[0].split(" : ")
    return int(points[0]) == int(points[1])
