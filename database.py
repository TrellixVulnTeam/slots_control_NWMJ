# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:37:25 2018

@author: Ed
"""

from sqlalchemy import Column,String,create_engine
from sqlalchemy.types import CHAR,Integer,String,Text,Time,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from flask import jsonify
from sqlalchemy import func


Base = declarative_base()

class Region(Base):
    __tablename__ = 'region'    
    region= Column('region',String(10),primary_key=True,nullable=False)
    ver=Column('ver',Integer)
    port = Column('port',String(3))
    remark=Column('remark',Text)

class Account(Base):
    __tablename__='account'
    id= Column('id',String(10),primary_key=True,nullable=False)
    function=Column('function',String(10))

class Arbitry(Base):
    __tablename__='arbitry'
    dest=Column('dest',String(50))
    orig=Column('orig',String(50),primary_key=True,nullable=False)
    a_40=Column('a_40',Integer)
    a_20=Column('a_20',Integer)
    a_hq=Column('a_hq',Integer)
    valid=Column('valid',Date)

class Freight(Base):
    __tablename__='freight'
    terms=Column('terms',Text)
    ver=Column('ver',Integer,primary_key=True,nullable=False)
    region= Column('region',String(10))
    port = Column('port',String(3))
    dest=Column('dest',String(50))
    fak_20=Column('fak_20',Integer)
    fak_40=Column('fak_40',Integer)
    fak_hq=Column('fak_hq',Integer)
    br_20=Column('br_20',Integer)    
    br_40=Column('br_40',Integer)
    br_hq=Column('br_hq',Integer)
    dir_trans=Column('dir_trans',String(1))

class Contact(Base):
    __tablename__='contact_list'
    region= Column('region',String(10),primary_key=True,nullable=False)
    addressee=Column('addressee', String(50))
    email=Column('email',String(50))
    to_or_copy=Column('to_or_copy',String(1))


class Ver(Base):
    __tablename__='ver'
    created=Column('created',Time)
    ver=Column('ver',Integer,primary_key=True,nullable=False)
    published=Column('published',Time)
    creator=Column('creator',String(10))

engine = create_engine('postgresql://postgres:*********@localhost:5432/workflow'
                       ,echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()


