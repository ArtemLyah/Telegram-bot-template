import logging

FORMAT = "[%(levelname)s] %(name)s | %(asctime)s\nmsg: %(message)s"

logging.basicConfig(
    filename="./utils/logs/logs.out", 
    filemode="w", 
    format=FORMAT, 
    level=logging.DEBUG
)
logger = logging.getLogger("Diarating")