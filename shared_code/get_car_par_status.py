from requests.auth import HTTPBasicAuth
import requests
import os   
import logging

from shared_code.base_shared_code.facility import Facility


HEADERS = {'content-type': 'application/json',
          'Authorization':'apikey {}'.format(os.environ['NSWAPIKey'])}


#Initialise constants
logging.basicConfig(level=logging.INFO)



#facility_dict=constants.FACILITY_DICT
facility_list=[]

def facility_init_base(HEADERS=HEADERS) -> dict:
    '''
    Initialise list of car park faciltieis and store in Dict
    :out returns dict of facilities
    '''
    derived_facility_dict=Facility.get_init_carpark(HEADERS)
    
    return derived_facility_dict

facility_dict=facility_init_base()

def get_carpark_status_facility_rt() -> dict:
    facility_current_carpark_dict={}
    for id,facility_obj in facility_dict.items():
        logging.info('Processing...{}'.format(facility_obj.facility_name))
        facility_current_carpark_dict[id]=facility_obj.get_carpark_data(headers=HEADERS)    
    return facility_current_carpark_dict

facility_current_carpark_dict=get_carpark_status_facility_rt()

def get_carpark_status_of_facility_eod() -> dict:
    facility_eod_carpark_dict={}
    for id,facility_obj in facility_dict.items():
        logging.info('Processing...{}'.format(facility_obj.facility_name))
        facility_eod_carpark_dict[id]=facility_obj.get_carpark_data_history(headers=HEADERS,current_date='2021-11-13')    
    return facility_eod_carpark_dict

facility_eod_carpark_dict=get_carpark_status_of_facility_eod()
