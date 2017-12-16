from src.external.logger import log
# import csv

# f = csv.writer(open("data.csv", "wb+"))

def finalize_fetch(fetched_data):
	log("handle " + str(len(fetched_data)) + " data particle")
	for data in fetched_data:
		print(data.keys())

def handle_single_match(match_data):
	pass