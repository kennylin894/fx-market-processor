class CurrencyPair:
    def __init__(self,base,quote):
        self.base_currency = base
        self.quote_currency = quote


# Test the class
if __name__ == "__main__":
    # Create a USD/EUR currency pair
    usd_eur = CurrencyPair("USD", "EUR")
    print(f"Base currency: {usd_eur.base_currency}")
    print(f"Quote currency: {usd_eur.quote_currency}")