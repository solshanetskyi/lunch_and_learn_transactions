from decimal import Decimal
from time import sleep

from account_model import Account
from common import create_session
from runner import runner


def first_flow(print_function):
    session = create_session("SERIALIZABLE")

    print_function("Reading account 1...")
    account = session.query(Account).filter(Account.name == "account1").one()
    print_function("Account 1 was read")

    print_function('Sleeping...')
    sleep(3)
    print_function('Waking up...')

    account.amount += Decimal('100')

    session.commit()


def second_flow(print_function):
    session = create_session("SERIALIZABLE")

    print_function("Reading account 1...")
    account = session.query(Account).filter(Account.name == "account1").one()
    print_function("Account 1 was read")

    print_function('Sleeping...')
    sleep(4)
    print_function('Waking up...')

    account.amount += Decimal('100')

    session.commit()


runner(first_flow, second_flow)
