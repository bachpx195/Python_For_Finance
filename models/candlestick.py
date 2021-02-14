import pandas as pd
from database.pymysql_conn import DataBase

db = DataBase()
SQL = "SELECT * FROM DailyTradingJournal_development.candlesticks;"


class Candlestick:
    def __init__(self):
        self.sql = SQL

    def to_df(self):
        db.cur.execute(SQL)
        columns = ['datetime', 'open', 'high', 'close', 'low', 'volumn']
        datas = list(db.cur.fetchall())
        data = [(da[8], da[3], da[4], da[5], da[6], da[11])for da in datas]
        df = pd.DataFrame(columns=columns, data=data)
        return df
