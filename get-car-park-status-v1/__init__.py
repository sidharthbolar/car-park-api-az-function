import datetime
import logging
import azure.functions as func
from shared_code.get_car_par_status import facility_init_base


def main(mytimer: func.TimerRequest) -> str:
 
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    

    if mytimer.past_due:
        logging.info('The timer is past due!')   
    

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    facility_dict=facility_init_base()
    print(facility_dict)
    message=str(facility_dict)
    return message