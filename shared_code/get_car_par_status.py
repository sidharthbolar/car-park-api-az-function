from requests.auth import HTTPBasicAuth
import requests
import os   
import logging

from shared_code.base_shared_code.facility import Facility


HEADERS = {'content-type': 'application/json',
          'Authorization':'apikey {}'.format(os.environ['NSWAPIKey'])}


#Initialise constants



#facility_dict=constants.FACILITY_DICT
facility_list=[]

def facility_init_base(HEADERS=HEADERS) -> dict:
    derived_facility_dict=Facility.get_init_carpark(HEADERS)
    print(derived_facility_dict)
    return derived_facility_dict
facility_dict=facility_init_base()

