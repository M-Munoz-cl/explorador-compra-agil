from dotenv import load_dotenv
import os

load_dotenv()

TICKET = os.getenv("TICKET")

BASE_URL = "https://api2.mercadopublico.cl"

HEADERS = {'ticket': TICKET}