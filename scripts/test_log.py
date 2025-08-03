import sys
import os

# Add root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.logger_config import logger

# Simple command 
logger.info("Logging is working!")