from decimal import Decimal
from time import sleep

from account_model import Account
from common import create_session, print_database
from runner import runner


def first_flow(print_function):
    transaction_level = "REPEATABLE READ"

    session = create_session(transaction_level)

    print_function(f"Using '{transaction_level}'. When we read the data first time ")
    print_function("we will create a fixed snapshot of the database")

    print_database(print_function, session)

    print_function('Sleeping...')
    sleep(5)
    print_function('Waking up...')

    print_function("The data in the DB has changed. But if we query it again ")
    print_function("we wont see any updates as we will be reading from the transaction snapshot")

    print_database(print_function, session)


def second_flow(print_function):
    session = create_session()

    print_function('Adding new account at the meantime...')
    account3 = Account(name='account3', amount=Decimal('33.33'))
    session.add(account3)

    account1 = session.query(Account).filter(Account.name == 'account1').one_or_none()
    account2 = session.query(Account).filter(Account.name == 'account2').one_or_none()

    if account1:
        print_function('Updating existing account at the meantime...')
        account1.name = 'Updated from second flow'
        session.commit()

    if account2:
        print_function('Deleting existing account at the meantime...')
        session.delete(account2)

    session.commit()
    print_function('Committed!!')


runner(first_flow, second_flow)
