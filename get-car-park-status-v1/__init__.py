import datetime
import logging
import os
from shared_code import get_car_par_status,get_weather_status
from shared_code.get_car_par_status import get_carpark_data
import requests
import azure.functions as func
from shared_code.get_weather_status import get_weather_carpark


def main(mytimer: func.TimerRequest) -> str:
 
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    

    if mytimer.past_due:
        logging.info('The timer is past due!')   
    

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print (str(get_carpark_data()).replace('None','\'\''))
    message=str(get_carpark_data()).replace('None','\'\'')
    return message