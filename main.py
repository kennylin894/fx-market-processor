print("Starting FX processor...")

from src.models.currency_pair import CurrencyPair
from src.models.price_quote import PriceQuote
from datetime import datetime

print("Imports successful!")

base = input("What is your base Currency? ")
quote = input("What currency are you trying to convert to? ")
bid = input("What is your bid price? ")
ask = input("What is your ask price? ")

print("Got all inputs, creating objects...")

pair = CurrencyPair(base, quote)
exchangeValue = PriceQuote(pair, bid, ask, datetime.now())

print("Objects created successfully!")