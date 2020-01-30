from sqlalchemy import Column, Integer, Table, CHAR, DATETIME, DateTime
from sqlalchemy.dialects.mysql import VARCHAR

from wafos_database.database import Base


class ShopInfo(Base):
    __tablename__ = 'ShopInfo'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    IPAddress = Column('IPAddress', VARCHAR(20))
    ShopName = Column('ShopName', VARCHAR(50))
    OwnerName = Column('OwnerName', VARCHAR(20))
    PostCode = Column('PostCode', VARCHAR(10))
    Address = Column('Address', VARCHAR(50))
    BusinessNumber = Column('BusinessNumber', VARCHAR(20))
    Phone = Column('Phone', VARCHAR(20))
    MobilePhone = Column('MobilePhone', VARCHAR(20))
    UseYN = Column('UseYN', CHAR(1))
    Maintenance = Column('Maintenance', VARCHAR(50))
    ShopCode = Column('ShopCode', VARCHAR(50))
    Memo = Column('Memo', VARCHAR(50))
    Password = Column('Password', VARCHAR(50))

class ShopMenu(Base):
    __tablename__ = 'ShopMenu'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    menu_wash = Column('Menu1', CHAR(1))
    menu_dry = Column('Menu2', CHAR(1))
    menu_shoes_wash = Column('Menu3', CHAR(1))
    menu_shoes_dry = Column('Menu4', CHAR(1))
    menu_item = Column('Menu5', CHAR(1))
    menu_point = Column('Menu6', CHAR(1))
    menu_air = Column('Menu7', CHAR(1))

class PointRule(Base):
    __tablename__ = 'PointRule'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    NormalWeekNew = Column('NormalWeekNew', Integer)
    NormalWeekWash = Column('NormalWeekWash', Integer)
    NormalWeekDry = Column('NormalWeekDry', Integer)
    NormalWeekShoeWash = Column('NormalWeekShoeWash', Integer)
    NormalWeekShoeDry = Column('NormalWeekShoeDry', Integer)
    NormalWeekendNew = Column('NormalWeekendNew', Integer)
    NormalWeekendWash = Column('NormalWeekendWash', Integer)
    NormalWeekendDry = Column('NormalWeekendDry', Integer)
    NormalWeekendShoeWash = Column('NormalWeekendShoeWash', Integer)
    NormalWeekendShoeDry = Column('NormalWeekendShoeDry', Integer)
    EventWeekNew = Column('EventWeekNew', Integer)
    EventWeekWash = Column('EventWeekWash', Integer)
    EventWeekDry = Column('EventWeekDry', Integer)
    EventWeekShoeWash = Column('EventWeekShoeWash', Integer)
    EventWeekShoeDry = Column('EventWeekShoeDry', Integer)
    EventWeekendNew = Column('EventWeekendNew', Integer)
    EventWeekendWash = Column('EventWeekendWash', Integer)
    EventWeekendDry = Column('EventWeekendDry', Integer)
    EventWeekendShoeWash = Column('EventWeekendShoeWash', Integer)
    EventWeekendShoeDry = Column('EventWeekendShoeDry', Integer)
    EventDateFrom = Column('EventDateFrom', VARCHAR(20))
    EventDateTo = Column('EventDateTo', VARCHAR(20))

class CustomerInfo(Base):
    __tablename__ = 'CustomerInfo'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    tel = Column('CustomerID', CHAR(13))
    reg_dttm = Column('OpenDate', DateTime)
    last_use_dttm = Column('LastLoginDate', DateTime)
    pwd = Column('CustomerPassword', VARCHAR(20))
    money = Column('CashBal', Integer)
    point = Column('PointBal', Integer)
    use_count = Column('UseCount', Integer)
    memo = Column('Memo', VARCHAR(40))


class CashPointTran(Base):
    __tablename__ = 'CashPointTran'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    tel = Column('CustomerID', CHAR(13))
    tran_dttm = Column('TranDateTime', DateTime)
    tran_type = Column('TranType', CHAR(6))
    cash_in = Column('CashIn', Integer)
    cash_out = Column('CashOut', Integer)
    cash_bal = Column('CashBalance', Integer)
    point_in = Column('PointIn', Integer)
    point_out = Column('PointOut', Integer)
    point_bal = Column('PointBalance', Integer)


class Machine(Base):
    __tablename__ = 'Machine'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    machine_id = Column('MachineID', Integer)
    controller_id = Column('ControllerID', Integer)
    MachineKind = Column('MachineKind', CHAR(6))
    status = Column('Status', CHAR(6))
    kg = Column('Capacity', VARCHAR(20))
    current_coin = Column('BasicFare', Integer)
    min_coin = Column('MinFare', Integer)
    max_coin = Column('MaxFare', Integer)
    min_etc_coin = Column('FareMinute', Integer)



class WashCourse(Base):
    __tablename__ = 'WashCourse'
    id = Column('SeqNo', Integer, primary_key=True)
    ShopID = Column('ShopID', Integer)
    machine_id = Column('MachineID', Integer)
    MachineType = Column('MachineType', CHAR(6))
    CourseName1 = Column('CourseName1', VARCHAR(50))
    Description1 = Column('Description1', VARCHAR(50))
    Fare1 = Column('Fare1', Integer)
    UseYN1 = Column('UseYN1', CHAR(1))
    CourseName2 = Column('CourseName2', VARCHAR(50))
    Description2 = Column('Description2', VARCHAR(50))
    Fare2 = Column('Fare2', Integer)
    UseYN2 = Column('UseYN2', CHAR(1))
    CourseName3 = Column('CourseName3', VARCHAR(50))
    Description3 = Column('Description3', VARCHAR(50))
    Fare3 = Column('Fare3', Integer)
    UseYN3 = Column('UseYN3', CHAR(1))
    CourseName4 = Column('CourseName4', VARCHAR(50))
    Description4 = Column('Description4', VARCHAR(50))
    Fare4 = Column('Fare4', Integer)
    UseYN4 = Column('UseYN4', CHAR(1))
    CourseName5 = Column('CourseName5', VARCHAR(50))
    Description5 = Column('Description5', VARCHAR(50))
    Fare5 = Column('Fare5', Integer)
    UseYN5 = Column('UseYN5', CHAR(1))
    CourseName6 = Column('CourseName6', VARCHAR(50))
    Description6 = Column('Description6', VARCHAR(50))
    Fare6 = Column('Fare6', Integer)
    UseYN6 = Column('UseYN6', CHAR(1))
    CourseName7 = Column('CourseName7', VARCHAR(50))
    Description7 = Column('Description7', VARCHAR(50))
    Fare7 = Column('Fare7', Integer)
    UseYN7 = Column('UseYN7', CHAR(1))
    CourseName8 = Column('CourseName8', VARCHAR(50))
    Description8 = Column('Description8', VARCHAR(50))
    Fare8 = Column('Fare8', Integer)
    UseYN8 = Column('UseYN8', CHAR(1))
