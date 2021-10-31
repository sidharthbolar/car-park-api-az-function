import datetime
import logging
import azure.functions as func
from shared_code.get_car_par_status import facility_init_base
import pytz

facility_dict=None

def main(mytimer: func.TimerRequest,
        carparkrt: func.Out[str],
        carparkeod: func.Out[str]) -> None:
 
    
    utc_timestamp = datetime.datetime.utcnow().replace(

        tzinfo=pytz.timezone(('Australia/Sydney')))
    


    if mytimer.past_due:
        logging.info('The timer is past due!')   
    logging.info('Python timer trigger function ran at %s', utc_timestamp.isoformat())

    #initialise List of facilities
    global facility_dict
    if facility_dict is None:
        facility_dict=facility_init_base()
    
    #Used to send messages to the respective Event Hub Topics for RT and EOD payloads
    message=str(facility_dict)
    carparkrt.set(message)
    carparkeod.set(message)

    return None