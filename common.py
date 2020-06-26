from decimal import Decimal

from colorama import Fore, Style
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from account_model import Account

connecting_string = f'mysql+mysqldb://root:sekret@127.0.0.1:52000/lunch_and_learn'
engine = create_engine(connecting_string, echo=False, connect_args={'connect_timeout': 10})


def create_session(isolation_level: str = 'REPEATABLE READ'):
    Session = sessionmaker(bind=engine, autoflush=True)
    session = Session(bind=engine.execution_options(isolation_level=isolation_level))

    return session


def clean_up():
    session = create_session()
    accounts = session.query(Account).all()

    for account in accounts:
        session.delete(account)

    session.commit()


def create_records():
    session = create_session()

    account1 = Account(name='account1', amount=Decimal('11.11'))
    account2 = Account(name='account2', amount=Decimal('22.22'))

    session.add(account1)
    session.add(account2)

    session.commit()


def print_database(print_function, session = None):
    print_function('Database state:')

    if not session:
        session = create_session()

    accounts = session.query(Account).all()

    for account in accounts:
        print_function(account)


def print_first(message: str):
    print(f"{Fore.BLUE}{Style.BRIGHT}Flow 1: {message}{Style.RESET_ALL}")
    print(Style.RESET_ALL, end='')


def print_second(message: str):
    print(f"{Fore.YELLOW}{Style.BRIGHT}Flow 2: {message}")
    print(Style.RESET_ALL, end='')


def print_final(message: str):
    print(f"{Fore.GREEN}Final: {Style.BRIGHT}{message}")
    print(Style.RESET_ALL, end='')


def print_error(message: str):
    print(f"{Fore.RED}{Style.BRIGHT}{message}")
    print(Style.RESET_ALL, end='')
