from util.read_input import read_input
from core.services import calculate_balance_from_text

if __name__ == '__main__':
    # Read the data input
    text_content = read_input()

    # Process the accounts and its transactions
    accounts = calculate_balance_from_text(text_content)

    # Display the accounts detail
    for consumer_name in sorted(accounts):
        account = accounts[consumer_name]

        if len(account.errors) == 0:
            print('{}: {}'.format(consumer_name, account.balance))

        else:
            print('{}: {}'.format(consumer_name, 'Error'))
