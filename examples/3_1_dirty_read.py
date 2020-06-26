from decimal import Decimal
from time import sleep

from account_model import Account
from common import create_session
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

    raise Exception("OOOOPPSSS error")


def second_flow(print_function):
    transaction_level = "READ UNCOMMITTED"

    print_function(f"Using '{transaction_level}'. We should not be surprised to see uncommitted data...")

    session = create_session(transaction_level)

    print_function('Adding account # 4...')
    account4 = Account(name='account4', amount=Decimal('44.44'))
    session.add(account4)

    account_count = session.query(Account).count()
    print_function(f"Account count: {account_count}")

    if account_count == 4:
        print_function('Sending email to CEO to say that we got 4 accounts!!!')

    print_function('Committing...')
    session.commit()
    print_function('Committed!!')


runner(first_flow, second_flow)
