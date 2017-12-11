#do magic
from src.external import adapter
from src.external.logger import log

log("application start")
adapter.receive_match_data()