import os

import requests
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
api_key = os.getenv("API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def update_db(data, symbol):
    """
    Updates the local DB with the ETF profile data for the symbol

    Args:
        data (dict): The ETF profile data
        symbol (str): The symbol of the ETF

    """
    # Connect to server
    cnx = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute()

def get_data_from_db():
    """
    fetches data from local DB, calls the function to fetch data from API for each symbol and saves the data in the DB
    """

    # Connect to server
    cnx = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT Symbol from `etf-list`")

    # Fetch one result
    row = cur.fetchall()
    for symbol in row:
        get_data_from_api(symbol[0])


def get_data_from_api(symbol="SPY"):
    """
    Fetches ETF profile data for the symbol from the Alpha Vantage API.

    This function constructs a URL using the provided API key to query the Alpha Vantage API
    for the ETF profile data of the symbol It sends a GET request to the API and
    prints the JSON response.

    Note:
        Replace the "demo" API key in the URL with your own key from https://www.alphavantage.co/support/#api-key.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the network request.

    """
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=ETF_PROFILE&symbol={symbol}&apikey={api_key}"
    r = requests.get(url, timeout=2)
    data = r.json()
    print(data)
    update_db(data, symbol)


if __name__ == "__main__":
    get_data_from_db()
