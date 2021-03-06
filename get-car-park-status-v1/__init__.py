import datetime
import logging
import azure.functions as func
from shared_code.get_car_par_status import facility_init_base,get_carpark_status_facility_rt
import pytz


def main(mytimer: func.TimerRequest,
        carparkrt: func.Out[str]) -> None:
 
    
    utc_timestamp = datetime.datetime.utcnow().replace(

        tzinfo=pytz.timezone(('Australia/Sydney')))
    


    if mytimer.past_due:
        logging.info('The timer is past due!')   
    logging.info('Python timer trigger function ran at %s', utc_timestamp.isoformat())

    #initialise List of facilities
    facility_dict=facility_init_base()
    
    logging.info('Starting current real time status')
    facility_current_carpark_dict=get_carpark_status_facility_rt()
    logging.info('Completed current real time status')

    #Used to send messages to the respective Event Hub Topics for RT and EOD payloads
    message_carparkrt=str(facility_current_carpark_dict)   
    carparkrt.set(message_carparkrt)

    return None