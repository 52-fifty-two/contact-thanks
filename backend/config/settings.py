import os

from dotenv import load_dotenv
load_dotenv()

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_BCC = os.getenv('MAIL_BCC')
