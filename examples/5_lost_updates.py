from decimal import Decimal
from time import sleep

from account_model import Account
from common import create_session, print_first, print_second
from runner import runner


def first_flow(print_function):
    session = create_session()

    print_function("Reading account 1...")
    account = session.query(Account).filter(Account.name == "account1").one()
    print_function("Account 1 was read")

    print_function("Updating account 1...")
    account.amount += Decimal('100')

    print_function('Sleeping...')
    sleep(5)
    print_function('Waking up...')

    print_function("Committing...")
    session.commit()
    print_function("Committed!")


def second_flow(print_function):
    session = create_session()

    print_function("Reading account 1...")
    account = session.query(Account).filter(Account.name == "account1").one()
    print_function("Account 1 was read")

    print_function("Updating account 1...")
    account.amount += Decimal('100')

    print_function("Committing...")
    session.commit()
    print_function("Committed!")


runner(first_flow, second_flow)
