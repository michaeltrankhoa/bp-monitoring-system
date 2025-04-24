# mqtt_firebase_server/logger.py
import logging

def setup_logger():
    logger = logging.getLogger("MQTTFirebase")
    logger.setLevel(logging.DEBUG)
    
    # Log vào console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger

logger = setup_logger()
