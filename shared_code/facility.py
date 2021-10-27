import logging
import constants
import helper
from shared_code.facilityinterface import FacilityInterface
import requests


#Constants Declaration
facility_dict=constants.FACILITY_DICT


class Facility(FacilityInterface):
    
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
        json_response = requests.get(url_carpark+self.facility_name, headers=headers).json()
        
        return json_response



    def get_carpark_data_history(self,date_range=helper.create_date_range_fn()) -> str:
        '''
        Keyword Arguments:
        Pass Facility and Date Range for which car park history needs to be extracted
        Returns:
        nested json response containing the current carpark status

        '''
        json_response = requests.get(url_carpark_history+self.facility_name, headers=headers).json()
        
        return json_response

