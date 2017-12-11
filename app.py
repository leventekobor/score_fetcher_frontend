#do magic
from src.external import adapter
from src.external.logger import log

log("application start")
try:
    adapter.receive_match_data()
except Exception as e:
	log(str(e), "ERROR")