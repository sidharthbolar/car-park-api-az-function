import datetime
import logging
from shared_code.get_car_par_status import get_carpark_data
import azure.functions as func



def main(mytimer: func.TimerRequest) -> str:
 
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    

    if mytimer.past_due:
        logging.info('The timer is past due!')   
    

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print (str(get_carpark_data()).replace('None','\'\''))
    message=str(get_carpark_data()).replace('None','\'\'')
    return message