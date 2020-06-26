# coding: utf-8
from sqlalchemy import Column, DECIMAL
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'account'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(100))
    amount = Column(DECIMAL(6, 2), nullable=False)

    def __str__(self):
        return f"Account: ({self.name}, {self.amount})"
