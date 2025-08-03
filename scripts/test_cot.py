import sys
import os

# Add root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app.cot_agent import gen_cot

# Dummy input
user_data = {"user_id": "user_001"}
gen_cot(user_data)

