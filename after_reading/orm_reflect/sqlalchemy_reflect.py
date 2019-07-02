from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime

HOSTNAME = "*"
PORT = 0
DATABASE = "*"
USERNAME = "*"
PASSWORD = "*"

DBI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username = USERNAME,
    password = PASSWORD,
    host = HOSTNAME,
    port = PORT,
    db = DATABASE
)

engine = create_engine(DBI, echo=False)
Base = automap_base()
Base.prepare(engine, reflect = True)

session = Session(bind = engine)

fund_info = Base.classes.fund_info

def select():
    res = session.query(fund_info).limit(3).all()
    return res

if __name__ == "__main__":
    for x in select():
        print(x.fund_name)