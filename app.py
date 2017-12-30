# do magic
from src.external.backend_adapter import receive_match_data
from src.external.logger import log

DEBUG = False

log("application start")

if DEBUG:
    receive_match_data()
else:
    try:
        receive_match_data()
    except Exception as e:
        log(str(e), "ERROR")
