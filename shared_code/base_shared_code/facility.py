import logging
import requests
from shared_code.base_shared_code.base_shared_helper_code import constants as constants
from shared_code.base_shared_code.base_shared_helper_code import helper as helper
from shared_code.base_shared_code.base_shared_helper_code.facilityinterface import FacilityInterface
import json
from time import sleep
import sys



class Facility(FacilityInterface):
    
    url_base_carpark=constants.URL_BASE_CARPARK
    url_carpark=constants.URL_CARPARK
    url_carpark_history=constants.URL_CARPARK_HISTORY
    
    #headers=constants.HEADERS
    def __init__(self,facility_id,facility_name):
        self.facility_id=facility_id
        self.facility_name=facility_name

    @property
    def facility_id(self):
        return self._facility_id
    
    @facility_id.setter
    def facility_id(self,facility_id):
        if isinstance(int(facility_id),int):
            self._facility_id=int(facility_id)
        else:
            logging.warning("Non Integer Facility ID received")
    
    @property
    def facility_name(self):
        return self._facility_name
    
    @facility_name.setter
    def facility_name(self,facility_name):
        if isinstance(facility_name,str):
            self._facility_name=facility_name
        else:
            logging.warn("NonString Facility Name received")

    def get_carpark_data(self,headers,url_carpark=url_carpark) -> str:
        '''
        Keyword Arguments:
        Pass Facility objects and call API to extract car park facility status

        Returns:
        json response containing the current carpark status
        '''
        try:
            response = requests.get(url_carpark+str(self.facility_id), headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.error("Exception occurred", exc_info=True)
            sys.exit(8)
        except requests.exceptions.Timeout as e:
            logging.error('Open NSW API is not Responding : --- >', exc_info=True)
            sys.exit(8)
        except requests.exceptions.TooManyRedirects as e:
            logging.error('Redirects Detected Abort : --- >', exc_info=True)
            sys.exit(8)

        response_string=response.content.decode('utf-8').replace('null', '""')
        response_json=json.loads(response_string)
        return response_json



    def get_carpark_data_history(self,headers,current_date,date_range=helper.create_date_range_fn(),url_carpark_history=url_carpark_history) -> str:
        '''
        Keyword Arguments:
        Pass Facility and Date Range for which car park history needs to be extracted
        Returns:
        nested json response containing the current carpark status

        '''
        try:
            response = requests.get(url_carpark_history+str(self.facility_id)+'&eventdate='+current_date, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.error("Exception occurred", exc_info=True)
            sys.exit(8)
        except requests.exceptions.Timeout as e:
            logging.error('Open NSW API is not Responding : --- >', exc_info=True)
            sys.exit(8)
        except requests.exceptions.TooManyRedirects as e:
            logging.error('Redirects Detected Abort : --- >', exc_info=True)
            sys.exit(8)

        response_string=response.content.decode('utf-8').replace('null', '""')     
        response_json=json.loads(response_string)
        return response_json

    @staticmethod
    def get_init_carpark(headers,url_base_carpark=url_base_carpark) -> dict :
        temp_dict={}
        facility_dict={}
        temp_dict = requests.get(url_base_carpark,headers=headers).json()
        for id,name in temp_dict.items():
            facility_dict[id]=Facility(id, name)
        return facility_dict