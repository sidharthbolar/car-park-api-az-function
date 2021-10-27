from requests.auth import HTTPBasicAuth
import requests
import os   
import logging
import constants 
import helper
from facility import Facility
#Initialise constants


facility_dict=constants.FACILITY_DICT
facility_list=[]

#headers=constants.HEADERS

#Initialise Facilities
for key,value in facility_dict.items():  
    logging.info('Processing Facilities :',key,' : ',value)
    facility_object=Facility()
    facility_object.facility_id=key
    facility_object.facility_name=value
    facility_list.append(facility_object)

#for date in helper.create_date_range_fn():
#    print(date.strftime('%Y-%m-%d'))

#Pending Initialise Facility and Extract Facility Status