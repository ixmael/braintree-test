class Account:
    def __init__(self, number_card: str, limit: int):
        self.number_card: str = number_card
        self.balance: int = 0
        self.limit: int = limit
        self.error: str = None
