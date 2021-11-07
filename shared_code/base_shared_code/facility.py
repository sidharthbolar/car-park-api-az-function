import logging
import requests
from shared_code.base_shared_code.base_shared_helper_code import constants as constants
from shared_code.base_shared_code.base_shared_helper_code import helper as helper
from shared_code.base_shared_code.base_shared_helper_code.facilityinterface import FacilityInterface


class Facility(FacilityInterface):
    
    url_base_carpark=constants.URL_BASE_CARPARK
    url_carpark=constants.URL_CARPARK
    url_carpark_history=constants.URL_CARPARK_HISTORY
    
    #headers=constants.HEADERS


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

    def get_carpark_data(self) -> str:
        '''
        Keyword Arguments:
        Pass Facility objects and call API to extract car park facility status

        Returns:
        json response containing the current carpark status
        '''
        try:
            response = response = requests.get(url_carpark+self.facility_name, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.ERROR('HTTP Error : --- >',e.response.text)
            sys.exit(8)
        except requests.exceptions.Timeout as e:
            logging.ERROR('Open NSW API is not Responding : --- >',e)
            sys.exit(8)
        except requests.exceptions.TooManyRedirects as e:
            logging.ERROR('Redirects Detected Abort : --- >',e)
            sys.exit(8)
        
        response_json=json.loads(response.content)
        return response_json



    def get_carpark_data_history(self,date_range=helper.create_date_range_fn()) -> str:
        '''
        Keyword Arguments:
        Pass Facility and Date Range for which car park history needs to be extracted
        Returns:
        nested json response containing the current carpark status

        '''
        try:
            response = requests.get(url_carpark_history+self.facility_name, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.ERROR('HTTP Error : --- >',e.response.text)
            sys.exit(8)
        except requests.exceptions.Timeout as e:
            logging.ERROR('Open NSW API is not Responding : --- >',e)
            sys.exit(8)
        except requests.exceptions.TooManyRedirects as e:
            logging.ERROR('Redirects Detected Abort : --- >',e)
            sys.exit(8)

        response_json=json.loads(response.content)
        return response_json

    @staticmethod
    def get_init_carpark(headers,url_base_carpark=url_base_carpark) -> dict :
        facility_dict={}
        facility_dict = requests.get(url_base_carpark,headers=headers).json()
        return facility_dict