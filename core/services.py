import re

from util.numbers import parse_number
from .validation_service import validate_account

from .domain.account import Account

def parse_transactions(source: str) -> dict[str, Account]:
    '''
    This reads a source text and search the accounts to calculate the balance
    '''
    consumers = dict()

    for row in source:
        if re.search("^Add\s*", row):
            # Add a new user

            values = row.split(' ')

            user_name = values[1]
            number_card = values[2]
            limit = parse_number(values[3])

            account = validate_account(Account(number_card, limit))

            consumers[user_name] = account

        elif re.search("^Charge\s*", row):
            # Increase balance
            values = row.split(' ')

            if consumers[values[1]].error is None:
                increment = parse_number(values[2])

                balance_to_update = consumers[values[1]].balance + increment
                if balance_to_update < consumers[values[1]].limit:
                    consumers[values[1]].balance = balance_to_update

        elif re.search("^Credit\s*", row):
            # Decrease balance
            values = row.split(' ')

            if consumers[values[1]].error is None:
                decrement = parse_number(values[2])
                consumers[values[1]].balance = consumers[values[1]].balance - decrement
    
    return consumers
