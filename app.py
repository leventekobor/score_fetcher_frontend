#do magic
from src.external.backend_adapter import receive_match_data
from src.external.logger import log

log("application start")
try:
    receive_match_data()
except Exception as e:
    log(str(e), "ERROR")
