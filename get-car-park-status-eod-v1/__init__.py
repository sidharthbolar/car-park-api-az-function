import datetime
import logging
from shared_code.get_car_par_status import facility_init_base,get_carpark_status_of_facility_eod

import azure.functions as func


def main(mytimer: func.TimerRequest,
        carparkeod: func.Out[str]) -> None:
 
    
    utc_timestamp = datetime.datetime.utcnow().replace(

        tzinfo=pytz.timezone(('Australia/Sydney')))
    


    if mytimer.past_due:
        logging.info('The timer is past due!')   
    logging.info('Python timer trigger function ran at %s', utc_timestamp.isoformat())

    #initialise List of facilities
    facility_dict=facility_init_base()
    
    logging.info('Starting current real time status')
    #facility_current_carpark_dict=get_carpark_status_facility_rt()
    logging.info('Completed current real time status')
    
    logging.info('Starting EOD status')
    #facility_eod_carpark_dict=get_carpark_status_of_facility_eod()
    logging.info('Completed EOD status')

    #Used to send messages to the respective Event Hub Topics for RT and EOD payloads
    #message_carparkrt=str(facility_current_carpark_dict)
    message_carparkeod=str(facility_dict)
    carparkeod.set(message_carparkeod)

    return None
