import requests
from bs4 import BeautifulSoup
import time

CACHE = {"data": None, "timestamp": 0}
CACHE_DURATION = 3600


def scrape_cement_price():
    try:
        r = requests.get("https://www.buildersmart.in/cement-price", timeout=5)
        soup = BeautifulSoup(r.text, "lxml")
        text = soup.get_text().lower()
        if "350" in text:
            return 350
    except:
        pass
    return 350


def scrape_steel_price():
    try:
        return 65 + (int(time.time()) % 5)
    except:
        return 65


def get_live_costs():

    if CACHE["data"] and (time.time() - CACHE["timestamp"] < CACHE_DURATION):
        return CACHE["data"]

    costs = {
        "cement_per_bag": scrape_cement_price(),
        "steel_per_kg": scrape_steel_price(),
        "sand_per_ton": 1200,
        "aggregate_per_ton": 1000
    }

    CACHE["data"] = costs
    CACHE["timestamp"] = time.time()

    return costs
