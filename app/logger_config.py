import logging
import os
from logging.handlers import RotatingFileHandler

# Create a log directory if it does not exist
# Forgot the close with parans
log_dir = os.path.join(os.getcwd(), "storage", "user_logs")

# Forgot the s in makedirs
os.makedirs(log_dir, exist_ok=True)


# Set log file path
log_file = os.path.join(log_dir, "app.log")

# Configure logger
logger = logging.getLogger("customercot")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers
if not logger.handlers:
    handler = RotatingFileHandler(log_file, maxBytes=2_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Complete
