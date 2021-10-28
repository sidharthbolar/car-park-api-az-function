import pandas as pd
from datetime import datetime,timedelta

def create_date_range_fn(days=31) -> list:
    '''
    :parm days:int - Number of days from which the range should be created
                     Defaulted to 31
    ''' 
    start_date=datetime.today() - timedelta(days=days)
    end_date=datetime.today()
    range_period_ls=pd.date_range(start=start_date, end=end_date).to_list()
    return range_period_ls
