"""
Copyright: Copyright (C) 2015 Baruch College
Description: automatic process to get stock close price
"""

# local imports
from download_earnings import make_dir

# 3rd party imports
import pandas.io.data as web
import datetime as dt

def download_SPX(date=None):
    '''
    @summary: download SPX index
    @param date: the date to create
    @return: None
    '''
    if date == None:
        date = dt.date.today()

    start = dt.datetime(1990,1,1)
    end = date
    f = web.DataReader("^GSPC", 'yahoo', start, end).fillna('NaN')
    f.to_csv(make_dir(date)+'/SPX.csv', date_format='%Y%m%d')


def main():
    download_SPX()


if __name__ == '__main__':
    main()