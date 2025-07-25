from .currency_pair import CurrencyPair

class PriceQuote:
    def __init__(self, currency_pair_obj, bid_price, ask_price, time_stamp):
        self.currency_pair = currency_pair_obj
        self.bid_price = bid_price
        self.ask_price = ask_price
        self.time_stamp = time_stamp