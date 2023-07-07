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

    '''
    counter = 0

    IS_ADD = False
    IS_CHARGE = False
    IS_CREDIT = False
    IS_AMOUNT = False

    IS_KEY = False
    IS_CARD = False

    acc = ''
    amount = ''
    account_key = None
    card_value = None

    max_source = len(source)
    print('max', max_source)
    for c in source:
        counter += 1

        print('counter', counter)
        print('acc', acc)
        print('key', account_key)
        print('card', card_value)
        print('amount', amount)
        print('\n\n\n\n')

        if c == '\n' or c == ' ' or counter == max_source:
            # Check the transaction type
            if len(acc) > 0:
                if acc == 'Add':
                    IS_ADD = True
                    acc = ''
                    IS_KEY = False
                    IS_CARD = False
                    IS_AMOUNT = False
                    continue
                elif acc == 'Charge':
                    IS_CHARGE = True
                    acc = ''
                    IS_KEY = False
                    IS_AMOUNT = False
                    continue
                elif acc == 'Credit':
                    IS_CREDIT = True
                    acc = ''
                    IS_KEY = False
                    IS_AMOUNT = False
                    continue
                elif IS_ADD or IS_CHARGE or IS_CREDIT:
                    if not IS_KEY:
                        account_key = acc
                        acc = ''
                        IS_KEY = True
                    elif not IS_CARD:
                        card_value = acc
                        acc = ''
                        IS_CARD = True
                    elif not IS_AMOUNT:
                        amount = acc
                        acc = ''
                        IS_AMOUNT = True

            if c == '\n':
                if IS_ADD and IS_CARD and IS_AMOUNT:
                    accounts[account_key] = create_new_account(card_value, amount)

                    account_key = ''
                    card_value = ''
                    amount = ''

                    IS_ADD = False
                    IS_CARD = False
                    IS_AMOUNT = False

                elif IS_CHARGE and IS_AMOUNT:
                    parsed_amount = parse_number(amount)

                    if account_key in accounts:
                        if len(accounts[account_key].errors) == 0:
                            new_balance = accounts[account_key].balance + parsed_amount
                            if new_balance < accounts[account_key].limit:
                                accounts[account_key].balance = new_balance

                    account_key = ''
                    amount = ''

                    IS_KEY = False
                    IS_CHARGE = False
                    IS_AMOUNT = False

                elif IS_CREDIT and IS_AMOUNT:
                    parsed_amount = parse_number(amount)

                    if account_key in accounts:
                        if len(accounts[account_key].errors) == 0:
                            accounts[account_key].balance = new_balance - parsed_amount

                    account_key = ''
                    amount = ''
                    IS_KEY = False
                    IS_CREDIT = False
                    IS_AMOUNT = False

            acc = ''
            continue

        acc = acc + c

    for c in source:
        counter += 1

        if c == '\n':
            if not IS_ADD or not IS_CHARGE or not IS_CREDIT:
                pass

            print(current)

            if current is not None :
                if IS_ADD:print('amount', amount)
                    # accounts[current[0]] = Account(current[1], current[3])
                    pass
                elif IS_CHARGE:
                    # accounts[current[0]] = Account(current[1], current[3])
                    pass

            # Clean
            acc = ''
            IS_ADD = False
            IS_CHARGE = False
            IS_CREDIT = False

            continue
        elif  counter == source_total:
            print('endfile')
            continue

        if c == ' ' or c == '\n':
            if len(acc) > 0:
                if acc == 'Add':
                    IS_ADD = True
                    acc = ''
                    current = []
                    continue
                elif acc == 'Charge':
                    IS_CHARGE = True
                    acc = ''
                    current = []
                    continue
                elif acc == 'Credit':
                    IS_CREDIT = True
                    acc = ''
                    current = []
                    continue

                if IS_ADD or IS_CHARGE or IS_CREDIT:
                    current.append(acc)
                    acc = ''

            continue

        acc = acc + c
    '''
    '''
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
    '''

    return accounts

