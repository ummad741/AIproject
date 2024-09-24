import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
AI_TOKEN = os.environ.get("AI_TOKEN")