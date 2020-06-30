from decimal import Decimal
from time import sleep

from account_model import Account
from common import create_session, print_first, print_second
from runner import runner


def first_flow(print_function):
    session = create_session()

    print_function('Adding account 3...')
    account3 = Account(name='account3', amount=Decimal('33.33'))
    session.add(account3)

    print_function('Flushing changes to the DB...')
    session.flush()

    print_function('Sleeping...')
    sleep(5)
    print_function('Waking up...')

    print_function('We didn\'t commit anything...')


def second_flow(print_function):
    transaction_level = "READ UNCOMMITTED"

    print_function(f"Using '{transaction_level}'. We should not be surprised to see uncommitted data...")

    session = create_session(transaction_level)

    account_3 = session.query(Account).filter(Account.name == 'account3').one_or_none()

    if account_3:
        print_function("Updating the newly created account that is not committed yet...")
        account_3.amount += 50

        print_function('Committing...')
        session.commit()
        print_function('Committed!!')


runner(first_flow, second_flow)
