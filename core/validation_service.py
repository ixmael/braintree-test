from luhncheck import is_luhn

from .domain.account import Account

def validate_account(account: Account) -> Account:
    '''
    Validate the account
    '''

    # Only validate the card number
    if not is_luhn(account.number_card):
        account.error = 'The number card is invalid'

    return account
