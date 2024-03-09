from dotenv import load_dotenv
import os

load_dotenv()


class DataProject:
    # base_url_select = os.getenv('BASE_URL') if os.environ['STADE'] == "prod" else "https://www.saucedemo.com/v1"
    BASE_URL = os.getenv('BASE_URL')
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
