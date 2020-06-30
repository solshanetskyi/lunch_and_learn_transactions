from decimal import Decimal
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from account_model import Account
from common import print_first

connecting_string = f'mysql+mysqldb://root:sekret@127.0.0.1:52000/lunch_and_learn'
engine = create_engine(connecting_string, echo=True, connect_args={'connect_timeout': 10})

Session = sessionmaker(bind=engine, autoflush=True)
session = Session()

account1 = Account(name='account1', amount=Decimal('11.11'))
account2 = Account(name='account2', amount=Decimal('22.22'))

session.add(account1)
session.add(account2)

session.flush()
# session.query(Account).count()

print_first('Sleeping..')
sleep(7)
print_first('Waking up!')

print_first('Committing...')
session.commit()
print_first('Committed')
