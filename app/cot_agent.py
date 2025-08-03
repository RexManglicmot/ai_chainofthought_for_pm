from app.logger_config import logger

def gen_cot(user_data):
    logger.info(f"Running CoT reasoning for user {user_data.get('user_id')}")
    print("basic test code is working, hurray!")