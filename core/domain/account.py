from luhncheck import is_luhn

class Account:
    def __init__(self, number_card: str, limit: int):
        self.number_card: str = number_card
        self.limit: int = limit
        self.balance: int = 0
        self.errors = []

        self.validate()

    def increment_balance(self, amount: int):
        '''
        This increments the balance
        '''
        if len(self.errors) == 0:
            updated_balance = self.balance + amount

            if updated_balance < self.limit:
                self.balance = updated_balance

    def decrement_balance(self, amount: int):
        '''
        This decrements the balance
        '''
        if len(self.errors) == 0:
            self.balance = self.balance - amount

    def validate(self):
        '''
        This validate the account
        '''
        if not is_luhn(self.number_card):
            self.errors.append('The number card is invalid')
