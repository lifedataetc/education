import psycopg2 as pc2
from string import Template
import pandas as pd
from datetime import date, timedelta, datetime

CONNECTION_STRING = "dbname=fred_ts host=localhost user=fred password=180389"

SCHEMA = 'fin_ts'
SERIES = [
    'DGS1MO','DGS3MO','DGS6MO','DGS1','DGS2',
    'DGS3','DGS5','DGS7','DGS10','DGS20','DGS30'
        ]

def execute_and_return(query):
    try:
        # connect to the system
        conn = pc2.connect(CONNECTION_STRING)
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return(data)
    # some basic error handling
    except pc2.Error as err:
        conn.rollback()
        cur.close()
        conn.close()
        return(str(err))
    except Exception as err:
        conn.rollback()
        cur.close()
        conn.close()
        return(str(err))

def get_dates(sdate,edate):
    delta = edate - sdate       # as timedelta

    all_dates = []
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        all_dates.append(day)

    return(all_dates)

def dt_con(in_dt):
    return(datetime.date(datetime.strptime(in_dt,'%Y-%m-%d')))

def dt_con_csv(in_dts):
    out_dts = []
    for in_dt in in_dts.split(','):
        out_dts.append(dt_con(in_dt))

    return(out_dts)

def get_yield_curves():
    yc_data = execute_and_return('SELECT * FROM fin_ts.yield_curve;')
    df = pd.DataFrame(yc_data,columns=['date','1_m', '3_m','6_m','1_y','2_y',
                                       '3_y','5_y','7_y','10_y','20_y','30_y'])

    # setup dates
    sdate = df.date.min()   # start date
    edate = datetime.date(datetime.today())   # end date

    all_dates = get_dates(sdate,edate)

    all_dates_df = pd.DataFrame(all_dates,columns=['date'])
    df = pd.merge(left=all_dates_df,right=df,on='date',how='left')
    df.ffill(inplace=True)

    return(df)