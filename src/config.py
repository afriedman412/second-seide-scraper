import os

SUBREDDITS = [
    s.replace("r/", "")
    for s in """r/Depop
r/DepopUK
r/Flipping
r/poshmark
r/therealreal
r/ThredUp
r/Grailed
r/grailedtalk
r/StockX
r/Etsy
r/Etsysellers""".split('\n')]

NUM_POSTS = 100

sql_string = "mysql://{}:{}@{}/{}".format(
        "o1yiw20hxluaaf9p",
        os.getenv('MYSQL_PW'),
        "phtfaw4p6a970uc0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
        "izeloqfyy070up9b"
    )


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://o1yiw20hxluaaf9p:{}@phtfaw4p6a970uc0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/izeloqfyy070up9b'.format(os.getenv("MYSQL_PW"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)