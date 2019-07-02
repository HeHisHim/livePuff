from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBI
app.config["JSON_AS_ASCII"] = False # 解决jsonify解析中文乱码

db = SQLAlchemy(app)

# 反射, 并获取fund_info表
db.reflect()
all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
fund_info = all_table["fund_info"]

@app.route("/")
def index():
    res = db.session.query(fund_info).limit(3).all()
    datas = {}
    for x in res:
        datas[x.fund_name] = x.fund_full_name
        print("{} -> {}".format(x.fund_name, x.fund_full_name))

    return jsonify(datas)

if __name__ == "__main__":
    app.run(debug = True)