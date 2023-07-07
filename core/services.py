from util.numbers import parse_number
from .domain.account import Account

def calculate_balance_from_text(source: str) -> dict[str, Account]:
    '''
    This reads a source text, parse it and calculates the balance of the accounts
    '''
    # The accounts list to return
    accounts = dict()

    # Parse lines
    for transaction in source.split('\n'):

        # Parse the items line
        elems = transaction.split(' ')

        if elems[0] == 'Add':
            # Check if is ADD action
            limit = parse_number(elems[3])
            accounts[elems[1]] = Account(elems[2], limit)

        elif elems[0] == 'Charge':
            # Check if is CHARGE action
            if elems[1] in accounts:
                parsed_amount = parse_number(elems[2])
                accounts[elems[1]].increment_balance(parsed_amount)

        elif elems[0] == 'Credit':
            # Check if is CREDIT action
            if elems[1] in accounts:
                parsed_amount = parse_number(elems[2])
                accounts[elems[1]].decrement_balance(parsed_amount)

    return accounts
