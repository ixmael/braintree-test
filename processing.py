from util.read_input import read_input
from core.services import parse_transactions

if __name__ == '__main__':
    # Read the data input
    text_content = read_input()

    # Process the accounts and its transactions
    accounts = parse_transactions(text_content.split('\n'))

    # Display the accounts detail
    for consumer_name in sorted(accounts):
        account = accounts[consumer_name]
        if not account.error:
            print('{}: {}'.format(consumer_name, account.balance))
        else:
            print('{}: {}'.format(consumer_name, 'Error'))
